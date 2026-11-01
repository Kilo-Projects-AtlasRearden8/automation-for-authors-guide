#!/usr/bin/env python3
"""Tests for scripts/draft_social_posts.py"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "draft_social_posts.py"


def run_script(*args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        check=False,
        capture_output=True,
        text=True,
    )


class DraftSocialPostsTests(unittest.TestCase):
    def test_dry_run_prints_drafts_and_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            out = tmp / "social.md"

            result = run_script(
                "--book", "Example Book",
                "--hook", "New cover reveal!",
                "--link", "https://example.com/book",
                "--out", str(out),
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("DRY-RUN", result.stdout)
            self.assertIn("Example Book", result.stdout)
            self.assertIn("New cover reveal!", result.stdout)
            self.assertFalse(out.exists(), "dry-run must not create the file")

    def test_apply_writes_draft_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            out = tmp / "social.md"

            result = run_script(
                "--book", "Example Book",
                "--hook", "New cover reveal!",
                "--link", "https://example.com/book",
                "--out", str(out),
                "--apply",
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("APPLY", result.stdout)
            self.assertIn("Drafts written to:", result.stdout)

            content = out.read_text(encoding="utf-8")
            self.assertIn("Example Book", content)
            self.assertIn("New cover reveal!", content)
            self.assertIn("https://example.com/book", content)

    def test_platforms_listed(self):
        result = run_script(
            "--book", "Example Book",
            "--hook", "Hook",
            "--link", "https://example.com/book",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        for platform in ["X / Twitter", "Instagram caption", "Facebook post",
                         "TikTok caption", "LinkedIn post",
                         "Mastodon / Bluesky / Threads"]:
            self.assertIn(platform, result.stdout)

    def test_missing_required_arguments_error(self):
        result = run_script("--book", "Example Book")
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
