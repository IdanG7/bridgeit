"""Tests for fix/dispatcher.py (task 2a.2.2).

Hand-off dispatcher: capture crash via MCP, write briefing, launch interactive Claude.
All external calls (capture_crash, subprocess.run) are monkeypatched — no real server
or claude binary needed.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from debugbridge.fix.models import CrashCapture
from debugbridge.models import CallFrame, ExceptionInfo


@pytest.fixture()
def git_repo(tmp_path: Path) -> Path:
    """Initialize a bare-minimum git repo so ensure_gitignore / is_git_repo work."""
    subprocess.run(
        ["git", "init"],
        cwd=str(tmp_path),
        capture_output=True,
        check=True,
    )
    subprocess.run(
        ["git", "commit", "--allow-empty", "-m", "init"],
        cwd=str(tmp_path),
        capture_output=True,
        check=True,
    )
    return tmp_path


def _canned_capture() -> CrashCapture:
    """Return a minimal CrashCapture matching the pattern from test_fix_models.py."""
    return CrashCapture(
        pid=42,
        process_name="crash_app.exe",
        binary_path="D:/x/crash_app.exe",
        exception=ExceptionInfo(
            code=0xC0000005,
            code_name="EXCEPTION_ACCESS_VIOLATION",
            address=0x7FF612341234,
            description="Access violation",
            is_first_chance=True,
            faulting_thread_tid=5678,
        ),
        callstack=[
            CallFrame(
                index=0,
                function="crash_null",
                module="crash_app",
                instruction_pointer=0xDEAD,
            ),
        ],
        threads=[],
        locals_=[],
        crash_hash="a1b2c3d4",
    )


def test_handoff_writes_briefing_and_invokes_claude_with_correct_args(
    git_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """run_handoff must:
    1. Write briefing to .debugbridge/briefings/crash-<hash>.md
    2. Write mcp-config to .debugbridge/mcp-config.json
    3. Invoke claude with --mcp-config, --strict-mcp-config, and a positional
       message referencing the briefing via @path.
    4. Return FixResult(ok=True, mode="handoff", crash_hash=...).
    """
    canned = _canned_capture()

    # Monkeypatch capture_crash to return canned data without MCP.
    monkeypatch.setattr(
        "debugbridge.fix.dispatcher.capture_crash",
        lambda pid, mcp_url, conn_str=None: canned,
    )

    # Monkeypatch ensure_server_running to no-op (returns None = server was already up).
    monkeypatch.setattr(
        "debugbridge.fix.dispatcher.ensure_server_running",
        lambda host="127.0.0.1", port=8585, startup_timeout_s=30.0: None,
    )

    # Record subprocess.run calls from run_claude_interactive.
    recorded_calls: list[dict] = []
    original_run = subprocess.run

    def fake_subprocess_run(*args, **kwargs):
        cmd = args[0] if args else kwargs.get("args", [])
        # Only intercept "claude" calls — let git commands through.
        if cmd and cmd[0] == "claude":
            recorded_calls.append({"args": cmd, "kwargs": kwargs})
            return subprocess.CompletedProcess(args=cmd, returncode=0)
        return original_run(*args, **kwargs)

    monkeypatch.setattr("debugbridge.fix.claude_runner.subprocess.run", fake_subprocess_run)

    from debugbridge.fix.dispatcher import run_handoff

    result = run_handoff(
        repo=git_repo,
        pid=42,
        host="127.0.0.1",
        port=8585,
    )

    # 1. Briefing file exists at the expected path.
    briefing_path = git_repo / ".debugbridge" / "briefings" / f"crash-{canned.crash_hash}.md"
    assert briefing_path.exists(), f"Briefing not found at {briefing_path}"
    briefing_content = briefing_path.read_text(encoding="utf-8")
    assert "crash-a1b2c3d4" in briefing_content

    # 2. MCP config exists.
    mcp_config_path = git_repo / ".debugbridge" / "mcp-config.json"
    assert mcp_config_path.exists(), f"MCP config not found at {mcp_config_path}"

    # 3. Claude was invoked with the right args.
    assert len(recorded_calls) == 1, f"Expected 1 claude call, got {len(recorded_calls)}"
    argv = recorded_calls[0]["args"]
    assert argv[0] == "claude", f"First arg must be 'claude', got {argv[0]}"
    assert "--mcp-config" in argv, f"--mcp-config not in argv: {argv}"
    assert "--strict-mcp-config" in argv, f"--strict-mcp-config not in argv: {argv}"
    # The positional message must reference the briefing via @path.
    positional_msg = argv[-1]
    assert "@.debugbridge/briefings/crash-" in positional_msg, (
        f"Positional message must contain @.debugbridge/briefings/crash-: {positional_msg}"
    )

    # 4. FixResult shape.
    assert result.ok is True
    assert result.mode == "handoff"
    assert result.crash_hash == canned.crash_hash
