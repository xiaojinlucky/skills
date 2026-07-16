from __future__ import annotations

import json
from pathlib import Path
from typing import Any


SKILL_ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_DIR = SKILL_ROOT / "evidence"
CONTENT_ID = "sha256:274ded5b3d35c7441243819591499fbaa9a9143f50fbbd8095f436bbe8666bce"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                records.append(json.loads(line))
    return records


def main() -> int:
    coverage = [
        record
        for record in read_jsonl(EVIDENCE_DIR / "source-coverage.jsonl")
        if record.get("content_id") == CONTENT_ID
    ]
    documents = [
        record
        for record in read_jsonl(EVIDENCE_DIR / "pdf-documents.jsonl")
        if record.get("content_id") == CONTENT_ID
    ]
    pages = [
        record
        for record in read_jsonl(EVIDENCE_DIR / "pdf-pages.jsonl")
        if record.get("content_id") == CONTENT_ID
    ]
    coverage_record = coverage[0] if coverage else {}
    document_record = documents[0] if documents else {}
    pages_by_number = {int(record["page_number"]): record for record in pages}
    page_19 = pages_by_number.get(19, {}).get("text", "")
    page_21 = pages_by_number.get(21, {}).get("text", "")
    page_24 = pages_by_number.get(24, {}).get("text", "")
    page_47 = pages_by_number.get(47, {}).get("text", "")
    page_58 = pages_by_number.get(58, {}).get("text", "")

    checks = [
        (len(coverage) == 1, "基础版来源记录应唯一"),
        (coverage_record.get("preservation_status") == "retained_ocr", "来源状态应为 retained_ocr"),
        (coverage_record.get("text_status") == "ocr_unverified", "来源质量不得升级"),
        (coverage_record.get("text_char_count") == 159856, "来源文字数不一致"),
        (len(documents) == 1, "基础版文档记录应唯一"),
        (document_record.get("page_count") == 274, "文档页数不一致"),
        (document_record.get("text_page_count") == 274, "OCR 覆盖页数不一致"),
        (document_record.get("total_extracted_chars") == 159856, "文档文字数不一致"),
        (document_record.get("review_status") == "ocr_unverified", "文档质量不得升级"),
        (len(pages) == 274, "基础版页记录数量不一致"),
        (set(pages_by_number) == set(range(1, 275)), "基础版页码不连续"),
        (
            all(page.get("extraction_status") == "text_extracted" for page in pages),
            "存在未提取页面",
        ),
        (
            all(page.get("text_quality") == "ocr_unverified" for page in pages),
            "存在错误升级的页面质量",
        ),
        (sum(page["char_count"] for page in pages) == 159856, "页级文字总数不一致"),
        (
            "看文献应该重点学习他们的思路和方法，而非研究结论" in page_19,
            "第 19 页核心阅读原则缺失",
        ),
        (
            "找出每个小标题的主要实验及样本分组" in page_21,
            "第 21 页 Figure 框架解析缺失",
        ),
        (
            "看透课题设计" in page_24 and "能够化为己用" in page_24,
            "第 24 页三层阅读目标缺失",
        ),
        (
            "Critical thinking" in page_47 and "终极问题" in page_47,
            "第 47 页批判性阅读与课题起点缺失",
        ),
        (
            "为什么做" in page_58 and "推出什么结论" in page_58,
            "第 58 页结果讲解结构缺失",
        ),
    ]
    failures = [label for condition, label in checks if not condition]
    passed = len(checks) - len(failures)
    print(f"RESULT: {passed} passed, {len(failures)} failed")
    for failure in failures:
        print(f"FAIL: {failure}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
