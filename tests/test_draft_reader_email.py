#!/usr/bin/env python3
"""Tests for scripts/draft_reader_email.py"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "draft_reader_email.py"


def run_script(*args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        check=False,
        capture_output=True,
        text=True,
    )


class DraftReaderEmailTests(unittest.TestCase):
    def test_dry_run_prints_email_and_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            out = tmp / "email.md"

            result = run_script(
                "--type", "thank-you",
                "--reader", "Alex",
                "--book", "Example Book",
                "--out", str(out),
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("DRY-RUN", result.stdout)
            self.assertIn("Example Book", result.stdout)
            self.assertIn("Alex", result.stdout)
            self.assertFalse(out.exists(), "dry-run must not create the file")

    def test_apply_writes_draft_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            out = tmp / "email.md"

            result = run_script(
                "--type", "thank-you",
                "--reader", "Alex",
                "--book", "Example Book",
                "--out", str(out),
                "--apply",
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("APPLY", result.stdout)
            self.assertIn("Draft written to:", result.stdout)

            content = out.read_text(encoding="utf-8")
            self.assertIn("Example Book", content)
            self.assertIn("Alex", content)
            self.assertIn("This script never sends email.", result.stdout)

    def test_all_email_types_work(self):
        for email_type in ["thank-you", "arc", "new-release"]:
            result = run_script(
                "--type", email_type,
                "--reader", "Alex",
                "--book", "Example Book",
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Example Book", result.stdout)

    def test_new_release_includes_link(self):
        result = run_script(
            "--type", "new-release",
            "--reader", "Alex",
            "--book", "Example Book",
            "--link", "https://example.com/book",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("https://example.com/book", result.stdout)

    def test_creates_output_folder(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            out = tmp / "nested" / "emails" / "email.md"

            run_script(
                "--type", "thank-you",
                "--reader", "Alex",
                "--book", "Example Book",
                "--out", str(out),
                "--apply",
            )
            self.assertTrue(out.exists())


if __name__ == "__main__":
    unittest.main()
