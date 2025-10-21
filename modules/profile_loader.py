"""
Utility helpers for loading user-specific configuration data.

Profiles are stored as JSON files under `config/profiles/`. The active profile
can be selected via the `JOB_APPLIER_PROFILE` or `JOB_APPLIER_PROFILE_FILE`
environment variables (optionally supplied from a `.env` file).

This module keeps personal information outside of version control while allowing
the rest of the application to import strongly-typed config modules.
"""

from __future__ import annotations

import json
import os
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict

BASE_DIR = Path(__file__).resolve().parents[1]
PROFILES_DIR = BASE_DIR / "config" / "profiles"
DEFAULT_PROFILE_NAME = "active"
ENV_PROFILE_NAME = "JOB_APPLIER_PROFILE"
ENV_PROFILE_FILE = "JOB_APPLIER_PROFILE_FILE"
ENV_FILE = BASE_DIR / ".env"


def _load_dotenv() -> None:
    """
    Minimal .env loader to avoid pulling an external dependency.
    Populates os.environ with key=value pairs if not already set.
    """
    if not ENV_FILE.exists():
        return
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


def _resolve_profile_path() -> Path:
    """
    Determine which profile file to load based on environment overrides.
    """
    _load_dotenv()

    explicit_path = os.getenv(ENV_PROFILE_FILE)
    if explicit_path:
        return Path(explicit_path).expanduser().resolve()

    profile_name = os.getenv(ENV_PROFILE_NAME, DEFAULT_PROFILE_NAME)
    return (PROFILES_DIR / f"{profile_name}.json").resolve()


@lru_cache(maxsize=1)
def _load_profile() -> Dict[str, Any]:
    """
    Load the active profile JSON. Returns an empty dict if the file is missing.
    """
    profile_path = _resolve_profile_path()
    if not profile_path.exists():
        return {}
    try:
        with profile_path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Failed to parse profile JSON at '{profile_path}'. "
            "Please fix the JSON syntax."
        ) from exc


def load_section(section: str) -> Dict[str, Any]:
    """
    Return the dictionary for a specific section (e.g. 'personals', 'questions').
    """
    profile = _load_profile()
    value = profile.get(section, {})
    if not isinstance(value, dict):
        raise ValueError(
            f"Section '{section}' in the active profile must be a JSON object."
        )
    return value


def list_missing_fields(section: str, required_fields: list[str]) -> list[str]:
    """
    Helper to determine which required fields are absent or blank in the active profile.
    """
    data = load_section(section)
    missing: list[str] = []
    for field in required_fields:
        raw = data.get(field)
        if raw is None:
            missing.append(field)
            continue
        if isinstance(raw, str) and not raw.strip():
            missing.append(field)
            continue
        if isinstance(raw, (list, dict)) and not raw:
            missing.append(field)
            continue
    return missing


__all__ = ["load_section", "list_missing_fields"]
