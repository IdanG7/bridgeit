---
phase: phase-2b-public-launch
type: execute
waves: 7
depends_on: [phase-2a-fix-loop-mvp]
autonomous: false  # mixed — many non-code tasks require human action
requirements:
  - "GOAL-1: README rewrite for public audience shipped on main"
  - "GOAL-2: Landing page at stackly.dev live, Lighthouse >= 90 all four categories"
  - "GOAL-3: 60-second demo video recorded, edited, captioned, uploaded, linked"
  - "GOAL-4: Submitted to >= 4 MCP directories, tracked in DIRECTORY_SUBMISSIONS.md"
  - "GOAL-5: Launch post drafts (HN, Reddit, Twitter) written, stored, NOT published"
  - "GOAL-6: Open-source scaffolding (CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, GH metadata, issue/PR templates)"
  - "GOAL-7: Discoverability sanity (robots.txt, sitemap.xml, GSC, repo description/homepage/topics)"
files_modified:
  - README.md
  - CHANGELOG.md
  - pyproject.toml
  - src/stackly/__init__.py  # version-string bump only, no functional change
  - CONTRIBUTING.md
  - CODE_OF_CONDUCT.md
  - SECURITY.md
  - .github/ISSUE_TEMPLATE/bug_report.yml
  - .github/ISSUE_TEMPLATE/feature_request.yml
  - .github/ISSUE_TEMPLATE/config.yml
  - .github/PULL_REQUEST_TEMPLATE.md
  - .gitattributes
  - site/**
  - server.json
  - .planning/phase-2b-public-launch/DEMO_SCRIPT.md
  - .planning/phase-2b-public-launch/LAUNCH_POSTS.md
  - .planning/phase-2b-public-launch/DIRECTORY_SUBMISSIONS.md
  - .planning/phase-2b-public-launch/LAUNCH_READINESS.md
must_haves:
  truths:
    # GOAL-1
    - "Stranger lands on README and understands the product in <60s"
    - "Stranger follows README quickstart on fresh Windows 10/11 box and reaches `stackly fix` hand-off"
    # GOAL-2
    - "stackly.dev resolves to a static landing page served over HTTPS"
    - "Landing page Lighthouse score >= 90 for Performance, Accessibility, Best Practices, SEO"
    - "Landing page embeds the 60s demo video above the fold"
    - "Landing page source committed to repo under site/"
    # GOAL-3
    - "60s demo video exists on YouTube (public), linked from README + landing page"
    - "Demo video has captions/subtitles"
    # GOAL-4
    - ">= 4 MCP directory submissions live or pending, tracked in DIRECTORY_SUBMISSIONS.md"
    # GOAL-5
    - "HN, Reddit (r/cpp + r/gamedev), Twitter drafts exist in LAUNCH_POSTS.md, explicitly unpublished"
    # GOAL-6
    - "CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md exist at repo root"
    - ".github/ISSUE_TEMPLATE/{bug_report.yml,feature_request.yml,config.yml} and .github/PULL_REQUEST_TEMPLATE.md exist"
    - "GitHub repo description, homepage, and topics are set"
    # GOAL-7
    - "robots.txt + sitemap.xml served from landing page"
    - "Google Search Console verified for stackly.dev, sitemap submitted"
  artifacts:
    - path: "README.md"
      provides: "Public-audience README (hero, quickstart, architecture diagram, MCP client configs, troubleshooting, demo embed)"
      min_lines: 180
    - path: "CONTRIBUTING.md"
      provides: "First-time contributor onramp"
      min_lines: 60
    - path: "CODE_OF_CONDUCT.md"
      provides: "Contributor Covenant 2.1 verbatim"
      min_lines: 100
    - path: "SECURITY.md"
      provides: "Responsible-disclosure policy"
      min_lines: 10
    - path: ".github/ISSUE_TEMPLATE/bug_report.yml"
      provides: "Structured bug report form"
    - path: ".github/ISSUE_TEMPLATE/feature_request.yml"
      provides: "Structured feature request form"
    - path: ".github/ISSUE_TEMPLATE/config.yml"
      provides: "Disables blank issues, adds Discussions + Security links"
    - path: ".github/PULL_REQUEST_TEMPLATE.md"
      provides: "PR checklist (tests, CHANGELOG, commit conventions)"
    - path: "site/astro.config.mjs"
      provides: "Astro project root with tailwind + sitemap integrations"
    - path: "site/src/pages/index.astro"
      provides: "Single-page landing page"
    - path: "site/src/layouts/BaseLayout.astro"
      provides: "SEO + OG + Twitter card meta via astro-seo"
    - path: "site/public/robots.txt"
      provides: "Allow-all robots + sitemap link"
    - path: "server.json"
      provides: "MCP Registry submission manifest (source-only via websiteUrl)"
    - path: ".planning/phase-2b-public-launch/DEMO_SCRIPT.md"
      provides: "Reviewed demo script used for recording"
    - path: ".planning/phase-2b-public-launch/LAUNCH_POSTS.md"
      provides: "HN + Reddit + Twitter launch drafts, clearly marked unpublished"
    - path: ".planning/phase-2b-public-launch/DIRECTORY_SUBMISSIONS.md"
      provides: "MCP directory submission tracker (directory, URL, date, status)"
    - path: ".planning/phase-2b-public-launch/LAUNCH_READINESS.md"
      provides: "Final go/no-go checklist mapping each GOAL criterion to proof"
  key_links:
    - from: "README.md"
      to: "YouTube demo video URL"
      via: "thumbnail markdown link in hero section"
      pattern: "youtu\\.be|youtube\\.com"
    - from: "README.md"
      to: "https://stackly.dev"
      via: "footer links + hero CTA"
      pattern: "stackly\\.dev"
    - from: "site/src/pages/index.astro"
      to: "YouTube demo video URL"
      via: "VideoEmbed.astro (lite-youtube-embed wrapper)"
      pattern: "lite-youtube|youtube"
    - from: "site/src/pages/index.astro"
      to: "https://github.com/IdanG7/stackly"
      via: "hero + footer CTA buttons"
      pattern: "github\\.com/IdanG7/stackly"
    - from: "site/public/robots.txt"
      to: "https://stackly.dev/sitemap-index.xml"
      via: "Sitemap: directive"
      pattern: "Sitemap:"
    - from: "server.json"
      to: "https://stackly.dev"
      via: "websiteUrl field"
      pattern: "websiteUrl"
    - from: "server.json"
      to: "https://github.com/IdanG7/stackly"
      via: "repository.url field"
      pattern: "repository"
    - from: ".planning/phase-2b-public-launch/DIRECTORY_SUBMISSIONS.md"
      to: "Official MCP Registry + Smithery + LobeHub + mcp.so entries"
      via: "tracker rows with submission URL + listing URL + status"
      pattern: "Official MCP Registry|Smithery|LobeHub|mcp\\.so"
---

# Phase 2b — Public Launch — Executable Plan

<!-- Revision 2 (iteration 2/3) — applied 9 checker fixes: 2 MAJOR (frontmatter files_modified + requests→stdlib), 4 MINOR (A.3 cross-ref, landing ScopeStatus, lite-youtube-embed step, tools-table grep), 3 NIT (CHANGELOG generic, Wave-1 B-track sequencing note, thumbnail path pre-decision). See .planning/phase-2b-public-launch/PLAN_CHECK.md. -->

**Plan date:** 2026-04-18
**Phase goal (one sentence):** Stackly is discoverable and installable by strangers on the internet — a stranger lands on a page, understands the product in under 60 seconds, follows a quickstart that works on a fresh Windows dev machine, and finds the project via multiple independent channels (MCP directories, HN, Reddit, Twitter, search).
**Source of truth:** `GOAL.md` (7 acceptance criteria), `RESEARCH.md` (Standard Stack in §Standard Stack, DAG in §11, effort estimates in §12, 9 Open Questions), `../ROADMAP.md` (Phase 2b scope lines 35-44).

---

## 1. Context

Phase 2a ships the `stackly fix` fix-loop MVP — the product surface is now demonstrable end-to-end (remote crash -> capture -> Claude Code hand-off -> diagnosis/patch). Phase 2b is pure marketing + packaging: it does NOT touch `src/stackly/`. Zero functional code changes. The job is to turn "a GitHub repo you can clone" into "a discoverable product strangers can find and install."

Seven deliverables, seven GOAL criteria, mapped to the `must_haves.truths` block above: README rewrite, landing page, demo video, 4 directory submissions, launch post drafts, OSS scaffolding (CONTRIBUTING/COC/SECURITY/.github templates), discoverability (GSC + repo metadata). Most of this is parallelizable — the RESEARCH.md §11 DAG identifies 4 mostly-independent tracks plus a final merge wave.

Explicitly deferred (from GOAL.md non-goals): PyPI publish (2c), docs site (2c), actually publishing launch posts (separate go/no-go), paid analytics, README translations, non-Windows demo content, enterprise landing copy, signed wheels, post-install hooks.

## 2. Architecture decisions (pinned)

These are locked for Phase 2b. Changing any of them requires updating this plan first.

1. **Landing page lives in `site/` subfolder of the Stackly repo** (not a sibling repo). Rationale: single CI, single deploy key, single place to search — solo-maintainer debt avoided. (RESEARCH.md §1, Open Question Q2 — resolved by planner per research recommendation.) GitHub's language-stats bar is kept Python-dominant via a `.gitattributes` entry marking `site/**` as `linguist-documentation` (or `linguist-vendored` if documentation flag proves insufficient).

2. **Stack: Astro 6 + Tailwind v4 + `@astrojs/sitemap` + `astro-seo`, deployed to Cloudflare Pages, domain on Cloudflare Registrar.** No Vercel (commercial-use clause), no Next.js (overkill), no plain HTML (Lighthouse SEO hard without plugins). (RESEARCH.md §Standard Stack, §1, §2.)

3. **Demo video hosted on YouTube, embedded via `lite-youtube-embed`.** No self-hosted MP4 on the landing page (tanks LCP). (RESEARCH.md §5, R3.)

4. **Demo script uses hand-off mode** (matches 2a default + honest-marketing constraint — no autonomous PR creation shown). (RESEARCH.md §5, Open Question Q5 — resolved.)

5. **MCP directory submission strategy: 2 active + 2 passive + 2 bonus.** Active = Official MCP Registry + Smithery. Passive = PulseMCP (ingests from Official Registry) + GitHub MCP Registry (ingests from Official Registry). Bonus = LobeHub + mcp.so + `awesome-mcp-servers` PR. "Submit to >= 4" in GOAL-4 is cleared by Official + Smithery + LobeHub + mcp.so, with PulseMCP/GitHub-MCP-Registry as free downstream wins. (RESEARCH.md §6.)

6. **Source-only MCP Registry submission via `websiteUrl`** — no PyPI dependency. The official schema accepts a minimal `server.json` with `repository` + `websiteUrl` and no `packages[]` array. (RESEARCH.md §6A.) Upgrade path in 2c: add `packages[]` with PyPI entry, re-publish.

7. **Launch posts: drafts only, stored in `.planning/phase-2b-public-launch/LAUNCH_POSTS.md`, with a `> NOT YET PUBLISHED — publication is a separate go/no-go.` banner at the top.** Publishing is a post-2b decision. (GOAL.md criterion 5, R7.)

8. **Analytics: Cloudflare Web Analytics** (cookieless, first-party, no banner). No second vendor. (RESEARCH.md §10.)

9. **No Lighthouse CI merge gate in 2b.** Manual Lighthouse runs before the landing page is announced are sufficient. (RESEARCH.md Open Question Q9 — resolved: defer to 2c or later.)

10. **Blog post (r/programming technical post) is deferred to 2c.** Phase 2b includes a `r/programming` draft ONLY as an entry in LAUNCH_POSTS.md marked `DEFERRED_TO_2C` — the active Reddit drafts are `r/cpp` + `r/gamedev`. (RESEARCH.md Open Question Q4 — resolved.)

### Open questions left to the executor as human-gated CHECKPOINTs

Four open questions from RESEARCH.md that the planner cannot resolve from a workspace (they need real-world information):

- **Q1 (domain availability).** Task 2b.0.1 is a CHECKPOINT: human runs WHOIS / registrar search, registers immediately if available, picks a fallback name if not. Fallback order: `stackly.app` > `getstackly.dev` > `usestackly.dev` > `stackly.run`.
- **Q3 (Twitter handle).** Task 2b.0.3 is a CHECKPOINT: human confirms `@IdanG7` is live or provides the correct handle, OR decides to skip Twitter entirely (in which case task 2b.D.3 becomes no-op and LAUNCH_POSTS.md reflects a two-platform launch).
- **Q8 (YouTube channel — personal vs project).** Task 2b.0.4 is a CHECKPOINT: human decides `personal @IdanG7` vs newly-created `Stackly` project channel. Affects task 2b.C.4 metadata.
- **Q6 (Reddit subreddit rules current state).** Task 2b.F.1 (launch-readiness) includes a re-verification step: human checks r/cpp and r/gamedev sidebars at submission time. Not a CHECKPOINT at planning time, but a pre-publication check baked into the LAUNCH_READINESS checklist.

## 3. Component / deliverable breakdown

Production artifacts, grouped by track:

```
D:/Projects/BridgeIt/
├── README.md                                  # REWRITTEN (Track A)
├── CHANGELOG.md                               # bump to 0.2.1 "docs + public launch"
├── pyproject.toml                             # version = "0.2.1"
├── CONTRIBUTING.md                            # NEW (Track A)
├── CODE_OF_CONDUCT.md                         # NEW (Track A)
├── SECURITY.md                                # NEW (Track A)
├── server.json                                # NEW (Track E)
├── .gitattributes                             # NEW (language-stats protection for site/)
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml                     # NEW
│   │   ├── feature_request.yml                # NEW
│   │   └── config.yml                         # NEW
│   └── PULL_REQUEST_TEMPLATE.md               # NEW
├── site/                                      # NEW (Track B)
│   ├── package.json
│   ├── astro.config.mjs                       # tailwind + sitemap integrations
│   ├── tailwind.config.mjs
│   ├── .gitignore                             # node_modules, dist
│   ├── public/
│   │   ├── favicon.svg
│   │   ├── og-image.png                       # 1200x630 social preview
│   │   ├── logo.svg
│   │   └── robots.txt
│   └── src/
│       ├── layouts/BaseLayout.astro           # astro-seo + CF analytics beacon
│       ├── components/
│       │   ├── Hero.astro
│       │   ├── VideoEmbed.astro               # lite-youtube-embed
│       │   ├── HowItWorks.astro
│       │   ├── WhyStackly.astro
│       │   ├── McpConfig.astro                # tabbed: Claude Code / Cursor / Claude Desktop
│       │   ├── WhoItsFor.astro
│       │   └── Footer.astro
│       └── pages/index.astro
└── .planning/phase-2b-public-launch/
    ├── DEMO_SCRIPT.md                         # NEW (Track A)
    ├── LAUNCH_POSTS.md                        # NEW (Track D)
    ├── DIRECTORY_SUBMISSIONS.md               # NEW (Track E)
    └── LAUNCH_READINESS.md                    # NEW (Track F — go/no-go checklist)
```

Track-level responsibility summary:

- **Track 0 (Prep).** Day-0 CHECKPOINTs for the 4 unresolved open questions. Domain registration is the only task that MUST happen Day 0 (squat risk). Twitter + YouTube decisions can happen later but block their respective track tails.
- **Track A (Content).** README rewrite, demo script, open-source scaffolding files. All text work. No external dependencies.
- **Track B (Infra).** Domain -> Cloudflare Pages -> Astro scaffold -> component work -> deploy. Needs demo video URL from Track C for final VideoEmbed wiring.
- **Track C (Video).** Script (from Track A) -> OBS recording -> Descript editing -> captions + thumbnail -> YouTube upload. Hard dependency: script exists.
- **Track D (Distribution).** Launch post drafts + GitHub repo metadata + social preview image. Can all start Day 0.
- **Track E (Directory submissions).** MCP Registry + Smithery + LobeHub + mcp.so + awesome-mcp-servers PR. Depends on README done + landing page URL live + video URL live.
- **Track F (Launch readiness).** Final merge: CHANGELOG bump, all-hands Lighthouse run, go/no-go checklist.

## 4. Atomic task list (the executable part)

Task-size legend: **XS** <= 10 min, **S** 10-30 min, **M** 30-60 min, **L** 1-3h (flagged for splitting if it grows), **XL** 3-8h (split wherever possible).
Autonomy legend: **AUTO** = Claude executes alone; **CHECKPOINT** = human interaction required (form submission, domain registration, video recording, external account login, publish-to-YouTube, etc.). Each CHECKPOINT task names its resume signal.

Global note: Phase 2b has near-zero code, so RED-first TDD is only triggered for the two small scripts that ARE code (link-checker and Lighthouse runner in Task 2b.F.2). Everything else is prose/markdown/config/form-submission and uses direct acceptance criteria.

---

### Phase 2b.0 — Prep (Day-0 CHECKPOINTs + open-question resolution)

Run these before committing to any other track. Domain registration MUST be Day 0 (squat risk R1).

#### Task 2b.0.1 — Verify `stackly.dev` availability and register

- **Files:** none (external action). Record outcome in `.planning/phase-2b-public-launch/DOMAIN.md` (new file — single line: `Registered stackly.dev at Cloudflare Registrar on 2026-MM-DD` or `Fallback chosen: <name>, reason: <primary taken>`).
- **Action (CHECKPOINT — human):**
  1. Check availability at [cloudflare.com/application-services/products/registrar/buy-dev-domains](https://www.cloudflare.com/application-services/products/registrar/buy-dev-domains/) or run `whois stackly.dev` on a box with WHOIS tooling.
  2. If available: register `stackly.dev` at Cloudflare Registrar (at-cost ~$10-12/yr, free WHOIS privacy). Do NOT register at Namecheap/Porkbun — Cloudflare Registrar auto-integrates DNS with Pages (Task 2b.B.4).
  3. If taken: pick fallback in this order — `stackly.app` > `getstackly.dev` > `usestackly.dev` > `stackly.run`. Update all references in this plan and in GOAL.md (`s/stackly.dev/<chosen>/g`). Commit the rename in a single diff titled `chore(phase-2b): rename landing domain to <chosen>`.
  4. Write `.planning/phase-2b-public-launch/DOMAIN.md` with: chosen domain, registrar, registration date, (if fallback) reason.
- **Acceptance criteria:**
  - Domain is registered under the maintainer's Cloudflare account (or fallback, documented).
  - `DOMAIN.md` exists and records the choice.
  - If fallback was needed, every `stackly.dev` reference in this plan, GOAL.md, and RESEARCH.md (search-and-replace scope documented in DOMAIN.md) is updated.
- **Size:** S (10 min if available and clean)
- **Autonomy:** CHECKPOINT
- **Resume signal:** "domain registered: <name>" or "fallback chosen: <name>"
- **Dependencies:** none.

#### Task 2b.0.2 — Set up Cloudflare Email Routing aliases

- **Files:** none (external action). Record outcome in `.planning/phase-2b-public-launch/DOMAIN.md` (append section: `Email aliases configured: security@, coc@, hello@ -> <maintainer inbox>`).
- **Action (CHECKPOINT — human):**
  1. Cloudflare dashboard -> Email -> Email Routing -> Enable for the registered domain.
  2. Create three custom address forwards: `security@<domain>`, `coc@<domain>`, `hello@<domain>` -> maintainer's real inbox.
  3. Verify destination address via the email Cloudflare sends.
  4. Send a test message to `security@<domain>` and confirm it arrives.
  5. Append outcome to `DOMAIN.md`.
- **Acceptance criteria:**
  - Three forwarding rules active in the Cloudflare Email Routing dashboard.
  - Test message to `security@<domain>` reaches the maintainer's inbox.
  - Rationale logged: `SECURITY.md` and `CODE_OF_CONDUCT.md` will reference these addresses (Task 2b.A.6 and 2b.A.7).
- **Size:** XS (5-10 min)
- **Autonomy:** CHECKPOINT
- **Resume signal:** "email routing active"
- **Dependencies:** 2b.0.1 (domain must be registered on Cloudflare first — if fallback registered elsewhere, use that registrar's email-routing equivalent or skip aliases and use a personal email in the scaffolding files).

#### Task 2b.0.3 — CHECKPOINT: confirm or skip Twitter/X handle

- **Files:** `.planning/phase-2b-public-launch/DECISIONS.md` (new file — append `Twitter handle: <value or SKIP>`).
- **Action (CHECKPOINT — human):** Decide between three options:
  - **Option A:** Use existing personal handle (e.g., `@IdanG7`). Verify it's live and the maintainer controls it.
  - **Option B:** Create a new project handle `@StacklyDev` (or similar). Reserve it now (takes 2 min).
  - **Option C:** Skip Twitter for 2b. Drops Twitter/X thread from LAUNCH_POSTS.md (Task 2b.D.3 becomes no-op); `astro-seo` config (Task 2b.B.6) omits `twitter.creator`.
- **Acceptance criteria:**
  - `DECISIONS.md` has a single line: `Twitter handle: @<handle>` or `Twitter handle: SKIP`.
  - If SKIP, Task 2b.D.3 is marked `N/A` in its own acceptance and LAUNCH_POSTS.md contains a placeholder noting Twitter deferred.
- **Size:** XS (2 min)
- **Autonomy:** CHECKPOINT
- **Resume signal:** "twitter: @<handle>" or "twitter: skip"
- **Dependencies:** none. Must resolve before Task 2b.B.6 (SEO meta config) and Task 2b.D.3 (Twitter thread draft).

#### Task 2b.0.4 — CHECKPOINT: choose YouTube channel (personal vs project)

- **Files:** `.planning/phase-2b-public-launch/DECISIONS.md` (append `YouTube channel: <name + URL>`).
- **Action (CHECKPOINT — human):** Decide between:
  - **Option A:** Upload under maintainer's personal YouTube channel (zero setup; mixes Stackly with unrelated personal content).
  - **Option B:** Create a new `Stackly` YouTube channel on the maintainer's Google account (15 min, dedicated project surface).
- **Acceptance criteria:**
  - `DECISIONS.md` has `YouTube channel: <display name>` + `Channel URL: <url>`.
  - If Option B, channel exists, channel art matches project branding (can be a placeholder logo — design polish lives in Task 2b.D.4 social-preview image work).
- **Size:** XS (2 min decision) or S (20 min if creating Option B channel)
- **Autonomy:** CHECKPOINT
- **Resume signal:** "youtube: <channel name>"
- **Dependencies:** none. Must resolve before Task 2b.C.4 (upload).

---

### Phase 2b.A — Content track (README, scaffolding, demo script)

Eight tasks. All AUTO (pure text production). All can start immediately — none depend on domain or video.

#### Task 2b.A.1 — Rewrite README.md for public audience

- **Files:** `README.md` (rewrite in place — current ~101 lines grow to ~200-250).
- **Action:** Section-by-section rewrite per RESEARCH.md §4 diff table. Specifically:
  1. **Title + one-liner:** Keep title. Rewrite one-liner to: `"Remote crash capture for Claude Code, Cursor, and Claude Desktop. Expose live Windows debugger state as MCP tools, and run an autonomous AI fix-loop on remote crashes."`
  2. **Badges row** (immediately under title): CI status badge, `License: MIT`, `Python 3.11+`, `platform: Windows 10/11` — exact markdown copied from RESEARCH.md §9 "Repo badges" block. No PyPI badge (2c).
  3. **Status callout:** Replace Phase 2a callout with: `"**Alpha** — API stable, not yet on PyPI (clone to install). MIT-licensed. Windows 10/11 only for now; Linux/macOS/Unity are on the roadmap (Phase 3)."`
  4. **Hero demo embed (NEW):** `[![Watch the 60s demo](docs/demo-thumb.png)](https://youtu.be/XXXX)` — placeholder URL until Task 2b.C.4 completes; the link gets updated by Task 2b.C.5. Thumbnail path is a placeholder too (real image lands in Task 2b.C.3).
  5. **Why Stackly (KEEP + ADD wedge sentence):** Keep current 30-60 min framing. Add: `"No other tool combines remote debugger capture, MCP exposure, and an autonomous repair agent in one flow."`
  6. **Architecture diagram (NEW):** Copy the ASCII TEST MACHINE <-> DEV MACHINE diagram from `.planning/PROJECT.md` lines 13-27 verbatim, fenced as ```` ```text ```` block.
  7. **Prerequisites (EXPAND):** Explicit version floors — Windows 10/11 x64, Python >= 3.11, uv >= 0.5, Windows Debugging Tools (link to installer at https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/), git >= 2.20, `claude` CLI on PATH (link to https://docs.claude.com/en/docs/claude-code/getting-started).
  8. **Install (REWRITE):** Full "from source" block:
     ```bash
     git clone https://github.com/IdanG7/stackly.git
     cd stackly
     uv sync
     uv run stackly doctor   # verifies prerequisites
     ```
     Add honest line: `"PyPI publish is tracked in [Phase 2c](./ROADMAP.md) — for now, install from source."` (roadmap link is relative; resolves to the planning dir which may not be public, so use `"tracked in the roadmap"` if `ROADMAP.md` is not at repo root — verify before shipping; if not at root, reference as `.planning/ROADMAP.md` or inline the statement.)
  9. **Quick start (REWRITE):** Current 4-step flow is fine but add "On a fresh Windows 10/11 box, after installing prerequisites:" preface and insert `uv run stackly doctor` before `serve`.
  10. **MCP client config snippets (EXPAND to 3 clients):** Claude Code via `claude mcp add stackly --transport http http://localhost:8585/mcp` (verify exact syntax against Claude Code docs at command-authoring time — if the CLI syntax differs, keep the JSON config example as primary and note CLI as alternative); Claude Desktop config block (current one is good); Cursor `.cursor/mcp.json` (current). Three fenced blocks, each with a `### Client name` subheading.
  11. **Tools table (KEEP):** Current 8-tool table stays; **add 9th row: `detach_process`** (added in Phase 2a.0.1). Descriptions in RESEARCH.md §4 implicit.
  12. **Fix-loop agent section (KEEP + REFINE):** Current is fine. Add callout after autonomous-mode example: `"> Hand-off mode is the default; \`--auto\` runs headless and should only be used after you've dogfooded the loop."`
  13. **"Why Stackly" competitive wedge (NEW):** 8-10 line section naming alternatives that do ONE piece: CrashReporter (capture only), Sentry (telemetry only), manual Claude Code (dev-machine only). Stackly = remote capture + MCP + autonomous repair in one flow.
  14. **Troubleshooting (NEW):** 5 FAQ items: (a) `stackly doctor` says pybag missing -> install Windows Debugging Tools; (b) symbols not resolved -> set `_NT_SYMBOL_PATH`; (c) port 8585 in use -> pass `--port N`; (d) `claude` command not found -> install Claude Code CLI; (e) attach fails with access denied -> run elevated.
  15. **Development section (MOVE):** Replace current dev block with `"For development setup, testing, and PR process, see [CONTRIBUTING.md](./CONTRIBUTING.md)."` (CONTRIBUTING.md itself lands in Task 2b.A.3.)
  16. **Links footer (NEW):** Landing page (`https://stackly.dev` or chosen fallback), GitHub Issues, GitHub Discussions, CHANGELOG, CONTRIBUTING, LICENSE.
  17. **License section (KEEP).**
  **Tone check — grep the final draft for forbidden words and fix each:** `auto-detect`, `automatically detects`, `cross-platform`, `pip install stackly\b` (the `\b` is the literal word-boundary test: `pip install stackly<space>` in a prose sentence is bad, `pip install stackly  # not yet on PyPI` in a code block with an honest-marketing comment is bad too — must be `clone and uv sync` per the honest-marketing constraint), `the fastest`, `the best`, `the only` (the wedge sentence is the one exception and should use "No other tool combines..." framing, which is falsifiable).
- **Acceptance criteria:**
  - `README.md` file size between 180 and 280 lines.
  - `grep -Ei '(auto-detect|automatically detect|cross-platform|\bpip install stackly\b|the fastest|the best|the only)' README.md` returns zero hits (except within the intentional "No other tool combines" wedge).
  - All 16 sections above appear in order; section headings exist verbatim.
  - Embedded demo thumbnail link uses an `https://youtu.be/` URL (placeholder `XXXX` acceptable until Task 2b.C.5 patches it).
  - Tools table has exactly 9 data rows (not counting header + separator) AND `grep -E '^\| detach_process' README.md` returns exactly 1 match (which must be inside the tools table — verify by eye the matching line is a table row).
  - Architecture ASCII diagram appears inside a ```` ```text ```` fenced block.
  - `uv run pytest -m "not integration"` still passes (no code changed — sanity check CI).
- **Size:** L (4-6h per RESEARCH.md §12)
- **Autonomy:** AUTO
- **Dependencies:** none. Can start Day 0. (Final URL substitutions for demo thumbnail + video link happen in Task 2b.C.5.)

#### Task 2b.A.2 — Write demo script to `DEMO_SCRIPT.md`

- **Files:** `.planning/phase-2b-public-launch/DEMO_SCRIPT.md` (new).
- **Action:** Write a 140-160 word script following RESEARCH.md §5 beat structure:
  - 0:00-0:05 Hook: crash_app on screen with red error dialog; text overlay "Your C++ app crashed on a test machine. What now?"
  - 0:05-0:15 Problem: voiceover describes the 30-min manual loop.
  - 0:15-0:25 Solution setup: terminal shows `stackly fix --pid <crash_app PID> --repo .` running on the dev machine.
  - 0:25-0:40 Live capture: terminal output shows "Capturing crash... 47 stack frames... Launching Claude Code..."
  - 0:40-0:50 AI diagnosis: Claude Code window shows the briefing + a diagnosis message identifying the null deref; patch preview visible.
  - 0:50-1:00 CTA: full-screen `stackly.dev` URL + GitHub logo + one-line read-aloud: "Works with Claude Code, Cursor, and Claude Desktop. Install from GitHub. stackly.dev."
  **Include explicit structure:**
  - Script timing: table with cols `Beat | Time | Visual | Voiceover`.
  - Word count under the table (must be 140-160).
  - **Honest-marketing constraint reminder at top of file:** "**CONSTRAINT:** This script describes hand-off mode only. Do NOT demonstrate autonomous PR creation or crash auto-detection — those are 2a-opt-in and 2.5 respectively."
  - **Mode declaration at top:** "Mode: hand-off (matches 2a default)."
  - **Read-aloud test spec:** instructions for the narrator to time themselves reading the full voiceover column; must land 60-65s. If over 65s, cut words — do not speed up delivery.
- **Acceptance criteria:**
  - File exists at `.planning/phase-2b-public-launch/DEMO_SCRIPT.md`.
  - Voiceover word count is between 140 and 160 (count words in Voiceover column only).
  - All six beats documented with start/end timestamps summing to 60s.
  - Honest-marketing constraint banner present.
  - `grep -Ei '(auto-detect|automatic crash|pip install|cross-platform)' DEMO_SCRIPT.md` returns zero hits.
- **Size:** S-M (1-2h per RESEARCH.md §12)
- **Autonomy:** AUTO (draft); human review before Track C recording begins is built into Task 2b.C.1.
- **Dependencies:** none. Can start Day 0.

#### Task 2b.A.3 — Create CONTRIBUTING.md

- **Files:** `CONTRIBUTING.md` (new at repo root).
- **Action:** Produce a first-time-contributor onramp with the 10 sections in RESEARCH.md §8 "CONTRIBUTING.md — Custom":
  1. **Welcome** (1 paragraph — lower the bar; note "good-first-issue" label convention).
  2. **Code of Conduct** — 1 line pointing at `CODE_OF_CONDUCT.md`.
  3. **Reporting bugs** — direct to `.github/ISSUE_TEMPLATE/bug_report.yml` via the "New Issue" button.
  4. **Suggesting features** — direct to `.github/ISSUE_TEMPLATE/feature_request.yml`.
  5. **Development setup** — expanded from README:
     ```bash
     git clone https://github.com/IdanG7/stackly.git
     cd stackly
     uv sync --all-extras
     uv run stackly doctor
     ```
  6. **Running tests** — split unit vs integration:
     - `uv run pytest -m "not integration"` (unit, ~15s, CI-safe)
     - `$env:PYBAG_INTEGRATION = "1"; uv run pytest` (requires Debugging Tools)
     - Integration test count from current `tests/` directory (verify count before writing; use `"currently 4 integration tests"` or whatever grep returns).
  7. **Code style** — `ruff format` + `ruff check` + `pyright` basic mode. Pre-commit hook note only if `.pre-commit-config.yaml` exists (verify; if not, omit).
  8. **Commit message conventions** — conventional commits (see `CHANGELOG.md` for examples); scope should be `phase-N.M` during phase work or `core` / `cli` / `docs` otherwise.
  9. **PR process** — branch naming (`feat/`, `fix/`, `docs/`, `chore/`); CI must be green; request review from `@IdanG7`; PR template fields are mandatory (Task 2b.A.8).
  10. **Release process** — maintainer-only; link to `CHANGELOG.md`; note that versioning follows semver.
- **Acceptance criteria:**
  - File exists at repo root, 80-200 lines.
  - All 10 numbered sections present in order with markdown `## ` headings.
  - Pre-commit note is either present (and `.pre-commit-config.yaml` exists in repo) or absent (and it does not).
  - No broken relative links (run `grep -oE '\]\([^)]+\)' CONTRIBUTING.md | sort -u` and spot-check each).
- **Size:** M (2-3h per RESEARCH.md §12)
- **Autonomy:** AUTO
- **Dependencies:** none. (References `.github/ISSUE_TEMPLATE/*` but those land in Task 2b.A.6 — the references are forward-safe because they document file paths that will exist before the reader clicks them.)

#### Task 2b.A.4 — Create CODE_OF_CONDUCT.md (Contributor Covenant 2.1)

- **Files:** `CODE_OF_CONDUCT.md` (new at repo root).
- **Action:** Copy Contributor Covenant 2.1 verbatim from https://www.contributor-covenant.org/version/2/1/code_of_conduct/ . Substitute the `[INSERT CONTACT METHOD]` placeholder with `coc@<domain>` where `<domain>` is the registered domain from Task 2b.0.1 (either `stackly.dev` or fallback). Email alias from Task 2b.0.2 must be active.
- **Acceptance criteria:**
  - File exists, 125-160 lines (Contributor Covenant 2.1 is 138 lines of prose + license notice).
  - `[INSERT CONTACT METHOD]` placeholder is replaced with the real `coc@<domain>` address.
  - Footer attribution line links to https://www.contributor-covenant.org preserved.
  - License notice at bottom preserved: `"This Code of Conduct is adapted from the Contributor Covenant, version 2.1..."`.
  - Sending a test email to `coc@<domain>` reaches the maintainer (inherit from Task 2b.0.2 verification).
- **Size:** XS (15 min — mostly copy-paste + one email substitution)
- **Autonomy:** AUTO
- **Dependencies:** 2b.0.2 (email alias must be active for the substituted address to work).

#### Task 2b.A.5 — Create SECURITY.md + enable GitHub private vulnerability reporting

- **Files:** `SECURITY.md` (new at repo root). Repo settings toggle via `gh` CLI.
- **Action:**
  1. Write `SECURITY.md` using the 20-line template in RESEARCH.md §8 "SECURITY.md". Substitute `security@stackly.dev` with `security@<chosen domain>`.
  2. Enable GitHub private vulnerability reporting:
     ```bash
     gh api -X PATCH /repos/IdanG7/stackly/private-vulnerability-reporting -f enabled=true
     # Alt via UI: repo Settings -> Code security and analysis -> Private vulnerability reporting -> Enable
     ```
     (Verify endpoint via `gh api --method GET /repos/IdanG7/stackly` before making changes — GitHub API occasionally renames these.)
- **Acceptance criteria:**
  - `SECURITY.md` exists with the two reporting channels (GitHub private reporting + email).
  - Acknowledgment / triage / fix-timeline expectations present.
  - `gh api /repos/IdanG7/stackly/private-vulnerability-reporting` returns `{"enabled": true}` (or the repo Security tab shows the feature enabled).
  - "Report a vulnerability" button visible on the repo's Security tab.
  - Test email to `security@<domain>` reaches maintainer.
- **Size:** XS-S (30 min — template + one API call)
- **Autonomy:** AUTO (file creation) + CHECKPOINT (GitHub API call may require the user to confirm admin permissions — if `gh api` returns 403, Claude pauses and asks the user to toggle the setting via the web UI).
- **Resume signal (if API path fails):** "private vuln reporting enabled via UI"
- **Dependencies:** 2b.0.2 (email alias must work).

#### Task 2b.A.6 — Create GitHub issue templates + config + PR template

- **Files:**
  - `.github/ISSUE_TEMPLATE/bug_report.yml` (new)
  - `.github/ISSUE_TEMPLATE/feature_request.yml` (new)
  - `.github/ISSUE_TEMPLATE/config.yml` (new)
  - `.github/PULL_REQUEST_TEMPLATE.md` (new)
- **Action:** Copy the four YAML/MD blocks from RESEARCH.md §8 verbatim:
  - `bug_report.yml`: name, description, title prefix `"[bug] "`, labels `["bug", "triage"]`, 8 form fields (what-happened, reproduction, version, os, python, doctor, logs).
  - `feature_request.yml`: name, description, title prefix `"[feature] "`, labels `["enhancement", "triage"]`, 4 form fields (problem, proposal, alternatives, scope checkboxes).
  - `config.yml`: `blank_issues_enabled: false`, contact links to Discussions and to security advisories.
  - `PULL_REQUEST_TEMPLATE.md`: Summary + Type-of-change + Test-plan + Checklist sections as specified.
  Verify the `IdanG7/stackly` URL in `config.yml`'s contact links matches the actual repo slug.
- **Acceptance criteria:**
  - All four files exist at their paths.
  - `yamllint` (or `python -c "import yaml; yaml.safe_load(open(p))"` as a fallback) parses the three YAML files without errors.
  - Opening https://github.com/IdanG7/stackly/issues/new/choose (post-push) renders the two forms and hides "blank issue" option.
  - Opening a new PR draft locally (`gh pr create --draft`) pre-populates the template fields.
- **Size:** S (30-45 min — mostly paste + verify)
- **Autonomy:** AUTO
- **Dependencies:** none.

#### Task 2b.A.7 — Add `.gitattributes` to keep GitHub language-stats Python-dominant

- **Files:** `.gitattributes` (new at repo root).
- **Action:** Write a minimal `.gitattributes`:
  ```gitattributes
  site/** linguist-documentation
  site/**/*.astro linguist-documentation
  ```
  Reference: https://github.com/github-linguist/linguist/blob/master/docs/overrides.md — `linguist-documentation=true` is the correct flag to exclude from language stats. (If the stats bar still goes TS-dominant after site/ lands in 2b.B, a follow-up can use `linguist-vendored=true` instead; start with `-documentation`.)
- **Acceptance criteria:**
  - File exists at repo root.
  - After the Astro scaffold commit (Task 2b.B.5) reaches `main` and GitHub re-indexes (~10 min), repo home page language bar shows Python as top language.
- **Size:** XS (5 min)
- **Autonomy:** AUTO
- **Dependencies:** none (file can land before site/ exists).

#### Task 2b.A.8 — Update CHANGELOG.md with Unreleased entry for 2b

- **Files:** `CHANGELOG.md` (prepend entry).
- **Action:** Add a new `## Unreleased` (or bump the existing one) section near the top of CHANGELOG.md summarizing Phase 2b work IN PROGRESS:
  ```markdown
  ## [Unreleased]

  ### Documentation
  - Rewrote README for public audience (hero, quickstart, architecture diagram, MCP client configs for Claude Code / Cursor / Claude Desktop, troubleshooting).
  - Added CONTRIBUTING.md, CODE_OF_CONDUCT.md (Contributor Covenant 2.1), SECURITY.md.
  - Added GitHub issue templates (bug report + feature request) and PR template.

  ### Marketing
  - Landing page shipped at https://stackly.dev (Astro + Tailwind, hosted on Cloudflare Pages).
  - 60-second demo video recorded and uploaded (YouTube).
  - Submitted to MCP directories (see `.planning/phase-2b-public-launch/DIRECTORY_SUBMISSIONS.md` for current status — directory names will be named specifically at release time in Task 2b.F.3 based on which submissions are live).

  ### No functional code changes in this release.
  ```
  (The final CHANGELOG entry gets version-bumped to `## [0.2.1]` in Task 2b.F.3 — 2b.A.8 just gets the text in place during Track A.)
