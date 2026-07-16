from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import sys
from pathlib import Path
from typing import Any, Iterable


TERM_RE = re.compile(r"[\w\u3400-\u4dbf\u4e00-\u9fff]+", re.UNICODE)
DB_ENV = "BIOADVANCE_CORPUS_DB"
KNOWN_DB_SHA256 = "dfdfc6e0aa5dafb1c0b0d42b04e83cd60d36483e2c1cf523f9f63da77be9e8a4"
EXCLUDED_BVID = "BV1spTy6DEb4"
CHANNELS = ("zsxq", "pdf", "video")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="跨来源只读检索 BioAdvance 原始材料")
    parser.add_argument("--query", required=True)
    parser.add_argument("--channel", choices=CHANNELS, action="append")
    parser.add_argument("--limit", type=int, default=5, help="每个来源通道最多返回多少条")
    parser.add_argument("--include-context", action="store_true", help="知识星球同时检索提问和评论")
    parser.add_argument("--zsxq-db", type=Path)
    parser.add_argument("--coverage", type=Path)
    parser.add_argument("--pdf-pages", type=Path)
    parser.add_argument("--pdf-documents", type=Path)
    return parser.parse_args()


def read_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"JSONL 解析失败: {path}:{line_number}: {exc}") from exc


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def terms_from_query(query: str) -> list[str]:
    terms = [term.casefold() for term in TERM_RE.findall(query) if term]
    if not terms:
        raise ValueError("查询中没有可检索文字")
    return list(dict.fromkeys(terms))


def contains_all(text: str, terms: list[str]) -> bool:
    folded = text.casefold()
    return all(term in folded for term in terms)


def lexical_score(title: str, text: str, terms: list[str]) -> int:
    title_folded = title.casefold()
    text_folded = text.casefold()
    return sum(3 * title_folded.count(term) + text_folded.count(term) for term in terms)


