# Contributing to DebugBridge

## Welcome

Thanks for your interest in contributing. This project is in its early days and the bar for contribution is intentionally low: typo fixes, clearer docs, new tests, a repro for a flaky case, or a small bug fix are all genuinely helpful. If you are looking for somewhere to start, issues labeled [`good-first-issue`](https://github.com/IdanG7/bridgeit/issues?q=is%3Aissue+is%3Aopen+label%3Agood-first-issue) are a friendly entry point — they are scoped so you can land a change without first reading the whole codebase.

## Code of Conduct

Participation in this project is governed by [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).

## Reporting bugs

Please file bugs via the [**New Issue**](https://github.com/IdanG7/bridgeit/issues/new/choose) button on GitHub. Selecting "Bug report" surfaces the form defined in [`.github/ISSUE_TEMPLATE/bug_report.yml`](./.github/ISSUE_TEMPLATE/bug_report.yml), which asks for the reproduction steps, `debugbridge version` output, OS build, and Python version we need to investigate. A tight repro is worth more than a long description — if you can reduce the failure to one command, include it.

## Suggesting features

Feature ideas also go through the [**New Issue**](https://github.com/IdanG7/bridgeit/issues/new/choose) flow. Pick "Feature request" to get the form at [`.github/ISSUE_TEMPLATE/feature_request.yml`](./.github/ISSUE_TEMPLATE/feature_request.yml). Tell us the problem you are hitting first, and the proposed solution second — we would rather discuss the shape of a change before you invest in a PR.

## Development setup

DebugBridge development happens on Windows 10/11. You will need Python 3.11+, [uv](https://docs.astral.sh/uv/) >= 0.5, git, and the [Windows Debugging Tools](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) (required for `pybag` — integration tests will skip without them, but you cannot run the MCP server against a real process).

```bash
git clone https://github.com/IdanG7/bridgeit.git
cd bridgeit
uv sync --all-extras
uv run debugbridge doctor
```

`uv sync --all-extras` installs the `dev` extras from `pyproject.toml` (pytest, ruff, pyright). `debugbridge doctor` verifies prerequisites and prints actionable errors if anything is missing.

## Running tests

Tests are split into two groups by marker so contributors without Debugging Tools can still run the unit suite.

**Unit tests** — CI-safe, no Debugging Tools needed, runs in roughly 15 seconds:

```bash
uv run pytest -m "not integration"
```

**Integration tests** — require Windows Debugging Tools and a live process. There are currently 6 integration tests, gated by the `PYBAG_INTEGRATION` environment variable (PowerShell syntax below):

```powershell
$env:PYBAG_INTEGRATION = "1"; uv run pytest
```

CI only runs the unit suite; integration tests are maintainer-executed on a real Windows box before release.

## Code style

We use `ruff` for formatting and linting and `pyright` in basic mode for type checking. Run these before opening a PR:

```bash
uv run ruff format .
uv run ruff check .
uv run pyright
```

Ruff settings (line length 100, selected rule families, double-quote style) and pyright settings (basic mode, `src` + `tests` included) live in `pyproject.toml`. CI runs all three checks; a PR with ruff or pyright errors will not go green.

## Commit message conventions

We use [Conventional Commits](https://www.conventionalcommits.org/) — `type(scope): subject`. See [CHANGELOG.md](./CHANGELOG.md) for the in-repo style.

**Type** is one of `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, `style`, `ci`.

**Scope** follows one of two rules:

- During active phase work, use `phase-N.M` (e.g. `phase-2a`, `phase-2b`).
- Otherwise, use a module name: `core`, `cli`, `mcp`, `docs`, or `tests`.

Examples from this repo's history:

```text
feat(phase-2a): README + CHANGELOG + version bump + CI constraint
fix: strip ANSI codes in CLI help-flag test (Rich output compat)
docs(phase-2b): add CONTRIBUTING.md
```

Subject line under 72 characters, imperative mood ("add" not "added"), no trailing period.

## PR process

Branch naming: `feat/<slug>`, `fix/<slug>`, `docs/<slug>`, or `chore/<slug>`. Keep the slug short and hyphenated.

Before requesting review:

1. Your branch is rebased on the latest `main`.
2. `uv run ruff check .`, `uv run ruff format --check .`, `uv run pyright`, and `uv run pytest -m "not integration"` all pass locally.
3. The GitHub Actions [`ci.yml`](./.github/workflows/ci.yml) workflow is green on your PR — this is a hard gate for merge.
4. Fill in the PR template at [`.github/PULL_REQUEST_TEMPLATE.md`](./.github/PULL_REQUEST_TEMPLATE.md). The **Summary**, **Test plan**, and **Checklist** fields are mandatory — PRs with these left blank will be asked to revise.

Request review from [@IdanG7](https://github.com/IdanG7). We squash-merge by default; your commit history within the PR does not need to be pristine, but the squash title should follow the conventional-commits format above.

## Release process

Releases are maintainer-only. DebugBridge follows [semantic versioning](https://semver.org/): `MAJOR.MINOR.PATCH`. Breaking changes to the MCP tool surface or CLI flags bump MAJOR, new tools or flags bump MINOR, and fixes bump PATCH. See [CHANGELOG.md](./CHANGELOG.md) for the release-notes pattern (one `## [X.Y.Z] — YYYY-MM-DD` section per release, grouped by `Added` / `Changed` / `Fixed`).

To cut a release, the maintainer bumps `version` in [`pyproject.toml`](./pyproject.toml) and `__version__` in [`src/debugbridge/__init__.py`](./src/debugbridge/__init__.py), updates `CHANGELOG.md`, commits, tags `vX.Y.Z`, and pushes the tag. PyPI publishing is tracked for Phase 2c; until then, users install from source per the [README](./README.md#install).
