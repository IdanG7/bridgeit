# Phase 2b — Public Launch — Goal

## The phase goal (one sentence)

DebugBridge is discoverable and installable by strangers on the internet: a stranger who has never heard of DebugBridge can land on a page, understand the product in under 60 seconds, follow a quickstart that works on a fresh Windows dev machine, and find the project via multiple independent channels (MCP directories, HN, Reddit, Twitter, search).

## Success criteria (phase exits when all are true)

1. **README rewrite for public audience is shipped on `main`:**
   - Hero paragraph aimed at strangers (not internal contributors), leading with the crash → fix loop and a 30-second pitch.
   - Includes an animated GIF or embedded video showing the `debugbridge fix` loop end-to-end.
   - Quickstart section that a stranger can follow on a fresh Windows 10/11 machine: install prerequisites (Windows Debugging Tools, `uv`, Claude Code CLI), clone, `uv sync`, run `debugbridge doctor`, run `debugbridge serve`, try the sample `crash_app`.
   - "Why DebugBridge" section naming the competitive wedge (remote debug state + MCP + autonomous repair — no other tool combines all three).
   - Architecture diagram (ASCII or embedded image) showing test machine → dev machine topology.
   - MCP client configuration snippets for Claude Code, Cursor, and Claude Desktop.
   - Troubleshooting section pointing at `debugbridge doctor`.
   - Links to landing page, PyPI (if shipped by 2c), GitHub issues, license, contributing guide.

2. **Landing page at `debugbridge.dev` is live:**
   - Static site (Vercel, Cloudflare Pages, or GitHub Pages — whichever minimizes ongoing cost and setup).
   - Domain `debugbridge.dev` registered and pointed at the host.
   - Above-the-fold content: product tagline, 60-second demo video embed, primary CTA ("Install from GitHub" until PyPI ships).
   - Secondary sections: who it's for (game studios, embedded, desktop apps), how it works (three-step diagram), MCP client setup snippets, "View on GitHub" button.
   - Page scores ≥ 90 on Lighthouse for Performance, Accessibility, Best Practices, SEO.
   - Open Graph + Twitter card metadata configured (title, description, preview image).
   - Favicon + logo consistent with GitHub repo avatar.
   - Page source is committed to the DebugBridge repo under `site/` (or a sibling repo, decided in PLAN.md) so the project owns its marketing surface.

3. **60-second demo video is recorded, edited, and uploaded:**
   - Script written and reviewed before recording (stored in `.planning/phase-2b-public-launch/DEMO_SCRIPT.md`).
   - Opening 5 seconds hooks the viewer (crash on screen, the pain point).
   - Shows: remote process crash on a test machine → `debugbridge fix` on dev machine → Claude Code diagnoses → patch written → build passes.
   - No dead air, no voiceover mumbling — tight, paced cuts. Subtitles/captions included.
   - Uploaded to: YouTube (primary, for embed); mirrored on landing page as a self-hosted `<video>` or Vercel-friendly alternative.
   - Video URL is linked from README and landing page.

4. **Submitted to at least 4 MCP directories and all submissions tracked:**
   - Submission status is tracked in `.planning/phase-2b-public-launch/DIRECTORY_SUBMISSIONS.md` with: directory name, submission URL, submission date, listing URL (once live), status (pending/live/rejected).
   - Submitted to: Smithery, PulseMCP, LobeHub MCP Marketplace, Anthropic's official MCP registry (if accepting submissions — else a documented reason).
   - Each submission includes: canonical name "DebugBridge", one-line description, install command, HTTP + stdio config examples, link to README + landing page + video, MIT license confirmation.

5. **Launch post drafts are written and reviewed:**
   - Drafts for: Hacker News (Show HN), Reddit (`r/programming`, `r/cpp`, `r/gamedev` as relevant), Twitter/X (launch thread).
   - Drafts stored in `.planning/phase-2b-public-launch/LAUNCH_POSTS.md`.
   - Each draft follows platform-specific conventions (HN prefers authentic first-person + link to the thing; Reddit prefers story/problem framing; Twitter prefers a hook thread with a demo GIF in tweet 1).
   - Drafts NOT published as part of Phase 2b — publication timing is a separate go/no-go decision after the landing page + video + directory submissions are all live. The drafts must be ready to ship at ≤ 30 minutes of polish notice.

