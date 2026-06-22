# Project Briefing: flightops.news

This doc is a handoff summary for Claude Code. It covers what this project is, how it's built, the decisions behind it, and known gotchas — so future work stays consistent with what's already here rather than reinventing it.

## What this is

An automated blog at **flightops.news**, owned by Vincent Miller (aviation business development / product leader). It publishes a new post every weekday with zero manual intervention: a script calls the Claude API (with web search) to research and write about real, recent news in aviation flight operations technology, commits it, and the site rebuilds and redeploys automatically. Vincent gets an email notification when a post goes live.

This was built entirely through a conversational chat interface (not Claude Code), with files handed to the user as downloads and the user manually uploading them to GitHub via the web UI. That process is the main reason Claude Code is now being introduced — to remove that manual step going forward.

## Architecture

- **Static site generator:** Hugo, no theme dependency — all layouts are custom and live in `layouts/`
- **Hosting:** GitHub Pages, custom domain `flightops.news` (DNS via Namecheap, A records pointed at GitHub's IPs, CNAME for `www`)
- **Automation:** Two GitHub Actions workflows:
  - `.github/workflows/daily-post.yml` — runs on a cron schedule (weekdays only, 13:00 UTC), calls `scripts/generate_post.py`, commits the new post, then explicitly triggers the deploy workflow, then emails Vincent
  - `.github/workflows/deploy.yml` — builds the Hugo site (`hugo --minify`) and deploys to GitHub Pages, triggered on push to `main` or manually
- **Content generation:** `scripts/generate_post.py` — calls the Anthropic API directly via `requests` (not the Python SDK), with the `web_search_20250305` tool enabled, asks for a single JSON object back, and writes it as a Hugo markdown file with front matter into `content/posts/`

## Repo secrets required (already configured)

- `ANTHROPIC_API_KEY` — for the post-generation API calls
- `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USERNAME`, `MAIL_PASSWORD`, `MAIL_TO` — SMTP creds for the email notification step (currently Gmail with an app password)

## Content rules (encoded in `scripts/generate_post.py`)

These were deliberately tuned through several rounds of feedback — don't loosen them without checking with Vincent first:

1. **Strict 7-day freshness window.** The prompt explicitly states today's date and the 7-day cutoff, and instructs the model to verify source publish dates and re-search rather than fall back to stale news.
2. **No repeats unless a real follow-up.** The script reads up to the last 60 posts (title, date, summary) and passes that history into the prompt. A repeat topic is only allowed if it's a genuine new development, and the post must say explicitly that it's a follow-up.
3. **Voice/persona.** The prompt includes a `VOICE` block with Vincent's real, verified career background (PM at Jeppesen ForeFlight, Bid Manager at SITA FOR AIRCRAFT, Head of Delivery at NAVBLUE/Skywise, Senior Product Consultant for Lido Navigation at Lufthansa Systems, BD Manager at FlightAware, licensed private pilot). Commentary should read like it's coming from this specific person.
4. **Strict no-fabrication guardrail.** This is important: the model may reference the *general nature* of Vincent's work (e.g. "having spent years on the bid-management side of aviation tech deals"), but is explicitly forbidden from inventing specific anecdotes, named deals, customers, dollar figures, or quotes and attributing them to his personal experience. This was a direct, deliberate request from Vincent — don't relax it.
5. **Style rules** (`STYLE_RULES` constant) ask for longer/developed sentences, natural contractions, measured/fact-forward tone (not hot-takes), and explicitly blocklist common AI-writing tells: "in today's rapidly evolving landscape," "it's worth noting," "moreover/furthermore," excessive em-dashes, false-balance hedging, and listy parallel structure.
6. **Output format:** the model must return ONLY a JSON object (title, summary, tags, body_markdown) as its final message, with no preamble. The script takes the *last* text block from the API response (not all of them, since web search produces intermediate commentary blocks) and has a regex fallback to extract a JSON object even if stray text sneaks in.

If asked to further tune voice/content, the right move is almost always editing the `VOICE`, `STYLE_RULES`, or `build_prompt()` function in `scripts/generate_post.py` — not changing the pipeline mechanics.

## Design system (in `static/css/style.css`)

Deliberately not a generic AI-default look (avoided: cream+terracotta, near-black+neon, broadsheet newspaper). Direction is "aviation instrument panel":

- **Colors:** deep navy (`--navy: #0B1F3A`) header/accents, instrument blue (`--sky: #2D7DD2`, `--sky-soft: #5FA8E0`), restrained amber accent (`--amber: #E8A33D`), off-white background (`--bg: #F7F8FA`)
- **Type:** Space Grotesk (display/headlines/nav — loaded via Google Fonts), Source Serif 4 (body text), JetBrains Mono (dates, tags, byline — reads like a flight-log timestamp)
- **Signature element:** a dashed "flight path" line (`.flight-path-rule`) used as the recurring divider instead of a plain `<hr>`
- **Header:** navy background, brand mark is a small inline SVG (dashed flight-path line with a waypoint dot), brand name "FlightOps.News" set large/prominent in Space Grotesk
- A header background illustration (`static/images/header-pattern.svg`, a faint runway/flight-path motif) was built but **Vincent decided against using it** — the file is still in the repo but unreferenced in CSS. Leave it removed unless asked to revisit.
- Content column width: `--max-width: 780px` base, widening to `880px` on screens ≥1200px, to avoid excessive empty space on large desktop monitors (this was a specific fix requested after initial design felt too narrow/centered).

## Page structure

- `content/posts/*.md` — blog posts, auto-generated, front matter: `title`, `date`, `tags`, `summary`, `draft: false`
- `content/about.md` — About page, `type: "page"`, includes Vincent's professional bio (text has been through a couple of rounds of edits from Vincent directly — treat his latest wording as authoritative, don't regenerate the bio text on your own) and his photo at `static/images/profile.jpg`
- `content/contact.md` — Contact page, `type: "page"`, contains an HTML contact form (raw HTML embedded in markdown, allowed because `markup.goldmark.renderer.unsafe = true` is set in `hugo.toml`) that POSTs to Formspree (`https://formspree.io/f/xwvjgqdk`) — this keeps Vincent's real email address out of the page source entirely
- Layouts in `layouts/_default/` (`baseof.html`, `single.html`, `list.html`) and `layouts/index.html` (homepage — note this lives directly under `layouts/`, NOT `layouts/_default/`, that's a real Hugo distinction that caused confusion before)

## Known gotchas / lessons learned (worth knowing before changing things)

1. **GitHub web UI "Add file" nested-folder bug:** if you click "Add file → Create new file" while browsing inside a subfolder and type a path starting from the root again, GitHub can create a duplicate nested folder (e.g. `.github/workflows/.github/workflows/deploy.yml`). Always start from the repo root before typing a full path. (This shouldn't be an issue once you're working via Claude Code directly with git, but worth knowing if Vincent ever edits manually again.)
2. **Pushes from the default `GITHUB_TOKEN` don't trigger other workflows.** This is why `daily-post.yml` has an explicit `gh workflow run deploy.yml` step (with `permissions: actions: write`) after committing a new post — without it, the deploy workflow silently never fires after an automated commit.
3. **Deploy race conditions.** If multiple commits/file uploads happen in quick succession, multiple deploy runs can queue and finish out of order, leaving a stale version live even though the latest run shows green. Fix: manually re-run "Build and Deploy Site" once, by itself, after a batch of changes.
4. **CSS/static asset caching.** GitHub Pages' CDN can serve a stale version of a static asset for a while after deploy. Hard refresh (Cmd+Shift+R) and incognito windows are the standard checks; if those still show stale content, suspect a deploy race condition (point 3) rather than just browser cache.
5. **Hugo `theme = ""` in `hugo.toml` breaks the build** — this project uses no theme at all (custom layouts only), so there should be no `theme` line in `hugo.toml` at all.
6. **Scheduled GitHub Actions cron triggers are not perfectly reliable.** GitHub documents possible delays under load, and in practice a scheduled run has at least once failed to fire at all with no clear error. Worth keeping an eye on whether the weekday 13:00 UTC run is consistently firing; manual `workflow_dispatch` is the fallback.

## Working style notes

- Vincent is new to web dev / git / GitHub generally — explanations have been kept step-by-step and exact (exact menu names, click paths). He's been using GitHub's web UI exclusively, not git locally.
- He prefers being told the direct answer/recommendation rather than long hedged option lists, but does want to be asked before consequential or ambiguous decisions.
- He has final say and has firmly corrected course a few times (e.g. rejecting the header background image, asking for a specific bio rewrite, insisting on no fabricated personal anecdotes in posts) — those decisions should be treated as settled, not revisited speculatively.