- **Acceptance criteria:**
  - CHANGELOG.md has an `## [Unreleased]` entry with Documentation, Marketing, and "No functional code changes" sections.
  - No code-surface changes listed (Phase 2b does not touch `src/`).
- **Size:** XS (10 min)
- **Autonomy:** AUTO
- **Dependencies:** none.

---

### Phase 2b.B — Infra track (domain -> Cloudflare Pages -> Astro scaffold -> deploy)

Seven tasks. Mix of CHECKPOINT (dashboard clicks) and AUTO (local scaffolding + config).

#### Task 2b.B.1 — Attach domain to Cloudflare account (DNS auto-setup)

- **Files:** `.planning/phase-2b-public-launch/DOMAIN.md` (append DNS verification section).
- **Action (CHECKPOINT — human):** If Task 2b.0.1 registered through Cloudflare Registrar, DNS is already in Cloudflare and this task is a 30s sanity check (dashboard -> Websites -> confirm domain appears with orange-cloud active). If the domain was registered elsewhere (fallback scenario), add the domain to Cloudflare as a Free-tier website and change nameservers at the fallback registrar per Cloudflare's onboarding instructions. Wait for propagation (up to 24h but typically < 1 hour).
- **Acceptance criteria:**
  - `dig <domain> NS` returns Cloudflare nameservers (`*.ns.cloudflare.com`).
  - Domain appears as "Active" in the Cloudflare dashboard.
