# Phase 2b — Public Launch — Research

**Researched:** 2026-04-18
**Domain:** Static-site stacks, MCP directory ecosystem, demo-video production, open-source scaffolding, developer-tool launch playbook
**Confidence:** HIGH on MCP directory submission mechanics (official docs and registry README), HIGH on static-site stack and hosting (current vendor docs + Cloudflare acquisition of Astro confirmed), HIGH on open-source scaffolding files (GitHub docs + Contributor Covenant canonical source), MEDIUM on launch-post conventions (community consensus, not a single authoritative source), MEDIUM on effort estimates (first-order based on solo-maintainer timings from similar launches), LOW on exact PulseMCP/Smithery approval timelines (not published SLAs).

## Summary

Phase 2b is marketing plumbing, not product work. Almost every deliverable has a well-trodden, documented path — the risk is not novelty, it is sequencing and scope creep. Key findings:

1. **The MCP directory ecosystem has consolidated around the official registry.** `registry.modelcontextprotocol.io` is the canonical source, and PulseMCP ingests from it weekly. Publishing once to the official registry gets the project onto PulseMCP automatically and into GitHub's MCP Registry automatically. This turns "submit to 4 directories" into "submit to 2 — official registry + Smithery + LobeHub + a GitHub-issue for mcp.so if we want extra surface." Big unlock for the plan.

2. **The official MCP registry accepts source-only servers.** You do NOT need to ship to PyPI first. A minimal `server.json` with just `name`, `version`, `description`, `repository.url`, and a `websiteUrl` pointing at the README's quickstart is accepted. This removes the Phase 2c dependency that would otherwise block Phase 2b's directory deliverable.

3. **Astro is the right static-site stack.** Plain HTML + Tailwind CDN is simpler but won't get ≥ 90 Lighthouse SEO without hand-rolling meta tags and sitemap generation. Next.js is overkill for a single landing page. Astro ships zero JS by default, has first-class Tailwind and Cloudflare Pages integration (Cloudflare acquired Astro in January 2026), and a contributor can edit `.astro` files with no framework knowledge. Recommendation: **Astro 6 + Tailwind v4 + `@astrojs/sitemap` + `astro-seo`, deployed to Cloudflare Pages**.

4. **Cloudflare Pages beats Vercel for this project.** Cloudflare: unlimited bandwidth, commercial-use-allowed free tier, and built-in Web Analytics that needs no cookie banner. Vercel's free tier is personal-use-only — commercial open-source marketing is a grey zone that triggers Pro ($20/mo). GitHub Pages would work but has no preview deploys and no built-in analytics. Recommendation: **Cloudflare Pages**.

5. **Landing page source should live under `site/` in the Stackly repo, not a sibling repo.** A sibling repo adds a second CI, second deploy key, and a second place to search — solo-maintainer debt. The Astro project is ~30 files and builds to a `dist/` directory that Cloudflare Pages can point at via the monorepo subdirectory setting. A single-line `.gitattributes` entry keeps GitHub's language-stats bar accurate (Python, not TypeScript).

6. **The README rewrite is ~60% new material.** Current README is developer-internal ("clone and `uv sync`"). Public version needs: stranger-friendly hero, animated demo GIF, explicit prerequisite list with version floors, MCP-client config snippets for three clients (Claude Code, Cursor, Claude Desktop), a "Why Stackly" competitive-wedge section, and a troubleshooting section that reflects actual user-facing errors. The tools table and dev-setup sections can be preserved roughly as-is.

7. **60-second demo video realistically takes 6–10 hours end-to-end for a first-timer.** Breakdown: script (1h), setup & rehearsal (1h), recording 3-5 takes (1-2h), editing (2-3h), caption generation + thumbnail (1h), revision pass (1h). Use OBS Studio for capture (MKV → remux to MP4), Descript for edit-by-transcript + auto-captions, YouTube for primary host (unlisted then public), embed via `<iframe>` on the landing page. Do not self-host the MP4 — it tanks Lighthouse Performance.

8. **"Show HN" and launch posts are drafts only for 2b — publication is deferred.** The phase goal is correct here: having the drafts ready lets us publish on a 30-minute polish notice once the landing page, video, and directory submissions are all green. HN timing research is consistent: Tuesday-Thursday, 8-11am ET, no superlatives, link to GitHub not landing page in the post body, reply to every top-level comment.

9. **Open-source scaffolding files are mostly boilerplate.** Contributor Covenant 2.1 is a copy-paste with one email substitution. SECURITY.md gets a 10-line responsible-disclosure template. CONTRIBUTING.md is the only one that requires real authorial work (dev setup, test commands, PR conventions). GitHub issue-forms YAML is the current best practice — strictly better than markdown templates for structured fields.

10. **Most deliverables are parallelizable.** The only hard sequences are: (a) the domain must be registered before anyone else grabs `stackly.dev`, (b) the video must exist before the landing page can embed it and before the directory submissions can link to it, (c) the landing page URL must exist before the directory submissions include it, (d) the launch-post drafts should reference the live landing page URL. Everything else (README, open-source scaffolding, GitHub metadata, launch-post drafts in stub form) can run in parallel.

**Primary recommendation:** Build Phase 2b as four parallelizable tracks, merged at the end: **Track A (content)** — README rewrite + demo script + open-source scaffolding; **Track B (infra)** — domain registration + landing page skeleton + Cloudflare Pages setup; **Track C (video)** — demo recording + editing + YouTube upload; **Track D (distribution)** — directory submission prep + launch-post drafts. Tracks A, B, D can all start immediately. Track C waits only on the demo script from A. Landing page integration and directory submissions are the final merge points.

---

## Standard Stack

### Landing-page core

| Library / Tool | Version | Purpose | Why Standard |
|----------------|---------|---------|--------------|
| Astro | 6.x (latest stable, post-Cloudflare acquisition) | Static-site generator | Zero-JS by default, first-class Tailwind and Cloudflare Pages integration, minimal learning curve (file-based routing, `.astro` = HTML+frontmatter). Industry default for content/marketing sites in 2026. |
| Tailwind CSS | v4.x | Styling | Single source of styling, JIT compiler means tiny output CSS, zero config via `@astrojs/tailwind`. Universal default for developer landing pages in 2026. |
| `@astrojs/sitemap` | latest | `sitemap.xml` auto-generation | First-party Astro integration; runs at build. One-line import; produces Google Search Console-ready output. |
| `astro-seo` | latest | Open Graph / Twitter Card / canonical meta tags | Idiomatic way to set per-page meta in Astro; avoids hand-rolling 15 `<meta>` tags in a `<Layout>` slot. |
| Cloudflare Pages | n/a (hosted) | Static hosting, CDN, TLS, preview deploys | Unlimited bandwidth on free tier, commercial-use allowed, built-in Web Analytics, automatic preview deploys per PR, custom domain free. |
| Cloudflare Web Analytics | n/a (hosted) | Privacy-respecting analytics | No cookie banner required, no GDPR consent flow, free on Cloudflare Pages, built-in Core Web Vitals. |
| Cloudflare Registrar | n/a (hosted) | Domain registration (`stackly.dev`) | At-cost pricing (≈$10/year for `.dev`), free WHOIS privacy, DNS auto-configured for Pages. |

### Video production

| Tool | Version | Purpose | Why Standard |
|------|---------|---------|--------------|
| OBS Studio | 30.x (Windows x64) | Screen + mic capture | Free, open-source, industry default. NVENC encoder on any RTX 20+ = zero CPU cost. MKV container recommended (crash-proof) then remux to MP4 via File → Remux Recordings. |
| Descript | free or $15/mo | Edit-by-transcript + auto-captions + filler-word removal | Fastest path from raw take to tight 60s cut for a non-editor. Speaker-transcript editing means "delete the bad sentence" is one keystroke. Auto-generates `.srt` for subtitle upload. |
| YouTube (unlisted → public) | — | Primary video host | Free, embeddable, auto-scaled streaming, auto-generated captions (editable), SEO indexed. Recommended over self-hosted MP4 (tanks Lighthouse Performance). |

### Open-source scaffolding

| File | Source | Purpose |
|------|--------|---------|
| `CODE_OF_CONDUCT.md` | Contributor Covenant 2.1 (verbatim copy) | Community standard, required for GitHub "Community Standards" compliance. |
| `CONTRIBUTING.md` | Custom (dev setup, test commands, PR conventions) | First-time-contributor onramp. GitHub surfaces it in the "New Issue" and "New PR" flows. |
| `SECURITY.md` | Custom 10-line template (email + response SLA) | Responsible disclosure, GitHub surfaces it under the "Security" tab. |
| `.github/ISSUE_TEMPLATE/bug_report.yml` | GitHub issue-forms YAML | Structured bug reports (far better than markdown template). |
| `.github/ISSUE_TEMPLATE/feature_request.yml` | GitHub issue-forms YAML | Structured feature requests. |
| `.github/ISSUE_TEMPLATE/config.yml` | GitHub issue-forms config | Disables blank issues, adds contact links (Discussions, Security). |
| `.github/PULL_REQUEST_TEMPLATE.md` | Custom 20-line markdown | PR checklist (tests pass, CHANGELOG updated, conventional-commit message). |

### Alternatives Considered

