from __future__ import annotations

import json
import os
import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("retrieve_method_units.py")


def run_cli(*arguments: str) -> subprocess.CompletedProcess[str]:
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


class RetrieveMethodUnitsTests(unittest.TestCase):
    def test_mode_filter(self) -> None:
        result = run_cli("--mode", "paper_reading", "--limit", "20")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["result_count"], 9)

    def test_honest_stage_gap(self) -> None:
        result = run_cli("--mode", "result_storyline", "--stage", "result_ledger")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["result_count"], 0)

    def test_exact_unit(self) -> None:
        result = run_cli("--unit-id", "method-topic-hypothesis-0001")
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["result_count"], 1)
        self.assertEqual(payload["results"][0]["unit_id"], "method-topic-hypothesis-0001")

    def test_candidate_filter(self) -> None:
        result = run_cli("--review-status", "candidate", "--limit", "100")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["result_count"], 16)

    def test_evidence_view(self) -> None:
        result = run_cli(
            "--unit-id",
            "method-result-strongest-claim-0001",
            "--view",
            "evidence",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        evidence = json.loads(result.stdout)["results"][0]["evidence_links"]
        self.assertTrue(evidence)
        self.assertTrue(all(item["anchor_id"] for item in evidence))

    def test_full_dump_requires_filter(self) -> None:
        result = run_cli()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("provide at least one filter", result.stderr)


if __name__ == "__main__":
    unittest.main()
