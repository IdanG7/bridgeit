"""Fix command dispatcher -- orchestrates hand-off and autonomous modes (task 2a.2.2).

Hand-off mode (``run_handoff``): captures crash state via MCP, writes a briefing
file and MCP config under ``.debugbridge/``, then launches an interactive Claude
Code session so the developer can collaborate on the fix.

Autonomous mode (``run_autonomous``) lands in task 2a.3.5.

Architecture constraint (PLAN.md decision #1): this module does NOT import
``debugbridge.session``. All debugger-state access goes through MCP.
"""

from __future__ import annotations

from pathlib import Path

from debugbridge.fix.briefing import extract_source_snippets, render_briefing, write_briefing
from debugbridge.fix.claude_runner import run_claude_interactive, write_mcp_config
from debugbridge.fix.mcp_client import capture_crash, ensure_server_running
from debugbridge.fix.models import FixResult
from debugbridge.fix.worktree import ensure_gitignore


def run_handoff(
    repo: Path,
    pid: int,
    host: str = "127.0.0.1",
    port: int = 8585,
    conn_str: str | None = None,
) -> FixResult:
    """Capture crash, write briefing, launch interactive Claude Code session.

    Flow:
    1. ``ensure_gitignore`` -- add ``.debugbridge/`` to ``.gitignore``.
    2. ``ensure_server_running`` -- spawn ``debugbridge serve`` if not already up.
    3. ``capture_crash`` -- attach to PID via MCP and snapshot crash state.
    4. ``extract_source_snippets`` + ``render_briefing`` + ``write_briefing``
       -- assemble the crash briefing Markdown file.
    5. ``write_mcp_config`` -- write ``mcp-config.json`` for Claude Code.
    6. ``run_claude_interactive`` -- launch claude with ``--mcp-config``,
       ``--strict-mcp-config``, and a positional message referencing the briefing.

    The server is intentionally NOT shut down after claude exits because in
    hand-off mode the user may continue interacting with Claude and the MCP
    server.

    Returns a :class:`FixResult` with ``mode="handoff"``.
    """
    mcp_url = f"http://{host}:{port}/mcp"

    # 1. Setup
    ensure_gitignore(repo)
    debugbridge_dir = repo / ".debugbridge"
    debugbridge_dir.mkdir(parents=True, exist_ok=True)

    # 2. Server
    ensure_server_running(host, port)
    try:
        # 3. Capture
        capture = capture_crash(pid, mcp_url, conn_str)

        # 4. Briefing
        snippets = extract_source_snippets(repo, capture.callstack)
        content = render_briefing(capture, snippets, build_cmd=None)
        briefing_path = debugbridge_dir / "briefings" / f"crash-{capture.crash_hash}.md"
        write_briefing(briefing_path, content)

        # 5. MCP config for Claude
        mcp_config_path = write_mcp_config(debugbridge_dir, host, port)

        # 6. Launch interactive
        briefing_rel = briefing_path.relative_to(repo)
        returncode = run_claude_interactive(repo, briefing_rel, mcp_config_path)

        return FixResult(
            ok=returncode == 0,
            mode="handoff",
            crash_hash=capture.crash_hash,
        )
    finally:
        # Don't shut down server in handoff mode -- user is now interacting.
        # If we spawned it, leave it running for the Claude session.
        pass


# TODO(task 2a.3.5): add run_autonomous(repo, pid, host, port, build_cmd, test_cmd, ...)