- **Size:** XS (if CF-registered) or M (if fallback nameserver switch required)
- **Autonomy:** CHECKPOINT
- **Resume signal:** "cloudflare DNS active for <domain>"
- **Dependencies:** 2b.0.1.

#### Task 2b.B.2 — Scaffold Astro project under `site/`

- **Files:** `site/*` — generated files from Astro minimal template + added integrations. See RESEARCH.md §1 "Recommended project structure" for the target tree.
- **Action:**
  ```bash
  cd <repo-root>
  npm create astro@latest site -- --template minimal --typescript strict --no-install --no-git
  cd site
  npm install
  npx astro add tailwind       # install & configure @astrojs/tailwind + tailwindcss
  npx astro add sitemap        # install & configure @astrojs/sitemap
  npm install astro-seo
  ```
  Then:
  - Set `site: "https://<chosen-domain>"` in `site/astro.config.mjs` (required for sitemap canonical URLs and astro-seo Astro.site resolution).
  - Add `site/.gitignore`: `node_modules/`, `dist/`, `.astro/`, `.wrangler/`.
  - Add `site/README.md` one-liner: `"See repo root README for project info. This subdir contains the Astro source for https://<domain>."`
  - Verify `npm run build` produces `site/dist/index.html` and `site/dist/sitemap-index.xml`.
  - Verify `npm run dev` serves on `http://localhost:4321` and renders the Astro welcome page.
