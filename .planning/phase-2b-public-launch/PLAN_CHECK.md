# Phase 2b — PLAN.md Checker Revision Log

**Revision:** 2 of 3
**Revised:** 2026-04-19
**Source:** Plan-checker review of `.planning/phase-2b-public-launch/PLAN.md` (1,419 lines → 1,431 lines)
**Verdict going in:** ISSUES FOUND — 0 BLOCKERs, 2 MAJORs, 4 MINORs, 3 NITs
**Verdict coming out:** all 9 issues resolved surgically; no tasks added beyond the ScopeStatus component inside existing Task 2b.B.4

Each section below records the original issue text (condensed), the fix applied, and the file:line locations of the change.

---

## MAJOR 1 — `files_modified` omits `src/stackly/__init__.py`

### Original issue

Frontmatter `files_modified` list did NOT include `src/stackly/__init__.py`, but Task 2b.F.3 step 1 modifies it ("Bump version in `pyproject.toml` and `src/stackly/__init__.py` to `0.2.1`"). This contradicts the phase-level "zero functional code changes to `src/stackly/`" constraint. Verified against repo: `__version__ = "0.2.0"` exists at line 3 of `src/stackly/__init__.py`, so the bump is real.

### Fix applied

**Both (a) and (b):**

- **(a)** Added `src/stackly/__init__.py` to frontmatter `files_modified` with trailing comment `# version-string bump only, no functional change` — makes the scope explicit in the frontmatter and discloses that the touch is packaging, not functional.
- **(b)** Rewrote Task 2b.F.3 step 1 from the single-sentence bump instruction into an explicit branch: run `grep -c '^__version__' src/stackly/__init__.py`; if 0, do NOT create the attribute (pyproject.toml is authoritative); if >= 1, bump in lockstep. Text also re-affirms the "no functional code" constraint.

### File:line changes

| File | Line | Change |
|------|------|--------|
| `.planning/phase-2b-public-launch/PLAN.md` | 19 | Added `- src/stackly/__init__.py  # version-string bump only, no functional change` inside `files_modified:` list |
| `.planning/phase-2b-public-launch/PLAN.md` | 1259 | Replaced step 1 of Task 2b.F.3 with explicit `grep -c`-driven branching |

---

## MAJOR 2 — Task 2b.F.2 uses `requests>=2.28` but it is not in pyproject.toml

### Original issue

PLAN.md specified `requests.head(url, ...)` with `"Use requests>=2.28 (already a likely transitive; else add to a [dev] optional group in pyproject.toml)"`. Verified `pyproject.toml` line 21-27 (core deps: `mcp[cli]`, `Pybag`, `pydantic`, `typer`, `rich`) and line 29-35 (dev deps: `pytest`, `pytest-asyncio`, `ruff`, `pyright`). `requests` is NOT a direct dep and `mcp[cli]` pulls `httpx`, not `requests`. First script run would `ImportError`.

### Fix applied

Replaced the `requests.head(...)` / `requests>=2.28` body of step 1 in Task 2b.F.2 with a stdlib-only spec: `urllib.request.build_opener()` + custom `HTTPRedirectHandler` to follow up to 5 redirects, `timeout=10s` on each request, 2xx / 3xx-after-redirect as pass, 4xx/5xx/timeout as fail, `urllib.parse` check before the request (skip `mailto:`, `javascript:`). Explicit guard: "Stdlib only — do NOT add any third-party HTTP client (no `requests`, no `httpx`). This keeps the script runnable without any `uv sync --extra ...` step."

Acceptance criteria for Task 2b.F.2 already reference `python scripts/check_launch_links.py ...` with exit code 0; no `uv sync --extra` step was ever listed, so no additional acceptance criterion needed removal.

### File:line changes

| File | Line | Change |
|------|------|--------|
| `.planning/phase-2b-public-launch/PLAN.md` | 1234 | Replaced `requests.head(...)` + `requests>=2.28` bullet with `urllib.request.build_opener()` spec |

---

## MINOR 1 — Task 2b.A.3 wrong task cross-reference

### Original issue

PLAN.md said `"References \`.github/ISSUE_TEMPLATE/*\` but those land in Task 2b.A.5"`. Task 2b.A.5 is SECURITY.md; issue templates are in Task 2b.A.6.

### Fix applied

Changed "Task 2b.A.5" → "Task 2b.A.6" in the dependency aside of Task 2b.A.3. Also swept for other forward-ref typos (`grep 2b.A.5`): found one unrelated typo in Task 2b.A.1 step 15 saying `"CONTRIBUTING.md itself lands in Task 2b.A.5"` — CONTRIBUTING.md is actually Task 2b.A.3. Fixed that too. Remaining `2b.A.5` occurrences (lines 437, 1284, 1290) are all legitimate references to SECURITY.md.

### File:line changes

