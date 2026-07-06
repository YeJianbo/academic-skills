#!/usr/bin/env python3
"""Stage-gated title/abstract screening for CS literature search results.

Input is the JSON payload from cs_lit_search.py. Output is a CSV with stage
status plus optional abstract and download queues. This script is deliberately
local-only: it does not fetch abstracts or download PDFs.

The output is a screening matrix, not an evidence matrix.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Any


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def split_keywords(raw: str) -> list[str]:
    out: list[str] = []
    for part in re.split(r"[,;|]", raw):
        term = normalize(part)
        if term:
            out.append(term)
    return out


def score_text(text: str, keywords: list[str]) -> tuple[int, list[str]]:
    norm = normalize(text)
    hits = [kw for kw in keywords if kw in norm]
    return len(hits), hits


def paper_id(item: dict[str, Any]) -> str:
    return item.get("doi") or item.get("arxiv_id") or normalize(item.get("title", ""))[:80]


def decide(item: dict[str, Any], keywords: list[str], title_yes: int, abstract_yes: int) -> dict[str, str]:
    title = item.get("title", "")
    abstract = item.get("abstract", "")
    title_score, title_hits = score_text(title, keywords)
    abstract_score, abstract_hits = score_text(abstract, keywords)

    if title_score >= title_yes:
        title_decision = "title_yes"
    elif title_score > 0:
        title_decision = "title_maybe"
    else:
        title_decision = "title_no"

    if title_decision == "title_no":
        stage = "title_no"
        next_action = "reject"
        screening_role = "reject"
    elif not abstract:
        stage = "needs_abstract"
        next_action = "abstract_queue"
        screening_role = "core-candidate" if title_score >= title_yes else "adjacent-candidate"
    elif abstract_score >= abstract_yes:
        stage = "auto_abstract_candidate"
        next_action = "manual_abstract_review"
        screening_role = "core-candidate"
    elif abstract_score > 0:
        stage = "auto_abstract_maybe"
        next_action = "manual_review"
        screening_role = "adjacent-candidate"
    else:
        stage = "auto_abstract_no"
        next_action = "reject"
        screening_role = "reject"

    return {
        "paper_id": paper_id(item),
        "stage": stage,
        "next_action": next_action,
        "screening_role": screening_role,
        "evidence_role": "",
        "read_status": "metadata_only",
        "title_score": str(title_score),
        "abstract_score": str(abstract_score),
        "title_hits": "; ".join(title_hits),
        "abstract_hits": "; ".join(abstract_hits),
    }


def load_items(path: str) -> list[dict[str, Any]]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, dict):
        return list(data.get("results") or data.get("items") or [])
    if isinstance(data, list):
        return data
    raise ValueError("Input must be a JSON object with results/items or a JSON list.")


def write_csv(path: str, rows: list[dict[str, str]], fields: list[str]) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--keywords", required=True, help="Comma-separated topic keywords/phrases.")
    parser.add_argument("--out", required=True)
    parser.add_argument("--abstract-queue")
    parser.add_argument("--download-queue")
    parser.add_argument("--title-yes", type=int, default=1)
    parser.add_argument("--abstract-yes", type=int, default=1)
    args = parser.parse_args()

    keywords = split_keywords(args.keywords)
    if not keywords:
        raise SystemExit("No keywords provided.")

    rows: list[dict[str, str]] = []
    for item in load_items(args.input):
        decision = decide(item, keywords, args.title_yes, args.abstract_yes)
        rows.append(
            {
                **decision,
                "title": item.get("title", ""),
                "year": str(item.get("year") or ""),
                "venue": item.get("venue", ""),
                "doi": item.get("doi", ""),
                "arxiv_id": item.get("arxiv_id", ""),
                "url": item.get("url", ""),
                "source": item.get("source", ""),
            }
        )

    fields = [
        "paper_id",
        "stage",
        "next_action",
        "screening_role",
        "evidence_role",
        "read_status",
        "title",
        "year",
        "venue",
        "doi",
        "arxiv_id",
        "url",
        "source",
        "title_score",
        "abstract_score",
        "title_hits",
        "abstract_hits",
    ]
    write_csv(args.out, rows, fields)

    if args.abstract_queue:
        write_csv(
            args.abstract_queue,
            [
                r
                for r in rows
                if r["next_action"] in {"abstract_queue", "manual_abstract_review", "manual_review"}
            ],
            fields,
        )
    if args.download_queue:
        write_csv(args.download_queue, [r for r in rows if r["next_action"] == "download_queued"], fields)

    summary = {
        "input": args.input,
        "out": args.out,
        "total": len(rows),
        "title_yes_or_maybe": sum(1 for r in rows if r["stage"] in {"title_yes", "title_maybe", "needs_abstract"}),
        "needs_abstract": sum(1 for r in rows if r["stage"] == "needs_abstract"),
        "auto_abstract_candidate": sum(1 for r in rows if r["stage"] == "auto_abstract_candidate"),
        "auto_abstract_maybe": sum(1 for r in rows if r["stage"] == "auto_abstract_maybe"),
        "auto_abstract_no": sum(1 for r in rows if r["stage"] == "auto_abstract_no"),
        "download_queued": sum(1 for r in rows if r["next_action"] == "download_queued"),
        "note": "Auto abstract candidates require human/main-thread abstract reading before download_queued.",
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