- **Acceptance criteria:**
  - `site/astro.config.mjs` exists and imports tailwind + sitemap integrations.
  - `site/package.json` contains `astro`, `@astrojs/tailwind`, `@astrojs/sitemap`, `tailwindcss`, `astro-seo` in `dependencies`.
  - `site/package-lock.json` committed.
  - `npm run build` succeeds in `site/` with zero errors.
  - `site/dist/` is gitignored (build artifact, not committed).
  - `site/astro.config.mjs` has `site:` field set to chosen domain.
- **Size:** M (1-1.5h)
- **Autonomy:** AUTO
- **Dependencies:** 2b.0.1 (need domain decided for `site:` field).

#### Task 2b.B.3 — Build `BaseLayout.astro` with astro-seo + analytics beacon

- **Files:** `site/src/layouts/BaseLayout.astro` (new).
- **Action:** Port the RESEARCH.md §1 "Per-page meta boilerplate" block verbatim, with two updates:
  - Replace `@IdanG7` placeholder in `twitter.creator` with the handle from DECISIONS.md (Task 2b.0.3). If `SKIP`, remove the `twitter.creator` field entirely.
  - Add the Cloudflare Web Analytics beacon block (the one-line `<script>` that Cloudflare generates in the Web Analytics dashboard after Task 2b.B.7). Since the beacon token doesn't exist until post-first-deploy, emit the block as a commented placeholder:
    ```html
    <!-- cloudflare-web-analytics-beacon: Task 2b.B.7 inserts the real <script> tag here post-deploy -->
    ```
    Task 2b.B.7 patches this line in-place with the real `<script>` tag.
- **Acceptance criteria:**
  - `BaseLayout.astro` has `<Props>` typed `{ title: string; description: string; image?: string }`.
  - Imports `SEO` from `astro-seo`.
  - `<SEO>` call includes `openGraph` + `twitter` cards.
  - Canonical URL derived from `Astro.url` + `Astro.site`.
  - `<slot />` exists within `<body>`.
  - Analytics placeholder comment present.
  - If Twitter handle is `SKIP`, no `twitter.creator` field present (verify with grep).
- **Size:** S (30 min)
- **Autonomy:** AUTO
- **Dependencies:** 2b.0.3, 2b.B.2.

#### Task 2b.B.4 — Build landing page components + index.astro

- **Files:**
  - `site/src/pages/index.astro`
  - `site/src/components/Hero.astro`
  - `site/src/components/VideoEmbed.astro`
  - `site/src/components/HowItWorks.astro`
  - `site/src/components/WhyStackly.astro`
  - `site/src/components/McpConfig.astro`
  - `site/src/components/WhoItsFor.astro`
  - `site/src/components/ScopeStatus.astro`
  - `site/src/components/Footer.astro`
  - `site/public/favicon.svg` (placeholder — design polish in Task 2b.D.4)
  - `site/public/logo.svg` (placeholder)
  - `site/public/robots.txt`
- **Action:** Implement the 8-section structure per RESEARCH.md §3 "Stackly-specific section map":
  - **Pre-step 0 (dependencies):** Run `npm i lite-youtube-embed` inside `site/`. Verify the entry appears in `site/package.json` under `dependencies`. Commit the updated `site/package.json` and `site/package-lock.json`. This MUST land before implementing the VideoEmbed component below.
  - **Hero:** Tagline ("Remote crash capture for Claude Code, Cursor, and Claude Desktop"), one-sentence elaboration, primary CTA button `[Watch 60s demo]` scrolling to #demo, secondary CTA `[View on GitHub]` to https://github.com/IdanG7/stackly. Badges row (MIT, Python 3.11+, Windows 10/11).
  - **VideoEmbed:** Use `lite-youtube-embed` wrapper (dependency installed in Pre-step 0). Import its CSS + web component from `lite-youtube-embed`. Props: `videoId` (placeholder `dQw4w9WgXcQ` until Task 2b.C.4 supplies real; Task 2b.C.5 patches). Zero-JS-until-interaction behavior documented in component.
  - **HowItWorks:** 3-step grid. (1) `dbgsrv.exe` on test box (one command), (2) `stackly serve` on dev box (Streamable HTTP MCP), (3) AI client sees the crash via MCP. ASCII or SVG diagram inline.
  - **WhyStackly:** Competitive-wedge section. 3-column comparison grid: Stackly vs CrashReporter (capture-only, no MCP, no repair) vs Sentry (telemetry, not debug state) vs manual-Claude-Code (dev-machine process only). Grid checkmarks/X marks.
  - **McpConfig:** Tabbed component, three tabs: Claude Code / Cursor / Claude Desktop. Each tab shows the exact config snippet. Uses a minimal Tailwind-only tab state (no JS framework — can use `<details>`/`<summary>` for progressive enhancement).
  - **WhoItsFor:** 5 user-type cards (game studios, embedded/IoT, desktop app devs, enterprise C++, DevOps/SRE). One-sentence pain-point per card, from PROJECT.md target-users table.
  - **ScopeStatus (NEW — required by GOAL.md "Today vs. Roadmap" constraint):** Two-column block with unique anchor `id="scope-status"`. Left column heading `Today`, content: "Windows 10/11 + Claude Code / Cursor / Claude Desktop + hand-off fix-loop + install from source." Right column heading `Roadmap`, content: "PyPI install (2c), crash auto-detection (2.5), Linux / macOS (3), enterprise / cloud (4)." Place below the install CTA / McpConfig section and above Footer. Both column headings must render as literal text `Today` and `Roadmap` inside the `#scope-status` section so the acceptance-criteria grep lands two hits in one anchor.
  - **Footer:** Repeated `[Install from GitHub]` CTA + links to GitHub, Issues, Discussions, LICENSE. Text: `"MIT-licensed. Maintained by @<handle-or-name>. Copyright (c) 2026."`
  - **index.astro:** Imports BaseLayout with `title="Stackly — Remote crash capture for Claude Code, Cursor, Claude Desktop"`, `description` (<= 160 chars), composed in order: Hero -> VideoEmbed -> HowItWorks -> WhyStackly -> McpConfig -> WhoItsFor -> ScopeStatus -> Footer.
  - **robots.txt:**
    ```
    User-agent: *
    Allow: /

    Sitemap: https://<domain>/sitemap-index.xml
    ```
  - Placeholder `favicon.svg` and `logo.svg`: plain glyph — a stylized "D" or a monochrome debugger/bridge icon. Polish lands in Task 2b.D.4.
- **Acceptance criteria:**
  - All 8 component files exist.
  - `site/src/pages/index.astro` imports all 7 components and renders in order.
  - `npm run build` succeeds; `site/dist/index.html` > 5 KB (has real content).
  - `site/dist/sitemap-index.xml` exists and references `/`.
  - `site/dist/robots.txt` contains the Sitemap directive pointing at the chosen domain.
  - **`grep -Ei '(auto-detect|automatically detect|cross-platform|pip install|the fastest|the best|the only)' site/src/**/*.astro` returns zero hits** (honest-marketing grep — same as README).
  - All external links open `https://github.com/IdanG7/stackly` and are not broken.
  - Video embed renders `lite-youtube-embed` wrapper with a placeholder thumbnail (real thumbnail lands post-Task 2b.C.3).
  - **"Today vs. Roadmap" scope-status section present and grep-verifiable:** `grep -Ei '(today|roadmap)' site/src/pages/index.astro` (or the rendered `site/dist/index.html`) returns >= 2 hits within the single `#scope-status` section. Verify by `grep -A 20 'id="scope-status"' site/src/components/ScopeStatus.astro | grep -cEi '(today|roadmap)'` returns >= 2.
- **Size:** L (6-8h per RESEARCH.md §12)
- **Autonomy:** AUTO
- **Dependencies:** 2b.B.3, 2b.0.3 (handle for Twitter meta in layout), 2b.A.2 (tagline derived from DEMO_SCRIPT CTA language so they match).

#### Task 2b.B.5 — Connect Cloudflare Pages to repo and trigger first deploy