| Instead of | Could Use | Tradeoff / Why not for 2b |
|------------|-----------|---------------------------|
| Astro | Plain HTML + Tailwind CDN | **Rejected.** Plain HTML works, but (a) no automatic `sitemap.xml`, (b) must hand-author OG/Twitter meta on every page, (c) CDN Tailwind is not production-recommended (page weight, no purging), (d) no image optimization. Astro gives all of that for 30 minutes of setup. |
| Astro | Next.js 15 static export | **Rejected.** Next.js is an SSR/RSC framework bent into static mode. More deps, more build config, more JS runtime in `output: export` mode. Pure overkill for a single landing page. |
| Astro | MkDocs Material / Docusaurus | **Rejected.** These are docs-site frameworks. Good for Phase 2c when we have a real docs surface; wrong for a marketing landing page. |
| Astro | Hugo | Viable, but Go toolchain adds friction for a JS-ecosystem contributor. Astro wins on contributor familiarity. |
| Cloudflare Pages | Vercel | **Rejected** for Stackly. Vercel's free tier is "personal, non-commercial" per ToS — open-source marketing with a planned paid tier (Phase 4) is a grey area. Cloudflare Pages has no such restriction, plus unlimited bandwidth. |
| Cloudflare Pages | GitHub Pages | Viable fallback. Missing: preview deploys per PR, server-side redirects/headers, built-in analytics. Works for a truly minimal site but forecloses the above upgrades. |
| Cloudflare Pages | Netlify | Comparable to Vercel. Same bandwidth limits (100 GB). Not differentiated enough from Cloudflare Pages to prefer. |
| Descript | DaVinci Resolve (free) | Rejected for 2b. DaVinci is professional-grade (Hollywood color, Fairlight audio) and overkill for a 60s talking-head-over-code demo. 10x steeper learning curve than Descript. Revisit if we ever need cinematic B-roll. |
| Descript | Shotcut / Kdenlive | Viable free alternatives. Traditional timeline editors — work fine but no transcript-editing workflow, no auto-captions, no filler-word removal. Slower for first-time editor. |
| YouTube embed | Cloudflare Stream self-host | Rejected for 2b. $1/1000 minutes delivered — cheap but adds a vendor. YouTube gives free hosting + discovery surface (YouTube search is the 2nd-largest search engine). Revisit if we want to strip YouTube's related-videos UI. |
| GitHub issue-forms YAML | Plain markdown `ISSUE_TEMPLATE.md` | Rejected. Forms produce structured, parseable issues and reduce noise. Official GitHub recommendation since 2022. |

**Installation (landing page):**

```bash
# Assuming site/ subdirectory in Stackly repo
cd site
npm create astro@latest . -- --template minimal --typescript strict --no-install --no-git
npm install
npx astro add tailwind      # installs @astrojs/tailwind + tailwindcss
npx astro add sitemap        # installs @astrojs/sitemap
npm install astro-seo
```

Cloudflare Pages is configured via the Cloudflare dashboard (no local CLI required); point it at `github.com/IdanG7/stackly`, set build command `cd site && npm install && npm run build`, set output directory `site/dist`.

---

## 1. Static Site Stack — Why Astro Wins

### The decision matrix

| Requirement | Plain HTML+Tailwind CDN | Astro | Next.js static | MkDocs Material | Docusaurus |
|-------------|-------------------------|-------|----------------|-----------------|------------|
| Single landing page | ✅ trivial | ✅ trivial | ❌ overkill | ❌ docs-oriented | ❌ docs-oriented |
| Zero runtime JS | ✅ | ✅ default | ⚠️ needs config | ✅ | ❌ React runtime |
| Tailwind integration | ⚠️ CDN (not prod-grade) | ✅ first-party | ✅ | ❌ | ⚠️ plugin |
| Sitemap auto | ❌ hand-roll | ✅ `@astrojs/sitemap` | ⚠️ via plugin | ✅ | ✅ |
| OG/Twitter meta | ❌ hand-roll | ✅ `astro-seo` | ⚠️ via `next/head` | ⚠️ theme-dependent | ⚠️ theme-dependent |
| Image optimization | ❌ | ✅ `astro:assets` | ✅ `next/image` | ❌ | ⚠️ |
| Contributor learning curve | minimal (but brittle) | low (HTML + frontmatter) | medium | low (Markdown) | medium |
| Lighthouse ≥ 90 all-green | hard | easy | medium | easy | medium |
| Maintained by future-me | medium (manual) | **low** | high (framework churn) | low | high (React churn) |

Astro wins because it inherits the simplicity of static HTML for authoring while automating sitemap, meta tags, and image optimization — the exact 3 things that would otherwise keep blocking Lighthouse green checks.

### The Cloudflare acquisition (January 2026)

In January 2026 Cloudflare acquired The Astro Technology Company. Astro remains MIT-licensed and continues to deploy anywhere, but Cloudflare Pages integration is now first-party with zero-config deploys. This is a tailwind for the Astro + Cloudflare Pages choice, not a lock-in concern — the static `dist/` output is vendor-agnostic.