6. **Open-source announcement is consolidated:**
   - `CONTRIBUTING.md` exists at repo root with guidance for first-time contributors (dev setup, test commands, PR conventions, code of conduct reference).
   - `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1, standard boilerplate).
   - `SECURITY.md` with responsible-disclosure instructions (email + response-time expectation).
   - GitHub repo "About" section filled in: short description, homepage URL (debugbridge.dev), tags (mcp, claude-code, windows, debugging, cpp, crash-reporter).
   - Issue templates (`bug_report.md`, `feature_request.md`) and a PR template (`.github/PULL_REQUEST_TEMPLATE.md`) in place.

7. **Discoverability sanity check passes:**
   - A fresh Google search for "DebugBridge MCP" or "debugbridge crash fix" surfaces the landing page or GitHub repo within the first two pages within 7 days of launch (measured manually, not blocking the phase exit — but set up Google Search Console so the site is indexable).
   - `robots.txt` + `sitemap.xml` on the landing page.
   - Repo has a clean `description` + `homepage` field set via `gh repo edit`.

## Non-goals (explicitly out of scope)

- **PyPI publish** — Phase 2c. The README + landing page reference "install from source" and document the path to `pip install debugbridge` coming in 2c. If PyPI ships during this phase as a side-effect, fine, but the phase exit does not depend on it.
- **Signed wheels / post-install hooks** — Phase 2c.
- **Docs site** (separate from landing page) with full API reference — Phase 2c.
- **Actually publishing the launch posts** — drafts only. Publication is a separate go/no-go.
- **Paid analytics, Mixpanel, Segment** — Phase 2b uses whatever free tier the static host provides (Vercel Analytics free tier or Plausible). No custom analytics code.
- **Multi-language README translations** — English only.
- **Marketing beyond HN/Reddit/Twitter drafts** — no newsletter, no cold outreach to influencers, no paid ads.
- **Enterprise-tier landing page copy** — the landing page is for individual developers; enterprise messaging comes in Phase 4.
- **Non-Windows demo** — the video shows Windows only, consistent with the current Phase 1 + 2a shipping scope. Non-Windows messaging is Phase 3.
- **Contributor onboarding video** — text-only CONTRIBUTING.md is sufficient for 2b.

## Constraints to respect

- **Honest marketing.** The landing page and README must not overstate current capabilities. Specifically: do not imply crash auto-detection (that's 2.5), cross-platform support (that's 3), or `pip install` (that's 2c). Call out what's shipping today vs. what's on the roadmap.
- **MIT license stays in place.** No license changes.
- **No secrets in the site repo.** Landing page deploy credentials live in the host's UI (Vercel/Cloudflare), never committed.
- **No changes to the existing MCP tool signatures or CLI behavior.** Phase 2b is pure marketing + packaging — zero functional code changes to `src/debugbridge/`. Tests and CI remain green.
- **Don't break `main`.** All landing page / docs work is either in its own directory (`site/`) or a sibling repo; functional code on `main` is untouched except for documentation (`README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `.github/`).
- **Demo video must reflect a real run, not a mockup.** If something in the live product doesn't work for the video, fix the product or cut the scene — never fake UI in post.
- **Landing page must remain maintainable by future-me.** Prefer a minimal stack (plain HTML + Tailwind CDN, or Astro, or Next.js static export) that a contributor can edit without learning a new framework.

## Acceptance demo

When Phase 2b is done, this sequence works for any stranger on the internet:

```
1. Stranger hears about DebugBridge via an HN post, a friend, or a Smithery search.
2. Clicks the link → lands on debugbridge.dev.
3. Watches the 60-second demo video embedded above the fold.
4. Clicks "View on GitHub" → lands on https://github.com/IdanG7/bridgeit.
5. Scrolls the README, sees the quickstart, copies the install commands.
6. On a fresh Windows 10/11 box with Debugging Tools installed:
     git clone https://github.com/IdanG7/bridgeit.git
     cd bridgeit
     uv sync
     uv run debugbridge doctor         # passes or prints clear guidance
     uv run debugbridge serve           # MCP server is up
   In another shell:
     uv run debugbridge fix --pid <crash_app.exe PID> --repo .
   → Claude Code opens with crash briefing preloaded.
7. Stranger tweets "wait, this actually works" → viral loop.
```

Phase exits when steps 1–6 work for a person who has never seen the codebase, and at least 4 MCP directory listings are live (step 1's "hears about DebugBridge" is backed by real discoverability surface).