- **Files:** none (external dashboard action). Record outcome in `.planning/phase-2b-public-launch/DOMAIN.md` (append `Cloudflare Pages project: <project name>, first deploy: <URL>`).
- **Action (CHECKPOINT — human):**
  1. Cloudflare dashboard -> Workers & Pages -> Create -> Pages -> "Connect to Git" -> select `IdanG7/stackly`.
  2. Set production branch: `main`. Preview branch pattern: all branches (so PRs get previews).
  3. Build settings:
     - **Framework preset:** Astro
     - **Build command:** `cd site && npm install && npm run build`
     - **Build output directory:** `site/dist`
     - **Root directory (advanced):** leave blank
     - **Environment variables:** none for 2b
  4. Click "Save and Deploy". First build should take ~2 min.
  5. Once green, custom domain: Pages project -> Custom domains -> "Set up a custom domain" -> enter `<domain>` and `www.<domain>`. DNS is auto-configured via Cloudflare Registrar; otherwise add CNAME records pointing at `<project>.pages.dev`.
  6. Verify TLS: visit `https://<domain>` (HTTPS is mandatory for `.dev` TLD due to HSTS preload).
- **Acceptance criteria:**
  - `<project>.pages.dev` URL returns 200 and renders the landing page.
  - `https://<domain>` returns 200 and renders the same page (DNS + TLS both green).
  - `https://<domain>/sitemap-index.xml` returns valid XML.
  - `https://<domain>/robots.txt` returns the expected text.
  - Cloudflare Pages dashboard shows the project with "main" connected for prod and "all branches" for previews.
  - DOMAIN.md records the project name + first deploy URL.
- **Size:** M (30-60 min, most of it waiting for DNS)
- **Autonomy:** CHECKPOINT
- **Resume signal:** "pages deployed, <domain> is live"
- **Dependencies:** 2b.B.2, 2b.B.4 (at least one commit of `site/` must exist before Pages can build), 2b.B.1 (DNS must resolve).

#### Task 2b.B.6 — Enable Cloudflare Web Analytics + patch beacon into layout

- **Files:** `site/src/layouts/BaseLayout.astro` (patch the placeholder comment from Task 2b.B.3).
- **Action:**
  1. (CHECKPOINT — human) Cloudflare dashboard -> Analytics & Logs -> Web Analytics -> Add a site -> select the Pages `<domain>` -> copy the beacon `<script>` tag.
  2. (AUTO) Replace the placeholder comment in `BaseLayout.astro` (`<!-- cloudflare-web-analytics-beacon: ... -->`) with the real `<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{"token": "..."}'></script>` tag.
  3. Commit and push; Cloudflare Pages redeploys. Wait ~5 min; dashboard should show `Page Views: 0` and transition to non-zero after a manual visit.
- **Acceptance criteria:**
  - `BaseLayout.astro` contains the real beacon `<script>` tag (no placeholder comment).
  - Manually loading `<domain>` registers a page view in Cloudflare Web Analytics within 5 minutes.
  - No cookie banner appears on the landing page (Cloudflare Web Analytics is cookieless).
- **Size:** S (15-20 min)
- **Autonomy:** CHECKPOINT (copy token from dashboard) then AUTO (patch file).
- **Resume signal (post-dashboard):** "beacon token: <paste>"
- **Dependencies:** 2b.B.5 (Pages project must exist before Web Analytics can attach).

#### Task 2b.B.7 — Verify Google Search Console + submit sitemap

- **Files:** none (external action). Record outcome in `.planning/phase-2b-public-launch/DOMAIN.md` (append section: `GSC: verified <date>, sitemap submitted <date>`).
- **Action (CHECKPOINT — human):**
  1. Go to https://search.google.com/search-console .
  2. Add property: domain-type (preferred) OR URL-prefix.
  3. Verify via DNS TXT record (Cloudflare DNS propagates in < 1 min, so DNS verification is fastest) OR via HTML file (upload `googleXXXX.html` to `site/public/`, redeploy, verify). Prefer DNS.
  4. Once verified, Sitemaps -> Add new sitemap: `sitemap-index.xml` (relative; GSC auto-prepends `https://<domain>/`).
  5. Wait for GSC to report "Success" (typically within 10 min).
  6. Append outcome to DOMAIN.md.
- **Acceptance criteria:**
  - GSC shows `<domain>` as verified.
  - Sitemap submission shows status `Success`.
  - GSC "Coverage" shows at least 1 URL discovered (may take 24-48h).
- **Size:** S (15-30 min, mostly waiting)
- **Autonomy:** CHECKPOINT
- **Resume signal:** "GSC verified + sitemap submitted"
- **Dependencies:** 2b.B.5 (domain must be live and serving `sitemap-index.xml`).

---

### Phase 2b.C — Video track (script review -> record -> edit -> upload)

Five tasks. Mix of AUTO (review/caption writing) and CHECKPOINT (recording, external uploads).

> **Critical dependency:** This entire track depends on Task 2b.A.2 producing `DEMO_SCRIPT.md`. Rest of track cannot start until script is reviewed and approved.

#### Task 2b.C.1 — Review + approve demo script

- **Files:** `.planning/phase-2b-public-launch/DEMO_SCRIPT.md` (append review log section).
- **Action (CHECKPOINT — human):** Read the draft from Task 2b.A.2 aloud with a stopwatch. Time must be 60-65s. Check against honest-marketing grep. If cut or edit needed, update the file and re-time. Append a `## Review log` section: date, reviewer, final word count, timed read-aloud duration (e.g. `62.3s`).
- **Acceptance criteria:**
  - Voiceover read-aloud is between 60-65s (documented in review log).
  - No prohibited marketing phrases (automatic check via grep).
  - Review log section appended with reviewer name + date + duration.
- **Size:** S (20-40 min including re-timing)
- **Autonomy:** CHECKPOINT
- **Resume signal:** "script approved, <duration>s"
- **Dependencies:** 2b.A.2.

#### Task 2b.C.2 — Record demo footage (OBS, multiple takes)

- **Files:** Raw recordings in local `C:/Users/<user>/Videos/stackly-demo-raw/` (NOT committed — recordings are local artifacts). Final remuxed MP4 also local until upload.
- **Action (CHECKPOINT — human):**
  1. Install OBS Studio 30+ from https://obsproject.com/ if not installed.
  2. Apply RESEARCH.md §5 "Settings for 1080p60 developer demos":
     - 1920x1080 @ 60 FPS, NVENC (or x264 Medium fallback), MKV, CQP, CQ 18-20.
     - 48 kHz mic sample rate; USB mic mandatory (not laptop built-in).
  3. Prepare scene: two monitors or windowed setup showing crash_app + terminal + Claude Code. Test machine crash_app can be a local simulation if no physical remote machine is handy (note in DEMO_SCRIPT.md comments if simulated).
  4. Record the 6 beats per DEMO_SCRIPT.md. Expect 3-5 takes per beat.
  5. Pick best takes. File -> Remux Recordings -> remux the selected MKV(s) to MP4 (lossless).
  6. Save the final raw MP4 locally; do not commit.
  **Note on demo authenticity (per R5):** the demo must show what 2a actually ships. Hand-off mode only — Claude Code window opens preloaded with briefing, shows a diagnosis message, shows a proposed patch as text. Do NOT show a PR being opened (that's post-2a). Do NOT show crash auto-detection (that's 2.5).
- **Acceptance criteria:**
  - A raw MP4 exists locally at 1920x1080, 60fps, ~60s duration, file size < 200MB (for Descript upload).
  - Audio is audible, no clipping, no mouse click heard on mic.
  - Terminal text is readable at 1080p (font size >= 18pt in terminal settings).
  - Claude Code's response visible in frame and readable.
- **Size:** L (2.5h per RESEARCH.md §12 — setup + 3-5 takes + remux)
- **Autonomy:** CHECKPOINT
- **Resume signal:** "raw footage ready, <duration>s, <path>"
- **Dependencies:** 2b.C.1.

#### Task 2b.C.3 — Edit in Descript + generate captions + thumbnail

- **Files:**
  - Local: final edited MP4, final `.srt` subtitle file (both stay local; YouTube gets them uploaded).
  - `site/public/demo-thumb.png` (1280x720 thumbnail — committed to repo for landing page and README use).
