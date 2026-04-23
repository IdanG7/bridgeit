---
phase: phase-2a.5-stackly-rename
type: execute
waves: 4
depends_on: [phase-2a-fix-loop-mvp]
autonomous: false  # Waves 1-3 are autonomous; Wave 4 is checkpoints (GH repo rename, PyPI placeholder)
requirements:
  - "All live code + docs + CI use 'stackly' / 'Stackly' instead of 'debugbridge' / 'DebugBridge'"
  - "src/debugbridge/ renamed to src/stackly/ via git mv (history preserved)"
  - "pyproject.toml name, entry points, urls all updated"
  - "uv.lock regenerated; uv pip install -e . succeeds"
  - "uv run pytest -m 'not integration' exits 0"
  - "CHANGELOG documents the 0.2.1 rename as a breaking change"
  - "Archival planning docs (phase-1, phase-2a) preserved verbatim"
  - "GitHub repo renamed to IdanG7/stackly (checkpoint)"
files_modified:
  - pyproject.toml
  - uv.lock
  - README.md
  - CHANGELOG.md
  - CONTRIBUTING.md
  - src/stackly/**        # renamed from src/debugbridge/**
  - tests/**
  - scripts/e2e_smoke.py
  - scripts/e2e_fix_smoke.py
  - .github/workflows/ci.yml
  - .github/ISSUE_TEMPLATE/bug_report.yml
  - .github/ISSUE_TEMPLATE/feature_request.yml
  - .github/ISSUE_TEMPLATE/config.yml
  - .github/PULL_REQUEST_TEMPLATE.md
  - .planning/PROJECT.md
  - .planning/ROADMAP.md
  - .planning/codebase/phase-1-tech.md
  - .planning/phase-2b-public-launch/*.md  # active, paused phase — renamed
  - .claude/settings.local.json
files_preserved_verbatim:
  - .planning/phase-2a-fix-loop-mvp/*.md   # archival
  - .planning/phase-1-*/*.md  # if it exists under this slug
---

# Phase 2a.5 — Rename to Stackly — Executable Plan

**Plan date:** 2026-04-23
**Source of truth:** `GOAL.md` (11 success criteria).
**Branch strategy:** Work on current branch `claude/zealous-heyrovsky-766577`. Rename commits are a single atomic unit — the branch tip must be green before the eventual PR lands.

---

## 1. Context

Product has been called "DebugBridge" through Phase 1 and Phase 2a. The name is being officially changed to **Stackly**. Availability verified 2026-04-23:

- PyPI `stackly` — available (unlike `debugbridge` which was never published; this is a fresh PyPI name)
- GitHub repo `IdanG7/stackly` — available as personal-account repo
- `.io` / `.sh` domains appear unregistered (if desired, registration is a follow-up user action; not blocking)
- `.dev` and `.com` are parked — not available for the project

The rename is purely mechanical: zero behavioral changes, zero new features, zero regressions. It lands before Phase 2.5 (auto-detection) starts so that every subsequent commit is written against the new name.

## 2. Architecture decisions (pinned)

1. **`git mv`, not delete + add.** Directory rename preserves per-file history.
2. **Single atomic PR.** Waves 1–3 may contain multiple intermediate commits for reviewability, but the branch tip must be green before merge.
3. **No hyphen in the Python package.** `stackly` (not `stackly-mcp` or `py-stackly`) — PyPI base name is available, so we use it.
4. **CLI command matches package.** `stackly serve` / `stackly fix` / `stackly doctor` — no separate `py-stackly` / `stackly-cli` split.
5. **Version bump to 0.2.1.** Patch release even though the rename is technically breaking, because (a) there are no public 0.2.0 consumers and (b) the diff is zero behavioral surface area.
6. **Cost/cache directory `.debugbridge/` → `.stackly/`.** Only in code paths; existing user workspaces aren't migrated. CHANGELOG notes this.
7. **Archival phase docs stay verbatim.** Phase 1 and Phase 2a planning dirs are read-only archives. Touching them rewrites history.

---

## 3. Task breakdown

### Wave 1 — Atomic directory rename + internal imports (SEQUENTIAL)

These must run in order. `git mv` first; then internal imports can be fixed before we even touch any other file.