| File | Line | Change |
|------|------|--------|
| `.planning/phase-2b-public-launch/PLAN.md` | 349 | Task 2b.A.1 step 15: `CONTRIBUTING.md itself lands in Task 2b.A.5` → `Task 2b.A.3` |
| `.planning/phase-2b-public-launch/PLAN.md` | 421 | Task 2b.A.3 dependency aside: `those land in Task 2b.A.5` → `Task 2b.A.6` |

---

## MINOR 2 — Landing page missing explicit "Today vs. Roadmap" section

### Original issue

GOAL.md constraint says "Call out what's shipping today vs. what's on the roadmap." README has this, but the landing page (Task 2b.B.4) did not mandate such a section.

### Fix applied

Added a new component `ScopeStatus.astro` to Task 2b.B.4:

- **Files list** gained `site/src/components/ScopeStatus.astro`.
- **Action section** gained a `ScopeStatus` spec: two-column block with unique anchor `id="scope-status"`; left column `Today` = "Windows 10/11 + Claude Code / Cursor / Claude Desktop + hand-off fix-loop + install from source"; right column `Roadmap` = "PyPI install (2c), crash auto-detection (2.5), Linux / macOS (3), enterprise / cloud (4)"; placed below the McpConfig install CTA and above Footer.
- **index.astro composition order** updated: `Hero -> VideoEmbed -> HowItWorks -> WhyStackly -> McpConfig -> WhoItsFor -> ScopeStatus -> Footer`.
- **Acceptance criterion** added: `grep -Ei '(today|roadmap)' site/src/pages/index.astro` returns >= 2 hits within the single `#scope-status` section; a secondary `grep -A 20 'id="scope-status"' site/src/components/ScopeStatus.astro | grep -cEi '(today|roadmap)'` returns >= 2.

### File:line changes

| File | Line | Change |
|------|------|--------|
| `.planning/phase-2b-public-launch/PLAN.md` | 604 | Added `site/src/components/ScopeStatus.astro` to Task 2b.B.4 files list |
| `.planning/phase-2b-public-launch/PLAN.md` | 617 | Added `ScopeStatus (NEW ...)` spec bullet in Action section |
| `.planning/phase-2b-public-launch/PLAN.md` | 619 | Updated index.astro composition to include ScopeStatus before Footer |
| `.planning/phase-2b-public-launch/PLAN.md` | 637 | Added grep-verifiable acceptance criterion for `Today` / `Roadmap` anchor |

---

## MINOR 3 — `lite-youtube-embed` install step is a parenthetical, not a formal step

### Original issue

"install via `npm i lite-youtube-embed` and import CSS + web component" was a parenthetical inside a bullet. Task 2b.B.2's scaffold acceptance criteria listed other Astro deps but omitted `lite-youtube-embed`.

### Fix applied

Chose option (b) — keeps Task 2b.B.2 scope limited to scaffold basics. Added a new `**Pre-step 0 (dependencies):**` bullet at the top of Task 2b.B.4's Action list, before the Hero bullet: "Run `npm i lite-youtube-embed` inside `site/`. Verify the entry appears in `site/package.json` under `dependencies`. Commit the updated `site/package.json` and `site/package-lock.json`. This MUST land before implementing the VideoEmbed component below."

### File:line changes

| File | Line | Change |
|------|------|--------|
| `.planning/phase-2b-public-launch/PLAN.md` | 610 | Inserted `Pre-step 0 (dependencies)` bullet before the Hero bullet in Task 2b.B.4 Action |

---

## MINOR 4 — Task 2b.A.1 tools-table check is weakly verifiable

### Original issue

Acceptance criterion `"Tools table has 9 rows (8 original + detach_process)"` — a reviewer could not confirm `detach_process` specifically made it vs. any other 9th row.

### Fix applied

Replaced with two-part criterion: `Tools table has exactly 9 data rows (not counting header + separator) AND grep -E '^\| detach_process' README.md returns exactly 1 match`.

### File:line changes

| File | Line | Change |
|------|------|--------|
| `.planning/phase-2b-public-launch/PLAN.md` | 358 | Replaced weak "9 rows" acceptance with 9-rows-AND-grep-matches criterion |

---

## NIT 1 — Task 2b.A.8 CHANGELOG pre-names directories that may not go live

### Original issue

CHANGELOG Unreleased pre-listed "Official MCP Registry, Smithery, LobeHub, mcp.so" before submissions are live. If Smithery (or any other) rejects, the CHANGELOG would claim a directory that isn't live at phase exit.

### Fix applied

- **Task 2b.A.8** CHANGELOG Marketing bullet genericized to: "Submitted to MCP directories (see `.planning/phase-2b-public-launch/DIRECTORY_SUBMISSIONS.md` for current status — directory names will be named specifically at release time in Task 2b.F.3 based on which submissions are live)."
- **Task 2b.F.3** gained new step 2a: "Read DIRECTORY_SUBMISSIONS.md; replace the generic Marketing bullet with the specific directory names that are `live` at phase-exit time. If a submission is still `pending` or `rejected`, do NOT list it. Minimum 4 named live directories are required to clear GOAL-4."

