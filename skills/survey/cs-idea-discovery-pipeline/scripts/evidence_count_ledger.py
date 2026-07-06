#!/usr/bin/env python3
"""Create a markdown evidence-count ledger from research-run CSV files."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def rows(path: str | None) -> list[dict[str, str]]:
    if not path:
        return []
    p = Path(path)
    if not p.exists():
        return []
    with p.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def count_field(records: list[dict[str, str]], *names: str) -> Counter[str]:
    out: Counter[str] = Counter()
    for row in records:
        value = ""
        for name in names:
            value = (row.get(name) or "").strip()
            if value:
                break
        out[value or "blank"] += 1
    return out


def line(label: str, count: int, source: str, notes: str) -> str:
    return f"| {label} | {count} | `{source}` | {notes} |"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    parser.add_argument("--screening")
    parser.add_argument("--download-status")
    parser.add_argument("--read-status")
    parser.add_argument("--evidence-matrix")
    args = parser.parse_args()

    screening = rows(args.screening)
    downloads = rows(args.download_status)
    reads = rows(args.read_status)

    stage_counts = count_field(screening, "stage", "screening_stage")
    download_counts = count_field(downloads, "download_status", "status")
    read_counts = count_field(reads, "read_status", "stage", "status")
    evidence_counts = count_field(reads, "evidence_role")

    evidence_matrix_rows = 0
    if args.evidence_matrix and Path(args.evidence_matrix).exists():
        text = Path(args.evidence_matrix).read_text(encoding="utf-8", errors="replace")
        evidence_matrix_rows = sum(1 for ln in text.splitlines() if ln.startswith("|") and "core-evidence" in ln)

    src_screening = args.screening or "not provided"
    src_download = args.download_status or "not provided"
    src_read = args.read_status or "not provided"
    src_matrix = args.evidence_matrix or "not provided"

    output = [
        "# Evidence Count Ledger",
        "",
        "| Gate | Count | Source file | Notes |",
        "|---|---:|---|---|",
        line("metadata_found", sum(stage_counts.values()), src_screening, "raw/screening rows; not evidence"),
        line("title_yes", stage_counts["title_yes"], src_screening, "title gate only"),
        line("title_maybe", stage_counts["title_maybe"], src_screening, "title gate only"),
        line("needs_abstract", stage_counts["needs_abstract"], src_screening, "requires abstract lookup/read"),
        line("auto_abstract_candidate", stage_counts["auto_abstract_candidate"], src_screening, "script candidate; not human read"),
        line("auto_abstract_maybe", stage_counts["auto_abstract_maybe"], src_screening, "script candidate; not human read"),
        line("auto_abstract_no", stage_counts["auto_abstract_no"], src_screening, "script rejection; sample if recall is uncertain"),
        line("human_abstract_yes", stage_counts["human_abstract_yes"] + stage_counts["abstract_yes"], src_screening, "human/main-thread abstract decision"),
        line("human_abstract_maybe", stage_counts["human_abstract_maybe"] + stage_counts["abstract_maybe"], src_screening, "human/main-thread abstract decision"),
        line("download_queued", stage_counts["download_queued"], src_screening, "after human abstract gate"),
        line("downloaded", download_counts["downloaded"] + stage_counts["downloaded"], src_download, "local PDF available"),
        line("download_failed", download_counts["failed"], src_download, "record failure reason"),
        line("fulltext_read", read_counts["fulltext_read"] + read_counts["matrix-done"] + evidence_counts["core-evidence"], src_read, "strong evidence only if evidence locations exist"),
        line("evidence_matrix_rows", evidence_matrix_rows, src_matrix, "best-effort count from matrix file"),
        "",
        "Rules:",
        "",
        "- `auto_abstract_candidate` is not `human_abstract_yes`.",
        "- `downloaded` is not `fulltext_read`.",
        "- Only `fulltext_read` / evidence-matrix rows can support structural gap claims.",
    ]

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(output) + "\n", encoding="utf-8")
    print(out_path.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