#### Task 2a.5.1 — `git mv src/debugbridge → src/stackly`

- **Files:** `src/debugbridge/` → `src/stackly/` (entire directory)
- **Action:**
  ```bash
  git mv src/debugbridge src/stackly
  git status   # confirm: renamed, not deleted+added
  ```
- **Acceptance:**
  - `ls src/` shows `stackly/` (no `debugbridge/`)
  - `git status` shows all files as `renamed:` (not `deleted:` + `new file:`)
- **Size:** XS
- **Autonomy:** AUTO

#### Task 2a.5.2 — Update all internal imports inside `src/stackly/`

- **Files:** every `*.py` inside `src/stackly/` and `src/stackly/fix/`
- **Action:**
  ```bash
  # Safe because 'debugbridge' only appears as an import target inside this tree
  grep -rl "debugbridge" src/stackly/ | xargs sed -i 's/\bdebugbridge\b/stackly/g'
  ```
  Then spot-check each file, especially `server.py` (contains `FastMCP("debugbridge")` string literal → `FastMCP("stackly")`) and `__init__.py` docstrings.
- **Acceptance:**
  - `grep -rn "debugbridge" src/stackly/` returns 0 hits
  - `uv run python -c "from stackly import __version__; print(__version__)"` prints `0.2.0` (version bump happens later)
- **Size:** S
- **Autonomy:** AUTO
- **Dependencies:** Task 2a.5.1

---

### Wave 2 — Config, tests, scripts, CI (PARALLEL — different files, no conflicts)

#### Task 2a.5.3 — Update `pyproject.toml` + regenerate `uv.lock`

- **Files:** `pyproject.toml`, `uv.lock`
- **Action:**
  1. Change `name = "debugbridge"` → `name = "stackly"`
  2. Bump `version = "0.2.0"` → `version = "0.2.1"`
  3. `[project.scripts] debugbridge = "debugbridge.cli:app"` → `stackly = "stackly.cli:app"`
  4. Any `[project.urls]` entries: swap `IdanG7/bridgeit` → `IdanG7/stackly`
  5. Run `uv sync` to regenerate `uv.lock` with the new name
  6. Run `uv pip install -e .` to confirm the editable install succeeds
- **Acceptance:**
  - `grep -n debugbridge pyproject.toml` returns 0
  - `uv run stackly --help` prints the CLI help (after `uv sync`)
  - `uv.lock` contains `name = "stackly"` not `debugbridge`
- **Size:** S
- **Autonomy:** AUTO
- **Dependencies:** Task 2a.5.2

#### Task 2a.5.4 — Update all test imports

- **Files:** `tests/**/*.py`, `tests/conftest.py`
- **Action:**
  ```bash
  grep -rl "debugbridge" tests/ | xargs sed -i 's/\bdebugbridge\b/stackly/g'
  ```
  Then sanity-check `tests/conftest.py` (it imports `debugbridge.env`).
- **Acceptance:**
  - `grep -rn "debugbridge" tests/` returns 0 hits
  - Tests that reference CLI invocations (`subprocess.run(["debugbridge", ...])`) also updated to `["stackly", ...]`
- **Size:** S
- **Autonomy:** AUTO
- **Dependencies:** Task 2a.5.2

#### Task 2a.5.5 — Update E2E scripts

- **Files:** `scripts/e2e_smoke.py`, `scripts/e2e_fix_smoke.py`
- **Action:**
  ```bash
  grep -rl "debugbridge" scripts/ | xargs sed -i 's/\bdebugbridge\b/stackly/g'
  ```
  Spot-check for subprocess invocations + MCP server name + working-directory conventions (`.debugbridge/` → `.stackly/`).
- **Acceptance:**
  - `grep -n debugbridge scripts/*.py` returns 0
  - `uv run python scripts/e2e_smoke.py --help` (or equivalent dry-run) doesn't error
- **Size:** S
- **Autonomy:** AUTO
- **Dependencies:** Task 2a.5.2

#### Task 2a.5.6 — Update CI workflow

