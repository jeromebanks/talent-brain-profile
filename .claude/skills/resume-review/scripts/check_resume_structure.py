#!/usr/bin/env python3
"""Deterministic resume text extraction and parser-safety checks.

This script deliberately performs no semantic evidence review, network access,
model invocation, proprietary ATS emulation, or AI-authorship detection.
"""

from __future__ import annotations

import argparse
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from typing import Iterable


CONVENTIONAL_SECTIONS = {
    "summary": "summary",
    "professional summary": "summary",
    "professional profile": "summary",
    "profile": "summary",
    "experience": "experience",
    "professional experience": "experience",
    "work experience": "experience",
    "employment": "experience",
    "employment history": "experience",
    "skills": "skills",
    "technical skills": "skills",
    "core competencies": "skills",
    "technologies": "skills",
    "languages": "skills",
    "frameworks": "skills",
    "data and platform": "skills",
    "data platforms": "skills",
    "cloud and infrastructure": "skills",
    "databases": "skills",
    "devops": "skills",
    "machine learning": "skills",
    "education": "education",
    "projects": "projects",
    "selected projects": "projects",
    "open source": "open_source",
    "open-source": "open_source",
    "leadership": "leadership",
    "technical leadership": "leadership",
    "publications": "publications",
    "patents": "patents",
    "certifications": "certifications",
    "awards": "awards",
}

EXPECTED_SECTIONS = ("summary", "experience", "skills", "education")

TITLE_RE = re.compile(
    r"\b(?:engineer|developer|architect|manager|director|principal|staff|lead|"
    r"consultant|analyst|scientist|president|founder|officer|administrator)\b",
    re.IGNORECASE,
)
EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
PHONE_RE = re.compile(r"(?<!\d)(?:\+?1[-.\s]?)?(?:\(?\d{3}\)?[-.\s])\d{3}[-.\s]\d{4}(?!\d)")
URL_RE = re.compile(r"\b(?:https?://|www\.)\S+", re.IGNORECASE)
DATE_PATTERNS = {
    "month-name": re.compile(
        r"\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
        r"Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|"
        r"Dec(?:ember)?)\.?\s+\d{4}\b",
        re.IGNORECASE,
    ),
    "numeric-month-year": re.compile(r"(?<!\d)(?:0?[1-9]|1[0-2])[/.-]\d{4}(?!\d)"),
    "iso-month": re.compile(r"(?<!\d)\d{4}-(?:0[1-9]|1[0-2])(?!\d)"),
}
YEAR_RE = re.compile(r"(?<!\d)(?:19|20)\d{2}(?!\d)")
RANGE_RE = re.compile(
    r"(?P<start>(?:19|20)\d{2}).{0,24}?(?:-|–|—|to).{0,8}?"
    r"(?P<end>(?:(?:19|20)\d{2}|present|current))",
    re.IGNORECASE,
)
SUSPICIOUS_SKILL_HEADING_RE = re.compile(
    r"^(?:production|production-grade|enterprise|mission[- ]critical|high[- ]scale|"
    r"scalable|robust)\s+(?:python|java|scala|javascript|typescript|go|rust|c\+\+|"
    r"data|ai|ml|apis?|systems?|platforms?|engineering)$",
    re.IGNORECASE,
)
GENERIC_ADJECTIVES = (
    "robust",
    "production-grade",
    "seamless",
    "cutting-edge",
    "highly scalable",
)
ABSTRACT_NOUNS = ("leadership", "innovation", "scalability", "impact")


class ExtractionError(RuntimeError):
    """Raised when deterministic local text extraction cannot proceed."""


