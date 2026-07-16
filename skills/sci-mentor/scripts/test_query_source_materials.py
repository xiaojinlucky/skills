from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


SCRIPT = Path(__file__).with_name("query_source_materials.py")


def run_query(*arguments: str) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    environment["PYTHONIOENCODING"] = "utf-8"
    return subprocess.run(
        [sys.executable, str(SCRIPT), *arguments],
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=environment,
    )


def check(condition: bool, label: str, failures: list[str]) -> None:
    if not condition:
        failures.append(label)


def main() -> int:
    failures: list[str] = []
    passed = 0

    result = run_query("--query", "科学假设", "--limit", "2")
    check(result.returncode == 0, "三通道查询应成功", failures)
    if result.returncode == 0:
        output = json.loads(result.stdout)
        check(output["result_counts"] == {"zsxq": 2, "pdf": 2, "video": 2}, "三通道结果数", failures)
        check(output["status"]["video"]["text_quality"] == "asr_unverified", "视频质量标签", failures)
        check(
            all(
                "BV1spTy6DEb4" not in item["source_id"]
                for items in output["results"].values()
                for item in items
            ),
            "排除视频不得返回",
            failures,
        )
    passed += 1

    result = run_query("--query", "科学假设", "--channel", "zsxq", "--limit", "3")
    check(result.returncode == 0, "知识星球单通道查询应成功", failures)
    if result.returncode == 0:
        output = json.loads(result.stdout)
        check(list(output["results"]) == ["zsxq"], "只返回指定通道", failures)
        check(all(item["author_role"] == "bioadvance" for item in output["results"]["zsxq"]), "默认仅作者内容", failures)
    passed += 1

    result = run_query("--query", "绝不可能出现的检索词ABC987654", "--limit", "1")
    check(result.returncode == 0, "空结果查询应成功", failures)
    if result.returncode == 0:
        output = json.loads(result.stdout)
        check(all(count == 0 for count in output["result_counts"].values()), "空结果不得伪造命中", failures)
    passed += 1

    result = run_query(
        "--query",
        "框架解析 Figure 小标题",
        "--channel",
        "pdf",
        "--limit",
        "10",
    )
    check(result.returncode == 0, "基础版 PDF 查询应成功", failures)
    if result.returncode == 0:
        output = json.loads(result.stdout)
        matches = output["results"]["pdf"]
        check(
            any(
                item["content_id"]
                == "sha256:274ded5b3d35c7441243819591499fbaa9a9143f50fbbd8095f436bbe8666bce"
                for item in matches
            ),
            "基础版 OCR 内容应可检索",
            failures,
        )
        check(
            any(item["text_quality"] == "ocr_unverified" for item in matches),
            "基础版 OCR 质量标签不得升级",
            failures,
        )
    passed += 1

    with tempfile.TemporaryDirectory() as directory:
        bad_database = Path(directory) / "bad.sqlite"
        bad_database.write_bytes(b"not the approved corpus")
        result = run_query("--query", "科学假设", "--channel", "zsxq", "--zsxq-db", str(bad_database))
        check(result.returncode != 0, "数据库指纹错误必须失败", failures)
    passed += 1

    if failures:
        print(f"RESULT: {passed - len(failures)} passed, {len(failures)} failed")
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print(f"RESULT: {passed} passed, 0 failed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
