from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import sys
from pathlib import Path
from typing import Any


TERM_RE = re.compile(r"[\w\u3400-\u4dbf\u4e00-\u9fff]+", re.UNICODE)
DB_ENV = "BIOADVANCE_CORPUS_DB"
KNOWN_DB_SHA256 = "dfdfc6e0aa5dafb1c0b0d42b04e83cd60d36483e2c1cf523f9f63da77be9e8a4"
EXCLUSION_SQL = [
    "lower(r.source_path) NOT LIKE '%cc-kaiti%'",
    "lower(r.title) NOT LIKE '%cc-kaiti%'",
    "lower(r.text) NOT LIKE '%cc-kaiti%'",
    "r.source_id NOT LIKE '%BV1spTy6DEb4%'",
    "coalesce(r.source_url, '') NOT LIKE '%BV1spTy6DEb4%'",
    "r.text NOT LIKE '%BV1spTy6DEb4%'",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="只读查询 BioAdvance 私有语料")
    parser.add_argument("--db", type=Path)
    parser.add_argument("--query", required=True)
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument(
        "--scope",
        choices=["bioadvance", "all"],
        default="bioadvance",
        help="bioadvance 只检索作者本人内容，all 也包含用户问题和社区评论",
    )
    parser.add_argument(
        "--text-kind",
        choices=["answer", "question", "body", "comment"],
        action="append",
    )
    return parser.parse_args()


def resolve_db(explicit: Path | None) -> Path:
    if explicit is not None:
        database = explicit
    else:
        value = os.environ.get(DB_ENV)
        if not value:
            raise ValueError(f"必须提供 --db 或设置环境变量 {DB_ENV}")
        database = Path(value)
    database = database.expanduser().resolve()
    if not database.is_file():
        raise FileNotFoundError(database)
    digest = hashlib.sha256(database.read_bytes()).hexdigest()
    if digest != KNOWN_DB_SHA256:
        raise ValueError(
            "数据库指纹不匹配。请使用经过排除审计的 bioadvance-corpus-v1.sqlite"
        )
    return database


def build_terms(query: str) -> list[str]:
    terms = [term for term in TERM_RE.findall(query) if term]
    if not terms:
        raise ValueError("查询中没有可检索文字")
    return terms


def quote_fts(term: str) -> str:
    return '"' + term.replace('"', '""') + '"'


def query_fts(
    connection: sqlite3.Connection,
    terms: list[str],
    scope: str,
    text_kinds: list[str] | None,
    limit: int,
) -> list[sqlite3.Row]:
    filters = ["corpus_fts MATCH ?"]
    filters.extend(EXCLUSION_SQL)
    params: list[Any] = [" AND ".join(quote_fts(term) for term in terms)]
    if scope == "bioadvance":
        filters.append("r.author_role = 'bioadvance'")
    if text_kinds:
        placeholders = ",".join("?" for _ in text_kinds)
        filters.append(f"r.text_kind IN ({placeholders})")
        params.extend(text_kinds)
    params.append(limit)
    sql = f"""
        SELECT r.source_id, r.topic_id, r.record_type, r.text_kind,
               r.author_role, r.published_at, r.title, r.source_path,
               r.source_url, bm25(corpus_fts, 2.0, 1.0) AS rank_score,
               snippet(corpus_fts, 1, '[', ']', ' … ', 24) AS matched_snippet
        FROM corpus_fts
        JOIN search_records AS r ON r.id = corpus_fts.rowid
        WHERE {' AND '.join(filters)}
        ORDER BY rank_score, r.published_at DESC
        LIMIT ?
    """
    return connection.execute(sql, params).fetchall()


def escape_like(term: str) -> str:
    return term.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")


def query_short_terms(
    connection: sqlite3.Connection,
    terms: list[str],
    scope: str,
    text_kinds: list[str] | None,
    limit: int,
) -> list[sqlite3.Row]:
    filters: list[str] = list(EXCLUSION_SQL)
    params: list[Any] = []
    for term in terms:
        filters.append("(title LIKE ? ESCAPE '\\' OR text LIKE ? ESCAPE '\\')")
        pattern = f"%{escape_like(term)}%"
        params.extend([pattern, pattern])
    if scope == "bioadvance":
        filters.append("author_role = 'bioadvance'")
    if text_kinds:
        placeholders = ",".join("?" for _ in text_kinds)
        filters.append(f"text_kind IN ({placeholders})")
        params.extend(text_kinds)
    sql = f"""
        SELECT r.source_id, r.topic_id, r.record_type, r.text_kind,
               r.author_role, r.published_at, r.title, r.source_path,
               r.source_url, r.text AS private_text, NULL AS rank_score
        FROM search_records AS r
        WHERE {' AND '.join(filters)}
        ORDER BY published_at DESC
    """
    candidates = connection.execute(sql, params).fetchall()

    def matches(row: sqlite3.Row) -> bool:
        haystack = f"{row['title']}\n{row['private_text']}"
        for term in terms:
            if re.fullmatch(r"[A-Za-z0-9_.+-]+", term):
                pattern = re.compile(
                    rf"(?<![A-Za-z0-9]){re.escape(term)}(?![A-Za-z0-9])",
                    re.IGNORECASE,
                )
                if not pattern.search(haystack):
                    return False
            elif term not in haystack:
                return False
        return True

    return [row for row in candidates if matches(row)][:limit]


def literal_context(text: str, terms: list[str], width: int = 420) -> str:
    lowered = text.lower()
    positions = [lowered.find(term.lower()) for term in terms]
    positions = [position for position in positions if position >= 0]
    center = min(positions) if positions else 0
    start = max(0, center - width // 3)
    end = min(len(text), start + width)
    prefix = "…" if start else ""
    suffix = "…" if end < len(text) else ""
    return prefix + text[start:end].replace("\r", " ").replace("\n", " ") + suffix


def public_result(row: sqlite3.Row, terms: list[str]) -> dict[str, Any]:
    result = dict(row)
    private_text = result.pop("private_text", None)
    if private_text is not None:
        result["matched_snippet"] = literal_context(private_text, terms)
    return result


def main() -> int:
    args = parse_args()
    if args.limit < 1 or args.limit > 100:
        raise ValueError("limit 必须在 1 到 100 之间")
    database = resolve_db(args.db)
    terms = build_terms(args.query)
    connection = sqlite3.connect(
        f"{database.as_uri()}?mode=ro&immutable=1", uri=True
    )
    connection.row_factory = sqlite3.Row
    try:
        if all(len(term) >= 3 for term in terms):
            rows = query_fts(connection, terms, args.scope, args.text_kind, args.limit)
            retrieval_mode = "fts5_trigram"
        else:
            rows = query_short_terms(
                connection, terms, args.scope, args.text_kind, args.limit
            )
            retrieval_mode = "literal_substring_for_short_term"
    finally:
        connection.close()

    output = {
        "database": str(database),
        "database_sha256": KNOWN_DB_SHA256,
        "query": args.query,
        "terms": terms,
        "scope": args.scope,
        "text_kinds": args.text_kind,
        "retrieval_mode": retrieval_mode,
        "result_count": len(rows),
        "results": [public_result(row, terms) for row in rows],
    }
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