class ResumeHTMLParser(HTMLParser):
    BLOCK_TAGS = {
        "address",
        "article",
        "br",
        "div",
        "footer",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "header",
        "li",
        "main",
        "p",
        "section",
        "tr",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.headings: list[dict[str, object]] = []
        self._skip_depth = 0
        self._heading_level: int | None = None
        self._heading_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "noscript", "svg"}:
            self._skip_depth += 1
            return
        if self._skip_depth:
            return
        if tag in self.BLOCK_TAGS:
            self.parts.append("\n")
        if tag == "li":
            self.parts.append("• ")
        if re.fullmatch(r"h[1-6]", tag):
            self._heading_level = int(tag[1])
            self._heading_parts = []

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "noscript", "svg"}:
            if self._skip_depth:
                self._skip_depth -= 1
            return
        if self._skip_depth:
            return
        if re.fullmatch(r"h[1-6]", tag) and self._heading_level is not None:
            value = normalize_inline(" ".join(self._heading_parts))
            if value:
                self.headings.append(
                    {"text": value, "level": self._heading_level, "source": "html"}
                )
            self._heading_level = None
            self._heading_parts = []
        if tag in self.BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self._skip_depth or not data:
            return
        self.parts.append(data)
        if self._heading_level is not None:
            self._heading_parts.append(data)


