"""Test the command a reviewer runs, without external files or network."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

CLI = Path(__file__).with_name("intake.py")


class IntakeTest(unittest.TestCase):
    def run_intake(self, directory, *flags):
        return subprocess.run([sys.executable, str(CLI), str(directory), *flags],
                              text=True, capture_output=True)

    def test_authorized_project_does_not_traverse_or_execute(self):
        with tempfile.TemporaryDirectory() as t:
            base = Path(t).resolve()
            root = base / "project"
            outside = base / "outside"
            root.mkdir()
            outside.mkdir()
            (outside / "not-authorized.md").write_text("OUTSIDE")
            (root / "plan.md").write_text("plan")
            (root / "test_foo.py").write_text("raise Exception('generated code must never run')")
            (root / ".env").write_text("secret")
            (root / "linked.md").symlink_to(outside / "not-authorized.md")
            (root / "subdir").symlink_to(outside, target_is_directory=True)
            os.link(outside / "not-authorized.md", root / "hardlink.md")
            (root / "large.csv").write_text("a" * 2048)
            result = self.run_intake(root, "--max-bytes", "1024")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertNotIn("OUTSIDE", result.stdout)
            result = json.loads(result.stdout)
            self.assertEqual({x["path"]: x["candidate_type"] for x in result["candidates"]},
                             {"plan.md": "plan", "test_foo.py": "evaluation"})
            self.assertEqual(result["skipped"]["symlink_or_special"], 3)
            self.assertEqual(result["skipped"]["oversize"], 1)
            self.assertTrue(result["coverage_incomplete"])
            self.assertNotEqual(self.run_intake(root / "subdir").returncode, 0)
            self.assertNotEqual(self.run_intake(root / "subdir" / "not-found").returncode, 0)

    def test_excluded_entries_use_budget_and_urls_fail(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t).resolve()
            for i in range(30):
                (root / f"secret-{i}.md").write_text("")
            result = json.loads(self.run_intake(root, "--max-entries", "4").stdout)
            self.assertTrue(result["entry_limit_reached"])
            self.assertEqual(result["entries_examined"], 4)
            self.assertEqual(result["skipped"]["excluded"], 4)
            self.assertFalse(result["candidates"])
        self.assertNotEqual(self.run_intake("https://example.invalid/a").returncode, 0)
        self.assertNotEqual(self.run_intake("/").returncode, 0)


if __name__ == "__main__":
    unittest.main()