Sources:
- [Astro in 2026: Why It's Beating Next.js for Content Sites](https://dev.to/polliog/astro-in-2026-why-its-beating-nextjs-for-content-sites-and-what-cloudflares-acquisition-means-6kl) (MEDIUM confidence — community post, aligns with official acquisition announcement)
- [Astro Cloudflare deploy guide](https://docs.astro.build/en/guides/deploy/cloudflare/) (HIGH — official docs)
- [Cloudflare Pages Astro framework guide](https://developers.cloudflare.com/pages/framework-guides/deploy-an-astro-site/) (HIGH — official docs)
- [Astro + Tailwind v4 setup (Tailkits, 2026)](https://tailkits.com/blog/astro-tailwind-setup/)

### Recommended project structure

```
site/
├── astro.config.mjs        # integrations: tailwind, sitemap
├── package.json
├── tailwind.config.mjs
├── public/
│   ├── favicon.svg
│   ├── og-image.png        # 1200x630, social preview
│   ├── logo.svg
│   └── robots.txt
├── src/
│   ├── layouts/
│   │   └── BaseLayout.astro    # <html>, <head> with astro-seo, <body>
│   ├── components/
│   │   ├── Hero.astro
│   │   ├── VideoEmbed.astro    # YouTube iframe with lite-youtube-embed fallback
│   │   ├── Features.astro
│   │   ├── HowItWorks.astro    # 3-step diagram
│   │   ├── McpConfig.astro     # Tabbed: Claude Code / Cursor / Claude Desktop
│   │   ├── WhoItsFor.astro
│   │   └── Footer.astro
│   └── pages/
│       └── index.astro         # Single page, no routing needed
└── README.md                    # "See root README for project info"
```

### Per-page meta boilerplate (copy-paste starter)

```astro
---
// src/layouts/BaseLayout.astro
import { SEO } from 'astro-seo';

export interface Props {
  title: string;
  description: string;
  image?: string;
}

const { title, description, image = '/og-image.png' } = Astro.props;
const canonicalUrl = new URL(Astro.url.pathname, Astro.site).toString();
---
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1.0" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <SEO
      title={title}
      description={description}
      canonical={canonicalUrl}
      openGraph={{
        basic: { title, type: 'website', image, url: canonicalUrl },
        optional: { description, siteName: 'Stackly' }
      }}
      twitter={{
        card: 'summary_large_image',
        creator: '@IdanG7',  // replace with actual handle
        title,
        description,
        image,
      }}
    />
  </head>
  <body>
    <slot />
  </body>
</html>
```

---

## 2. Hosting + Domain Mechanics

### Domain registration — `stackly.dev`

**Current availability:** Unconfirmed by this research. WHOIS lookup tooling is not available in the research environment and no reliable public WHOIS snapshot surfaced for this specific domain. **Plan action:** first planner task is `whois stackly.dev` (or check at `https://www.namecheap.com/domains/registration/results/?domain=stackly.dev`). If taken, fall back candidates: `stackly.app`, `stackly.io` (expensive), `getstackly.dev`, `usestackly.dev`.

**Register at Cloudflare Registrar** (not Namecheap/Porkbun), because:
- At-cost pricing (≈$10–12/year for `.dev`, no markup).
- Free WHOIS privacy by default.
- Auto-integrates DNS with Cloudflare Pages (one-click domain attachment — no manual CNAME).
- Same dashboard as analytics + Pages.

`.dev` TLD note: Google Registry runs the `.dev` TLD. It is on the HSTS preload list — HTTPS is mandatory. Cloudflare Pages provisions TLS via its Universal SSL automatically (usually within minutes of DNS propagation).

Sources:
- [Cloudflare Registrar — `.dev` pricing](https://www.cloudflare.com/application-services/products/registrar/buy-dev-domains/) (HIGH)
- [.dev TLD on Wikipedia](https://en.wikipedia.org/wiki/.dev) — HSTS preload, Google Registry operator (MEDIUM)

### Hosting tier comparison (free-tier specs as of April 2026)

| Spec | Cloudflare Pages | Vercel | GitHub Pages |
|------|------------------|--------|--------------|
| Custom domain | ✅ free + TLS | ✅ free + TLS | ✅ + TLS via Let's Encrypt |
| Bandwidth/month | **unlimited** | 100 GB | ~100 GB soft |
| Build minutes/month | 500 | 6,000 | via GitHub Actions quota |
| Concurrent builds | 1 | 1 | via Actions |
| Preview deploys per PR | ✅ | ✅ | ❌ |
| Server-side redirects/headers (`_redirects`, `_headers`) | ✅ | ✅ | ❌ (meta refresh only) |
| Analytics | built-in Web Analytics (free) | Vercel Analytics (free tier) | none |
| Commercial use on free tier | ✅ | ⚠️ ToS says personal only | ✅ |
| Deploy source | Git (GitHub/GitLab) or wrangler | Git or CLI | Git or Actions |

**Recommendation: Cloudflare Pages.** The commercial-use clause is the dealbreaker for Vercel — Stackly has a planned paid tier (Phase 4), which makes the project commercial even pre-revenue.

Sources:
- [Cloudflare Pages vs Vercel vs Netlify (hosting-ranked.com, 2026)](https://hosting-ranked.com/cloudflare-pages-vs-vercel-vs-netlify/) (MEDIUM)
- [Vercel vs Netlify vs Cloudflare Pages (HTMLPub Blog)](https://htmlpub.com/blog/vercel-vs-netlify-vs-cloudflare) (MEDIUM)
- [Cloudflare Pages Astro framework guide](https://developers.cloudflare.com/pages/framework-guides/deploy-an-astro-site/) (HIGH — vendor docs)

### Cloudflare Pages deploy — exact steps

1. Push `site/` directory to `main` on `IdanG7/stackly`.
2. Cloudflare dashboard → Pages → "Create a project" → "Connect to Git" → select `stackly` repo.
3. Build settings:
   - **Framework preset:** Astro
   - **Build command:** `cd site && npm install && npm run build`
   - **Build output directory:** `site/dist`
   - **Root directory (advanced):** leave blank
   - **Environment variables:** none needed for 2b
4. Click "Save and Deploy". First build: ~2 min.
5. After first successful deploy → Custom domains → "Set up a custom domain" → enter `stackly.dev` and `www.stackly.dev`. If domain registered via Cloudflare Registrar, DNS is auto-configured; otherwise add CNAME records pointing at `<project>.pages.dev`.
6. Enable Web Analytics: Cloudflare dashboard → Analytics & Logs → Web Analytics → "Add a site" → select the pages.dev or custom domain. Copy the one-line beacon script into `BaseLayout.astro`.
7. Submit sitemap to Google Search Console: `search.google.com/search-console` → add property → verify via DNS TXT record (Cloudflare auto-handles this) → Sitemaps → submit `https://stackly.dev/sitemap-index.xml`.

Preview deploy URLs: every PR gets a unique `<branch>-<hash>.stackly.pages.dev` URL automatically. Use this to preview README/landing-page changes before merging.

---

## 3. Landing Page Content Structure

### Structural skeleton (synthesized from Bun, Biome, uv, mise — all 2026)

From reading the live landing pages of Bun, Biome, uv, and mise, the invariant structure for a single-page developer tool site is:

| Section | Position | Content pattern | Reference |
|---------|----------|-----------------|-----------|
| Hero | Above fold, top | Tagline (≤ 12 words) + 1-sentence elaboration + primary CTA (install command or "Get started") + secondary CTA ("View on GitHub") | Bun: "Bun is a fast JavaScript all-in-one toolkit"; uv: "An extremely fast Python package and project manager, written in Rust" |
| Demo | Above fold, immediately under hero | 60s video embed OR animated GIF OR interactive demo | Biome: before/after code block; Bun: benchmark chart |
| Social proof | Above fold or just below | "Used by" logos OR testimonial quotes | Bun: Lovable/CodeRabbit/Replit/Cursor logos; Biome: AWS/Google/Microsoft logos |
| Value prop grid | Below fold | 3–6 feature cards, each with icon + 1-line headline + 2-line description | uv: 6 capability sections; mise: 3 cards |
| How it works | Below value grid | 3–5 step diagram OR animated flow | mise: 3-step install → use → activate |
| Code / usage example | Below how-it-works | Tabbed or stacked code blocks showing real usage | Bun: 8 code examples (HTTP, WebSocket, SQL, etc.); Biome: formatted code before/after |
| Benchmarks / comparison | Mid-page | "Vs. alternative" metrics, charts, or feature matrix | Bun: bar charts vs Node/Deno; Biome: 35x faster than Prettier |
| Client/integration setup | Below benchmarks | How to wire the tool into your existing stack | (Stackly-specific: MCP client config snippets for Claude Code / Cursor / Claude Desktop, tabbed) |
| Who it's for / use cases | Lower third | 3–5 user-type cards with pain-point framing | (Stackly: game studios, embedded, desktop app devs, enterprise C++, DevOps/SRE) |
| CTA repeat + footer | Bottom | Install command repeated + link to docs/GitHub/Discord + license + maintainer attribution | All four reference sites do this |

### Stackly-specific section map

```
┌─────────────────────────────────────────────────────────────┐
│ HERO                                                         │
│   "Remote crash capture for Claude Code, Cursor, Claude Desktop"
│   "An MCP server that exposes live Windows debugger state"  │
│   [▶ Watch 60s demo]  [View on GitHub]                      │
├─────────────────────────────────────────────────────────────┤
│ DEMO VIDEO EMBED (YouTube iframe, 16:9)                     │
├─────────────────────────────────────────────────────────────┤
│ 3-STEP "HOW IT WORKS"                                        │
│   ① dbgsrv.exe on test box  ② stackly serve on dev box │
│   ③ MCP client sees the crash                                │
├─────────────────────────────────────────────────────────────┤
│ WHY DEBUGBRIDGE (competitive wedge)                          │
│   "No other tool combines remote debugger state + MCP +      │
│    autonomous repair."                                       │
│   [Comparison grid: CrashReporter vs. Stackly etc.]      │
├─────────────────────────────────────────────────────────────┤
│ MCP CLIENT SETUP (tabbed: Claude Code / Cursor / Desktop)    │
├─────────────────────────────────────────────────────────────┤
│ WHO IT'S FOR                                                 │
│   Game studios • Embedded/IoT • Desktop app devs • Enterprise C++
├─────────────────────────────────────────────────────────────┤
│ INSTALL (repeated CTA, with honest "install from source"     │
│ language until Phase 2c ships PyPI)                          │
├─────────────────────────────────────────────────────────────┤
│ FOOTER                                                       │
│   GitHub • Issues • License (MIT) • Maintained by @IdanG7   │
└─────────────────────────────────────────────────────────────┘
```

Total page: ~1 screen hero + video, then ~4 scrolls. No page-2. No docs — those come in Phase 2c.

Sources:
- [Bun landing page](https://bun.sh/) (direct fetch, 2026-04-18)
- [uv landing page](https://docs.astral.sh/uv/) (direct fetch, 2026-04-18)
- [Biome landing page](https://biomejs.dev/) (direct fetch, 2026-04-18)
- [mise landing page](https://mise.jdx.dev/) (direct fetch, 2026-04-18)

---

## 4. README Rewrite — Section-by-Section Diff

Current README (repo root, ~100 lines) is developer-internal. Here's the concrete diff plan:

| Current section | Action | Public-version content |
|-----------------|--------|------------------------|
| Title + one-liner | **REWRITE** | Keep title. Rewrite one-liner for strangers: "Remote crash capture for Claude Code, Cursor, and Claude Desktop. Expose live Windows debugger state as MCP tools, and run an autonomous AI fix-loop on remote crashes." |
| Status callout ("Phase 2a -- in active development") | **REPLACE** | "Alpha — API stable, not yet on PyPI (clone to install). MIT-licensed." + badges: MIT, Python 3.11+, Windows 10/11 x64, CI status. |
| "Why" paragraph | **KEEP** (lightly edited) | Current "30–60 minutes per crash" framing is excellent. Add one sentence about MCP + autonomous repair combination (the wedge). |
| (NEW) Demo GIF/video | **ADD** | `![demo](docs/demo.gif)` — 5–10MB GIF rendered from the 60s video (ffmpeg: `ffmpeg -i demo.mp4 -r 12 -vf scale=800:-1 demo.gif`) OR embed the YouTube link as `[![Watch the demo](docs/demo-thumb.png)](https://youtu.be/XXXX)`. |
| Install (current: `uv pip install stackly # not yet on PyPI`) | **REWRITE** | Full "from source" path: git clone + uv sync + doctor + serve. Be honest: "PyPI publish is Phase 2c — for now, install from source." Link to the 2c milestone issue. |
| Prerequisite callout | **EXPAND** | Explicit version floors: Windows 10/11 x64, Python ≥3.11, uv ≥0.5, Windows Debugging Tools (link to installer), git ≥2.20. |
| (NEW) "Architecture" diagram | **ADD** | Copy the ASCII diagram from PROJECT.md (TEST MACHINE ↔ DEV MACHINE) into the README. |
| Quick start (4 steps) | **REWRITE** | Current skeleton is good but needs stranger context. Add: "On a fresh Windows 10/11 box, after installing prerequisites:" + explicit `uv run stackly doctor` before `serve`. |
| MCP client config snippets (Claude Desktop, Cursor) | **EXPAND** | Add Claude Code as a third client: `claude mcp add stackly http://localhost:8585/mcp` (or equivalent config file). Show the exact command for each. |
| Tools table (8 tools) | **KEEP** | Current table is good for a public README. |
| Fix-loop agent section | **KEEP** (minor edits) | Currently good. Add a callout: "Hand-off mode is the default — it launches Claude Code with the crash preloaded. Use `--auto` only after you've trusted the loop." |
| Development section | **KEEP + MOVE** | Move to a dedicated CONTRIBUTING.md; leave a 3-line "For contributors, see CONTRIBUTING.md" in README. |
| License | **KEEP** | Unchanged. |
| (NEW) "Why Stackly" competitive wedge section | **ADD** | Short section explaining the 3-way combo: remote debug capture + MCP exposure + autonomous repair. Name alternatives that do *one* of those things (CrashReporter, Sentry, manual Claude Code). |
| (NEW) Troubleshooting | **ADD** | Pointers to `stackly doctor`, common errors (pybag not found, symbols missing, port in use). 5 FAQ items tops. |
| (NEW) Links footer | **ADD** | Landing page, GitHub issues, Discussions, CHANGELOG, CONTRIBUTING, LICENSE. |

**Net length estimate:** current README is ~100 lines; public version will be ~200–250 lines. Roughly 60% new material.

---

## 5. 60-Second Demo Video Production

### Script structure (hook → problem → solution → CTA, 140–160 words)

| Beat | Time | Content | Example (first draft — planner refines) |
|------|------|---------|------------------------------------------|
| Hook | 0:00–0:05 | Crash on screen. Visual pain point. No voiceover yet, or single sentence. | [crash_app.exe window with red error dialog] "Your C++ app crashed on a test machine. What now?" |
| Problem | 0:05–0:15 | The manual loop: walk over, read stack, paste, paste, paste. Framed as lost time. | "You walk over, read the stack, copy it into Slack, paste it into Claude, write a fix… 30 minutes gone. Multiply by 5 crashes a day." |
| Solution setup | 0:15–0:25 | Show the command. `stackly fix --pid <crash_app.exe> --repo .` | "Stackly flips this. One command." [terminal: `stackly fix --pid 4892 --repo .`] |
| Solution — live capture | 0:25–0:40 | Terminal shows briefing generation. Then Claude Code opens with crash preloaded. | [terminal output: "Capturing crash… 47 stack frames… 12 locals… Launching Claude Code…"] |
| Solution — AI diagnosis | 0:40–0:50 | Claude Code's response identifies the bug (null deref on `render_target`). Shows a proposed patch. | [Claude Code panel: "Null dereference at `render_target` in `draw.cpp:127`. Proposed fix:" → patch preview] |
| CTA | 0:50–1:00 | URL on screen, one spoken line. Focus on where to go. | "Works with Claude Code, Cursor, and Claude Desktop. Install from GitHub. **stackly.dev**." [full-screen URL + GitHub logo] |

Timing checkpoints: 0:05 hook lands, 0:25 command visible, 0:50 CTA starts. Read-aloud test: script must time to 60–65s at natural pace. If it runs over 65s, cut — do not speed up.

Sources:
- [Demo Video Script Template (ngram.com)](https://www.ngram.com/blog/article/demo-video-script-template)
- [How to Craft a Compelling Product Demo Script (Demio)](https://www.demio.com/blog/compelling-product-demo-script)

### Recording tooling — OBS Studio (Windows)

**Install:** OBS Studio 30+ from [obsproject.com](https://obsproject.com/) (free, no account).

**Settings for 1080p60 developer demos** (Settings → Output → Output Mode: Advanced):

| Setting | Value | Why |
|---------|-------|-----|
| Video → Base (Canvas) Resolution | 1920×1080 | Match recording target |
| Video → Output (Scaled) Resolution | 1920×1080 | No downscale |
| Video → FPS | 60 | Smooth terminal scrolling; YouTube accepts 60 |
| Output → Recording → Format | **mkv** (then remux to mp4) | MKV is crash-proof; OBS can remux losslessly |
| Output → Recording → Encoder | NVENC (if RTX 20+) else x264 | NVENC is zero-CPU; x264 Medium is fine fallback |
| Output → Recording → Rate Control | CQP (Constant Quality) | File-size friendly |
| Output → Recording → CQ Level | 18–20 | Visually lossless for screen captures |
| Audio → Sample Rate | 48 kHz | YouTube-optimal |
| Audio → Mic input | USB mic (Blue Yeti, Samson Q2U, Rode NT-USB etc.) | Integrated laptop mics sound amateurish |

**After recording:** File → Remux Recordings → select the MKV → output MP4. Takes seconds, lossless.

Sources:
- [The Best OBS Setting for Recording in 2026 (obsbot.com)](https://www.obsbot.com/blog/video-recording/obs-setting-for-recording) (MEDIUM)
- [OBS Studio Complete Guide 2026 (ruahcreativehouse.org)](https://ruahcreativehouse.org/blog/obs-studio-complete-guide/) (MEDIUM)

### Editing — Descript

**Why:** edit-by-transcript (delete a sentence in the transcript → deletes the corresponding video segment); auto-generates captions; one-click "remove filler words" (um, uh, so); exports to MP4 and `.srt` separately.

**Workflow:**
1. Import MKV (or remuxed MP4) → Descript auto-transcribes in ~1 min.
2. Read the transcript, delete bad takes by selecting text and pressing Delete.
3. Run "Remove Filler Words" → review suggested cuts.
4. Add on-screen text overlays at beat transitions (optional).
5. Export Multitrack → MP4 (1080p, H.264, 60fps) + `.srt` separately.

**Cost:** Free tier has watermark and 1h upload limit — enough for iteration. $15/mo Creator removes watermark. For 2b, subscribe for the one month it takes to ship.

**Alternative:** DaVinci Resolve free (no watermark, no subscription) — more powerful but 10x steeper learning curve. Worth it if we want cinematic output; overkill for a 60s terminal-cap demo.

Sources:
- [Descript alternatives (Riverside)](https://riverside.com/blog/descript-alternatives) (MEDIUM)
- [DaVinci Resolve vs Descript (SelectHub)](https://www.selecthub.com/video-editing-software/davinci-resolve-vs-descript/) (MEDIUM)

### Hosting + captions

- **Upload to YouTube** as unlisted for internal review. Flip to public at launch. Embed on landing page via `<iframe>` (use [`lite-youtube-embed`](https://github.com/paulirish/lite-youtube-embed) to avoid the 500KB YouTube iframe shipping with the page).
- **Captions:** YouTube auto-generates, but upload the Descript-exported `.srt` instead — cleaner. Edit the first-pass transcript for technical terms (`pybag` gets transcribed as "pie bag", etc.).
- **Thumbnail:** 1280×720, one image. Show the crash dialog or a `diff` with a patch — something visually distinct. Tools: Canva free, or just Figma. Avoid Photoshop tutorials aesthetic (giant arrows + shouting face).

### Realistic effort estimate (first-time creator)

| Phase | Hours |
|-------|-------|
| Script (draft + review + time-to-read check) | 1.0 |
| OBS setup + mic test + dry-run | 1.0 |
| Recording (expect 3–5 takes of each beat) | 1.5 |
| Editing in Descript (cut, filler removal, text overlays) | 2.5 |
| Caption editing (fix technical terms in auto-transcript) | 0.5 |
| Thumbnail design + YouTube upload + metadata | 0.5 |
| Revision pass after dogfooding | 1.0 |
| **Total** | **8.0** |

Add 50% if first-time with OBS or Descript. **Plan for 10–12 hours wall-clock across 2–3 sessions.**

---

## 6. MCP Directory Ecosystem (April 2026)

### Key finding — the ecosystem has consolidated

The **official MCP Registry** (`registry.modelcontextprotocol.io`) launched preview in September 2025 and is the canonical, Anthropic-and-MCP-Steering-Group-maintained source. Two consequences:

1. **PulseMCP ingests from the official registry daily and processes weekly.** Submitting to the official registry = automatically listed on PulseMCP within a week.
2. **GitHub's MCP Registry pulls from the OSS Community Registry.** Same flow: publish once, appear on GitHub MCP Registry automatically.

This collapses the "4 directory submissions" from the ROADMAP into effectively **2 active submissions** (official registry, Smithery) + **1 passive (LobeHub via their Submit MCP form)** + **1 GitHub issue (mcp.so)**. The PulseMCP listing is a downstream side-effect of the official registry submission.

### Submission details per directory

#### A. Official MCP Registry (`registry.modelcontextprotocol.io`) — PRIMARY

**Status (April 2026):** Still labeled "preview" but actively accepting submissions. Quality-gated but not restrictive.

**Auth:** GitHub OAuth (for `io.github.<user>/*` namespace) or domain DNS/HTTP verification (for custom namespace like `com.stackly/*`).

**Flow:**
```bash
# 1. Install publisher CLI (macOS/Linux has Homebrew; Windows: download binary from GitHub releases)
brew install mcp-publisher    # or gh release download -R modelcontextprotocol/registry ...

# 2. Authenticate with GitHub
mcp-publisher login github
# (follows OAuth device flow, code pasted to github.com/login/device)

# 3. Create server.json in the repo root (or use `mcp-publisher init`)
# Minimal source-only server.json for Stackly (no PyPI yet):
cat > server.json <<'EOF'
{
  "$schema": "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json",
  "name": "io.github.idang7/stackly",
  "title": "Stackly",
  "description": "Remote crash capture MCP server for Windows native apps. Exposes live DbgEng debugger state (stack, locals, threads, exception info) to MCP clients.",
  "version": "0.2.0",
  "repository": {
    "url": "https://github.com/IdanG7/stackly",
    "source": "github"
  },
  "websiteUrl": "https://stackly.dev"
}
EOF

# 4. Publish
mcp-publisher publish

# 5. Verify
curl "https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.idang7/stackly"
```

**Accepted without PyPI:** Yes. The official schema documents the `websiteUrl` path for "servers that follow a custom installation path or are embedded in applications without standalone packages." A minimal server.json with `repository` + `websiteUrl` and no `packages[]` array is valid. **This unblocks the Phase 2c dependency.**

**Approval timeline:** Automatic on publish. The registry is open — there is no human review. Spam is moderated after the fact.

**Quality gates:** Namespace ownership only (GitHub OAuth match). No PyPI/npm requirement for source-only submissions. Rejection causes: invalid JWT, namespace mismatch, malformed `server.json`.

**Upgrade path:** When PyPI ships in Phase 2c, add a `packages[]` entry with `registryType: "pypi"`, bump version, re-publish.

Sources:
- [Official MCP Registry](https://registry.modelcontextprotocol.io/) (HIGH)
- [Registry publishing quickstart](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/quickstart.mdx) (HIGH)
- [Server.json schema reference](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/server-json/generic-server-json.md) (HIGH)
- [Introducing the MCP Registry (blog, Sep 2025)](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/) (HIGH)

#### B. Smithery (`smithery.ai`) — SECONDARY

**Flow (two options):**

1. **CLI:**
   ```bash
   npm install -g @smithery/cli     # Node required
   smithery mcp publish "https://<your-hosted-server>" -n IdanG7/stackly
   ```
   Note: Smithery's `publish` command expects a reachable URL. For a local-only server like Stackly, you submit the repo reference via the web form instead (option 2).

2. **Web dashboard:** [smithery.ai/new](https://smithery.ai/new) → "Submit a server" → fill the form (name, description, GitHub URL, install command, transport type, example config). Smithery accepts both remote-hosted and install-from-source servers.

**Approval timeline:** Manual review, typically 1–5 business days. Smithery is curated (7,000+ servers but not every submission is accepted).

**Quality gates:** Working install flow documented; README present; MIT or similar license. Smithery flags broken installs and removes servers without GitHub activity for 90+ days.

**Metadata to prepare:**
- One-line description (≤ 120 chars)
- Install command: `git clone https://github.com/IdanG7/stackly.git && cd stackly && uv sync`
- Config JSON for Claude Desktop:
  ```json
  {"mcpServers": {"stackly": {"url": "http://localhost:8585/mcp"}}}
  ```
- Link to README, landing page, demo video
- License: MIT

Sources:
- [Smithery CLI docs](https://smithery.ai/docs/concepts/cli) (HIGH)
- [Smithery main site](https://smithery.ai/) (HIGH)
- [Smithery AI overview (WorkOS)](https://workos.com/blog/smithery-ai) (MEDIUM)

#### C. PulseMCP (`www.pulsemcp.com`) — PASSIVE (via official registry)

**Flow:** **None required beyond official registry.** PulseMCP explicitly states: "We ingest entries from the Official MCP Registry daily and process them weekly."

**If the listing is wrong or delayed > 1 week after official registry publish:** email PulseMCP support (contact info on the submit page).

**What appears on PulseMCP:** description, GitHub link, install instructions, transport config — auto-extracted from `server.json` and the linked README.

Sources:
- [PulseMCP submit page](https://www.pulsemcp.com/submit) (HIGH — verbatim quote via web fetch)
- [PulseMCP server directory](https://www.pulsemcp.com/servers) (HIGH)

#### D. LobeHub MCP Marketplace (`lobehub.com/mcp`) — SECONDARY

**Flow:** LobeHub has a "Submit MCP" button on the marketplace page. Submission is form-based (URL + metadata). LobeHub documents setup at [lobehub.com/mcp/skill.md](https://lobehub.com/mcp/skill.md) (skill metadata format). Approval is manual.

**Approval timeline:** 2–7 days based on listing-date patterns observed on the marketplace (not a published SLA).

**Recommendation:** Submit after landing page is live (LobeHub surfaces the `websiteUrl`).

Sources:
- [LobeHub MCP Marketplace](https://lobehub.com/mcp) (HIGH)
- [LobeHub main](https://github.com/lobehub/lobehub) (HIGH)

#### E. mcp.so — BONUS (low-effort, high-traffic)

**Flow:** GitHub issue on the mcp.so repo, OR "Submit" button on [mcp.so/submit](https://mcp.so/submit) (web form).

**Why bother:** 20,000+ servers listed; one of the top-3 Google search results for "MCP servers." High SEO value for our name.

Sources:
- [mcp.so servers directory](https://mcp.so/) (HIGH)
- [mcp.so/submit](https://mcp.so/submit) (HIGH)

#### F. `awesome-mcp-servers` (GitHub) — BONUS

Three maintained lists: `punkpeye/awesome-mcp-servers`, `appcypher/awesome-mcp-servers`, `wong2/awesome-mcp-servers`.

**Flow:** Fork → add one line in alphabetical order under the appropriate category (likely "Developer Tools" or "Debugging") → open PR.

Contribution format (from `punkpeye/awesome-mcp-servers/CONTRIBUTING.md`):
```markdown
- [IdanG7/stackly](https://github.com/IdanG7/stackly) 🎖️ - Remote crash capture for native Windows processes. Exposes DbgEng debugger state (call stack, exception info, threads, locals) to MCP clients.
```

**Approval timeline:** Varies by maintainer; `punkpeye` is reasonably active (weekly).

Sources:
- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) (HIGH)
- [Contributing guide](https://github.com/punkpeye/awesome-mcp-servers/blob/main/CONTRIBUTING.md) (HIGH)

### Summary submission matrix (recommended for Phase 2b)

| Directory | Priority | Effort | Timeline | Depends on |
|-----------|----------|--------|----------|------------|
| Official MCP Registry | **P0** | 30 min | instant | — |
| Smithery | **P0** | 20 min | 1–5 days | README + landing page URL |
| LobeHub | **P1** | 15 min | 2–7 days | landing page URL |
| mcp.so | **P1** | 10 min | 2–7 days | README |
| PulseMCP | **P2** (automatic) | 0 min | ≤ 1 week after official registry | official registry |
| GitHub MCP Registry | **P2** (automatic) | 0 min | automatic after official registry | official registry |
| `awesome-mcp-servers` (punkpeye) | **P2** (bonus) | 20 min (PR) | maintainer-dependent | README |

The GOAL.md's "at least 4 directory submissions" is easily cleared: official registry + Smithery + LobeHub + mcp.so = 4, with PulseMCP, GitHub MCP Registry, and awesome-mcp-servers as free bonuses.

---

## 7. Launch-Post Conventions (HN / Reddit / Twitter)

### Hacker News ("Show HN")

**Post format:**
- **Title:** `Show HN: Stackly – Remote crash capture for Windows C++, exposed via MCP`
  - Under 80 chars
  - Use an em-dash or colon after the name
  - Name the product and what it does in the title
- **Link:** Point to GitHub, **not** the landing page. HN readers click through to READMEs; landing pages trigger "marketing" allergic reaction. (Source: multiple HN launch retrospectives.)
- **Body (the first comment from the OP):** 4–8 sentences. Plain English, no superlatives. Structure:
  1. Who you are + why you built this (personal motivation)
  2. What it does in one sentence
  3. What the state-of-the-art alternative is and why you thought you could do better
  4. Honest limitations (Windows-only, C++-only, not on PyPI yet, not auto-detecting crashes)
  5. Request for feedback (specific: "anyone tried shipping a pybag-based tool, curious about your symbol-path experience")
  6. Link to landing page at the bottom

**Timing:** Tuesday/Wednesday/Thursday, 8–11am ET. (EDT in April.) Mondays are catch-up, Fridays bleed to weekend, weekends have lower volume but lower competition.

**Engagement rule:** reply to every top-level comment within the first 2 hours. Criticism gets "thank you, you're right about X — here's why we did Y" (not defensive).

**Avoid:**
- Superlatives: "fastest", "best", "first-of-its-kind"
- Marketing-speak: "synergy", "leverage", "empower"
- Implying parity with tools we don't have parity with
- Stating "auto-detects crashes" or "cross-platform" (NOT TRUE YET per honest-marketing constraint)

Sources:
- [How to launch a dev tool on Hacker News (markepear.dev)](https://www.markepear.dev/blog/dev-tool-hacker-news-launch) (MEDIUM)
- [How to do a successful Hacker News launch (lucasfcosta.com)](https://www.lucasfcosta.com/blog/hn-launch) (MEDIUM)
- [How to crush your Hacker News launch (dev.to)](https://dev.to/dfarrell/how-to-crush-your-hacker-news-launch-10jk) (MEDIUM)
- [When is the best time to post on Show HN (HN discussion)](https://news.ycombinator.com/item?id=44625897) (MEDIUM)

### Reddit — `r/programming`, `r/cpp`, `r/gamedev`

**Important:** `r/programming` has strict self-promotion norms and bans outright product plugs. `r/cpp` is much friendlier to tool releases; `r/gamedev` has a weekly "Feedback Friday" thread which is the only place self-promotion is welcome.

**`r/cpp`** (most welcoming for Stackly):
- Post format: link + body text. OP body should walk through a technical decision (e.g., "we wrote a pybag/DbgEng wrapper to expose remote crashes to MCP; here's why we used WinDbg command parsing instead of the native COM APIs"). Technical war-story sells better than a pitch.
- Link target: GitHub (not landing page).
- Flair: post flair required; pick "Show and Tell" or "Tooling" (verify in sidebar at post time — rules evolve).
- Title: "Stackly: Remote DbgEng capture exposed to Claude Code via MCP (open source)"

**`r/programming`** (caution — high rejection risk):
- Post only if the project is *unusually* technically interesting (Stackly qualifies — MCP + remote debugger COM wrappers + autonomous agents is non-trivial).
- Do NOT post a "launch" — post the technical write-up. E.g., link to a blog post titled "How to expose a remote Windows debugger to an AI via MCP" that happens to mention Stackly. Landing page/GitHub gets mentioned in paragraph 3, not paragraph 1.
- Fallback if no blog post ready: skip r/programming in Phase 2b and revisit in 2c.

**`r/gamedev`** (relevant per PROJECT.md's game-studio target segment):
- ONLY post in the Feedback Friday thread (sidebar rules are enforced; standalone self-promotion = 24h ban).
- Short post (2-3 sentences + link) on Friday morning.

Sources:
- [Reddit self-promotion rules (replyagent.ai, 2026)](https://www.replyagent.ai/blog/reddit-self-promotion-rules-naturally-mention-product) (MEDIUM)
- [How to market on Reddit without getting banned (onlinemoderation.com)](https://www.onlinemoderation.com/market-on-reddit-without-getting-banned/) (LOW)
- r/cpp and r/programming specific rule pages — Reddit couldn't be fetched in research, **planner should verify sidebar rules at post time** (flagged as open question).

### Twitter / X

**Thread structure (5–8 tweets):**

1. **Hook tweet + media:** 1 sentence problem statement + demo GIF (not video — GIFs autoplay in-feed, videos don't on mobile). Include `https://stackly.dev` in this tweet (link is surfaced in feed preview).
   > "Your Windows C++ app crashed on a test machine. No AI tool can see the stack. You walk over. 30 minutes lost. → [demo GIF] → stackly.dev"
2. **The solution:** 1 sentence + code screenshot.
   > "Stackly runs an MCP server on your dev machine that attaches to the remote crash. Claude Code / Cursor / Claude Desktop can read the stack directly."
3. **Why it works:** competitive wedge.
4. **What's open-source / free:** MIT license, GitHub link.
5. **Demo:** link to YouTube.
6. **Honest limitations:** Windows-only, not auto-detecting yet.
7. **Call to action:** "Star on GitHub + let me know what breaks."
8. **Quote-repost hook:** tag 2–3 relevant accounts (Anthropic, Cursor, MCP official, Windows Dev).

**GIF placement:** Tweet 1 only. Subsequent tweets: screenshots (higher engagement than plain text).

**Timing:** weekday morning ET. Thread, not a single tweet — threads get 2-4x engagement.

**Avoid:** thread-bombing (> 10 tweets loses engagement); motivational-speaker opening ("Here's a thread on how I built…"); emojis except possibly one in tweet 1 for visual anchor.

---

## 8. Open-Source Scaffolding Files

### `CODE_OF_CONDUCT.md` — Contributor Covenant 2.1

**Source:** [contributor-covenant.org/version/2/1/code_of_conduct.html](https://www.contributor-covenant.org/version/2/1/code_of_conduct/) — canonical. Use the interactive builder at the same site to fill `[INSERT CONTACT METHOD]` with the maintainer email (create `coc@stackly.dev` mail alias via Cloudflare Email Routing for free).

**Length:** ~150 lines, verbatim copy. Zero editorial work beyond the email substitution.

### `CONTRIBUTING.md` — Custom (requires authorial work)

Recommended sections (in order):
1. **Welcome** (1 paragraph, lower the bar for contribution)
2. **Code of Conduct** (1 line: "Participation is governed by CODE_OF_CONDUCT.md")
3. **Reporting bugs** (pointer to issue-forms)
4. **Suggesting features** (pointer to issue-forms)
5. **Development setup** (git clone, uv sync, uv run pytest — copy from README's dev section then expand)
6. **Running tests** (unit vs integration split, PYBAG_INTEGRATION env var)
7. **Code style** (pyright + ruff, pre-commit if configured)
8. **Commit message conventions** (conventional commits — matches existing CHANGELOG.md pattern)
9. **PR process** (branch naming, CI must be green, request review)
10. **Release process** (link to CHANGELOG; note that maintainer handles releases)

**Length target:** ~150–200 lines. Write once, rarely edit.

### `SECURITY.md` — 10-line responsible disclosure template

```markdown
# Security Policy

## Reporting a Vulnerability

Please report security vulnerabilities privately using one of the following channels:

1. **Preferred:** GitHub's private vulnerability reporting — go to the [Security tab](https://github.com/IdanG7/stackly/security) and click "Report a vulnerability".
2. **Email:** security@stackly.dev

Please do NOT open a public issue for security vulnerabilities.

### Response expectations

- **Acknowledgment:** within 72 hours
- **Triage:** within 7 days
- **Fix timeline:** depends on severity; we will coordinate disclosure with you

Thank you for helping keep Stackly and its users safe.
```

Enable GitHub's private-vulnerability-reporting feature in repo settings → Security → Private vulnerability reporting.

Sources:
- [GitHub docs — adding a security policy](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository) (HIGH)
- [Coordinated Vulnerability Disclosure for OSS (GitHub blog)](https://github.blog/security/vulnerability-research/coordinated-vulnerability-disclosure-cvd-open-source-projects/) (HIGH)
- [Upptime SECURITY.md reference](https://github.com/upptime/.github/blob/main/SECURITY.md) (HIGH — widely copied template)

### `.github/ISSUE_TEMPLATE/bug_report.yml` — YAML issue form

```yaml
name: Bug Report
description: Report a reproducible bug in Stackly
title: "[bug] "
labels: ["bug", "triage"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to file a bug. Please fill out the following so we can reproduce it.
  - type: textarea
    id: what-happened
    attributes:
      label: What happened?
      description: Describe the bug and what you expected to happen.
    validations:
      required: true
  - type: textarea
    id: reproduction
    attributes:
      label: Steps to reproduce
      description: Commands, configs, and environment setup.
      render: shell
    validations:
      required: true
  - type: input
    id: version
    attributes:
      label: Stackly version
      description: Output of `stackly version`.
      placeholder: "0.2.0"
    validations:
      required: true
  - type: input
    id: os
    attributes:
      label: OS + Build
      description: e.g. "Windows 11 Pro 23H2, build 22631.3447"
    validations:
      required: true
  - type: input
    id: python
    attributes:
      label: Python version
      placeholder: "3.11.7"
    validations:
      required: true
  - type: textarea
    id: doctor
    attributes:
      label: stackly doctor output
      description: Paste the full output of `stackly doctor`.
      render: shell
    validations:
      required: true
  - type: textarea
    id: logs
    attributes:
      label: Relevant logs / error output
      render: shell
```

### `.github/ISSUE_TEMPLATE/feature_request.yml`

```yaml
name: Feature Request
description: Propose a new capability for Stackly
title: "[feature] "
labels: ["enhancement", "triage"]
body:
  - type: textarea
    id: problem
    attributes:
      label: What problem does this solve?
      description: Describe the use case or pain point.
    validations:
      required: true
  - type: textarea
    id: proposal
    attributes:
      label: Proposed solution
      description: How would you like Stackly to solve this?
    validations:
      required: true
  - type: textarea
    id: alternatives
    attributes:
      label: Alternatives considered
  - type: checkboxes
    id: scope
    attributes:
      label: Scope
      options:
        - label: This is a breaking API change
        - label: This requires new MCP tools
        - label: This requires changes to the fix-loop agent
```

### `.github/ISSUE_TEMPLATE/config.yml`

```yaml
blank_issues_enabled: false
contact_links:
  - name: Questions / Discussions
    url: https://github.com/IdanG7/stackly/discussions
    about: For open-ended questions, use Discussions instead of Issues.
  - name: Security vulnerabilities
    url: https://github.com/IdanG7/stackly/security/advisories/new
    about: Report security issues privately here.
```

### `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
## Summary

<!-- What does this PR do, and why? -->

## Type of change

- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change
- [ ] Documentation / refactor (no functional change)

## Test plan

<!-- How did you verify this works? -->

- [ ] Unit tests pass: `uv run pytest -m "not integration"`
- [ ] Integration tests pass (if touching pybag/DbgEng code): `$env:PYBAG_INTEGRATION = "1"; uv run pytest`
- [ ] `stackly doctor` reports clean
- [ ] Manual end-to-end sanity check (if behavior-changing): `scripts/e2e_smoke.py`

## Checklist

- [ ] CHANGELOG.md updated under `## Unreleased`
- [ ] Docs updated (README or CONTRIBUTING)
- [ ] Conventional commit message on the merge commit
```

Sources:
- [GitHub docs — issue forms syntax](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms) (HIGH)
- [GitHub docs — form schema](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema) (HIGH)
- [Configuring issue templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository) (HIGH)
- [stevemao/github-issue-templates (reference collection)](https://github.com/stevemao/github-issue-templates) (MEDIUM)

---

## 9. GitHub Repo Metadata for Discoverability

### Fields to set via `gh repo edit`

```bash
gh repo edit IdanG7/stackly \
  --description "Remote crash capture MCP server for native Windows applications. Exposes live DbgEng debugger state (stack, exception, threads, locals) to Claude Code, Cursor, and Claude Desktop." \
  --homepage "https://stackly.dev" \
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

**Canonical tags for this project:** `mcp`, `mcp-server`, `model-context-protocol`, `claude-code`, `cursor`, `windows`, `debugging`, `debugger`, `cpp`, `crash-reporter`, `ai-agents`, `developer-tools`.

GitHub caps topics at 20; we're using 13, leaving headroom.

**Important ranking signals on GitHub search:**
- Topic matches (exact)
- Recent pushes (keep repo active)
- Star count (chicken-and-egg; launch → HN → stars)
- README quality (README is indexed for search)

### Social preview image

GitHub → Settings → General → Social preview → Upload. **Spec:** 1280×640 (minimum), 1MB max, PNG/JPG. Appears in Twitter, LinkedIn, Slack, Discord, etc. link unfurls.

Design: project logo + tagline + screenshot of debugger state. Figma or Canva free templates. Tools like [socialify.git.ci](https://socialify.git.ci/) can auto-generate one if time-pressed.

### Repo badges (README top)

```markdown
[![CI](https://github.com/IdanG7/stackly/actions/workflows/ci.yml/badge.svg)](https://github.com/IdanG7/stackly/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Windows](https://img.shields.io/badge/platform-Windows%2010%2F11-blue)](https://www.microsoft.com/windows/)
```

(No PyPI badge until Phase 2c ships.)

Sources:
- [GitHub docs — classifying your repository with topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics) (HIGH)
- [GitHub MCP Registry blog post](https://github.blog/ai-and-ml/github-copilot/meet-the-github-mcp-registry-the-fastest-way-to-discover-mcp-servers/) (HIGH) — confirms `mcp` and `mcp-server` topics are the canonical GitHub topics for the ecosystem.

---

## 10. SEO + Analytics Minimums

### Technical SEO checklist (Astro handles most)

| Item | Tool | How |
|------|------|-----|
| `sitemap.xml` | `@astrojs/sitemap` | Auto-generated at build; one import in `astro.config.mjs`. |
| `robots.txt` | Static file | `site/public/robots.txt` — allow all, point at sitemap. |
| Open Graph tags | `astro-seo` | Per-page via `<SEO>` component in layout. |
| Twitter Card tags | `astro-seo` | Same component; `card: "summary_large_image"`. |
| Canonical URL | `astro-seo` | Auto from `Astro.url` + `astro.config.mjs` → `site` field. |
| Alt text on images | Manual | Every `<img>` and `<Image>` needs `alt=""` (decorative) or a real description. |
| Core Web Vitals | Lighthouse | Run `npx lighthouse https://stackly.dev --view` post-deploy. |
| Structured data (JSON-LD) | Manual `<script type="application/ld+json">` | **Not worth it for 2b.** JSON-LD helps `Organization`/`SoftwareApplication` rich results in Google, but for a single landing page the SEO gain is marginal (< 5% CTR uplift per Google docs). Add in 2c if the docs site makes it meaningful. |
| Google Search Console | Manual setup | Verify domain via Cloudflare DNS TXT → submit sitemap URL. |

### `robots.txt` template

```
User-agent: *
Allow: /

Sitemap: https://stackly.dev/sitemap-index.xml
```

### Analytics — Cloudflare Web Analytics

**Why over Plausible/Umami:**
- Free with Cloudflare Pages (bundled).
- No cookie banner required (cookieless tracking).
- No second vendor / dashboard.
- GDPR/CCPA compliant out of the box.
- Core Web Vitals collected automatically.

**Setup:** After first Cloudflare Pages deploy → dashboard → Analytics & Logs → Web Analytics → Add a site → pick the Pages domain → copy the one-line beacon script → paste into `BaseLayout.astro` `<head>`.

**What it tracks:** pageviews, unique visitors (by anonymized IP hash), referrers, top pages, CWV (LCP, FID, CLS). Sufficient for 2b's "did HN drive traffic" question.

**Alternative — Plausible Community Edition** (self-hosted, $5/mo on Railway): slightly prettier dashboard, same privacy posture. Not worth the second vendor.

Sources:
- [Best Privacy-First Analytics Compared (Nuxt Scripts)](https://scripts.nuxt.com/learn/privacy-first-analytics-compared) (MEDIUM)
- [Vercel Analytics vs Plausible vs Umami 2026 (PkgPulse)](https://www.pkgpulse.com/blog/vercel-analytics-vs-plausible-vs-umami-privacy-first-2026) (MEDIUM)
- [Best Privacy-Compliant Analytics Tools for 2026 (Mitzu)](https://mitzu.io/post/best-privacy-compliant-analytics-tools-for-2026/) (MEDIUM)

---

## 11. Dependency DAG — What Parallelizes, What Doesn't

### Dependency graph

```
[Track A: Content]
   README rewrite ──────────────────┐
   Demo script ──► Track C depends on this
   CONTRIBUTING.md ─────────────────┤
   CODE_OF_CONDUCT.md ──────────────┤
   SECURITY.md ─────────────────────┤
   Issue templates + PR template ───┤
                                    ▼
[Track B: Infra]                   ALL READY ─────────► Merge to main
   Domain whois + register ─► DNS setup ─┐
   Cloudflare Pages project setup ──────┤
   Astro scaffold + base layout ────────┤
   Content sections (Hero/Features/etc) ┤       
   Needs: demo video URL for embed ─────┼──┐
                                        ▼  │
[Track C: Video]                                    
   Demo script (from A) ─► Recording ─► Editing ─► YouTube upload
                                                       │
                                                       ▼ (video URL)
[Track D: Distribution]
   Launch-post drafts (HN, Reddit, Twitter) ── can start now
   Directory submission prep (metadata, blurbs) ── can start now
   Social preview image ── can start now
   GitHub repo metadata (topics, description) ── can start now
   Submit to: official MCP registry ◄── needs README + landing URL
   Submit to: Smithery ◄── needs README + landing URL + video
   Submit to: LobeHub ◄── needs landing URL
   Submit to: mcp.so ◄── needs README
```

### Hard sequencing constraints

1. **Domain registration before anything else.** Worst case: someone squats `stackly.dev` while we're planning. Register Day 0 of Phase 2b.
2. **Demo video must exist before landing page ships.** Hero CTA embeds the video.
3. **Landing page URL must exist before any directory submission** (all 4 directories surface the landing page URL as `websiteUrl`).
4. **README rewrite should be complete before first directory submission** (all directories surface README content).
5. **Launch post drafts don't need directory listings to exist** — drafts reference landing page + GitHub, not Smithery etc.
6. **CHANGELOG.md update for 0.2.1 "docs + public launch" release** is the last thing before submission.

### True parallelism — things that can run simultaneously

- README rewrite + demo script drafting (independent)
- Domain registration + CONTRIBUTING.md (independent)
- Astro scaffold + issue templates (independent)
- Demo recording + GitHub repo metadata setup (independent)
- Launch-post drafts + landing page content writing (independent)

---

## 12. Effort Estimates (solo maintainer, hours)

| Deliverable | Hours (realistic) | Notes |
|-------------|-------------------|-------|
| Domain register + Cloudflare Registrar + DNS | 0.5 | 10 min if everything is clean |
| README rewrite | 4–6 | Most writing-heavy single item. Research + draft + dogfood |
| Demo script | 1–2 | Iterate to hit 60s |
| Demo recording (multiple takes) | 1.5 | Expect 3-5 attempts |
| Demo editing (Descript) | 2–3 | First-timer; faster on second demo |
| Captions + thumbnail + YouTube upload | 1 | |
| Astro scaffold + Tailwind + SEO plugins | 1 | Reproducible from an Astro template |
| Landing page content (Hero, Features, How-it-Works, MCP setup, Who-it's-for, Footer) | 6–8 | Copy + code + minimal design |
| Landing page responsive polish + Lighthouse ≥ 90 | 2–3 | Usually need 1-2 rounds of fixes |
| Cloudflare Pages deploy + custom domain + analytics | 1 | |
| CONTRIBUTING.md | 2–3 | Write once; needs real thought |
| CODE_OF_CONDUCT.md | 0.25 | Copy-paste |
| SECURITY.md | 0.5 | Template + email alias |
| Issue templates + PR template | 1 | Copy-paste + customize |
| GitHub repo metadata (topics, description, social image) | 1 | Includes designing social image |
| Official MCP Registry submission | 0.5 | CLI install + publish |
| Smithery submission | 0.5 | Form fill |
| LobeHub submission | 0.25 | Form fill |
| mcp.so submission | 0.25 | GitHub issue |
| awesome-mcp-servers PR | 0.5 | Bonus |
| Launch-post drafts (HN + 2 Reddit + Twitter thread) | 3–4 | Drafting + review + iteration |
| DIRECTORY_SUBMISSIONS.md tracking doc | 0.5 | |
| DEMO_SCRIPT.md storage | 0.25 | |
| LAUNCH_POSTS.md storage | 0.25 | |
| CHANGELOG 0.2.1 entry + version bump | 0.5 | |
| **Total** | **31–43 hours** | **≈ 1 full work-week for a solo dev** |

**Calibration:** This assumes zero surprises. Realistic ship date is 2–3 weeks wall-clock because (a) domain/DNS propagation waits, (b) video revisions after dogfooding, (c) directory approval timelines are not instant.

---

## 13. Risks and Gotchas

### R1: `stackly.dev` may be squatted

**Probability:** Low-medium. `.dev` is popular but "stackly" is a distinctive compound. Still, Stackly is not trademarked and someone reading this ROADMAP publicly could grab it.

**Mitigation:** Register Day 0 of Phase 2b (before any public mentions). Plan fallback names in case it's taken: `stackly.app`, `getstackly.dev`, `usestackly.dev`, `stackly.run`. **Planner's first task should be to verify and register.**

### R2: MCP directory approval might block on PyPI (PARTIAL MITIGATION FOUND)

**Original concern:** Smithery/PulseMCP might require installable packages before accepting the listing.

**Research finding:** Official MCP Registry accepts source-only via `websiteUrl` (confirmed from schema docs). PulseMCP ingests from the official registry, so same path. **Smithery policy is less clear** — submission form accepts GitHub URLs but Smithery's historical listings lean toward "installable in one command" servers.

**Mitigation:** Prepare a Smithery listing that uses a `git clone` install flow as the "install command." If rejected, escalate Phase 2c (PyPI publish) and resubmit. **This is the single biggest risk to Phase 2b's "submit to ≥ 4 directories" exit criterion.** Budget: if Smithery rejects, fall back to 4 = (official MCP registry + LobeHub + mcp.so + awesome-mcp-servers PR).

### R3: Demo video size tanks landing-page Lighthouse

**Concern:** Self-hosting the demo MP4 on Cloudflare Pages would make the HTML request include a 20-50MB asset, destroying LCP (Largest Contentful Paint).

**Mitigation:** Use YouTube embed, wrapped in [`lite-youtube-embed`](https://github.com/paulirish/lite-youtube-embed). Zero JS until interaction; shows only a thumbnail. Lighthouse gives full score.

### R4: HN post timing vs. landing page uptime

**Concern:** Post goes live → HN front page → landing page has a broken image / typo / 404 → reputation hit.

**Mitigation:** Run a 48-hour soak period on the landing page before publishing the HN post. Use Cloudflare Pages preview deploys to validate PRs. Run Lighthouse CI as part of the deploy pipeline (GitHub Action from [treosh/lighthouse-ci-action](https://github.com/treosh/lighthouse-ci-action)).

### R5: Demo shows something the product doesn't actually do

**Concern:** Video shows a seamless crash-to-PR flow but the actual product (per PROJECT.md) is hand-off mode by default; autonomous mode is `--auto` opt-in; PR creation is stretch goal.

**Mitigation:** Script the video to match what 2a actually ships (hand-off mode → Claude Code opens preloaded → user sees diagnosis). Do NOT show a PR being opened automatically; show the patch file instead. **Phase goal explicitly requires the demo to be a real run, not a mockup** — this is already well-governed.

### R6: CI rate limits on automated metadata updates

**Concern:** GitHub rate-limits `gh repo edit` and social preview uploads.

**Mitigation:** Non-issue for a single-repo, single-user workflow. 5,000 req/hour authenticated. 15 metadata updates is nothing.

### R7: `launch posts published prematurely`

**Concern:** The launch posts are drafts per GOAL.md; publication is a separate go/no-go. But drafts-in-LAUNCH_POSTS.md could accidentally be posted if someone confuses "draft" for "publish when ready."

**Mitigation:** Keep LAUNCH_POSTS.md as clearly labeled drafts. Add a header: "**NOT YET PUBLISHED — publication is a separate go/no-go decision.**" Put the actual publication step in a separate post-Phase-2b tracking issue.

### R8: Maintainer email exposure

**Concern:** SECURITY.md and CODE_OF_CONDUCT.md want a contact email. Using a personal email exposes the maintainer to spam.

**Mitigation:** Cloudflare Email Routing (free with Cloudflare-managed domain) — set up `security@stackly.dev`, `coc@stackly.dev`, `hello@stackly.dev` as forwards to the real inbox. Takes 10 minutes, no ongoing maintenance.

### R9: Google Search Console domain verification requires DNS TXT

**Concern:** Standard DNS propagation can take up to 24h. If we're trying to launch fast, this could be a blocker.

**Mitigation:** Cloudflare DNS propagates in < 1 min. Add the TXT record before you need GSC live. Alternative: HTML file verification (upload `google<hash>.html` to `site/public/` and redeploy) — works instantly.

### R10: "Honest marketing" constraint conflicts with attention-grabbing copy

**Concern:** Landing pages naturally lean on superlatives ("the fastest," "the easiest"); our constraint forbids overstating.

**Mitigation:** Use specific, falsifiable claims instead. "Captures 47-frame stacks in < 2s" is better than "the fastest." "MCP-native remote capture" is better than "best-in-class." Grep the landing-page draft for: "auto", "automatic", "cross-platform", "pip install", "the first", "the only" — remove or qualify each one.

---

## Open Questions (for planner to resolve)

### Q1: Is `stackly.dev` available?

**Must answer Day 0.** Research cannot verify from this environment. Planner's first concrete task: run `whois stackly.dev` or check a domain registrar. If unavailable, planner decides fallback name before any work proceeds.

### Q2: Landing page repo location — `site/` subfolder vs. sibling repo?

**Research recommends:** `site/` subfolder in the Stackly repo. Reasoning: single CI, single deploy key, single place to search, cleaner for solo maintainer.

**Case for sibling repo:** keeps GitHub language-bar as pure Python; isolates site CI from main CI.

**Planner decision needed.** If planner chooses sibling repo, update R8 (domain email routing) and the Cloudflare Pages config accordingly.

### Q3: Publicly available maintainer Twitter/X handle

Research mentions `@IdanG7` in metadata but does not verify this is the actual handle. Planner should confirm or update references. If no Twitter presence, skip Twitter/X launch or spin up a project handle.

### Q4: Should we publish blog-post content alongside the launch?

ROADMAP says Phase 2b scope includes "HN / Reddit / Twitter launch post" drafts. Research recommends considering a technical blog post ("How we expose a Windows debugger to an AI via MCP") for r/programming. **Planner decision:** in scope for 2b, or defer to 2c/2.5?

### Q5: Demo script — autonomous mode or hand-off mode?

The 60s video could show either. Hand-off mode is the default product (per 2a scope); autonomous mode is more visually dramatic (shows the patch file being written). **Research recommends hand-off mode** — matches honest-marketing constraint and default-path principle. Planner confirms.

### Q6: r/cpp and r/programming current self-promotion rules

Reddit couldn't be fetched in this research. The planner should **verify sidebar rules at post time** — specifically:
- Does r/cpp require a "Show and Tell" flair?
- Is there a weekly self-promo thread on r/cpp or r/programming?
- What does r/programming's current policy say about "technical post-that-happens-to-mention-our-project"?

These rules evolve; research findings here are patterns, not current state.

### Q7: Smithery source-install acceptability (PARTIAL UNKNOWN)

**What we know:** Smithery CLI's `publish` command expects a reachable URL. Smithery web form accepts GitHub URLs in general.
**What's unclear:** Smithery's quality bar for source-only (not `npx`/`uvx`/`pip`-installable) servers specifically. Listings in the Smithery marketplace skew toward one-command-install servers.
**Recommendation:** Submit during Phase 2b and observe outcome. If rejected, escalate — either (a) pull Phase 2c forward, or (b) accept 4 directories without Smithery.

### Q8: YouTube channel — personal vs. project?

Research recommends YouTube as the primary video host but does not resolve: upload under the maintainer's personal channel, or create a `Stackly` project channel? Project channel adds one more surface to maintain; personal channel mixes content.

### Q9: Preview-deploy gating of merges to main

**Suggestion (not a research finding):** Add a GitHub Action that runs Lighthouse CI on every PR's Cloudflare Pages preview and blocks merge if any score drops below 90. **Planner decides** whether this is in scope for 2b or deferred.

---

## Sources

### Primary (HIGH confidence — official docs or canonical projects)

- [Official MCP Registry](https://registry.modelcontextprotocol.io/) — canonical registry
- [modelcontextprotocol/registry on GitHub](https://github.com/modelcontextprotocol/registry) — publishing docs, CLI
- [Server.json generic schema](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/server-json/generic-server-json.md) — complete schema reference
- [Registry publish quickstart](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/quickstart.mdx) — step-by-step
- [Introducing the MCP Registry (official blog, 2025-09)](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/)
- [Smithery CLI docs](https://smithery.ai/docs/concepts/cli) — publish command
- [Smithery main site](https://smithery.ai/)
- [PulseMCP submit page](https://www.pulsemcp.com/submit) — verbatim "ingest from official registry" quote
- [PulseMCP servers directory](https://www.pulsemcp.com/servers)
- [LobeHub MCP Marketplace](https://lobehub.com/mcp)
- [mcp.so directory](https://mcp.so/)
- [mcp.so submit page](https://mcp.so/submit)
- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) and its CONTRIBUTING.md
- [GitHub MCP Registry announcement](https://github.blog/ai-and-ml/github-copilot/meet-the-github-mcp-registry-the-fastest-way-to-discover-mcp-servers/)
- [Astro docs — Cloudflare deploy](https://docs.astro.build/en/guides/deploy/cloudflare/)
- [Cloudflare Pages — Astro framework guide](https://developers.cloudflare.com/pages/framework-guides/deploy-an-astro-site/)
- [Cloudflare Registrar — `.dev` domains](https://www.cloudflare.com/application-services/products/registrar/buy-dev-domains/)
- [GitHub docs — issue forms syntax](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms)
- [GitHub docs — form schema](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema)
- [GitHub docs — configuring issue templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)
- [GitHub docs — adding a security policy](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository)
- [GitHub docs — classifying your repo with topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- [Coordinated Vulnerability Disclosure for OSS (GitHub blog)](https://github.blog/security/vulnerability-research/coordinated-vulnerability-disclosure-cvd-open-source-projects/)
- [Contributor Covenant 2.1 canonical](https://www.contributor-covenant.org/version/2/1/code_of_conduct/)
- [EthicalSource/contributor_covenant](https://github.com/EthicalSource/contributor_covenant)
- Live landing pages (direct fetched 2026-04-18): [bun.sh](https://bun.sh), [docs.astral.sh/uv](https://docs.astral.sh/uv/), [biomejs.dev](https://biomejs.dev/), [mise.jdx.dev](https://mise.jdx.dev/)

### Secondary (MEDIUM confidence — community posts cross-verified with official sources)

- [Cloudflare Pages vs Vercel vs Netlify (2026)](https://hosting-ranked.com/cloudflare-pages-vs-vercel-vs-netlify/)
- [Vercel vs Netlify vs Cloudflare Pages (HTMLPub)](https://htmlpub.com/blog/vercel-vs-netlify-vs-cloudflare)
- [Astro in 2026 (dev.to)](https://dev.to/polliog/astro-in-2026-why-its-beating-nextjs-for-content-sites-and-what-cloudflares-acquisition-means-6kl)
- [Astro + Tailwind v4 setup (Tailkits)](https://tailkits.com/blog/astro-tailwind-setup/)
- [Best Privacy-First Analytics (Nuxt Scripts)](https://scripts.nuxt.com/learn/privacy-first-analytics-compared)
- [Privacy-Compliant Analytics for 2026 (Mitzu)](https://mitzu.io/post/best-privacy-compliant-analytics-tools-for-2026/)
- [The Best OBS Setting for Recording in 2026 (obsbot.com)](https://www.obsbot.com/blog/video-recording/obs-setting-for-recording)
- [OBS Studio Complete Guide 2026 (ruahcreativehouse.org)](https://ruahcreativehouse.org/blog/obs-studio-complete-guide/)
- [Descript alternatives (Riverside)](https://riverside.com/blog/descript-alternatives)
- [DaVinci Resolve vs Descript (SelectHub)](https://www.selecthub.com/video-editing-software/davinci-resolve-vs-descript/)
- [Demo Video Script Template (ngram.com)](https://www.ngram.com/blog/article/demo-video-script-template)
- [How to Craft a Compelling Product Demo Script (Demio)](https://www.demio.com/blog/compelling-product-demo-script)
- [How to launch a dev tool on Hacker News (markepear.dev)](https://www.markepear.dev/blog/dev-tool-hacker-news-launch)
- [How to do a successful Hacker News launch (lucasfcosta.com)](https://www.lucasfcosta.com/blog/hn-launch)
- [How to crush your Hacker News launch (dev.to)](https://dev.to/dfarrell/how-to-crush-your-hacker-news-launch-10jk)
- [When is the best time to post on Show HN (HN discussion)](https://news.ycombinator.com/item?id=44625897)
- [MCP Server Directories: The Complete List (DYNO Mapper)](https://dynomapper.com/blog/ai/mcp-server-directories/)
- [Smithery AI: A central hub for MCP servers (WorkOS)](https://workos.com/blog/smithery-ai)
- [stevemao/github-issue-templates reference collection](https://github.com/stevemao/github-issue-templates)
- [Upptime SECURITY.md reference](https://github.com/upptime/.github/blob/main/SECURITY.md)

### Tertiary (LOW confidence — community posts, flagged for validation)

- [.dev TLD Wikipedia](https://en.wikipedia.org/wiki/.dev) — HSTS preload claim
- [Reddit self-promotion rules (replyagent.ai 2026)](https://www.replyagent.ai/blog/reddit-self-promotion-rules-naturally-mention-product) — general patterns, not subreddit-specific
- r/cpp and r/programming specific rules — **could not fetch Reddit in this research environment; planner must re-verify at post time.**
- Effort-estimate hours — first-order estimates based on solo-dev patterns; expect ±50% variance.
- Smithery approval timeline (1–5 business days) — observed pattern, not a published SLA.
- LobeHub approval timeline (2–7 days) — observed pattern, not a published SLA.

---

## Metadata

**Confidence breakdown:**
- MCP directory ecosystem: HIGH — official docs + registry README read directly; verified source-only submissions are accepted
- Static-site stack (Astro): HIGH — official docs, Cloudflare acquisition confirmed, live landing page examples
- Hosting choice (Cloudflare Pages): HIGH — ToS-grounded reasoning; vendor docs
- Demo video tooling: MEDIUM-HIGH — established tools, community consensus on settings
- README rewrite plan: HIGH — straightforward diff against current README
- Open-source scaffolding: HIGH — GitHub official docs + canonical templates
- SEO + analytics: HIGH — vendor docs; Cloudflare Web Analytics is first-party
- Launch-post conventions: MEDIUM — consistent pattern across community retrospectives; Reddit subreddit rules could not be verified live
- Effort estimates: MEDIUM — first-order solo-dev rough estimates
- Domain availability: UNKNOWN — could not verify in research environment; first planner task
- Smithery source-only acceptance: LOW — no explicit confirmation; observed mix; flag for in-flight learning

**Research date:** 2026-04-18
**Valid until:** 2026-07-18 (3 months). MCP registry is in active development; re-verify `server.json` schema and directory lists if work extends beyond the phase exit. Astro major versions ship every 4–6 months; re-verify if picking up work after 2026-10.
