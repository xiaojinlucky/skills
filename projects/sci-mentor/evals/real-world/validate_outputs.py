from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "outputs"

EXPECTED_OUTPUTS = [
    *(f"paper-{index:03d}.md" for index in range(1, 6)),
    *(f"topic-{index:03d}.md" for index in range(1, 4)),
    *(f"result-{index:03d}.md" for index in range(1, 3)),
]

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
    "进一步深入探讨",
    "为后续研究奠定基础",
    "这是一个复杂而多维的问题",
]

INTERNAL_PATTERNS = [
    r"\btask_mode\b",
    r"\bmode\b",
    r"\bstage\b",
    r"\breview_status\b",
    r"\bmethod-[a-z0-9-]+\b",
    r"方法单元",
    r"来源编号",
    r"来源账本",
    r"证据锚点",
    r"候选状态",
    r"内部评分",
]

REQUIRED_GROUPS = {
    "paper": [
        ("科学问题", "真正解决", "研究问题"),
        ("Figure", "图 1", "图1"),
        ("科研思路", "研究动作", "为什么选择", "值得学习"),
        ("边界", "不能推出", "尚未", "不足"),
        ("判断问题", "带回自己的课题", "可复用", "迁移"),
    ],
    "topic": [
        ("当前判断", "值得推进", "暂不优先"),
        ("推荐", "优先方向", "优先做", "首轮应压缩"),
        ("第一阶段", "第一步", "第一优先级"),
        ("停止", "转向", "收窄"),
    ],
    "result": [
        ("最强结论", "当前数据最多支持", "当前最多支持"),
        ("冲突", "相反", "不一致"),
        ("Figure", "图 1", "图1"),
        ("证据断点", "还缺", "缺少"),
        ("下一步", "第一优先级", "第一项"),
    ],
}


def validate_file(path: Path) -> list[str]:
    failures: list[str] = []
    if not path.exists():
        return ["文件不存在"]

    text = path.read_text(encoding="utf-8")
    if len(text.strip()) < 300:
        failures.append("输出过短或为空")

    for literal in FORBIDDEN_LITERALS:
        if literal in text:
            failures.append(f"包含禁用表达或字符 {literal!r}")

    for pattern in INTERNAL_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            failures.append(f"暴露内部维护术语 {pattern}")

    mode = path.stem.split("-")[0]
    for alternatives in REQUIRED_GROUPS.get(mode, []):
        if not any(term in text for term in alternatives):
            failures.append("缺少实质内容组 " + " / ".join(alternatives))

    return failures


def main() -> int:
    passed = 0
    failed = 0
    for name in EXPECTED_OUTPUTS:
        failures = validate_file(OUTPUT_DIR / name)
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
