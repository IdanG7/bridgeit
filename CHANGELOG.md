# Changelog

## [0.2.1] — 2026-04-23 — Renamed to Stackly

**BREAKING CHANGES.** This release is the rename of the project from DebugBridge to Stackly. Zero behavioral changes, zero new features, zero regressions — but every name-surface is new, which breaks any config that referenced the old name.

### Breaking

- **Python package renamed:** `debugbridge` → `stackly`. Imports change from `from debugbridge...` to `from stackly...`.
- **CLI command renamed:** `debugbridge` → `stackly`. Update any scripts that invoke `debugbridge serve`, `debugbridge doctor`, `debugbridge fix`, or `debugbridge version` — all four are now `stackly ...`.
- **MCP server name changed:** `debugbridge` → `stackly`. Update MCP client configs (Claude Code, Claude Desktop, Cursor) — the JSON key `"mcpServers": {"debugbridge": {...}}` becomes `"mcpServers": {"stackly": {...}}`. Claude Code's tool prefix also changed: `mcp__debugbridge__*` → `mcp__stackly__*`.
- **Artifact directory renamed:** `.debugbridge/` → `.stackly/` for briefings, patches, failure reports, and per-crash worktrees. Existing user workspaces are not migrated; the old directory can be deleted safely.
- **GitHub repo renamed:** `IdanG7/bridgeit` → `IdanG7/stackly`. GitHub installs a permanent redirect, so existing `git clone` URLs keep working, but update your remote with `git remote set-url origin https://github.com/IdanG7/stackly.git`.
- **PyPI package renamed:** was never published under `debugbridge`; fresh `stackly` release.

### Internal

- All internal `.github/`, `CI`, `tests/`, `scripts/`, `CONTRIBUTING.md`, `README.md`, and live planning docs rewritten to reference Stackly. Phase 1 and Phase 2a archival planning docs preserved verbatim as historical record.

### No functional code changes in this release.

## 0.2.0 -- Fix-loop MVP (Phase 2a)

### Added
- `debugbridge fix` command -- hand-off (interactive) and autonomous (`--auto`) modes
- `detach_process` MCP tool -- releases the target process without stopping the server
- `debugbridge doctor` now checks for `claude` CLI and bypass-permission acknowledgement
- `fix/` subpackage: crash capture via MCP, briefing generator, git worktree isolation,
  Claude Code headless subprocess wrapper, build/test runner, patch writer, retry-feedback
  loop, signal handlers, cost tracking
- Architecture constraint enforcement: CI grep step + unit test block `DebugSession` imports in `fix/`

## 0.1.0 -- MCP Crash Capture (Phase 1)

### Added
- 8 MCP tools: attach_process, get_exception, get_callstack, get_threads, get_locals,
  set_breakpoint, step_next, continue_execution
- Streamable HTTP + stdio transport via FastMCP
- `debugbridge serve`, `debugbridge doctor`, `debugbridge version` CLI
- DebugSession pybag wrapper with lazy imports and thread-safe locking
- Test crash_app C++ fixture with null/stack/throw/wait modes
