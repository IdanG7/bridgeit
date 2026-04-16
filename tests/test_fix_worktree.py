"""Tests for fix/worktree.py — gitignore + git detection half (task 2a.2.1).

Subsequent worktree tests (create/remove/diff, compute_crash_hash) land in
task 2a.3.1.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from debugbridge.fix.worktree import detect_dirty, ensure_gitignore, is_git_repo


def _init_git_repo(path: Path) -> None:
    """Initialize a minimal git repo with a single commit so HEAD exists."""
    subprocess.run(["git", "init", "-q"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=path, check=True)
    (path / "README.md").write_text("# test\n", encoding="utf-8")
    subprocess.run(["git", "add", "README.md"], cwd=path, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "init"], cwd=path, check=True)


def test_is_git_repo_false_for_plain_dir(tmp_path: Path) -> None:
    assert is_git_repo(tmp_path) is False


def test_is_git_repo_true_after_init(tmp_path: Path) -> None:
    _init_git_repo(tmp_path)
    assert is_git_repo(tmp_path) is True


def test_detect_dirty_reports_clean_then_dirty(tmp_path: Path) -> None:
    _init_git_repo(tmp_path)
    assert detect_dirty(tmp_path) is False

    # Modify a tracked file → dirty.
    (tmp_path / "README.md").write_text("# changed\n", encoding="utf-8")
    assert detect_dirty(tmp_path) is True


def test_ensure_gitignore_appends_entry_when_missing(tmp_path: Path) -> None:
    _init_git_repo(tmp_path)
    gitignore = tmp_path / ".gitignore"
    gitignore.write_text("node_modules/\n", encoding="utf-8")

    ensure_gitignore(tmp_path)
    content = gitignore.read_text(encoding="utf-8")

    # Pre-existing content preserved.
    assert "node_modules/" in content
    # Debugbridge entry added (accept either "/.debugbridge/" or ".debugbridge/").
    assert "/.debugbridge/" in content or ".debugbridge/" in content


def test_ensure_gitignore_is_idempotent(tmp_path: Path) -> None:
    _init_git_repo(tmp_path)
    gitignore = tmp_path / ".gitignore"
    gitignore.write_text("node_modules/\n", encoding="utf-8")

    ensure_gitignore(tmp_path)
    first = gitignore.read_text(encoding="utf-8")
    ensure_gitignore(tmp_path)
    second = gitignore.read_text(encoding="utf-8")
    assert first == second  # Exactly identical; no double-append.


def test_ensure_gitignore_creates_file_when_missing(tmp_path: Path) -> None:
    _init_git_repo(tmp_path)
    # Ensure no .gitignore exists.
    gitignore = tmp_path / ".gitignore"
    assert not gitignore.exists()

    ensure_gitignore(tmp_path)
    assert gitignore.exists()
    content = gitignore.read_text(encoding="utf-8")
    # Exactly one entry — no stray blank lines or duplicates.
    assert content.count(".debugbridge") == 1


def test_ensure_gitignore_detects_existing_dotprefixed_entry(tmp_path: Path) -> None:
    """If .gitignore already contains '/.debugbridge/', don't double-add."""
    _init_git_repo(tmp_path)
    gitignore = tmp_path / ".gitignore"
    gitignore.write_text("/.debugbridge/\n", encoding="utf-8")

    ensure_gitignore(tmp_path)
    content = gitignore.read_text(encoding="utf-8")
    assert content.count(".debugbridge") == 1