- **Action (CHECKPOINT — human):**
  1. Subscribe to Descript Creator ($15/mo, one month is enough; can cancel post-launch).
  2. Import raw MP4 -> Descript auto-transcribes in ~1 min.
  3. Edit-by-transcript: remove bad takes, silences, filler words ("um", "uh", "so").
  4. Run "Remove Filler Words" suggester; review each suggested cut.
  5. Add on-screen text overlays at beat transitions per DEMO_SCRIPT.md.
  6. Proofread auto-transcript for technical terms: `pybag` (often transcribed "pie bag"), `DbgEng`, `MCP`, `Claude Code`, `stackly`, `Cursor`, etc. Fix each manually.
  7. Export Multitrack -> MP4 (1080p, H.264, 60fps) + `.srt` separately. No watermark (requires paid tier).
  8. Create thumbnail: 1280x720 PNG. Tools: Canva free, Figma, or static frame from the recording with added overlay. Must show crash dialog or debugger state — something visually distinct. **Do NOT** use shouty-YouTube-influencer aesthetic (big arrows, yelling face).
  9. **Write the thumbnail to both paths (pre-decided — do not punt to execution):**
     - Canonical README path: `docs/demo-thumb.png` (renders cleanly in GitHub's README preview — this is the path the README embed in Task 2b.A.1 step 4 references).
     - Site-served copy: `site/public/demo-thumb.png` (a two-line `cp` from `docs/demo-thumb.png`; served by Astro at `/demo-thumb.png`, which is what the landing-page `VideoEmbed.astro` component references in Task 2b.B.4).
     Both files are committed. No further path-decision is required downstream.
- **Acceptance criteria:**
  - Final MP4 duration is 60-65s, 1080p60, no watermark.
  - `.srt` file exists and is syntactically valid (load in a text editor; cues formatted `HH:MM:SS,ms --> HH:MM:SS,ms`).
  - Both `docs/demo-thumb.png` (canonical, referenced from README) and `site/public/demo-thumb.png` (served by Astro at `/demo-thumb.png`) exist, each 1280x720, < 500 KB. The two files have identical content (byte-equal `cp`).
  - Transcript free of auto-transcription errors for technical terms (spot-check: search for `pie bag`, `debug bridge` without camelcase, etc.).
- **Size:** L (3-4h per RESEARCH.md §12, first-timer)
- **Autonomy:** CHECKPOINT
- **Resume signal:** "final MP4 + srt + thumbnail ready"
- **Dependencies:** 2b.C.2.

#### Task 2b.C.4 — Upload to YouTube (unlisted) + set metadata

- **Files:** `.planning/phase-2b-public-launch/DECISIONS.md` (append `Demo video URL: <URL>` + `Video ID: <ID>`).
- **Action (CHECKPOINT — human):**
  1. Upload the final MP4 from Task 2b.C.3 to the YouTube channel chosen in Task 2b.0.4.
  2. Visibility: **unlisted** (for soak period).
  3. Title: `Stackly — Remote crash capture for Claude Code (60s demo)`.
  4. Description (pull from a reusable snippet — RESEARCH.md §7.Twitter tweet 1 is a starting point):
     ```
     Stackly is an MCP server that exposes live Windows debugger state to Claude Code, Cursor, and Claude Desktop. One command captures a remote crash; Claude Code reads the stack and proposes a fix.

     Install (from source): https://github.com/IdanG7/stackly
     Landing page: https://<domain>
     Docs: https://github.com/IdanG7/stackly#quick-start
     ```
  5. Tags: `mcp`, `model context protocol`, `claude code`, `debugger`, `windows`, `c++`, `crash reporting`, `developer tools`.
  6. Upload captions: use the `.srt` from Task 2b.C.3, NOT YouTube's auto-generated captions. Set language to English.
  7. Thumbnail: upload `demo-thumb.png` from Task 2b.C.3.
  8. Record video URL (`https://youtu.be/<ID>`) and video ID in DECISIONS.md.
- **Acceptance criteria:**
  - Video is listed on YouTube (unlisted), URL in DECISIONS.md.
  - Captions show the Descript-generated text (not YouTube auto-CC).
  - Thumbnail shows the custom image, not an auto-frame.
  - Duration matches the final MP4 (60-65s).
- **Size:** S-M (30-60 min, includes waiting for YouTube processing)
- **Autonomy:** CHECKPOINT
- **Resume signal:** "video uploaded: <URL>"
- **Dependencies:** 2b.C.3, 2b.0.4.

#### Task 2b.C.5 — Patch video URL + thumbnail into README + landing page, flip YouTube to public

- **Files:**
  - `README.md` (replace `youtu.be/XXXX` placeholder + `docs/demo-thumb.png` placeholder with real values from DECISIONS.md + shipped thumbnail from Task 2b.C.3).
  - `site/src/components/VideoEmbed.astro` (replace placeholder videoId with real ID).
- **Action:**
  1. (AUTO) Read `.planning/phase-2b-public-launch/DECISIONS.md` for `Video ID` and `Demo video URL`.
  2. (AUTO) Patch `README.md`:
     - Replace `https://youtu.be/XXXX` -> real URL.
     - The `docs/demo-thumb.png` reference already matches the canonical path committed in Task 2b.C.3 — confirm the file exists at `docs/demo-thumb.png` and no further path substitution is required. (Landing page uses `/demo-thumb.png` served from `site/public/demo-thumb.png` — also already in place.)
  3. (AUTO) Patch `site/src/components/VideoEmbed.astro` videoId prop with the real video ID.
  4. (AUTO) `npm run build` in `site/` and verify no broken references.
  5. (CHECKPOINT — human) Once landing page + README are patched and landing-page staging looks good, YouTube Studio -> change video visibility from **unlisted** to **public**.
- **Acceptance criteria:**
  - `grep -F 'youtu.be/XXXX' README.md` returns no matches (placeholder patched).
  - `grep -F 'dQw4w9WgXcQ' site/src/components/VideoEmbed.astro` returns no matches (Rick Astley placeholder gone).
  - Loading `https://<domain>` shows the real video thumbnail (not a 404).
  - Clicking the video thumbnail plays the real demo.
  - YouTube video is public (verify incognito).
- **Size:** S (15-30 min)
- **Autonomy:** AUTO + CHECKPOINT (visibility flip)
- **Resume signal:** "video is public"
- **Dependencies:** 2b.C.4, 2b.A.1 (README exists), 2b.B.5 (site deployed with placeholders).

---

### Phase 2b.D — Distribution track (launch drafts + GH metadata + social preview)

Four tasks. All can run in parallel with Tracks A-C (no dependency on landing/video), except that launch drafts should reference the live URLs once they exist (final edit pass in Task 2b.F.2).

#### Task 2b.D.1 — Update GitHub repo metadata (description, homepage, topics)

- **Files:** none (external action via `gh` CLI). Record outcome in DECISIONS.md.
- **Action (AUTO with CHECKPOINT if `gh` hits rate limit or permission error — in practice this is one API call):**
  ```bash
  gh repo edit IdanG7/stackly \
    --description "Remote crash capture MCP server for native Windows applications. Exposes live DbgEng debugger state (stack, exception, threads, locals) to Claude Code, Cursor, and Claude Desktop." \
    --homepage "https://<domain>" \
    --add-topic mcp \
    --add-topic model-context-protocol \
    --add-topic mcp-server \
    --add-topic claude-code \
    --add-topic cursor \
    --add-topic claude-desktop \
    --add-topic windows \
    --add-topic debugging \
    --add-topic debugger \
    --add-topic cpp \
    --add-topic crash-reporter \
    --add-topic crash-analysis \
    --add-topic ai-agents \
    --add-topic developer-tools
  ```
  (Description stays under 350 chars per GitHub API cap; the one above is ~260 chars.)
- **Acceptance criteria:**
  - `gh repo view IdanG7/stackly --json description,homepageUrl,repositoryTopics` returns the expected description, homepage `https://<domain>`, and all 13 topics.
  - Visiting `https://github.com/IdanG7/stackly` shows the About sidebar populated (description, homepage link, topic chips).
- **Size:** XS (5 min)
- **Autonomy:** AUTO
- **Dependencies:** 2b.0.1.

#### Task 2b.D.2 — Design + upload social preview image (1280x640)

- **Files:** `docs/social-preview.png` (local source file for archival; actual upload is via GitHub UI).
- **Action (CHECKPOINT — human):**
  1. Design a 1280x640 PNG, < 1 MB: project logo + tagline + a screenshot of the debugger state (or a stylized version). Tools: Canva free template, Figma, or `socialify.git.ci` for auto-generated fallback. Avoid shouty-influencer aesthetic.
  2. Save to `docs/social-preview.png` in the repo (archival).
  3. GitHub repo -> Settings -> General -> Social preview -> Upload new image.
  4. Verify by posting `https://github.com/IdanG7/stackly` in a Slack/Discord/Twitter DM to self — the unfurl should use the new preview.
- **Acceptance criteria:**
  - `docs/social-preview.png` exists, 1280x640, < 1 MB.
  - GitHub settings show the custom social preview (not the auto-generated default).
  - A link unfurl test (Slack or Twitter preview) renders the custom preview.
- **Size:** S-M (1h per RESEARCH.md §12)
- **Autonomy:** CHECKPOINT (design + upload via UI)
- **Resume signal:** "social preview uploaded"
- **Dependencies:** 2b.0.1.

#### Task 2b.D.3 — Draft launch posts in LAUNCH_POSTS.md

- **Files:** `.planning/phase-2b-public-launch/LAUNCH_POSTS.md` (new).
- **Action:** Write drafts following the conventions in RESEARCH.md §7. Structure:
  ```markdown
  # Stackly — Launch Post Drafts

  > **NOT YET PUBLISHED.** These are drafts only. Publication is a separate go/no-go decision after landing page + video + directory submissions are all live. See `LAUNCH_READINESS.md`.

  ## Review log
  - Drafted: <date>
  - Last revised: <date>
  - Reviewer: <@handle>

  ---

  ## Hacker News — "Show HN"

  **Title (under 80 chars):** `Show HN: Stackly – Remote crash capture for Windows C++, exposed via MCP`
  **Link target:** `https://github.com/IdanG7/stackly` (NOT the landing page — HN readers click through to READMEs).
  **Timing:** Tue/Wed/Thu, 8-11am ET.
  **First-comment body (4-8 sentences — follows RESEARCH.md §7 HN structure):**
  > [full draft here, 4-8 sentences, first-person, no superlatives, honest limitations, request for specific feedback]

  ---

  ## Reddit — r/cpp (primary target)

  **Title:** `Stackly: Remote DbgEng capture exposed to Claude Code via MCP (open source)`
  **Flair:** "Show and Tell" or "Tooling" (verify at post time — Task 2b.F.2).
  **Link target:** `https://github.com/IdanG7/stackly`.
  **Body (technical war-story framing — NOT a marketing pitch):**
  > [draft walking through a technical decision — e.g., "we used WinDbg command parsing because pybag's wrappers for GetLineByOffset raise E_NOTIMPL; here's the implementation and tradeoffs"; mention project in closing paragraph]

  ---

  ## Reddit — r/gamedev Feedback Friday

  **Where:** weekly Feedback Friday thread only (standalone posts = 24h ban per sidebar rules — verify at post time).
  **Timing:** Friday morning ET.
  **Body (2-3 sentences + link):**
  > [short draft framing Stackly for game-studio crash triage]

  ---

  ## Reddit — r/programming

  **Status:** `DEFERRED_TO_2C`. Research recommends tying to a technical blog post which is out of scope for 2b (see Decision #10 in PLAN.md §2).

  ---

  ## Twitter / X launch thread

  **Status:** [ACTIVE | DEFERRED — per DECISIONS.md Twitter handle decision]

  **Thread (5-8 tweets):**
  1. Hook + demo GIF (not video — autoplays in feed) + `https://<domain>` link.
  2. [...]
  3. [...]
  ...
  8. Quote-repost hook: tag `@AnthropicAI`, `@cursor_ai`, `@ModelContextP`, `@windows_dev` (or equivalent current handles — verify at post time).

  ---

  ## Pre-publication checklist (copy into LAUNCH_READINESS.md)

  - [ ] Landing page live with Lighthouse >= 90
  - [ ] Video public on YouTube, embedded on landing page and README
  - [ ] >= 4 directory submissions live or pending
  - [ ] README rewrite shipped to main
  - [ ] OSS scaffolding merged (CONTRIBUTING, CoC, SECURITY)
  - [ ] Repo About metadata populated
  - [ ] Social preview image uploaded
  - [ ] 48-hour soak period on landing page complete (R4 mitigation)
  - [ ] Sidebar rules for r/cpp and r/gamedev re-verified at post time
  ```
- **Acceptance criteria:**
  - LAUNCH_POSTS.md exists with the banner `NOT YET PUBLISHED` at the top.
  - Four sections: HN draft, r/cpp draft, r/gamedev draft, Twitter thread.
  - r/programming section present with `DEFERRED_TO_2C` status.
  - Twitter section reflects DECISIONS.md Twitter handle (ACTIVE or DEFERRED).
  - No draft post is listed as "final" — all have `## Review log` sections stating pre-publication status.
  - Honest-marketing grep on the file: `grep -Ei '(auto-detect|automatically detect|cross-platform|pip install|the fastest|the best|first-of-its-kind)' LAUNCH_POSTS.md` returns zero unintentional hits (uses in "honest limitations" context like `"auto-detect is Phase 2.5, not today"` are acceptable — review manually).
- **Size:** L (3-4h per RESEARCH.md §12)
- **Autonomy:** AUTO
- **Dependencies:** 2b.0.3 (Twitter handle decision), 2b.C.4 (YouTube URL for Twitter thread media reference — but can draft with placeholder). Final URL substitutions happen in Task 2b.F.2.

#### Task 2b.D.4 — Replace placeholder favicon + logo with polished versions

- **Files:**
  - `site/public/favicon.svg` (replace placeholder from Task 2b.B.4).
  - `site/public/logo.svg` (replace placeholder from Task 2b.B.4).
  - `site/public/og-image.png` (new: 1200x630 social card image).
- **Action:**
  1. Design favicon (24x24 effective, but SVG so it scales) — monochrome glyph (e.g., stylized "DB" or a debugger-bridge pictogram).
  2. Design logo (horizontal SVG: glyph + wordmark "Stackly").
  3. Design `og-image.png` at 1200x630: project name + tagline + small screenshot. This is the image surfaced in Twitter / LinkedIn / Slack link unfurls of `https://<domain>` (distinct from GitHub repo social preview in 2b.D.2).
  4. Confirm favicon renders at 16x16 and 32x32 (browsers/OS scale it down automatically).
  5. Push; Cloudflare Pages redeploys.
- **Acceptance criteria:**
  - `site/public/favicon.svg` is valid SVG, < 5 KB, renders recognizably at 16x16.
  - `site/public/logo.svg` is valid SVG, includes wordmark.
  - `site/public/og-image.png` is 1200x630, < 500 KB.
  - Loading `https://<domain>` in a browser shows the custom favicon in the tab.
  - `curl -sI https://<domain>/og-image.png` returns 200 with `Content-Type: image/png`.
  - `astro-seo` in BaseLayout references `/og-image.png` as the default OG image.
- **Size:** M-L (1-2h design + iteration)
- **Autonomy:** AUTO (if using a template/generator) or CHECKPOINT (if human design in Figma/Canva). Default to CHECKPOINT.
- **Resume signal:** "brand assets shipped"
- **Dependencies:** 2b.B.5 (needs site deployed so changes can be seen).

---

### Phase 2b.E — Directory submissions

Five tasks. All depend on README + landing page URL + video URL being live. Initialize tracker first.

#### Task 2b.E.0 — Create DIRECTORY_SUBMISSIONS.md tracker

- **Files:** `.planning/phase-2b-public-launch/DIRECTORY_SUBMISSIONS.md` (new).
- **Action:** Create tracker with a fixed header + rows-to-fill:
  ```markdown
  # MCP Directory Submissions

  **Strategy (per PLAN.md Decision #5):** 2 active submissions (Official Registry, Smithery) + 2 bonus (LobeHub, mcp.so) = 4 to clear GOAL-4. PulseMCP + GitHub MCP Registry auto-ingest from Official Registry.

  ## Tracker

  | Directory | Type | Submission URL | Submitted | Listing URL | Status | Notes |
  |-----------|------|----------------|-----------|-------------|--------|-------|
  | Official MCP Registry | active | registry.modelcontextprotocol.io | (date) | (listing URL once live) | pending/live/rejected | Source-only submission via websiteUrl |
  | Smithery | active | smithery.ai/new | (date) | | pending/live/rejected | Source-install flow; monitor for rejection (R2) |
  | LobeHub | bonus | lobehub.com/mcp | (date) | | pending/live/rejected | |
  | mcp.so | bonus | mcp.so/submit | (date) | | pending/live/rejected | |
  | awesome-mcp-servers (punkpeye) | bonus | github PR | (date) | | pending/live/rejected | |
  | PulseMCP | passive | (auto from Official) | n/a | | auto | Ingests from Official Registry ~weekly |
  | GitHub MCP Registry | passive | (auto from Official) | n/a | | auto | Ingests from Official Registry |

  ## Per-directory metadata prep (shared)

  **Canonical name:** Stackly
  **Namespace:** io.github.idang7/stackly (lowercase per registry convention)
  **One-line description (<= 120 chars):** Remote crash capture MCP server for Windows native apps. Exposes live DbgEng debugger state to Claude Code, Cursor, Desktop.
  **Install command (source-only for 2b):** `git clone https://github.com/IdanG7/stackly.git && cd stackly && uv sync`
  **Config snippet (Claude Desktop):** `{"mcpServers": {"stackly": {"url": "http://localhost:8585/mcp"}}}`
  **License:** MIT
  **Links:** README, landing page, demo video — all three populated from real URLs.

  ## Fallback if Smithery rejects (R2 mitigation)

  If Smithery rejects the source-install listing, escalate Phase 2c (PyPI publish) and re-submit, OR accept a different bonus directory (e.g., push `awesome-mcp-servers` PR and count it as submission #4). Either path keeps GOAL-4 achievable.
  ```
- **Acceptance criteria:**
  - File exists with all 5 active/bonus rows + 2 passive rows.
  - Shared metadata block populated with real values (landing URL + video URL from prior tasks).
  - Fallback strategy documented.
- **Size:** XS (10 min)
- **Autonomy:** AUTO
- **Dependencies:** 2b.A.1, 2b.B.5, 2b.C.5 (need all three URLs).

#### Task 2b.E.1 — Submit to Official MCP Registry (`registry.modelcontextprotocol.io`)

- **Files:**
  - `server.json` (new at repo root).
  - Update `DIRECTORY_SUBMISSIONS.md` row for Official Registry.
- **Action (CHECKPOINT — human action: `mcp-publisher login github` requires OAuth device-flow interaction):**
  1. Write `server.json` verbatim from RESEARCH.md §6A (source-only minimal):
     ```json
     {
       "$schema": "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json",
       "name": "io.github.idang7/stackly",
       "title": "Stackly",
       "description": "Remote crash capture MCP server for Windows native apps. Exposes live DbgEng debugger state (stack, locals, threads, exception info) to MCP clients.",
       "version": "0.2.1",
       "repository": {
         "url": "https://github.com/IdanG7/stackly",
         "source": "github"
       },
       "websiteUrl": "https://<chosen-domain>"
     }
     ```
     Note: `version` MUST match the version bump from Task 2b.F.3 (0.2.1) or be bumped simultaneously.
  2. Install `mcp-publisher` CLI. On Windows: download the latest Windows binary from https://github.com/modelcontextprotocol/registry/releases and place on PATH, OR use `brew install mcp-publisher` if on a mac / WSL.
  3. Authenticate: `mcp-publisher login github` (OAuth device flow — paste code at github.com/login/device).
  4. Publish: `mcp-publisher publish` from the repo root.
  5. Verify: `curl "https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.idang7/stackly"` returns the published entry.
  6. Update DIRECTORY_SUBMISSIONS.md row: submission date, listing URL (`https://registry.modelcontextprotocol.io/v0.1/servers/io.github.idang7/stackly` or similar), status = `live`.
- **Acceptance criteria:**
  - `server.json` exists at repo root, validates against the linked schema (spot-check via https://validator.schemastore.org or paste into https://www.jsonschemavalidator.net).
  - `mcp-publisher publish` exits 0.
  - Curl query above returns the server entry with `name == "io.github.idang7/stackly"`.
  - DIRECTORY_SUBMISSIONS.md updated.
- **Size:** M (30-60 min, most of it OAuth + first-time CLI install on Windows)
- **Autonomy:** CHECKPOINT (OAuth device flow)
- **Resume signal:** "MCP registry live: <listing URL>"
- **Dependencies:** 2b.E.0, 2b.B.5 (landing page must be live before `websiteUrl` is reachable), 2b.A.1 (README shipped so visitors have content).

#### Task 2b.E.2 — Submit to Smithery (`smithery.ai`)

- **Files:** Update `DIRECTORY_SUBMISSIONS.md` row for Smithery.
- **Action (CHECKPOINT — human):** Use web form (RESEARCH.md §6B option 2 — not CLI, since Stackly is source-install, not a hosted URL):
  1. Go to https://smithery.ai/new .
  2. Fill form with values from DIRECTORY_SUBMISSIONS.md "shared metadata" block.
  3. Submit.
  4. Update tracker row: submission date, status = `pending`.
  5. **Monitoring:** Check back in 3-7 days. If approved -> `live` + listing URL. If rejected -> `rejected` + reason. If rejected, apply R2 fallback: push `awesome-mcp-servers` PR (Task 2b.E.5 already covers this) and count it as the 4th submission.
- **Acceptance criteria:**
  - Form submitted; Smithery confirmation email received.
  - DIRECTORY_SUBMISSIONS.md row status = `pending` (initial) or `live`/`rejected` after review period.
  - If rejected, fallback rationale logged in DIRECTORY_SUBMISSIONS.md Notes column.
- **Size:** S (20 min submission + 3-7 day wait, not blocking)
- **Autonomy:** CHECKPOINT
- **Resume signal:** "smithery submitted" (initial) or "smithery: live|rejected" (post-review)
- **Dependencies:** 2b.E.0.

#### Task 2b.E.3 — Submit to LobeHub (`lobehub.com/mcp`)

- **Files:** Update DIRECTORY_SUBMISSIONS.md row.
- **Action (CHECKPOINT — human):** Go to https://lobehub.com/mcp , click "Submit MCP" (or equivalent button — verify current UI). Fill form with shared metadata. Submit. Update tracker row.
- **Acceptance criteria:**
  - Form submitted; tracker row shows `pending`.
  - Listing goes `live` within 2-7 days.
- **Size:** XS-S (15 min)
- **Autonomy:** CHECKPOINT
- **Resume signal:** "lobehub submitted"
- **Dependencies:** 2b.E.0.

#### Task 2b.E.4 — Submit to mcp.so

- **Files:** Update DIRECTORY_SUBMISSIONS.md row.
- **Action (CHECKPOINT — human):** Go to https://mcp.so/submit (web form) or open a GitHub issue on the mcp.so repo (form is easier). Fill and submit. Update tracker row.
- **Acceptance criteria:**
  - Form submitted (or issue opened); tracker row shows `pending`.
  - Listing goes `live` within 2-7 days.
- **Size:** XS (10 min)
- **Autonomy:** CHECKPOINT
- **Resume signal:** "mcp.so submitted"
- **Dependencies:** 2b.E.0.

#### Task 2b.E.5 — (BONUS) Open PR to `punkpeye/awesome-mcp-servers`

- **Files:** PR to `punkpeye/awesome-mcp-servers` (external repo). Update DIRECTORY_SUBMISSIONS.md row.
- **Action (AUTO — git + gh, no form fill):**
  1. `gh repo clone punkpeye/awesome-mcp-servers <tmp>`.
  2. Branch: `add/stackly`.
  3. Locate the "Developer Tools" or "Debugging" category. Add line in alphabetical order:
     ```markdown
     - [IdanG7/stackly](https://github.com/IdanG7/stackly) 🎖️ - Remote crash capture for native Windows processes. Exposes DbgEng debugger state (call stack, exception info, threads, locals) to MCP clients.
     ```
  4. Respect their CONTRIBUTING.md format — the 🎖️ emoji means "official" (verify against their latest conventions; emoji set may have changed).
  5. `gh pr create --title "Add Stackly" --body "<one-liner + link to README + license>"`.
  6. Update tracker row: PR URL, date, status = `pending`.
  7. Serves as R2 Smithery-rejection fallback if needed.
- **Acceptance criteria:**
  - PR exists and is open against `punkpeye/awesome-mcp-servers`.
  - PR passes any automated checks on the target repo.
  - Entry is alphabetically placed in the correct category.
  - Tracker row updated with PR URL.
- **Size:** S (20-30 min)
- **Autonomy:** AUTO
- **Dependencies:** 2b.E.0.

---

### Phase 2b.F — Launch readiness verification

Three tasks. The gate that asserts all 7 GOAL criteria are met before the phase exits.

#### Task 2b.F.1 — Build LAUNCH_READINESS.md checklist mapping all 7 GOAL criteria to evidence

- **Files:** `.planning/phase-2b-public-launch/LAUNCH_READINESS.md` (new).
- **Action:** Construct a single-file go/no-go checklist. Structure:
  ```markdown
  # Phase 2b — Launch Readiness Checklist

  **Target state:** Every row below is checked and has a link to evidence.

  ## GOAL-1: README rewrite shipped on main
  - [ ] README.md rewritten per RESEARCH.md §4 (evidence: commit SHA + GitHub URL)
  - [ ] Hero demo thumbnail links to real YouTube URL (evidence: grep -F 'youtu.be' README.md)
  - [ ] Quick-start executes cleanly on a fresh Windows 10/11 VM (evidence: screen recording or terminal log in DEMO_DOGFOOD.md, optional)
  - [ ] Architecture diagram present (evidence: grep -A 10 'TEST MACHINE' README.md)
  - [ ] MCP client configs for Claude Code + Cursor + Claude Desktop (evidence: 3 fenced code blocks under the MCP client section)
  - [ ] Honest-marketing grep passes (evidence: grep results logged)

  ## GOAL-2: Landing page at <domain> live
  - [ ] <domain> resolves and returns 200 (evidence: curl -sI https://<domain>)
  - [ ] Lighthouse >= 90 on Performance, Accessibility, Best Practices, SEO (evidence: `npx lighthouse https://<domain> --view` saved output; scores in this file)
  - [ ] Video embedded above the fold (evidence: lighthouse screenshot or view-source)
  - [ ] OG + Twitter cards set (evidence: `curl -s https://<domain> | grep -E 'og:|twitter:'`)
  - [ ] Favicon + logo consistent with repo (evidence: view tab icon + logo.svg)
  - [ ] Page source committed under site/ (evidence: git log site/)

  ## GOAL-3: 60-second demo video recorded + uploaded
  - [ ] YouTube URL public (evidence: incognito visit)
  - [ ] Captions/subtitles present (evidence: YouTube CC button shows English)
  - [ ] Video URL linked from README and landing page (evidence: grep + landing page visual)

  ## GOAL-4: >= 4 MCP directory submissions tracked
  - [ ] DIRECTORY_SUBMISSIONS.md shows >= 4 rows with submission dates
  - [ ] At least 4 rows are pending or live (rejected rows don't count)
  - [ ] Each row has: directory, submission URL, submission date, listing URL (once live), status, metadata notes

  ## GOAL-5: Launch post drafts written
  - [ ] LAUNCH_POSTS.md has HN + r/cpp + r/gamedev + Twitter sections
  - [ ] Top banner `NOT YET PUBLISHED` present
  - [ ] r/programming noted as `DEFERRED_TO_2C`

  ## GOAL-6: Open-source scaffolding
  - [ ] CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md exist at repo root
  - [ ] .github/ISSUE_TEMPLATE/*.yml + .github/PULL_REQUEST_TEMPLATE.md exist
  - [ ] GitHub repo About panel (description, homepage, topics) populated
  - [ ] Social preview image uploaded

  ## GOAL-7: Discoverability
  - [ ] robots.txt + sitemap.xml served from <domain>
  - [ ] Google Search Console verified for <domain>; sitemap submitted
  - [ ] Repo description + homepage + topics set (see GOAL-6)

  ## Pre-publication (separate go/no-go, NOT a 2b exit criterion)
  - [ ] 48-hour soak period on landing page post-deploy (R4 mitigation)
  - [ ] Sidebar rules for r/cpp and r/gamedev re-verified at post time
  - [ ] Final Lighthouse re-run immediately before HN post
  - [ ] CHANGELOG 0.2.1 entry finalized and tagged

  ## Exit status
  - **All GOAL rows checked:** <YES / NO>
  - **Phase 2b exit date:** <YYYY-MM-DD>
  - **Next phase:** Phase 2c (PyPI + onboarding polish)
  ```
- **Acceptance criteria:**
  - File exists with all 7 GOAL sections + pre-publication section.
  - Each row has concrete evidence fields (URL, command, or file path — not vague phrasing).
  - No row says "looks good" — every one has a deterministic check.
- **Size:** S (30 min)
- **Autonomy:** AUTO
- **Dependencies:** none (can draft before other tasks land — this is a specification of what OTHER tasks must prove).

#### Task 2b.F.2 — Write + run link-checker and Lighthouse scripts (TDD-first because they are code)

- **Files:**
  - `scripts/check_launch_links.py` (new).
  - `scripts/check_lighthouse.py` (new, thin wrapper around `npx lighthouse`).
  - `tests/test_check_launch_links.py` (new).
  - `.planning/phase-2b-public-launch/LAUNCH_READINESS.md` (append "Check results" section with scores + any dead links found).
- **Failing test to write first:**
  - `tests/test_check_launch_links.py::test_extract_urls_from_markdown_finds_all_formats` — build a markdown string with `[inline link](https://a.com)`, `<https://b.com>`, `https://c.com` bare, and `[ref-style][ref]\n\n[ref]: https://d.com`; call `extract_urls(md_text)`; assert the returned set equals `{"https://a.com", "https://b.com", "https://c.com", "https://d.com"}`.
- **Action:**
  1. Implement `scripts/check_launch_links.py`:
     - CLI: `python scripts/check_launch_links.py README.md site/src/**/*.astro .planning/phase-2b-public-launch/LAUNCH_POSTS.md`.
     - `extract_urls(text: str) -> set[str]` — handles `[text](url)`, `<url>`, bare-http, ref-style `[ref]: url`.
     - For each URL: use `urllib.request.build_opener()` with a custom `urllib.request.HTTPRedirectHandler` to follow up to 5 redirects; `timeout=10s` on each request. Treat 2xx as pass, 3xx-after-redirect as pass (final URL returns 2xx), 4xx/5xx/timeout as fail. `urllib.parse` check before the request (skip `mailto:`, `javascript:`). Stdlib only — do NOT add any third-party HTTP client (no `requests`, no `httpx`). This keeps the script runnable without any `uv sync --extra ...` step.
     - Output: table of URL / status / source file, exit 1 if any broken.
  2. Implement `scripts/check_lighthouse.py`:
     - CLI: `python scripts/check_lighthouse.py https://<domain>`.
     - Shells out to `npx lighthouse <url> --output json --output-path -` (needs `npx` / `npm` on PATH).
     - Parses the JSON, extracts the 4 scores (performance, accessibility, best-practices, seo), fails (exit 1) if any < 90.
  3. Run both scripts; paste outputs into LAUNCH_READINESS.md "Check results" section.
- **Acceptance criteria:**
  - Failing test passes after `extract_urls` is implemented (RED -> GREEN).
  - `python scripts/check_launch_links.py README.md LAUNCH_POSTS.md site/src/pages/index.astro` exits 0 (no broken links).
  - `python scripts/check_lighthouse.py https://<domain>` exits 0 with all 4 scores >= 90.
  - LAUNCH_READINESS.md "Check results" section has both script outputs pasted + date.
- **Size:** M (1h — two small scripts + one test)
- **Autonomy:** AUTO
- **Dependencies:** 2b.F.1, 2b.B.5, 2b.C.5.

#### Task 2b.F.3 — Version bump to 0.2.1, finalize CHANGELOG, tag, commit

- **Files:**
  - `pyproject.toml` (bump `version = "0.2.1"`).
  - `CHANGELOG.md` (promote Unreleased to `## [0.2.1] - <date>`).
  - `src/stackly/__init__.py` (bump `__version__` if present — verify).
  - `server.json` (already bumped in Task 2b.E.1 — verify it matches).
  - `.planning/phase-2b-public-launch/LAUNCH_READINESS.md` (flip "Exit status" fields to YES + date).
- **Action:**
  1. Bump version in `pyproject.toml` to `0.2.1`. Then, for `src/stackly/__init__.py`: run `grep -c '^__version__' src/stackly/__init__.py`. If the count is 0, do NOT create the attribute — `pyproject.toml` is authoritative and the bump is a single-file change to `pyproject.toml` only. If the count is >= 1, bump `__version__` to `"0.2.1"` in lockstep with `pyproject.toml` (this is a version-string change only — no functional code changes, consistent with the phase-level constraint). The frontmatter lists `src/stackly/__init__.py` with that disclosure comment.
  2. Promote CHANGELOG's `## [Unreleased]` to `## [0.2.1] - YYYY-MM-DD`.
  2a. Read `.planning/phase-2b-public-launch/DIRECTORY_SUBMISSIONS.md`; replace the generic Marketing bullet ("Submitted to MCP directories (see DIRECTORY_SUBMISSIONS.md ...)") with the specific directory names that are `live` at phase-exit time. If a submission is still `pending` or `rejected`, do NOT list it. Minimum 4 named live directories are required to clear GOAL-4; if fewer than 4 are live, pause and resolve before tagging.
  3. Verify `server.json` `version` matches.
  4. Run full test suite: `uv run pytest -m "not integration"` — must pass (0 functional code changes this phase, so no regressions).
  5. Commit: `chore(phase-2b): version bump to 0.2.1 + launch readiness`.
  6. Tag: `git tag v0.2.1` (not pushed until launch go/no-go; tagging early makes CHANGELOG reference consistent).
  7. Update LAUNCH_READINESS.md: set `All GOAL rows checked: YES` and `Phase 2b exit date: <today>`.
  8. DO NOT push tag to remote yet — that signals launch and is the separate go/no-go decision.
- **Acceptance criteria:**
  - `grep '^version' pyproject.toml` returns `version = "0.2.1"`.
  - CHANGELOG.md has `## [0.2.1] - <date>` section; no `[Unreleased]` header anymore (or an empty one for future work).
  - `uv run pytest -m "not integration"` exits 0.
  - `git tag --list v0.2.1` shows the tag exists locally.
  - Commit exists with the specified message.
  - LAUNCH_READINESS.md shows all rows checked + exit date.
- **Size:** S (15-30 min)
- **Autonomy:** AUTO
- **Dependencies:** ALL prior tasks. This is the merge-to-finish gate.

---

## 5. Dependency graph + wave ordering

### Task-level dependency graph

```
Wave 0 (Prep — Day 0)
  2b.0.1 domain register ─┐
                          ├─► Wave B starts
  2b.0.2 email routing ───┤    (2b.A.4, 2b.A.5 need email alias)
  2b.0.3 twitter decision ┤
  2b.0.4 youtube decision ┘

Wave 1 (Track A content + Track B scaffold + Track D metadata — all parallel)
  Track A: 2b.A.1 README, 2b.A.2 DEMO_SCRIPT, 2b.A.3 CONTRIBUTING, 2b.A.6 templates, 2b.A.7 gitattributes, 2b.A.8 CHANGELOG
  Track A: 2b.A.4 COC (needs 2b.0.2 email), 2b.A.5 SECURITY (needs 2b.0.2 email)
  Track B (internal sequence: B.1 ∥ B.2 → B.3 — B.1 can run in parallel with B.2; B.3 waits for B.2): 2b.B.1 DNS sanity (needs 2b.0.1), 2b.B.2 Astro scaffold (needs 2b.0.1), 2b.B.3 BaseLayout (needs 2b.0.3 + 2b.B.2)
  Track D: 2b.D.1 gh metadata (needs 2b.0.1), 2b.D.2 social preview (needs 2b.0.1), 2b.D.3 launch drafts (needs 2b.0.3)

Wave 2 (Track B components + Track C recording)
  Track B: 2b.B.4 components (needs 2b.B.3 + 2b.0.3 + 2b.A.2)
  Track C: 2b.C.1 script review (needs 2b.A.2)
  Track C: 2b.C.2 recording (needs 2b.C.1)

Wave 3 (Track B deploy + Track C edit)
  Track B: 2b.B.5 Pages deploy (needs 2b.B.2 + 2b.B.4 + 2b.B.1)
  Track C: 2b.C.3 Descript edit (needs 2b.C.2)

Wave 4 (Track B analytics + GSC + Track C upload + Track D polish)
  Track B: 2b.B.6 analytics (needs 2b.B.5)
  Track B: 2b.B.7 GSC (needs 2b.B.5)
  Track C: 2b.C.4 YT upload (needs 2b.C.3 + 2b.0.4)
  Track D: 2b.D.4 brand assets (needs 2b.B.5)

Wave 5 (Track C integration into site/README)
  Track C: 2b.C.5 patch URLs + flip public (needs 2b.C.4 + 2b.A.1 + 2b.B.5)

Wave 6 (Directory submissions — all need URLs from prior waves)
  Track E: 2b.E.0 tracker (needs 2b.A.1 + 2b.B.5 + 2b.C.5)
  Track E: 2b.E.1 Official Registry (needs 2b.E.0)
  Track E: 2b.E.2 Smithery (needs 2b.E.0) — parallel to E.1
  Track E: 2b.E.3 LobeHub (needs 2b.E.0) — parallel
  Track E: 2b.E.4 mcp.so (needs 2b.E.0) — parallel
  Track E: 2b.E.5 awesome-mcp-servers PR (needs 2b.E.0) — parallel

Wave 7 (Launch readiness)
  2b.F.1 LAUNCH_READINESS spec (can start Wave 1 — no blocking deps)
  2b.F.2 checker scripts (needs 2b.F.1 + 2b.B.5 + 2b.C.5)
  2b.F.3 version bump + tag (needs ALL prior)
```

### Hard sequencing constraints

1. **2b.0.1 first** (domain squat risk R1).
2. **2b.A.2 before 2b.C.1** (script must exist before review begins).
3. **2b.C.1 before 2b.C.2** (no recording until script approved).
4. **2b.C.4 before 2b.C.5** (need real video URL before patching).
5. **2b.B.5 before 2b.B.6, 2b.B.7, 2b.C.5 landing-page test, 2b.E.*** (live URL required).
6. **2b.A.1 + 2b.B.5 + 2b.C.5 before 2b.E.** (all three URLs required for directory metadata).
7. **2b.F.3 last** (merge-to-finish gate).

### Parallelism wins

- Wave 1 runs 10+ tasks in parallel (Tracks A, B, D all start together).
- Wave 6 runs 5 directory submissions in parallel.
- Track C is the critical path (script -> record -> edit -> upload -> patch). Wall-clock minimum ~10-15h total across 2-3 sessions.

### Critical path length

Critical path: 2b.0.1 -> 2b.A.2 -> 2b.C.1 -> 2b.C.2 -> 2b.C.3 -> 2b.C.4 -> 2b.C.5 -> 2b.E.1 -> 2b.F.2 -> 2b.F.3.

10 sequential tasks, dominated by video production hours. Total wall-clock 2-3 weeks per RESEARCH.md §12 (30-45 hours of work, pipelined with waits on DNS / Smithery review / video takes).

---

## 6. Non-goals reaffirmed

From GOAL.md — anything in this list that appears in a task is a bug in the plan:

- NO PyPI publish work (`pip install stackly` stays Phase 2c).
- NO signed wheels.
- NO standalone docs site (separate from landing page).
- NO publishing of launch posts (drafts only).
- NO paid analytics; Cloudflare Web Analytics is the ceiling.
- NO README translations.
- NO cold outreach / newsletter / paid ads.
- NO enterprise-tier landing copy.
- NO non-Windows demo footage.
- NO contributor onboarding video.
- NO Lighthouse CI as merge gate (manual run pre-launch only).
- NO functional code changes to `src/stackly/`.

## 7. Manual verification needed for phase exit

Beyond automated checks in 2b.F.2, a human must sign off on:

1. **Strangers-on-the-internet dogfood** — ideally the maintainer asks one friend who has never seen the project to:
   - Open `https://<domain>` fresh.
   - Report their understanding of what the product does within 60s.
   - Click "View on GitHub" and follow the quickstart on a Windows machine with Debugging Tools already installed.
   - Report any point of friction.
   - Result logged in `.planning/phase-2b-public-launch/DOGFOOD_LOG.md` (optional file, nice-to-have).
2. **48-hour soak period** — landing page deployed, no changes for 48h, no broken links reported, analytics show no 404 spikes. (R4 mitigation.)
3. **Honest-marketing final pass** — grep all public artifacts for the forbidden phrases one final time before 2b.F.3:
   ```bash
   grep -rEi '(auto-detect|automatically detect|cross-platform|\bpip install stackly\b|the fastest|the best|the only|first-of-its-kind)' \
     README.md site/src/ .planning/phase-2b-public-launch/LAUNCH_POSTS.md server.json
   ```
   Zero unintentional hits required.
4. **GOAL-7 one-week discoverability check** — 7 days post-launch, manually Google "Stackly MCP" and "stackly crash fix"; confirm landing page or GitHub repo appears in first 2 pages. Log in `.planning/phase-2b-public-launch/DISCOVERABILITY_LOG.md`. (Per GOAL.md: not blocking phase exit, but tracked.)

---

## 8. Appendix A: file-level honest-marketing grep invocation

Running this single command over all public artifacts should yield only deliberate uses (e.g., in a "what's NOT auto-detected" FAQ):

```bash
grep -rEi \
  --include='*.md' \
  --include='*.astro' \
  --include='*.json' \
  '(auto-detect|automatically detect|cross-platform|\bpip install stackly\b|the fastest|the best|the only|first-of-its-kind)' \
  README.md \
  CONTRIBUTING.md \
  SECURITY.md \
  CODE_OF_CONDUCT.md \
  site/ \
  server.json \
  .planning/phase-2b-public-launch/LAUNCH_POSTS.md \
  .planning/phase-2b-public-launch/DEMO_SCRIPT.md \
  .github/
```

## 9. Appendix B: summary of open-question resolutions

| Q | Topic | Resolution |
|---|-------|------------|
| Q1 | stackly.dev availability | Task 2b.0.1 CHECKPOINT Day 0; fallbacks `stackly.app > getstackly.dev > usestackly.dev > stackly.run` |
| Q2 | site/ subdir vs sibling repo | **site/ subdir** (Decision #1) |
| Q3 | Twitter handle | Task 2b.0.3 CHECKPOINT; three options (personal / project / skip) |
| Q4 | r/programming technical blog | **Deferred to 2c** (Decision #10); LAUNCH_POSTS.md marks `DEFERRED_TO_2C` |
| Q5 | Demo mode (hand-off vs autonomous) | **Hand-off** (Decision #4) |
| Q6 | r/cpp and r/programming current sidebar rules | Re-verified at post time in Task 2b.F.1 pre-publication checklist |
| Q7 | Smithery source-install acceptance | Submit in Task 2b.E.2; if rejected, fall back to awesome-mcp-servers PR for 4th count |
| Q8 | YouTube channel (personal vs project) | Task 2b.0.4 CHECKPOINT; either option acceptable |
| Q9 | Lighthouse CI merge gate | **Deferred** (Decision #9); manual runs only for 2b |

---

**End of PLAN.md.** Executor: follow task order by wave; parallelize within waves where autonomy allows. Every task is either AUTO (Claude runs alone) or CHECKPOINT (human input needed — paused on resume signal). Every task lists exact files, actions, and acceptance criteria. Ship.