def excerpt(text: str, terms: list[str], width: int = 420) -> str:
    folded = text.casefold()
    positions = [folded.find(term) for term in terms]
    positions = [position for position in positions if position >= 0]
    center = min(positions) if positions else 0
    start = max(0, center - width // 3)
    end = min(len(text), start + width)
    clean = text[start:end].replace("\r", " ").replace("\n", " ")
    return ("…" if start else "") + clean + ("…" if end < len(text) else "")


def default_paths() -> dict[str, Path]:
    skill_root = Path(__file__).resolve().parents[1]
    repository_root = Path(__file__).resolve().parents[3]
    return {
        "coverage": skill_root / "evidence" / "source-coverage.jsonl",
        "pdf_pages": skill_root / "evidence" / "pdf-pages.jsonl",
        "pdf_documents": skill_root / "evidence" / "pdf-documents.jsonl",
        "zsxq_db": repository_root / "corpus" / "private-index" / "bioadvance-corpus-v1.sqlite",
    }


def resolve_zsxq_db(explicit: Path | None, fallback: Path) -> Path:
    value = explicit or (Path(os.environ[DB_ENV]) if os.environ.get(DB_ENV) else fallback)
    path = value.expanduser().resolve()
    if not path.is_file():
        raise FileNotFoundError(path)
    digest = file_sha256(path)
    if digest != KNOWN_DB_SHA256:
        raise ValueError("知识星球数据库指纹不匹配")
    return path


def query_zsxq(path: Path, terms: list[str], limit: int, include_context: bool) -> list[dict[str, Any]]:
    connection = sqlite3.connect(f"{path.as_uri()}?mode=ro&immutable=1", uri=True)
    connection.row_factory = sqlite3.Row
    try:
        rows = connection.execute(
            """
            SELECT source_id, record_type, text_kind, author_role, published_at,
                   title, text, source_path, source_url
            FROM search_records
            ORDER BY id
            """
        ).fetchall()
    finally:
        connection.close()

    results: list[dict[str, Any]] = []
    for row in rows:
        if not include_context and row["author_role"] != "bioadvance":
            continue
        haystack = f"{row['title']}\n{row['text']}"
        if not contains_all(haystack, terms):
            continue
        results.append(
            {
                "channel": "zsxq",
                "source_id": row["source_id"],
                "title": row["title"],
                "author_role": row["author_role"],
                "published_at": row["published_at"],
                "locator": row["source_id"],
                "source_path": row["source_path"],
                "source_url": row["source_url"],
                "text_quality": "reliable_text",
                "score": lexical_score(row["title"], row["text"], terms),
                "matched_excerpt": excerpt(row["text"], terms),
            }
        )
    return sorted(results, key=lambda item: (-item["score"], item["source_id"]))[:limit]


def pdf_metadata(documents_path: Path, coverage: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    coverage_by_content = {
        item["content_id"]: item
        for item in coverage
        if item.get("source_kind") == "pdf_document" and item.get("candidate_role") != "excluded"
    }
    metadata: dict[str, dict[str, Any]] = {}
    for document in read_jsonl(documents_path):
        content_id = document["content_id"]
        if content_id not in coverage_by_content:
            continue
        item = coverage_by_content[content_id]
        metadata[content_id] = {
            "source_id": item["source_id"],
            "title": item["title"],
            "source_path": item["source_path"],
            "text_quality": item["text_status"],
        }
    return metadata


def query_pdf(
    pages_path: Path,
    documents_path: Path,
    coverage: list[dict[str, Any]],
    terms: list[str],
    limit: int,
) -> list[dict[str, Any]]:
    metadata = pdf_metadata(documents_path, coverage)
    results: list[dict[str, Any]] = []
    for page in read_jsonl(pages_path):
        info = metadata.get(page["content_id"])
        if info is None or page.get("extraction_status") != "text_extracted":
            continue
        text = page.get("text") or ""
        haystack = f"{info['title']}\n{text}"
        if not contains_all(haystack, terms):
            continue
        results.append(
            {
                "channel": "pdf",
                "source_id": info["source_id"],
                "content_id": page["content_id"],
                "title": info["title"],
                "locator": f"{page['content_id']}#page={page['page_number']}",
                "source_path": info["source_path"],
                "source_url": None,
                "text_quality": info["text_quality"],
                "score": lexical_score(info["title"], text, terms),
                "matched_excerpt": excerpt(text, terms),
            }
        )
    return sorted(results, key=lambda item: (-item["score"], item["locator"]))[:limit]


def read_video_segments(path: Path) -> list[dict[str, Any]]:
    return [record for record in read_jsonl(path) if record.get("record_type") == "segment"]


def query_video(coverage: list[dict[str, Any]], terms: list[str], limit: int) -> tuple[list[dict[str, Any]], int]:
    results: list[dict[str, Any]] = []
    missing_files = 0
    seen_content: set[str] = set()
    for item in coverage:
        if item.get("source_kind") != "bilibili_video" or item.get("candidate_role") == "excluded":
            continue
        content_id = item.get("content_id")
        if not content_id or content_id in seen_content:
            continue
        seen_content.add(content_id)
        raw_path = Path(item["source_path"]) if item.get("source_path") else None
        if raw_path is None or not raw_path.is_file():
            missing_files += 1
            continue
        segments = read_video_segments(raw_path)
        joined = "".join(segment.get("text_raw", "") for segment in segments)
        haystack = f"{item['title']}\n{joined}"
        if not contains_all(haystack, terms):
            continue
        folded = joined.casefold()
        first_position = min(position for term in terms if (position := folded.find(term)) >= 0)
        consumed = 0
        matched_index = 0
        for index, segment in enumerate(segments):
            consumed += len(segment.get("text_raw", ""))
            if consumed > first_position:
                matched_index = index
                break
        start_index = max(0, matched_index - 2)
        end_index = min(len(segments), matched_index + 3)
        window = segments[start_index:end_index]
        window_text = "".join(segment.get("text_raw", "") for segment in window)
        results.append(
            {
                "channel": "video",
                "source_id": item["source_id"],
                "content_id": content_id,
                "title": item["title"],
                "locator": f"{item['source_id']}#t={window[0]['start_ms']}-{window[-1]['end_ms']}ms",
                "source_path": str(raw_path),
                "source_url": item.get("source_url"),
                "text_quality": item["text_status"],
                "score": lexical_score(item["title"], joined, terms),
                "matched_excerpt": window_text,
            }
        )
    ordered = sorted(results, key=lambda value: (-value["score"], value["source_id"]))[:limit]
    return ordered, missing_files


def main() -> int:
    args = parse_args()
    if args.limit < 1 or args.limit > 50:
        raise ValueError("limit 必须在 1 到 50 之间")
    defaults = default_paths()
    paths = {
        "coverage": (args.coverage or defaults["coverage"]).expanduser().resolve(),
        "pdf_pages": (args.pdf_pages or defaults["pdf_pages"]).expanduser().resolve(),
        "pdf_documents": (args.pdf_documents or defaults["pdf_documents"]).expanduser().resolve(),
    }
    for path in paths.values():
        if not path.is_file():
            raise FileNotFoundError(path)

    selected = list(dict.fromkeys(args.channel or CHANNELS))
    terms = terms_from_query(args.query)
    coverage = list(read_jsonl(paths["coverage"]))
    results: dict[str, Any] = {}
    status: dict[str, Any] = {}

    if "zsxq" in selected:
        database = resolve_zsxq_db(args.zsxq_db, defaults["zsxq_db"])
        results["zsxq"] = query_zsxq(database, terms, args.limit, args.include_context)
        status["zsxq"] = {"status": "ok", "database_sha256": KNOWN_DB_SHA256}
    if "pdf" in selected:
        results["pdf"] = query_pdf(paths["pdf_pages"], paths["pdf_documents"], coverage, terms, args.limit)
        status["pdf"] = {"status": "ok", "text_quality": "page_text_extraction"}
    if "video" in selected:
        video_results, missing_files = query_video(coverage, terms, args.limit)
        results["video"] = video_results
        status["video"] = {
            "status": "ok" if missing_files == 0 else "partial",
            "text_quality": "asr_unverified",
            "missing_transcript_files": missing_files,
        }

    output = {
        "schema_version": 1,
        "query": args.query,
        "terms": terms,
        "channels": selected,
        "limit_per_channel": args.limit,
        "coverage_sha256": file_sha256(paths["coverage"]),
        "status": status,
        "result_counts": {channel: len(records) for channel, records in results.items()},
        "results": results,
    }
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
