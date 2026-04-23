# Phase 2a.5 — Rename to Stackly — Goal

**Inserted between** Phase 2a (✅ complete) and Phase 2b (paused — see ROADMAP.md). This phase is pure repository-level rebranding before any further architecture or launch work lands. Every additional commit that references `debugbridge` compounds the cost of renaming later.

## The phase goal (one sentence)

Every live surface of the project uses **Stackly** / `stackly` instead of **DebugBridge** / `debugbridge`: Python package, CLI command, MCP server name, entry points, repo slug, live docs, and CI. Archival planning docs (Phase 1, Phase 2a) stay verbatim as historical record. All tests pass. `pip install -e .` + `stackly doctor` + `stackly serve` work.

## Success criteria (phase exits when all are true)

1. **Python package renamed:**
   - `src/debugbridge/` moved to `src/stackly/` via `git mv` (history preserved)
   - Every `from debugbridge` / `import debugbridge` inside `src/stackly/**/*.py` becomes `from stackly` / `import stackly`
   - `src/stackly/__init__.py` still exports `__version__`

2. **`pyproject.toml` updated:**
   - `name = "stackly"` (base `stackly` is available on PyPI — verified 2026-04-23)
   - `[project.scripts]` has `stackly = "stackly.cli:app"` (not `debugbridge = ...`)
   - `[project.urls]` (if present) point at `https://github.com/IdanG7/stackly`
   - `uv.lock` regenerated to match the new name
   - `uv pip install -e .` succeeds

3. **MCP server + CLI branding updated:**
   - `src/stackly/server.py` — `FastMCP("stackly")` (not `FastMCP("debugbridge")`)
   - `src/stackly/cli.py` — Typer app `name="stackly"`, help text says "Stackly"
   - `src/stackly/__main__.py` — import path updated
   - `stackly serve`, `stackly doctor`, `stackly version`, `stackly fix` all runnable from a fresh install
   - Cost/cache directory convention `.debugbridge/` → `.stackly/` (in code — existing user workspaces not migrated)

4. **Tests pass:**
   - Every `tests/**/*.py` import updated
   - `tests/conftest.py` updated (it references `debugbridge.env`)
   - `uv run pytest -m "not integration"` exits 0 on a clean `uv sync`
   - Integration tests still skip cleanly when Debugging Tools are absent

5. **Scripts updated:**
   - `scripts/e2e_smoke.py` — `mcp_server_command` references `stackly serve` (or whatever it currently invokes)
   - `scripts/e2e_fix_smoke.py` — same treatment

6. **CI workflow updated:**
   - `.github/workflows/ci.yml` — all `debugbridge` references become `stackly`
   - CI runs green on the rename commit (post-push)

7. **Live docs updated:**
   - `README.md` — title, all `debugbridge` commands/imports/paths, badge URLs, install block (`pip install stackly` or `git clone https://github.com/IdanG7/stackly.git`), MCP client config snippets all reference `stackly`
   - `CONTRIBUTING.md` — all clone URLs + CLI commands + package names
   - `CHANGELOG.md` — new top entry `## [0.2.1] — Renamed to Stackly` documenting the breaking change for anyone on 0.2.0
   - `.github/ISSUE_TEMPLATE/bug_report.yml` — references to `debugbridge version` / `debugbridge doctor`
   - `.github/ISSUE_TEMPLATE/feature_request.yml`, `config.yml`, `PULL_REQUEST_TEMPLATE.md` — repo slug updates
   - `.planning/PROJECT.md`, `.planning/ROADMAP.md` — live project state updated
   - `.planning/codebase/phase-1-tech.md` — **decision:** this file describes the current codebase map. Rename. (If preferred as frozen 2026-04-16 snapshot, duplicate it into `.planning/phase-1-mcp-crash-capture/CODEBASE_SNAPSHOT.md` first, then rename the live version.)
   - `.planning/phase-2b-public-launch/*.md` — active (paused) phase docs rename to Stackly
   - `.planning/phase-2a.5-stackly-rename/*.md` — this phase's own files use Stackly throughout

8. **Archival docs preserved verbatim:**
   - `.planning/phase-2a-fix-loop-mvp/*.md` — not touched (historical record of 2a decisions when the project was DebugBridge)
   - Git history for `src/debugbridge/**/*` preserved through `git mv` (not deleted-then-added)

