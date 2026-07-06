#!/usr/bin/env python3
"""No-key CS literature metadata search via DBLP, Crossref, arXiv, and optional OpenAlex.

This script intentionally avoids paid/key-only APIs. It returns a deduplicated
JSON list suitable for screening and later PDF download via scansci-pdf.

Default mode is optimized for speed and avoids OpenAlex by default: query DBLP
first, then Crossref if the seed pool is too small. Use ``--sources openalex``
explicitly when OpenAlex metadata is needed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time
from datetime import datetime
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from typing import Any


def cache_key(url: str) -> str:
    return hashlib.sha256(url.encode("utf-8")).hexdigest() + ".cache"


def fetch_bytes(url: str, timeout: int, cache_dir: str | None, cache_ttl_hours: int) -> bytes:
    cache_path = None
    if cache_dir:
        cache_root = Path(cache_dir)
        cache_root.mkdir(parents=True, exist_ok=True)
        cache_path = cache_root / cache_key(url)
        if cache_path.exists():
            age_hours = (time.time() - cache_path.stat().st_mtime) / 3600
            if age_hours <= cache_ttl_hours:
                return cache_path.read_bytes()

    req = urllib.request.Request(url, headers={"User-Agent": "cs-literature-search/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
    if cache_path:
        cache_path.write_bytes(data)
    return data


def fetch_json(url: str, timeout: int, cache_dir: str | None, cache_ttl_hours: int) -> dict[str, Any]:
    return json.loads(fetch_bytes(url, timeout, cache_dir, cache_ttl_hours).decode("utf-8"))


def fetch_text(url: str, timeout: int, cache_dir: str | None, cache_ttl_hours: int) -> str:
    return fetch_bytes(url, timeout, cache_dir, cache_ttl_hours).decode("utf-8", errors="replace")


def normalize_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


def query_terms(query: str) -> list[str]:
    stop = {
        "a",
        "an",
        "and",
        "are",
        "for",
        "in",
        "of",
        "on",
        "or",
        "the",
        "to",
        "with",
        "via",
        "using",
    }
    return [t for t in normalize_title(query).split() if len(t) > 2 and t not in stop]


def relevance_score(item: dict[str, Any], terms: list[str]) -> int:
    title = normalize_title(item.get("title", ""))
    abstract = normalize_title(item.get("abstract", ""))
    score = 0
    for term in terms:
        if term in title:
            score += 3
        if term in abstract:
            score += 1
    return score


def matched_term_count(item: dict[str, Any], terms: list[str]) -> int:
    text = normalize_title(f"{item.get('title', '')} {item.get('abstract', '')}")
    return sum(1 for term in terms if term in text)


def inverted_abstract(index: dict[str, list[int]] | None) -> str:
    if not index:
        return ""
    words: list[tuple[int, str]] = []
    for word, positions in index.items():
        for pos in positions:
            words.append((pos, word))
    return " ".join(word for _, word in sorted(words))[:1200]


def search_openalex(
    query: str,
    year_from: int | None,
    year_to: int | None,
    limit: int,
    timeout: int,
    cache_dir: str | None,
    cache_ttl_hours: int,
    mailto: str | None,
) -> list[dict[str, Any]]:
    filters = []
    if year_from:
        filters.append(f"from_publication_date:{year_from}-01-01")
    if year_to:
        filters.append(f"to_publication_date:{year_to}-12-31")
    params = {
        "search": query,
        "per_page": str(min(limit, 200)),
        "sort": "publication_date:desc",
    }
    if mailto:
        params["mailto"] = mailto
    if filters:
        params["filter"] = ",".join(filters)
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    data = fetch_json(url, timeout, cache_dir, cache_ttl_hours)
    out = []
    for item in data.get("results", []):
        doi = (item.get("doi") or "").replace("https://doi.org/", "")
        out.append(
            {
                "title": item.get("title") or "",
                "year": item.get("publication_year"),
                "venue": (item.get("primary_location") or {}).get("source", {}).get("display_name") or "",
                "doi": doi,
                "arxiv_id": "",
                "url": item.get("id") or "",
                "source": "OpenAlex",
                "cited_by_count": item.get("cited_by_count", 0),
                "abstract": inverted_abstract(item.get("abstract_inverted_index")),
            }
        )
    return out


def search_arxiv(
    query: str,
    year_from: int | None,
    year_to: int | None,
    limit: int,
    timeout: int,
    cache_dir: str | None,
    cache_ttl_hours: int,
    mailto: str | None,
) -> list[dict[str, Any]]:
    del mailto
    terms = query_terms(query)[:8]
    search_query = " AND ".join(f"all:{term}" for term in terms) if terms else f'all:"{query}"'
    params = {
        "search_query": search_query,
        "start": "0",
        "max_results": str(min(limit, 100)),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)
    text = fetch_text(url, timeout, cache_dir, cache_ttl_hours)
    root = ET.fromstring(text)
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    out = []
    for entry in root.findall("atom:entry", ns):
        title = " ".join((entry.findtext("atom:title", default="", namespaces=ns) or "").split())
        published = entry.findtext("atom:published", default="", namespaces=ns) or ""
        year = int(published[:4]) if published[:4].isdigit() else None
        if year_from and year and year < year_from:
            continue
        if year_to and year and year > year_to:
            continue
        if year and year > datetime.now().year + 1:
            continue
        arxiv_url = entry.findtext("atom:id", default="", namespaces=ns) or ""
        arxiv_id = arxiv_url.rsplit("/", 1)[-1]
        summary = " ".join((entry.findtext("atom:summary", default="", namespaces=ns) or "").split())
        out.append(
            {
                "title": title,
                "year": year,
                "venue": "arXiv",
                "doi": "",
                "arxiv_id": arxiv_id,
                "url": arxiv_url,
                "source": "arXiv",
                "cited_by_count": None,
                "abstract": summary[:1200],
            }
        )
    return out


def search_crossref(
    query: str,
    year_from: int | None,
    year_to: int | None,
    limit: int,
    timeout: int,
    cache_dir: str | None,
    cache_ttl_hours: int,
    mailto: str | None,
) -> list[dict[str, Any]]:
    filters = []
    if year_from:
        filters.append(f"from-pub-date:{year_from}-01-01")
    if year_to:
        filters.append(f"until-pub-date:{year_to}-12-31")
    params = {
        "query.bibliographic": query,
        "rows": str(min(limit, 100)),
        "sort": "published",
        "order": "desc",
    }
    if filters:
        params["filter"] = ",".join(filters)
    if mailto:
        params["mailto"] = mailto
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
    data = fetch_json(url, timeout, cache_dir, cache_ttl_hours)
    out = []
    for item in (data.get("message") or {}).get("items", []):
        title = " ".join((item.get("title") or [""])[0].split())
        issued = item.get("published-print") or item.get("published-online") or item.get("issued") or {}
        parts = issued.get("date-parts") or []
        year = parts[0][0] if parts and parts[0] else None
        if year_from and year and year < year_from:
            continue
        if year_to and year and year > year_to:
            continue
        out.append(
            {
                "title": title,
                "year": year,
                "venue": (item.get("container-title") or [""])[0],
                "doi": item.get("DOI") or "",
                "arxiv_id": "",
                "url": item.get("URL") or "",
                "source": "Crossref",
                "cited_by_count": item.get("is-referenced-by-count", 0),
                "abstract": re.sub(r"<[^>]+>", " ", item.get("abstract") or "")[:1200],
            }
        )
    return out


def search_dblp(
    query: str,
    year_from: int | None,
    year_to: int | None,
    limit: int,
    timeout: int,
    cache_dir: str | None,
    cache_ttl_hours: int,
    mailto: str | None,
) -> list[dict[str, Any]]:
    del mailto
    params = {
        "q": query,
        "format": "json",
        "h": str(min(limit, 100)),
    }
    url = "https://dblp.org/search/publ/api?" + urllib.parse.urlencode(params)
    data = fetch_json(url, timeout, cache_dir, cache_ttl_hours)
    hits = (((data.get("result") or {}).get("hits") or {}).get("hit") or [])
    out = []
    for hit in hits:
        info = hit.get("info") or {}
        year_raw = str(info.get("year") or "")
        year = int(year_raw) if year_raw.isdigit() else None
        if year_from and year and year < year_from:
            continue
        if year_to and year and year > year_to:
            continue
        if year and year > datetime.now().year + 1:
            continue
        out.append(
            {
                "title": re.sub(r"<[^>]+>", " ", info.get("title") or "").strip(),
                "year": year,
                "venue": info.get("venue") or "",
                "doi": info.get("doi") or "",
                "arxiv_id": "",
                "url": info.get("url") or "",
                "source": "DBLP",
                "cited_by_count": None,
                "abstract": "",
            }
        )
    return out


def dedupe(items: list[dict[str, Any]], terms: list[str], min_term_matches: int) -> list[dict[str, Any]]:
    seen: set[str] = set()
    out = []
    for item in items:
        key = item.get("doi") or item.get("arxiv_id") or normalize_title(item.get("title", ""))
        if not key or key in seen:
            continue
        seen.add(key)
        item["matched_terms"] = matched_term_count(item, terms)
        if terms and item["matched_terms"] < min_term_matches:
            continue
        item["relevance_score"] = relevance_score(item, terms)
        if terms and item["relevance_score"] <= 0:
            continue
        out.append(item)
    return sorted(
        out,
        key=lambda x: (
            x.get("relevance_score") or 0,
            x.get("year") or 0,
            x.get("cited_by_count") or 0,
        ),
        reverse=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True)
    parser.add_argument("--year-from", type=int)
    parser.add_argument("--year-to", type=int)
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument(
        "--sources",
        choices=["quick", "all", "openalex", "dblp", "crossref", "arxiv"],
        default="quick",
        help="quick runs DBLP first and calls Crossref only if too few results are found. OpenAlex is explicit only.",
    )
    parser.add_argument("--min-results", type=int, default=10, help="Quick mode stops after OpenAlex if this many results are found.")
    parser.add_argument("--min-term-matches", type=int, default=2, help="Drop results matching fewer query terms.")
    parser.add_argument("--timeout", type=int, default=12, help="Per-endpoint network timeout in seconds.")
    parser.add_argument("--cache-dir", help="Optional HTTP cache directory for repeated searches.")
    parser.add_argument("--cache-ttl-hours", type=int, default=168)
    parser.add_argument("--mailto", default=os.environ.get("OPENALEX_MAILTO"), help="Optional OpenAlex polite-pool email.")
    parser.add_argument("--out")
    args = parser.parse_args()

    results: list[dict[str, Any]] = []
    errors: list[str] = []

    def run_source(name: str) -> None:
        fn_map = {
            "openalex": search_openalex,
            "dblp": search_dblp,
            "crossref": search_crossref,
            "arxiv": search_arxiv,
        }
        fn = fn_map[name]
        try:
            results.extend(
                fn(
                    args.query,
                    args.year_from,
                    args.year_to,
                    args.limit,
                    args.timeout,
                    args.cache_dir,
                    args.cache_ttl_hours,
                    args.mailto,
                )
            )
        except Exception as exc:  # Keep other sources usable if one endpoint fails.
            errors.append(f"{name}: {exc}")

    terms = query_terms(args.query)
    if args.sources == "openalex":
        run_source("openalex")
    elif args.sources == "arxiv":
        run_source("arxiv")
    elif args.sources == "crossref":
        run_source("crossref")
    elif args.sources == "dblp":
        run_source("dblp")
    elif args.sources == "all":
        run_source("dblp")
        run_source("crossref")
        run_source("arxiv")
    else:
        run_source("dblp")
        if len(dedupe(results, terms, args.min_term_matches)) < args.min_results:
            run_source("crossref")

    payload = {
        "query": args.query,
        "sources": args.sources,
        "count": 0,
        "errors": errors,
        "results": [],
    }
    payload["results"] = dedupe(results, terms, args.min_term_matches)[: args.limit]
    payload["count"] = len(payload["results"])

    text = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    else:
        print(text)
    return 0 if payload["results"] else 2


if __name__ == "__main__":
    sys.exit(main())
