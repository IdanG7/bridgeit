"""Git worktree management for the fix subpackage (task 2a.2.1 — detection half).

Landed now:
- is_git_repo: True iff path has a valid .git directory or is inside one.
- detect_dirty: True iff the working tree has uncommitted changes.
- ensure_gitignore: idempotently adds '/.debugbridge/' to .gitignore.

TODO for task 2a.3.1:
- compute_crash_hash(CrashCapture) -> str (8-char sha1 of exception + top frame)
- create_worktree(repo, crash_hash) -> Path (with stale-worktree cleanup)
- capture_diff(worktree) -> str (unified diff vs branch-off base)
- cleanup_worktree_on_success(worktree) -> None
- cleanup_worktree_on_failure(worktree) -> None
"""

from __future__ import annotations

import subprocess
from pathlib import Path

__all__ = ["detect_dirty", "ensure_gitignore", "is_git_repo"]

_GITIGNORE_ENTRY = "/.debugbridge/"


def _run_git(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    """Run a git command with UTF-8 text capture. Never raises on non-zero exit."""
    return subprocess.run(
        ["git", *args],
        cwd=str(cwd),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )


def is_git_repo(path: Path) -> bool:
    """Return True iff ``path`` is inside a git working tree.

    Uses ``git rev-parse --is-inside-work-tree``; returns False on any error
    (non-zero exit, git not on PATH, path doesn't exist).
    """
    if not path.exists():
        return False
    result = _run_git(["rev-parse", "--is-inside-work-tree"], cwd=path)
    return result.returncode == 0 and result.stdout.strip() == "true"


def detect_dirty(path: Path) -> bool:
    """Return True iff the working tree has uncommitted changes.

    Uses ``git status --porcelain``: any non-empty output = dirty. Returns False
    (pessimistically "clean") on git error — we don't want to block the fix
    agent over a false positive if git is mis-configured.
    """
    result = _run_git(["status", "--porcelain"], cwd=path)
    if result.returncode != 0:
        return False
    return bool(result.stdout.strip())


def ensure_gitignore(repo: Path) -> None:
    """Idempotently add ``/.debugbridge/`` to ``repo / '.gitignore'``.

    Creates the file if missing. Does nothing if the entry is already present
    (matching either ``/.debugbridge/`` or ``.debugbridge/`` so we don't
    duplicate a pre-existing user entry in a different form).
    """
    gitignore = repo / ".gitignore"

    existing = ""
    if gitignore.exists():
        existing = gitignore.read_text(encoding="utf-8")

    # Check for either form of the entry as a whole line.
    lines = existing.splitlines()
    already = any(
        line.strip() in ("/.debugbridge/", ".debugbridge/", "/.debugbridge", ".debugbridge")
        for line in lines
    )
    if already:
        return

    # Append; add trailing newline only if the existing file didn't end with one.
    prefix = existing
    if prefix and not prefix.endswith("\n"):
        prefix += "\n"
    gitignore.write_text(prefix + _GITIGNORE_ENTRY + "\n", encoding="utf-8")