9. **`.claude/settings.local.json` updated:**
   - Permission allowlist entries that reference `debugbridge` CLI invocations extended with `stackly` equivalents (keep old entries as comments or remove — user's call)

10. **External artifacts handled (checkpoints — human action):**
    - GitHub repo renamed: `IdanG7/bridgeit` → `IdanG7/stackly` via `gh repo rename stackly` (or the Settings UI). GitHub installs a permanent redirect; existing clones break until users update their remote URL.
    - PyPI placeholder reserved: a `0.0.0.dev0` version of `stackly` pushed to PyPI to squat the name before anyone else takes it. (Optional but recommended.)
    - Existing MCP client configs on users' machines reference `debugbridge` — a one-line note in CHANGELOG + README covers this; no migration tool is in scope.

11. **Grep sanity check:**
    - `grep -rIi --exclude-dir=.venv --exclude-dir=.git --exclude-dir=__pycache__ --exclude-dir=.planning/phase-2a-fix-loop-mvp --exclude-dir=.planning/phase-1-mcp-crash-capture "debugbridge" . | wc -l` returns 0 (or only intentional historical callouts inside CHANGELOG's 0.2.0 entry).

## Non-goals (explicitly out of scope)

- **Domain registration.** `stackly.io` / `stackly.sh` appear unregistered but buying them is a separate user decision. The rename proceeds with GitHub URL as the canonical home.
- **Website commit.** The website mentioned in conversation has not been located in this worktree; if files arrive, they commit as a follow-up referencing Stackly from the start (no rename transformation needed).
- **Phase 2b revival.** The earlier "finish architecture first" decision stands. Phase 2b stays paused; this phase does not republish or re-pitch anything.
- **Feature changes.** Zero behavioral changes. Pure mechanical rebrand.
- **Historical planning doc rewrites.** Phase 1 + Phase 2a artifacts stay as "DebugBridge" — they are the record of what was decided when.
- **Migration tooling for existing 0.2.0 users.** There are no public users yet (never pushed to PyPI); a CHANGELOG note and README breaking-change callout is sufficient.
- **Rewriting git history** (no `git filter-branch` / `filter-repo`). The `git mv` preserves per-file history; commit SHAs stay stable.

## Constraints to respect

- **Single atomic PR.** The whole rename lands as one merge so `main` is never in a half-renamed state. Intermediate commits on the feature branch are fine and encouraged for reviewability; squashing is optional.
- **`git mv`, not delete-then-add.** Directory rename must be done with `git mv src/debugbridge src/stackly` to preserve per-file history.
- **Tests must stay green at the end of the PR.** Individual commits inside the PR may temporarily break (during the refactor), but the tip of the branch is green.
- **No changes to MCP tool signatures.** The 9 tools (attach_process, get_exception, get_callstack, get_threads, get_locals, set_breakpoint, step_next, continue_execution, detach_process) keep their exact names, parameters, and return shapes. Only the server name and package name change.
- **CHANGELOG documents the breaking change.** Anyone who built against `0.2.0`'s `debugbridge` import will break on `0.2.1`; the CHANGELOG calls this out explicitly.
- **CI runner runs green post-rename.** If the workflow file references `debugbridge` anywhere (install step, test invocation, artifact name), those update too.
- **Version bump.** Rename ships as `0.2.1` (patch bump is technically debatable for a rename, but a new PyPI name means a fresh release line anyway).

## Acceptance demo

When Phase 2a.5 is done, this sequence works on a fresh clone:

```
git clone https://github.com/IdanG7/stackly.git
cd stackly
uv sync
uv pip install -e .
uv run stackly version         # prints 0.2.1
uv run stackly doctor          # same checks, new branding
uv run stackly serve &         # MCP server starts on :8585, advertises name "stackly"
uv run pytest -m "not integration"   # green
grep -rIi --exclude-dir=.venv --exclude-dir=.git \
   --exclude-dir=.planning/phase-2a-fix-loop-mvp debugbridge . | wc -l   # 0
```

Phase exits when the above sequence passes on a fresh Windows 10/11 box (same env as Phase 2a acceptance) and the GitHub repo is live at its new slug.
