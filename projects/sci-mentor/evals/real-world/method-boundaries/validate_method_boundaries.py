from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "outputs"

FORBIDDEN_LITERALS = [
    '"',
    "“",
    "”",
    "——",
    "—",
    "–",
    "值得注意的是",
    "不难发现",
    "综上所述",
    "总的来说",
    "为我们提供了新的视角",
    "具有重要的理论意义和实践价值",
    "通过以上分析可以看出",
]

INTERNAL_PATTERNS = [
    r"\btask_mode\b",
    r"\bmode\b",
    r"\bstage\b",
    r"\breview_status\b",
    r"\bmethod-[a-z0-9-]+\b",
    r"方法单元",
    r"来源账本",
    r"证据锚点",
    r"候选状态",
    r"内部评分",
]


def validate(path: Path) -> list[str]:
    if not path.exists():
        return ["文件不存在"]

    failures: list[str] = []
    text = path.read_text(encoding="utf-8")
    if len(text.strip()) < 120:
        failures.append("输出过短或为空")

    for literal in FORBIDDEN_LITERALS:
        if literal in text:
            failures.append(f"包含禁用表达或字符 {literal!r}")

    for pattern in INTERNAL_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            failures.append(f"暴露内部维护术语 {pattern}")

    return failures


def main() -> int:
    passed = 0
    failed = 0
    for index in range(1, 17):
        name = f"boundary-{index:03d}.md"
        failures = validate(OUTPUT_DIR / name)
        if failures:
            failed += 1
            print(f"FAIL {name}")
            for item in failures:
                print(f"  - {item}")
        else:
            passed += 1
            print(f"PASS {name}")

    print(f"RESULT: {passed} passed, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