### File:line changes

| File | Line | Change |
|------|------|--------|
| `.planning/phase-2b-public-launch/PLAN.md` | 512 | Genericized Task 2b.A.8 CHANGELOG directory bullet |
| `.planning/phase-2b-public-launch/PLAN.md` | 1261 | Added Task 2b.F.3 step 2a to finalize CHANGELOG from tracker |

---

## NIT 2 — Wave 1 B-track DAG is sequenced, not parallel

### Original issue

Wave 1 table/narrative listed 2b.B.1, 2b.B.2, 2b.B.3 as "Wave 1" but 2b.B.3 depends on 2b.B.2 — strict parallelization would violate the DAG.

### Fix applied

Changed Wave 1 Track B narrative line to prefix with `(internal sequence: B.1 ∥ B.2 → B.3 — B.1 can run in parallel with B.2; B.3 waits for B.2)`. The Wave 1 header itself is unchanged — the internal sequencing note makes the DAG-honouring order explicit.

### File:line changes

| File | Line | Change |
|------|------|--------|
| `.planning/phase-2b-public-launch/PLAN.md` | 1296 | Prepended B-track internal sequence note to the Wave 1 Track B narrative line |

---

## NIT 3 — Task 2b.C.3 punts thumbnail path to execution time

### Original issue

Thumbnail path (`docs/demo-thumb.png` vs. `site/public/demo-thumb.png` for README embed) was unresolved — steps 8 and 9 said "pick whichever renders cleanly in GitHub's README preview before choosing".

### Fix applied

Pre-decided: **canonical is `docs/demo-thumb.png`** (renders cleanly in GitHub README preview; avoids confusion with Astro public-dir path semantics).

- **Task 2b.C.3** step 8 simplified (no longer says "Save as `site/public/demo-thumb.png`" with punt); new step 9 writes thumbnail to BOTH paths: `docs/demo-thumb.png` (canonical README) + `site/public/demo-thumb.png` (Astro-served; landing page references `/demo-thumb.png`). Two-line `cp` from canonical to site path.
- **Task 2b.A.1** README embed already uses `docs/demo-thumb.png` (step 4) — unchanged.
- **Task 2b.B.4** VideoEmbed references `/demo-thumb.png` (served from `site/public/`) — no change needed; ScopeStatus spec ordering update.
- **Task 2b.C.5** step 2 simplified: removed the "pick whichever renders" punt; now says the canonical path is already committed in Task 2b.C.3, confirm file exists, no further substitution required.

### File:line changes

| File | Line | Change |
|------|------|--------|
| `.planning/phase-2b-public-launch/PLAN.md` | 762 | Task 2b.C.3 step 8 slimmed; step 9 rewritten to commit to both paths explicitly |
| `.planning/phase-2b-public-launch/PLAN.md` | 814 | Task 2b.C.5 step 2 drops "pick whichever renders" punt; asserts docs/ path is canonical |

---

## Summary

| Severity | Count | Resolved |
|----------|-------|----------|
| BLOCKER | 0 | 0 |
| MAJOR | 2 | 2 |
| MINOR | 4 | 4 |
| NIT | 3 | 3 |
| **TOTAL** | **9** | **9** |

- **Lines of PLAN.md:** 1,419 → 1,431 (+12).
- **Tasks added:** 0 (ScopeStatus added as a component inside existing Task 2b.B.4 — no new task numbers).
- **Waves modified:** 0 (Wave 1 narrative gained a parenthetical note only; wave count and dependencies unchanged).
- **Frontmatter change:** `files_modified` gained one entry with disclosure comment.
- **Revision changelog comment:** present at PLAN.md line 134 under the title.

### Supporting tightenings (in-spirit, not separate issues)

Two follow-on edits consolidate the checker fixes — neither adds new behavior, each removes ambiguity the fix introduced:

| Change | PLAN.md line | Why |
|--------|-------------|-----|
| Task 2b.B.4 VideoEmbed bullet reworded: "(dependency installed in Pre-step 0). Import its CSS + web component from `lite-youtube-embed`." | ~612 | Removed redundant `npm i lite-youtube-embed` parenthetical now that Pre-step 0 is the install point (MINOR 3 follow-on) |
| Task 2b.C.3 acceptance criterion strengthened: requires BOTH `docs/demo-thumb.png` AND `site/public/demo-thumb.png` to exist, each 1280x720, < 500 KB, byte-equal | ~769 | Matches the two-path pre-decision in NIT 3 (the previous criterion only checked the Astro-served copy) |

### Revision budget remaining

Iteration 2 of 3 used. One iteration remains if the checker still finds issues.