- **Files:** `.github/workflows/ci.yml`
- **Action:** Replace every `debugbridge` occurrence with `stackly`. Pay attention to: cache keys, artifact names, test invocations, coverage output paths.
- **Acceptance:**
  - `grep -n debugbridge .github/workflows/ci.yml` returns 0
  - Workflow YAML still parses: `python -c "import yaml; yaml.safe_load(open('.github/workflows/ci.yml'))"` exits 0
- **Size:** XS
- **Autonomy:** AUTO

#### Task 2a.5.7 — Update `.claude/settings.local.json`

- **Files:** `.claude/settings.local.json`
- **Action:** Find the `debugbridge` permission entry and add a `stackly` equivalent (keep the old entry too — harmless, just unused).
- **Acceptance:**
  - `grep -c "stackly" .claude/settings.local.json` ≥ 1
  - JSON still parses: `python -c "import json; json.load(open('.claude/settings.local.json'))"` exits 0
- **Size:** XS
- **Autonomy:** AUTO

---

### Wave 3 — Docs + live planning (PARALLEL — different files, no conflicts)

#### Task 2a.5.8 — Rewrite `README.md`, `CONTRIBUTING.md`, CHANGELOG, templates

- **Files:** `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `.github/ISSUE_TEMPLATE/*.yml`, `.github/PULL_REQUEST_TEMPLATE.md`
- **Action:**
  1. README: title stays "Stackly" (H1). Replace every `debugbridge` / `DebugBridge` / `bridgeit` occurrence. Update clone URL to `https://github.com/IdanG7/stackly.git`. Update CI badge URL. Update MCP client config snippets (all `"debugbridge"` keys become `"stackly"`). Install block becomes either `pip install stackly` (once PyPI lands) or `git clone + uv sync` (for now).
  2. CONTRIBUTING: clone URL, CLI command names.
  3. CHANGELOG: **prepend a new entry** `## [0.2.1] — 2026-04-23` documenting:
     - BREAKING: Python package renamed `debugbridge` → `stackly`
     - BREAKING: CLI command renamed `debugbridge` → `stackly`
     - BREAKING: MCP server name changed; users must update their client configs
     - BREAKING: Artifact directory `.debugbridge/` → `.stackly/`
     - Repo renamed to `IdanG7/stackly`; GitHub installs a permanent redirect from `IdanG7/bridgeit`
     - No functional/behavioral changes
  4. Issue templates + PR template: `debugbridge version` → `stackly version`, repo slug updates.
- **Acceptance:**
  - `grep -rIi "debugbridge\|bridgeit" README.md CONTRIBUTING.md .github/` returns 0
  - `CHANGELOG.md` has a top-of-file `## [0.2.1]` entry with the 6 breaking-change bullets
  - The existing `## [Unreleased]` entry (added in Phase 2b) is either retained or merged into the `0.2.1` section — writer's call, but no duplication
- **Size:** M (README alone is ~185 lines with many references)
- **Autonomy:** AUTO

#### Task 2a.5.9 — Update live planning docs

- **Files:** `.planning/PROJECT.md`, `.planning/ROADMAP.md`, `.planning/codebase/phase-1-tech.md`, `.planning/phase-2b-public-launch/*.md`, `.planning/phase-2a.5-stackly-rename/*.md` (this phase's own files)
- **Action:**
  1. `PROJECT.md`: one-liner + architecture diagram labels + "Tech stack" rows. Replace `debugbridge` throughout. Title line: "**DebugBridge → Stackly** — Project Brief" (signals the rename, preserves searchability).
  2. `ROADMAP.md`: **insert new row** for Phase 2a.5 between Phase 2a and Phase 2b with status `✅ COMPLETE` (after this PR merges) or `in progress` (during execution). Change every `debugbridge` in-prose to `stackly`.
  3. `codebase/phase-1-tech.md`: **decision — option A (rename)**. The file describes current codebase, not historical decisions. Replace `debugbridge` throughout. If the snapshot-freezing option is preferred instead, copy to `.planning/phase-1-mcp-crash-capture/CODEBASE_SNAPSHOT.md` first then rename live. Default: option A.
  4. Phase 2b docs: `GOAL.md`, `PLAN.md`, `PLAN_CHECK.md`, `RESEARCH.md`, `DEMO_SCRIPT.md`, `LAUNCH_READINESS.md` — all still active (paused), not archived. Replace `debugbridge` / `DebugBridge` throughout. Note: these docs reference a future launch; rename does not re-enable them.
  5. This phase's own docs (`phase-2a.5-stackly-rename/*`) are born as Stackly, no transformation needed.
- **Acceptance:**
  - `grep -rIi "debugbridge" .planning/PROJECT.md .planning/ROADMAP.md .planning/codebase/ .planning/phase-2b-public-launch/` returns 0
  - `.planning/phase-2a-fix-loop-mvp/` is UNCHANGED (archival preservation — verify via `git status` — no entries from that directory)
- **Size:** M
- **Autonomy:** AUTO

#### Task 2a.5.10 — Global sweep check

- **Files:** none written — verification only
- **Action:** Run the canonical sweep:
  ```bash
  grep -rIi \
      --exclude-dir=.venv --exclude-dir=.git --exclude-dir=__pycache__ \
      --exclude-dir=.planning/phase-2a-fix-loop-mvp \
      --exclude-dir=.claude/worktrees \
      "debugbridge\|bridgeit" . \
    | grep -v 'CHANGELOG.md.*0\.2\.0\|CHANGELOG.md.*0\.1\.0'
  ```
  Any remaining hits must be intentional (e.g., CHANGELOG's historical `0.2.0` and `0.1.0` entries retaining "DebugBridge" for accuracy — those lines are an exception to the sweep).
- **Acceptance:**
  - Output is empty, OR output contains only CHANGELOG historical-entry lines explicitly whitelisted
- **Size:** XS
- **Autonomy:** AUTO

---

### Wave 4 — Verify + external checkpoints

#### Task 2a.5.11 — Full test suite + dogfood smoke

- **Files:** none written — verification only
- **Action:**
  ```bash
  uv sync
  uv pip install -e .
  uv run pytest -m "not integration" -v
  uv run stackly --help
  uv run stackly version    # should print 0.2.1
  uv run stackly doctor     # should pass or print clear guidance (same as 2a behavior)
  ```
- **Acceptance:**
  - pytest exits 0 (same number of tests as pre-rename; no new failures)
  - `stackly --help` prints CLI help without traceback
  - `stackly version` prints exactly `0.2.1`
- **Size:** S
- **Autonomy:** AUTO

#### Task 2a.5.12 — CHECKPOINT: rename GitHub repo

- **Action (human-confirmed, Claude can execute):**
  ```bash
  gh repo rename stackly -R IdanG7/bridgeit --confirm
  # GitHub installs a permanent redirect from IdanG7/bridgeit → IdanG7/stackly.
  # Existing 'git remote' URLs keep working via redirect but users should run:
  #   git remote set-url origin https://github.com/IdanG7/stackly.git
  ```
  After rename, update any repository-settings fields that embed the old slug:
  - Description (optional rename; current description doesn't embed the slug)
  - Homepage URL (blank until Phase 2b ships — leave blank)
- **Acceptance:**
  - `curl -s -o /dev/null -w "%{http_code}" https://github.com/IdanG7/stackly` returns 200
  - `curl -s -o /dev/null -w "%{http_code}" https://github.com/IdanG7/bridgeit` returns 301/302 (redirect to the new slug)
- **Size:** XS
- **Autonomy:** CHECKPOINT (destructive external action — confirm with user before running)
- **Resume signal:** "repo renamed to stackly"

#### Task 2a.5.13 — CHECKPOINT: reserve `stackly` on PyPI (optional but recommended)

- **Action (human-only — requires maintainer PyPI account):**
  User pushes a placeholder release:
  ```bash
  # In a throwaway scratch directory:
  mkdir -p /tmp/stackly-placeholder && cd /tmp/stackly-placeholder
  cat > pyproject.toml <<EOF
  [project]
  name = "stackly"
  version = "0.0.0.dev0"
  description = "Placeholder — real release coming in 0.2.1. See https://github.com/IdanG7/stackly."
  requires-python = ">=3.11"
  [build-system]
  requires = ["hatchling"]
  build-backend = "hatchling.build"
  EOF
  mkdir -p src/stackly && touch src/stackly/__init__.py
  uv build
  uv publish   # or: twine upload dist/*
  ```
  This squats the name. The real `0.2.1` release happens as a follow-up after this phase (or immediately — writer's call).
- **Acceptance:**
  - `curl -s https://pypi.org/pypi/stackly/json | jq .info.name` returns `"stackly"`
  - `pip install stackly==0.0.0.dev0` works from a clean venv (sanity)
- **Size:** S (15–20 min, mostly waiting on PyPI API)
- **Autonomy:** CHECKPOINT (user action — Claude has no PyPI credentials)
- **Resume signal:** "pypi placeholder reserved"

#### Task 2a.5.14 — Commit + open PR

- **Action:** Commit all Wave 1–3 changes as a series of atomic commits on `claude/zealous-heyrovsky-766577` (or a new branch `chore/phase-2a.5-stackly-rename` — writer's call; atomic-PR discipline matters more than branch name). Example commit sequence:
  - `chore(phase-2a.5): git mv src/debugbridge → src/stackly (task 2a.5.1)`
  - `chore(phase-2a.5): update internal imports inside src/stackly/ (task 2a.5.2)`
  - `chore(phase-2a.5): pyproject + uv.lock rename (task 2a.5.3)`
  - `chore(phase-2a.5): update test + script + CI imports (tasks 2a.5.4/5/6/7)`
  - `docs(phase-2a.5): rename debugbridge → stackly in README + CONTRIBUTING + CHANGELOG + templates (task 2a.5.8)`
  - `docs(phase-2a.5): rename debugbridge → stackly in live planning docs (task 2a.5.9)`
  Push branch. Open PR against `main` titled `chore: rename DebugBridge → Stackly (phase-2a.5)`.
- **Acceptance:**
  - PR is green on CI
  - PR description summarizes the 11 breaking-change bullets for reviewer visibility
  - Branch tip passes the Task 2a.5.10 sweep
- **Size:** S
- **Autonomy:** AUTO (commit) + CHECKPOINT (merge to main is user action)

---

## 4. Dependency graph

```
Wave 1 (sequential, blocking):
  2a.5.1 git mv → 2a.5.2 internal imports

Wave 2 (parallel, depends on 2a.5.2):
  2a.5.3 pyproject ∥ 2a.5.4 tests ∥ 2a.5.5 scripts ∥ 2a.5.6 CI ∥ 2a.5.7 .claude settings

Wave 3 (parallel, depends on 2a.5.3):
  2a.5.8 docs ∥ 2a.5.9 planning ∥ 2a.5.10 sweep check

Wave 4 (sequential, depends on Wave 3):
  2a.5.11 test + smoke → 2a.5.12 gh repo rename (CP) → 2a.5.13 pypi placeholder (CP) → 2a.5.14 commit + PR
```

Critical path: 2a.5.1 → 2a.5.2 → 2a.5.3 → 2a.5.11 → 2a.5.14. Estimated wall-clock for autonomous tasks: 30–60 min. Checkpoints (2a.5.12, 2a.5.13) add ~10 min each but are human-gated.

## 5. Rollback plan

If the rename breaks something not caught in tests:
- `git reset --hard <pre-rename-SHA>` on the feature branch restores state
- On `main`, nothing changed (PR not yet merged)
- GitHub repo rename (Task 2a.5.12) is reversible via `gh repo rename bridgeit -R IdanG7/stackly` — GitHub reinstalls the reverse redirect
- PyPI placeholder (Task 2a.5.13) is NOT reversible — `stackly==0.0.0.dev0` stays on PyPI forever. If the rename is abandoned, the placeholder is harmless (nobody depends on it).

## 6. Manual verification after phase exit

Reviewer confirms:

1. `git clone https://github.com/IdanG7/stackly.git` works on a fresh box
2. `uv sync` + `uv pip install -e .` succeeds
3. `stackly version` prints `0.2.1`
4. `stackly serve` starts the MCP server, advertises name `stackly`
5. Adding the new server to Claude Desktop config (key: `"stackly"` not `"debugbridge"`) connects cleanly
6. Full unit test suite green: `uv run pytest -m "not integration"`
7. No `debugbridge` references outside the archival planning dirs and CHANGELOG historical entries
