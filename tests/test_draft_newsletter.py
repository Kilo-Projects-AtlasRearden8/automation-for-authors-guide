#!/usr/bin/env python3
"""Tests for scripts/draft_newsletter.py"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "draft_newsletter.py"


def run_script(*args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        check=False,
        capture_output=True,
        text=True,
    )


class DraftNewsletterTests(unittest.TestCase):
    def test_dry_run_prints_draft_and_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            out = tmp / "newsletter.md"

            result = run_script(
                "--book", "Example Book",
                "--update", "Chapter three is finished.",
                "--out", str(out),
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("DRY-RUN", result.stdout)
            self.assertIn("Example Book", result.stdout)
            self.assertIn("Chapter three is finished.", result.stdout)
            self.assertFalse(out.exists(), "dry-run must not create the file")

    def test_apply_writes_draft_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            out = tmp / "newsletter.md"

            result = run_script(
                "--book", "Example Book",
                "--update", "Chapter three is finished.",
                "--first-name", "Alex",
                "--out", str(out),
                "--apply",
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("APPLY", result.stdout)
            self.assertIn("Draft written to:", result.stdout)

            content = out.read_text(encoding="utf-8")
            self.assertIn("Example Book", content)
            self.assertIn("Chapter three is finished.", content)
            self.assertIn("Alex", content)
            self.assertIn("This script never sends email.", result.stdout)

    def test_creates_output_folder(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            out = tmp / "nested" / "drafts" / "newsletter.md"

            run_script(
                "--book", "Example Book",
                "--update", "Update.",
                "--out", str(out),
                "--apply",
            )
            self.assertTrue(out.exists())

    def test_missing_required_arguments_error(self):
        result = run_script("--book", "Example Book")
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
