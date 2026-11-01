#!/usr/bin/env python3
"""Tests for scripts/kdp_upload_prep.py"""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "kdp_upload_prep.py"
EXAMPLE = Path(__file__).resolve().parent.parent / "scripts" / "books.example.json"


def run_script(*args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        check=False,
        capture_output=True,
        text=True,
    )


def write_metadata(folder: Path, data: dict) -> Path:
    p = folder / "book.json"
    p.write_text(json.dumps(data), encoding="utf-8")
    return p


class KdpUploadPrepTests(unittest.TestCase):
    def test_dry_run_prints_checklist_and_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            out = tmp / "kdp-prep"
            metadata = write_metadata(tmp, {
                "title": "Example Book",
                "author": "Example Author",
                "description": "A short description.",
                "keywords": ["keyword one"],
                "categories": ["Fiction"],
                "isbn": "9781234567890",
                "manuscript_file": "manuscript.docx",
                "cover_file": "cover.jpg",
            })

            result = run_script("--metadata", str(metadata), "--out", str(out))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("DRY-RUN", result.stdout)
            self.assertIn("Example Book", result.stdout)
            self.assertFalse(out.exists(), "dry-run must not create files")

    def test_apply_writes_prep_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            metadata = write_metadata(tmp, {
                "title": "Example Book",
                "author": "Example Author",
                "description": "A short description.",
                "keywords": ["keyword one"],
                "categories": ["Fiction"],
                "isbn": "9781234567890",
                "manuscript_file": "manuscript.docx",
                "cover_file": "cover.jpg",
            })
            out = tmp / "kdp-prep"

            result = run_script("--metadata", str(metadata), "--out", str(out),
                                "--apply")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("APPLY", result.stdout)

            md = (out / "kdp-prep-checklist.md").read_text(encoding="utf-8")
            self.assertIn("Example Book", md)
            self.assertIn("No issues found", md)

            manifest = json.loads((out / "kdp-prep-manifest.json").read_text(
                encoding="utf-8"))
            self.assertTrue(manifest["ready"])
            self.assertEqual(manifest["title"], "Example Book")

    def test_reports_issues(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            metadata = write_metadata(tmp, {
                "title": "",
                "author": "",
                "description": "x" * 5000,
                "keywords": ["a"] * 10,
                "categories": ["a", "b", "c"],
                "isbn": "not-an-isbn",
                "manuscript_file": "manuscript.xyz",
                "cover_file": "cover.bmp",
            })
            out = tmp / "kdp-prep"

            result = run_script("--metadata", str(metadata), "--out", str(out),
                                "--apply")
            self.assertEqual(result.returncode, 0, result.stderr)

            md = (out / "kdp-prep-checklist.md").read_text(encoding="utf-8")
            self.assertIn("Issues to fix before upload", md)
            self.assertIn("Keywords", md)
            self.assertIn("Description", md)

            manifest = json.loads((out / "kdp-prep-manifest.json").read_text(
                encoding="utf-8"))
            self.assertFalse(manifest["ready"])
            self.assertGreater(len(manifest["issues"]), 0)

    def test_example_metadata_is_clean(self):
        result = run_script("--metadata", str(EXAMPLE))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("No issues found", result.stdout)

    def test_missing_metadata_argument_error(self):
        result = run_script()
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