def normalize_inline(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def normalize_text(parts: Iterable[str] | str) -> str:
    raw = parts if isinstance(parts, str) else "".join(parts)
    lines = [normalize_inline(line) for line in raw.replace("\r", "\n").split("\n")]
    return "\n".join(line for line in lines if line)


def read_local_text(path: Path) -> tuple[str, list[str]]:
    raw = path.read_bytes()
    warnings: list[str] = []
    if b"\x00" in raw:
        warnings.append("Input contains NUL bytes and may be binary or malformed.")
    decoded = raw.decode("utf-8", errors="replace")
    if "\ufffd" in decoded:
        warnings.append("Input contained invalid UTF-8 bytes; replacement characters were used.")
    return decoded, warnings


def extract_html(path: Path) -> tuple[str, list[dict[str, object]], list[str], str]:
    source, warnings = read_local_text(path)
    parser = ResumeHTMLParser()
    try:
        parser.feed(source)
        parser.close()
    except Exception as exc:  # HTMLParser errors are rare; keep JSON output clear.
        raise ExtractionError(f"HTML parsing failed: {exc}") from exc
    return normalize_text(parser.parts), parser.headings, warnings, "python-html-parser"


def extract_markdown(path: Path) -> tuple[str, list[dict[str, object]], list[str], str]:
    source, warnings = read_local_text(path)
    headings: list[dict[str, object]] = []
    text_lines: list[str] = []
    in_fence = False
    for raw_line in source.splitlines():
        if re.match(r"^\s*```", raw_line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        heading_match = re.match(r"^\s*(#{1,6})\s+(.+?)\s*#*\s*$", raw_line)
        if heading_match:
            value = normalize_inline(heading_match.group(2))
            headings.append(
                {"text": value, "level": len(heading_match.group(1)), "source": "markdown"}
            )
            text_lines.append(value)
            continue
        line = re.sub(r"!\[([^]]*)\]\([^)]*\)", r"\1", raw_line)
        line = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", line)
        line = re.sub(r"^\s*[-*+]\s+", "• ", line)
        line = re.sub(r"[*_`]+", "", line)
        text_lines.append(line)
    return normalize_text("\n".join(text_lines)), headings, warnings, "python-markdown-text"


def detect_plain_headings(text: str) -> list[dict[str, object]]:
    headings: list[dict[str, object]] = []
    for line in text.splitlines():
        value = normalize_inline(line)
        if not value or value.startswith("• ") or len(value) > 100:
            continue
        lowered = normalize_heading(value)
        if lowered in CONVENTIONAL_SECTIONS:
            headings.append({"text": value, "level": 2, "source": "plain"})
            continue
        prefix = value.split(":", 1)[0].strip() if ":" in value else value
        if SUSPICIOUS_SKILL_HEADING_RE.fullmatch(prefix):
            headings.append({"text": prefix, "level": 3, "source": "plain-label"})
            continue
        if value.endswith(":") and len(value) <= 50 and not re.match(
            r"^(?:email|phone|location|linkedin|github|website):$", value, re.IGNORECASE
        ):
            headings.append({"text": value[:-1].strip(), "level": 2, "source": "plain"})
        elif value.isupper() and 2 <= len(value.split()) <= 5 and any(c.isalpha() for c in value):
            headings.append({"text": value, "level": 2, "source": "plain"})
    return headings


def extract_plain(path: Path) -> tuple[str, list[dict[str, object]], list[str], str]:
    source, warnings = read_local_text(path)
    text = normalize_text(source)
    return text, detect_plain_headings(text), warnings, "python-text-reader"


def extract_pdf(
    path: Path, pdf_extractor: str | None = None
) -> tuple[str, list[dict[str, object]], list[str], str]:
    extractor = pdf_extractor or shutil.which("pdftotext")
    if not extractor:
        raise ExtractionError(
            "PDF extraction requires the local 'pdftotext' executable (Poppler). "
            "Install Poppler or provide an HTML, Markdown, or plain-text resume."
        )
    try:
        completed = subprocess.run(
            [extractor, "-layout", str(path), "-"],
            check=False,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise ExtractionError(f"Local PDF extraction failed: {exc}") from exc
    if completed.returncode != 0:
        detail = normalize_inline(completed.stderr) or f"exit code {completed.returncode}"
        raise ExtractionError(f"Local PDF extraction failed: {detail}")
    text = normalize_text(completed.stdout)
    return text, detect_plain_headings(text), [], f"pdftotext:{Path(extractor).name}"


def extract_resume(
    path: Path, pdf_extractor: str | None = None
) -> tuple[str, list[dict[str, object]], list[str], str, str]:
    suffix = path.suffix.lower()
    if suffix in {".html", ".htm"}:
        text, headings, warnings, extractor = extract_html(path)
        return text, headings, warnings, extractor, "html"
    if suffix in {".md", ".markdown"}:
        text, headings, warnings, extractor = extract_markdown(path)
        return text, headings, warnings, extractor, "markdown"
    if suffix in {".txt", ".text"}:
        text, headings, warnings, extractor = extract_plain(path)
        return text, headings, warnings, extractor, "text"
    if suffix == ".pdf":
        text, headings, warnings, extractor = extract_pdf(path, pdf_extractor)
        return text, headings, warnings, extractor, "pdf"
    raise ExtractionError(
        f"Unsupported resume format '{suffix or '(no extension)'}'. "
        "Use PDF, HTML, Markdown, or plain text."
    )


def normalize_heading(value: str) -> str:
    value = re.sub(r"\s+", " ", value.strip().rstrip(":"))
    return value.casefold()


def classify_headings(
    headings: list[dict[str, object]], text: str
) -> tuple[list[str], list[dict[str, str]], list[dict[str, str]]]:
    combined = list(headings)
    seen = {normalize_heading(str(item["text"])) for item in combined}
    for item in detect_plain_headings(text):
        key = normalize_heading(str(item["text"]))
        if key not in seen:
            combined.append(item)
            seen.add(key)

    found: list[str] = []
    nonstandard: list[dict[str, str]] = []
    jd_derived: list[dict[str, str]] = []
    for item in combined:
        value = str(item["text"])
        level = int(item["level"])
        normalized = normalize_heading(value)
        conventional = CONVENTIONAL_SECTIONS.get(normalized)
        if conventional and conventional not in found:
            found.append(conventional)
            continue
        suspicious = bool(SUSPICIOUS_SKILL_HEADING_RE.fullmatch(normalized))
        if suspicious:
            finding = {
                "heading": value,
                "reason": "Nonstandard capability heading; likely wording-derived taxonomy.",
            }
            jd_derived.append(finding)
            nonstandard.append(finding)
        elif level == 2:
            nonstandard.append(
                {
                    "heading": value,
                    "reason": "Top-level heading is not in the conventional resume section set.",
                }
            )
    return found, nonstandard, jd_derived


def date_analysis(text: str) -> dict[str, object]:
    styles = [name for name, pattern in DATE_PATTERNS.items() if pattern.search(text)]
    masked = text
    for pattern in DATE_PATTERNS.values():
        masked = pattern.sub("", masked)
    if YEAR_RE.search(masked):
        styles.append("year-only")

    start_years: list[int] = []
    for line in text.splitlines():
        match = RANGE_RE.search(line)
        if match:
            start_years.append(int(match.group("start")))
    possible_reverse_order_issue = any(
        later > earlier for earlier, later in zip(start_years, start_years[1:])
    ) if len(start_years) >= 3 else False

    return {
        "date_count": len(YEAR_RE.findall(text)),
        "styles_detected": styles,
        "mixed_styles": len(styles) > 1,
        "employment_range_start_years": start_years,
        "possible_reverse_chronology_issue": possible_reverse_order_issue,
        "chronology_note": (
            "Possible issue only; ordering is inferred conservatively from visible date ranges."
            if possible_reverse_order_issue
            else "No obvious reverse-chronology issue detected from visible date ranges."
        ),
    }


def contact_analysis(text: str) -> dict[str, object]:
    lowered = text.casefold()
    email = bool(EMAIL_RE.search(text))
    phone = bool(PHONE_RE.search(text))
    url = bool(URL_RE.search(text))
    linkedin = "linkedin.com" in lowered
    github = "github.com" in lowered
    return {
        "email_visible": email,
        "phone_visible": phone,
        "url_visible": url,
        "linkedin_visible": linkedin,
        "github_visible": github,
        "contact_information_visible": email and (phone or url or linkedin or github),
    }


def employment_visibility(text: str, headings: list[dict[str, object]]) -> dict[str, object]:
    lines = text.splitlines()
    title_lines = [line for line in lines if TITLE_RE.search(line)]
    date_lines = [line for line in lines if YEAR_RE.search(line)]
    employer_like = [
        line
        for line in lines
        if YEAR_RE.search(line) and (TITLE_RE.search(line) or re.search(r"\s[|—–]\s", line))
    ]
    role_headings = [
        str(item["text"])
        for item in headings
        if int(item["level"]) >= 3 and TITLE_RE.search(str(item["text"]))
    ]
    return {
        "title_text_detected": bool(title_lines or role_headings),
        "date_text_detected": bool(date_lines),
        "company_or_employer_line_detected": bool(employer_like or role_headings),
        "title_line_count": len(title_lines),
        "date_line_count": len(date_lines),
        "employment_entry_signal_count": len(employer_like) + len(role_headings),
        "note": "Company/title/date visibility is heuristic and does not verify factual correctness.",
    }


def bullet_lines(text: str) -> list[str]:
    return [line[2:].strip() for line in text.splitlines() if line.startswith("• ")]


def style_proxy_analysis(text: str) -> dict[str, object]:
    bullets = bullet_lines(text)
    starters: dict[str, int] = {}
    formula_count = 0
    for bullet in bullets:
        words = re.findall(r"[A-Za-z][A-Za-z'-]*", bullet.casefold())
        if words:
            starter = words[0]
            starters[starter] = starters.get(starter, 0) + 1
        if re.search(
            r"^(?:led|built|developed|designed|implemented|architected)\b.*\b"
            r"(?:resulting in|driving|delivering|improving|increasing|reducing)\b",
            bullet,
            re.IGNORECASE,
        ):
            formula_count += 1

    repeated = [
        {"starter": starter, "count": count}
        for starter, count in sorted(starters.items(), key=lambda item: (-item[1], item[0]))
        if count >= 3 and bullets and count / len(bullets) >= 0.35
    ]
    lowered = text.casefold()
    generic_terms = {
        term: len(re.findall(rf"\b{re.escape(term)}\b", lowered))
        for term in GENERIC_ADJECTIVES + ABSTRACT_NOUNS
    }
    generic_terms = {term: count for term, count in generic_terms.items() if count}
    concrete_bullets = sum(
        1
        for bullet in bullets
        if re.search(
            r"\d|\b(?:after|because|instead of|tradeoff|constraint|adopted|used by|"
            r"pilot|outage|failure|unsafe)\b",
            bullet,
            re.IGNORECASE,
        )
    )
    return {
        "purpose": "Mechanical writing-pattern proxies for human review; not AI-authorship detection.",
        "bullet_count": len(bullets),
        "repeated_bullet_starters": repeated,
        "uniform_accomplishment_formula_count": formula_count,
        "generic_term_counts": generic_terms,
        "concrete_detail_bullet_count": concrete_bullets,
    }


def analyze(path: Path, pdf_extractor: str | None = None) -> dict[str, object]:
    base: dict[str, object] = {
        "schema_version": "1.0",
        "file": str(path),
        "format": path.suffix.lower().lstrip(".") or "unknown",
        "status": "error",
        "extraction": {"success": False},
        "parser_safety": {},
        "style_proxies": {},
        "warnings": [],
        "errors": [],
        "disclaimers": [
            "This is a parser-safety proxy, not a proprietary ATS simulation.",
            "This script does not detect AI authorship or evaluate factual support.",
        ],
    }
    if not path.exists():
        base["errors"] = [f"Resume file does not exist: {path}"]
        return base
    if not path.is_file():
        base["errors"] = [f"Resume path is not a file: {path}"]
        return base

    try:
        text, headings, extraction_warnings, extractor, format_name = extract_resume(
            path, pdf_extractor
        )
    except (ExtractionError, OSError) as exc:
        base["errors"] = [str(exc)]
        return base

    word_count = len(re.findall(r"\b\w+\b", text))
    useful_text = word_count >= 50
    found, nonstandard, jd_derived = classify_headings(headings, text)
    missing = [section for section in EXPECTED_SECTIONS if section not in found]
    dates = date_analysis(text)
    contacts = contact_analysis(text)
    employment = employment_visibility(text, headings)
    warnings = list(extraction_warnings)
    errors: list[str] = []

    if not useful_text:
        errors.append(
            f"Extracted only {word_count} words; the resume is empty, malformed, or not usefully parseable."
        )
    if missing:
        warnings.append("Missing conventional sections: " + ", ".join(missing) + ".")
    if nonstandard:
        warnings.append("One or more nonstandard section or capability headings need human review.")
    if not contacts["contact_information_visible"]:
        warnings.append("Contact information may not be sufficiently visible in extracted text.")
    if not employment["title_text_detected"] or not employment["date_text_detected"]:
        warnings.append("Role/title or date text may not be sufficiently visible in extracted text.")
    if dates["mixed_styles"]:
        warnings.append("Multiple date formats were detected; check consistency manually.")
    if dates["possible_reverse_chronology_issue"]:
        warnings.append("Visible date ranges may not be in reverse chronological order.")

    base.update(
        {
            "format": format_name,
            "status": "error" if errors else ("warning" if warnings else "ok"),
            "extraction": {
                "success": useful_text,
                "extractor": extractor,
                "word_count": word_count,
                "line_count": len(text.splitlines()),
                "useful_text_extracted": useful_text,
                "text": text,
            },
            "parser_safety": {
                "expected_sections": {
                    "found": found,
                    "missing": missing,
                },
                "headings": headings,
                "nonstandard_headings": nonstandard,
                "likely_jd_derived_headings": jd_derived,
                "contact": contacts,
                "employment_visibility": employment,
                "dates": dates,
            },
            "style_proxies": style_proxy_analysis(text),
            "warnings": warnings,
            "errors": errors,
        }
    )
    return base


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract resume text locally and emit parser-safety proxy JSON."
    )
    parser.add_argument("resume", type=Path, help="PDF, HTML, Markdown, or text resume")
    parser.add_argument("--pretty", action="store_true", help="indent JSON output")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    result = analyze(args.resume)
    json.dump(result, sys.stdout, indent=2 if args.pretty else None, sort_keys=True)
    sys.stdout.write("\n")
    return 2 if result["status"] == "error" else 0


if __name__ == "__main__":
    raise SystemExit(main())
