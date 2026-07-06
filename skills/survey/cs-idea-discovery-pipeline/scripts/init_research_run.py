#!/usr/bin/env python3
"""Initialize a fresh CS idea-discovery run manifest."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--topic", required=True)
    parser.add_argument("--year-window", default="recent 3 years")
    parser.add_argument("--target-venue", default="unspecified")
    parser.add_argument("--search-scope", required=True)
    parser.add_argument("--reputation-policy", default="live web check + CCF/reference lists + official proceedings")
    parser.add_argument("--exclude-scope", default="")
    parser.add_argument("--fresh-start", action="store_true")
    parser.add_argument("--forbidden-old-dir", action="append", default=[])
    parser.add_argument("--local-validation", default="")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for child in ["metadata", "pdf/core", "pdf/adjacent", "notes/matrices", "results", "scripts"]:
        (out_dir / child).mkdir(parents=True, exist_ok=True)

    forbidden = "\n".join(f"- `{p}`" for p in args.forbidden_old_dir) or "- none"
    manifest = f"""# Run Manifest

Created: {datetime.now().isoformat(timespec="seconds")}

## Scope Contract

| Field | Value |
|---|---|
| Topic | {args.topic} |
| Year window | {args.year_window} |
| Optional target venue | {args.target_venue} |
| Search scope venues | {args.search_scope} |
| Reputation policy | {args.reputation_policy} |
| Exclude scope | {args.exclude_scope or "none"} |
| Local validation | {args.local_validation or "to be defined"} |
| Fresh start requested | {"yes" if args.fresh_start else "no"} |

## Fresh-Start Boundary

Forbidden old directories:

{forbidden}

Rules:

- Do not use PDFs, matrices, notes, pilot results, or conclusions from forbidden old directories.
- Metadata/title/abstract screening is not evidence.
- Only full-text-read papers with recorded evidence locations may support structural gaps.
- The optional target venue is for fit assessment and does not restrict literature search.

## Evidence Count Ledger

Update `metadata/evidence_counts.md` after each gate.

| Gate | Count | Source file | Notes |
|---|---:|---|---|
| metadata_found | 0 | pending | raw metadata only |
| title_screened | 0 | pending | title gate only |
| auto_abstract_candidate | 0 | pending | script candidate, not human read |
| human_abstract_yes | 0 | pending | human/main-thread abstract decision |
| download_queued | 0 | pending | after abstract gate |
| downloaded | 0 | pending | local PDF available |
| fulltext_read | 0 | pending | evidence matrix entry exists |
| evidence_matrix_rows | 0 | pending | strong evidence only |

"""
    (out_dir / "run_manifest.md").write_text(manifest, encoding="utf-8")
    print((out_dir / "run_manifest.md").resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

