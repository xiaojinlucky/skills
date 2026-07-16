from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable


TERM_RE = re.compile(r"[A-Za-z0-9_.+-]+|[\u3400-\u4dbf\u4e00-\u9fff]+")
MODES = ("paper_reading", "topic_ideation", "result_storyline")
STATUSES = ("candidate", "accepted", "accepted_with_boundary", "rejected", "superseded")


def read_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"JSONL parse failed: {path}:{line_number}: {exc}") from exc


def parse_args() -> argparse.Namespace:
    default_catalog = Path(__file__).resolve().parents[1] / "references" / "method-units.jsonl"
    parser = argparse.ArgumentParser(description="Retrieve BioAdvance research-method units")
    parser.add_argument("--catalog", type=Path, default=default_catalog)
    parser.add_argument("--mode", choices=MODES)
    parser.add_argument("--stage")
    parser.add_argument("--unit-id")
    parser.add_argument("--query")
    parser.add_argument("--review-status", choices=STATUSES, action="append")
    parser.add_argument("--view", choices=("action", "evidence", "full"), default="action")
    parser.add_argument("--limit", type=int, default=10)
    return parser.parse_args()


def query_terms(query: str | None) -> list[str]:
    if not query:
        return []
    return [term.lower() for term in TERM_RE.findall(query) if term]


def searchable_text(unit: dict[str, Any]) -> str:
    values = [
        unit["unit_id"],
        unit["title"],
        unit["reasoning_topic"],
        unit["decision_action"],
        unit["rule_origin"]["distilled_creator_method"],
        unit["rule_origin"]["scientific_guardrail"],
        *unit["trigger_signals"],
        *unit["do_not_trigger"],
        *(step["action"] for step in unit["execution_steps"]),
        *(item["rule"] for item in unit["completion_rules"]),
        *(item["rule"] for item in unit["stop_or_pivot_rules"]),
    ]
    return "\n".join(values).lower()


def matches(unit: dict[str, Any], args: argparse.Namespace, terms: list[str]) -> bool:
    if args.mode and args.mode not in unit["task_modes"]:
        return False
    if args.stage and args.stage not in unit["task_stages"]:
        return False
    if args.unit_id and args.unit_id != unit["unit_id"]:
        return False
    if args.review_status and unit["review_status"] not in args.review_status:
        return False
    haystack = searchable_text(unit)
    return all(term in haystack for term in terms)


def action_view(unit: dict[str, Any]) -> dict[str, Any]:
    keys = (
        "unit_id",
        "title",
        "unit_type",
        "task_modes",
        "task_stages",
        "preconditions",
        "decision_action",
        "rule_origin",
        "trigger_signals",
        "do_not_trigger",
        "execution_steps",
        "completion_rules",
        "stop_or_pivot_rules",
        "applicability_scope",
        "alternative_explanations",
        "review_status",
        "review_note",
    )
    result = {key: unit[key] for key in keys}
    result["evidence_anchor_ids"] = [link["anchor_id"] for link in unit["evidence_links"]]
    return result


def evidence_view(unit: dict[str, Any]) -> dict[str, Any]:
    return {
        "unit_id": unit["unit_id"],
        "title": unit["title"],
        "task_modes": unit["task_modes"],
        "task_stages": unit["task_stages"],
        "evidence_links": unit["evidence_links"],
        "validation": unit["validation"],
        "review_status": unit["review_status"],
    }


def main() -> int:
    args = parse_args()
    if args.limit < 1 or args.limit > 100:
        raise ValueError("limit must be between 1 and 100")
    if not any((args.mode, args.stage, args.unit_id, args.query, args.review_status)):
        raise ValueError("provide at least one filter; full-catalog dumping is disabled")
    catalog = args.catalog.expanduser().resolve()
    if not catalog.is_file():
        raise FileNotFoundError(catalog)
    terms = query_terms(args.query)
    units = [unit for unit in read_jsonl(catalog) if matches(unit, args, terms)]
    units.sort(key=lambda item: (item["task_modes"], item["task_stages"], item["unit_id"]))
    units = units[: args.limit]
    if args.view == "action":
        results = [action_view(unit) for unit in units]
    elif args.view == "evidence":
        results = [evidence_view(unit) for unit in units]
    else:
        results = units
    digest = hashlib.sha256(catalog.read_bytes()).hexdigest()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print(
        json.dumps(
            {
                "schema_version": 1,
                "catalog": str(catalog),
                "catalog_sha256": digest,
                "filters": {
                    "mode": args.mode,
                    "stage": args.stage,
                    "unit_id": args.unit_id,
                    "query": args.query,
                    "review_status": args.review_status,
                },
                "view": args.view,
                "result_count": len(results),
                "results": results,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
