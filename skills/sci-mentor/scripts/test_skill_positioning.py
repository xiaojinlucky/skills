from __future__ import annotations

from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    paper = (SKILL_ROOT / "references" / "paper-reading.md").read_text(encoding="utf-8")
    guide = (SKILL_ROOT / "references" / "basic-guide-literature-reading.md").read_text(encoding="utf-8")
    writing = (SKILL_ROOT / "references" / "writing-quality.md").read_text(encoding="utf-8")
    checks = [
        ("表层先把文献讲清楚" in skill, "缺少文献解读表层定位"),
        ("深层还原作者如何提出问题" in skill, "缺少科研思维深层定位"),
        (
            "最终把从文献中学到的研究方法迁移到用户自己的课题" in skill,
            "缺少课题推进最终定位",
        ),
        (
            "[basic-guide-literature-reading.md](references/basic-guide-literature-reading.md)"
            in skill,
            "读文献未强制加载基础版方法",
        ),
        ("第一层，把论文讲清楚" in paper, "缺少第一层文献解释"),
        ("第二层，还原作者的科研思维" in paper, "缺少第二层科研思维"),
        ("第三层，联系用户自己的课题" in paper, "缺少第三层课题迁移"),
        ("用 Figure 还原论文骨架" in guide, "缺少基础版 Figure 框架解析"),
        ("追问论文没有直接写出的选题起点" in guide, "缺少课题起点反推"),
        ("最终落到自己的课题" in guide, "缺少课题迁移落点"),
        ("普通回答不展示 Skill 的维护语言" in writing, "缺少对外去内部术语规则"),
    ]
    failures = [label for condition, label in checks if not condition]
    passed = len(checks) - len(failures)

    if failures:
        print(f"RESULT: {passed - len(failures)} passed, {len(failures)} failed")
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print(f"RESULT: {passed} passed, 0 failed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
