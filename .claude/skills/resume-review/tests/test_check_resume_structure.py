from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = SKILL_ROOT / "scripts" / "check_resume_structure.py"
SKILL_FILE = SKILL_ROOT / "SKILL.md"
FIXTURES = Path(__file__).resolve().parent / "fixtures"
RUBRIC = SKILL_ROOT / "references" / "rubric.md"

SPEC = importlib.util.spec_from_file_location("check_resume_structure", SCRIPT)
assert SPEC and SPEC.loader
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


class ResumeStructureTests(unittest.TestCase):
    def test_html_text_extraction_and_conventional_sections(self) -> None:
        result = CHECKER.analyze(FIXTURES / "resume.html")
        self.assertEqual(result["format"], "html")
        self.assertTrue(result["extraction"]["useful_text_extracted"])
        self.assertGreater(result["extraction"]["word_count"], 50)
        self.assertIn("Northwind Labs", result["extraction"]["text"])
        self.assertEqual(
            set(result["parser_safety"]["expected_sections"]["found"]),
            {"summary", "skills", "experience", "education"},
        )
        self.assertTrue(result["parser_safety"]["contact"]["email_visible"])
        self.assertTrue(
            result["parser_safety"]["employment_visibility"]["title_text_detected"]
        )

    def test_markdown_and_plain_text_handling(self) -> None:
        markdown = CHECKER.analyze(FIXTURES / "resume.md")
        plain = CHECKER.analyze(FIXTURES / "resume.txt")
        self.assertEqual(markdown["format"], "markdown")
        self.assertEqual(plain["format"], "text")
        self.assertTrue(markdown["extraction"]["useful_text_extracted"])
        self.assertTrue(plain["extraction"]["useful_text_extracted"])
        self.assertFalse(markdown["parser_safety"]["expected_sections"]["missing"])
        self.assertFalse(plain["parser_safety"]["expected_sections"]["missing"])

    def test_empty_or_malformed_resume_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            empty = Path(directory) / "empty.txt"
            empty.write_bytes(b"\x00\x00")
            result = CHECKER.analyze(empty)
        self.assertEqual(result["status"], "error")
        self.assertFalse(result["extraction"]["useful_text_extracted"])
        self.assertTrue(any("empty, malformed" in item for item in result["errors"]))

    def test_production_python_regression_is_flagged(self) -> None:
        result = CHECKER.analyze(FIXTURES / "production-python.md")
        findings = result["parser_safety"]["likely_jd_derived_headings"]
        self.assertIn("Production Python", [item["heading"] for item in findings])
        self.assertIn(
            "Production Python",
            [item["heading"] for item in result["parser_safety"]["nonstandard_headings"]],
        )

    def test_production_python_inline_label_and_generic_heading_are_flagged(self) -> None:
        _, nonstandard, jd_derived = CHECKER.classify_headings(
            [{"text": "Why This Candidate", "level": 2, "source": "markdown"}],
            "Production Python: FastAPI, Pydantic, internal APIs, pytest",
        )
        self.assertIn("Production Python", [item["heading"] for item in jd_derived])
        self.assertIn("Why This Candidate", [item["heading"] for item in nonstandard])

    def test_cli_output_is_valid_json(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), str(FIXTURES / "resume.html")],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["schema_version"], "1.0")
        self.assertNotIn("ats_score", payload)

    def test_pdf_without_extractor_has_clear_local_guidance(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            pdf = Path(directory) / "resume.pdf"
            pdf.write_bytes(b"%PDF-1.4\nsynthetic fixture")
            with mock.patch.object(CHECKER.shutil, "which", return_value=None):
                result = CHECKER.analyze(pdf)
        self.assertEqual(result["status"], "error")
        self.assertIn("pdftotext", result["errors"][0])
        self.assertIn("Poppler", result["errors"][0])

    def test_pdf_uses_available_local_extractor(self) -> None:
        extracted = (FIXTURES / "resume.txt").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as directory:
            pdf = Path(directory) / "resume.pdf"
            pdf.write_bytes(b"%PDF-1.4\nsynthetic fixture")
            extractor = Path(directory) / "pdftotext"
            extractor.write_text(
                "#!/usr/bin/env python3\nprint(" + repr(extracted) + ")\n",
                encoding="utf-8",
            )
            extractor.chmod(0o755)
            result = CHECKER.analyze(pdf, pdf_extractor=str(extractor))
        self.assertEqual(result["format"], "pdf")
        self.assertTrue(result["extraction"]["useful_text_extracted"])
        self.assertIn("pdftotext", result["extraction"]["extractor"])

    def test_deterministic_script_has_no_network_or_model_invocation(self) -> None:
        source = SCRIPT.read_text(encoding="utf-8").casefold()
        banned_imports = ("import requests", "import urllib", "import httpx", "import socket")
        banned_commands = ("codex exec", "claude ", "openai", "anthropic")
        for token in banned_imports + banned_commands:
            self.assertNotIn(token, source)
        self.assertNotIn("api_key", source)

    def test_skill_requires_profile_virtualenv_for_python_execution(self) -> None:
        instructions = SKILL_FILE.read_text(encoding="utf-8")
        self.assertIn("Use the profile-root `.venv` for every Python", instructions)
        self.assertIn(
            ".venv/bin/python .claude/skills/resume-review/scripts/check_resume_structure.py",
            instructions,
        )
        self.assertIn("python3 -m venv .venv", instructions)
        self.assertNotIn("python3 scripts/check_resume_structure.py", instructions)

    def test_unsupported_and_synthetic_sounding_are_distinct_findings(self) -> None:
        rubric = RUBRIC.read_text(encoding="utf-8")
        self.assertIn(
            "Do not classify unsupported language as merely synthetic-sounding.", rubric
        )
        self.assertIn("`Unsupported` is an evidence-integrity finding.", rubric)
        self.assertIn("`Synthetic-sounding` is a presentation finding", rubric)

    def test_repetitive_fixture_surfaces_style_proxies(self) -> None:
        result = CHECKER.analyze(FIXTURES / "repetitive.md")
        proxies = result["style_proxies"]
        self.assertTrue(proxies["repeated_bullet_starters"])
        self.assertGreaterEqual(proxies["uniform_accomplishment_formula_count"], 3)
        self.assertIn("robust", proxies["generic_term_counts"])
        self.assertIn("not AI-authorship detection", proxies["purpose"])

    def test_identity_bearing_fixture_preserves_concrete_signals(self) -> None:
        result = CHECKER.analyze(FIXTURES / "identity-bearing.md")
        proxies = result["style_proxies"]
        self.assertFalse(proxies["repeated_bullet_starters"])
        self.assertEqual(proxies["uniform_accomplishment_formula_count"], 0)
        self.assertGreaterEqual(proxies["concrete_detail_bullet_count"], 2)


if __name__ == "__main__":
    unittest.main()
