"""Tests for env.py — Debugging Tools detection. No pybag import."""

from __future__ import annotations

import os
from pathlib import Path
from unittest.mock import patch

from debugbridge.env import (
    CANONICAL_DEBUGGERS_X64,
    check_debugging_tools,
    ensure_dbgeng_on_path,
)


def test_check_returns_structured_result() -> None:
    result = check_debugging_tools()
    # Shape only — don't assert ok=True because CI will run without tools.
    assert isinstance(result.found, dict)
    assert isinstance(result.missing, list)
    assert result.ok == (not result.missing)


def test_check_all_missing_produces_guidance() -> None:
    fake_nonexistent = Path(r"C:\definitely\not\here")
    with (
        patch("debugbridge.env.shutil.which", return_value=None),
        patch("debugbridge.env.CANONICAL_DEBUGGERS_X64", fake_nonexistent),
    ):
        result = check_debugging_tools()
    assert not result.ok
    assert "dbgsrv.exe" in result.missing
    assert result.guidance is not None
    assert "Windows SDK" in result.guidance


def test_ensure_dbgeng_on_path_idempotent() -> None:
    """Calling ensure_dbgeng_on_path twice should not duplicate the entry."""
    if not CANONICAL_DEBUGGERS_X64.exists():
        # On a machine without Debugging Tools, ensure_dbgeng_on_path is a no-op.
        ensure_dbgeng_on_path()
        return
    original_path = os.environ.get("PATH", "")
    try:
        ensure_dbgeng_on_path()
        first_count = os.environ["PATH"].count(str(CANONICAL_DEBUGGERS_X64))
        ensure_dbgeng_on_path()
        second_count = os.environ["PATH"].count(str(CANONICAL_DEBUGGERS_X64))
        assert first_count == second_count
        assert first_count >= 1
    finally:
        os.environ["PATH"] = original_path
