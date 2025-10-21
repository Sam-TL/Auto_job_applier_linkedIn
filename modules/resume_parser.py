"""
Utilities for ingesting resume text and extracting structured facts that can
support automated question answering.
"""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path
from typing import Dict, Iterable, List

from modules.profile_loader import load_resume_ingestion

BASE_DIR = Path(__file__).resolve().parents[1]

YEAR_NEAR_TERM = r"(?:(\d{{1,2}})\+?\s*(?:years?|yrs?)[^.\n]{{0,80}}?{term}|{term}[^.\n]{{0,80}}?(\d{{1,2}})\+?\s*(?:years?|yrs?))"


def _resolve_path(relative_path: str) -> Path:
    candidate = (BASE_DIR / relative_path).resolve()
    if candidate.exists():
        return candidate
    return Path(relative_path).expanduser().resolve()


@lru_cache(maxsize=1)
def _load_resume_text() -> str:
    config = load_resume_ingestion()
    resume_path = config.get("text_path")
    if not resume_path:
        return ""
    path = _resolve_path(resume_path)
    if not path.exists():
        return ""
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(errors="ignore")


def _normalize_skill_key(key: str) -> str:
    return key.lower().strip()


def _find_years_for_terms(text: str, terms: Iterable[str]) -> str | None:
    for term in terms:
        pattern = re.compile(YEAR_NEAR_TERM.format(term=re.escape(term)), re.IGNORECASE)
        match = pattern.search(text)
        if match:
            years = match.group(1) or match.group(2)
            if years:
                return years
    return None


@lru_cache(maxsize=1)
def get_skill_years() -> Dict[str, str]:
    """
    Return a mapping of skill keywords (lowercase) to the number of years of
    experience inferred from the resume. Falls back to user-provided defaults
    when extraction is unsuccessful.
    """
    text = _load_resume_text()
    if not text:
        return {}

    config = load_resume_ingestion()
    skill_keywords = config.get("skill_keywords", {})
    fallbacks = {
        _normalize_skill_key(k): str(v)
        for k, v in config.get("fallbacks", {}).items()
        if v is not None
    }

    results: Dict[str, str] = {}

    for raw_key, term_values in skill_keywords.items():
        key = _normalize_skill_key(raw_key)
        if isinstance(term_values, str):
            terms = [term_values]
        elif isinstance(term_values, Iterable):
            terms = [str(item) for item in term_values]
        else:
            continue

        extracted = _find_years_for_terms(text, terms)
        if extracted:
            results[key] = extracted
        elif key in fallbacks:
            results[key] = fallbacks[key]

    # Include explicit fallbacks for any skills not listed in skill_keywords
    for key, value in fallbacks.items():
        results.setdefault(key, value)

    return results


def find_years_for_label(label: str) -> str | None:
    """
    Attempt to match a question label to a known skill and return its years of
    experience.
    """
    if not label:
        return None
    normalized = label.lower()
    for skill, years in get_skill_years().items():
        if skill in normalized:
            return years
    return None


def _extract_intro(text: str, limit_words: int = 80) -> str:
    words = text.split()
    if not words:
        return ""
    excerpt = " ".join(words[:limit_words]).strip()
    return excerpt


def _format_skill_summary(skill_years: Dict[str, str]) -> str:
    if not skill_years:
        return ""
    lines = [
        f"{skill.title()}: {years} years of experience."
        for skill, years in sorted(skill_years.items())
    ]
    return "\n".join(lines)


def _additional_highlights() -> List[str]:
    config = load_resume_ingestion()
    highlights = config.get("highlights", [])
    if isinstance(highlights, str):
        return [highlights]
    if isinstance(highlights, Iterable):
        return [str(item) for item in highlights]
    return []


def compose_user_information(base_text: str) -> str:
    """
    Append auto-generated resume highlights to the provided user information
    block.
    """
    auto_lines: List[str] = []
    text = _load_resume_text()
    if text:
        intro = _extract_intro(text)
        if intro:
            auto_lines.append(intro)

    skill_summary = _format_skill_summary(get_skill_years())
    if skill_summary:
        auto_lines.append("Core Experience Highlights:")
        auto_lines.append(skill_summary)

    highlights = _additional_highlights()
    if highlights:
        auto_lines.append("Additional Highlights:")
        auto_lines.extend(highlights)

    if not auto_lines:
        return base_text

    auto_block = "\n\n".join(auto_lines).strip()
    if not auto_block:
        return base_text

    base_clean = base_text.strip()
    if base_clean:
        return base_clean + "\n\n" + auto_block
    return auto_block


__all__ = ["get_skill_years", "find_years_for_label", "compose_user_information"]
