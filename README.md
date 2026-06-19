# Flight Ops Tech Digest — automated blog

A Hugo static site that gets a new post written and published **automatically every weekday (Mon-Fri)**, with no manual steps once set up, and emails you when a post goes live. Lives at **flightops.news**. Topic: news and trends in aviation flight operations tech (AI, deals, product launches).

## How it works

1. **`daily-post.yml`** (GitHub Actions, runs on a weekday cron — no weekends) calls the Claude API with web search enabled, asks it to research and write a post about one current development in flight ops tech, commits the result as a markdown file in `content/posts/`, then **emails you** with the title and summary.
2. **`deploy.yml`** runs automatically on every push to `main` — it builds the Hugo site and publishes it to GitHub Pages.
3. Net effect: every weekday, a new post appears on your live site and you get an email, with zero clicks from you.

## One-time setup

1. **Create a new GitHub repo** (public or private) and push everything in this folder to it.

2. **Get an Anthropic API key** at https://console.anthropic.com if you don't have one. This is a *pay-as-you-go API key*, separate from a claude.ai subscription.

3. **Add the API key as a repo secret:**
   Repo → Settings → Secrets and variables → Actions → New repository secret
   - Name: `ANTHROPIC_API_KEY`
   - Value: your key

4. **Add email secrets** (same place, Settings → Secrets and variables → Actions). These are used to send you a notification whenever a post publishes. Any SMTP provider works — easiest is usually Gmail with an [app password](https://support.google.com/accounts/answer/185833):
   - `MAIL_SERVER` — e.g. `smtp.gmail.com`
   - `MAIL_PORT` — e.g. `465`
   - `MAIL_USERNAME` — the sending email address
   - `MAIL_PASSWORD` — app password (not your regular email password)
   - `MAIL_TO` — the address(es) you want notified (comma-separated for multiple)

5. **Enable GitHub Pages with Actions as the source:**
   Repo → Settings → Pages → Build and deployment → Source: "GitHub Actions"

6. **Point your domain (flightops.news) at GitHub.** This repo is already configured for `flightops.news` (see `hugo.toml` and `static/CNAME`). You still need to:
   - In your domain registrar's DNS settings, add 4 A records for `@` pointing to: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - Add a CNAME record for `www` pointing to `YOUR-GITHUB-USERNAME.github.io`
   - In GitHub: Settings → Pages → Custom domain → enter `flightops.news` → Save
   - Wait for the DNS check to go green (can take minutes to a few hours), then check **Enforce HTTPS**

7. **Push to `main`.** That alone triggers the deploy workflow and publishes an empty site.

8. **Test the post generator manually** before waiting for the schedule:
   Repo → Actions → "Generate Daily Post" → Run workflow (the `workflow_dispatch` trigger lets you run it on demand). Check that a new file appears in `content/posts/`, that you get the email, and that the deploy workflow then runs automatically.

## Adjusting things later

- **Cadence:** edit the `cron` line in `.github/workflows/daily-post.yml`. Cron times are UTC. Currently set to weekdays only (`0 13 * * 1-5`).
- **Topic/theme:** edit the `THEME` string at the top of `scripts/generate_post.py`.
- **Tone/length/structure:** edit the prompt text in `build_prompt()` in the same file.
- **Avoiding repeats:** the script already reads your last 15 post titles and tells Claude not to repeat them.
- **Cost:** each post is one API call with web search (a handful of search calls + a few thousand output tokens) — typically a few cents per post depending on current pricing. Check current rates in the Anthropic console.

## Recommended: a safety check

Right now this publishes fully unattended. If you'd rather review before it goes live, two options:
- Change the daily workflow to open the post as a **draft PR** instead of committing to `main` directly (ask me and I'll adjust the workflow for this).
- Add a Slack/email notification step so you at least see what got published each day.

## Local preview (optional)

If you install Hugo locally (https://gohugo.io/installation/):
```
hugo server
```
Then visit `http://localhost:1313`.
