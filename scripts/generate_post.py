#!/usr/bin/env python3
"""
Generates one new blog post markdown file under content/posts/ by calling
the Anthropic API (with web search enabled) and writing the result as a
Hugo-compatible markdown file with front matter.

Requires env var: ANTHROPIC_API_KEY
"""

import os
import re
import json
import glob
import sys
import datetime
import requests

THEME = (
    "News and trends in aviation flight operations technology — including "
    "new product developments, uses of AI in flight planning / digital "
    "cockpit / dispatch / airline operations, and notable deals or "
    "partnerships signed in the industry."
)

VOICE = (
    "Write commentary in the voice of Vincent Miller, an aviation business "
    "development and product leader with 15+ years in aviation technology. "
    "His real, verified background: Product Manager at Jeppesen ForeFlight; "
    "Bid Manager at SITA FOR AIRCRAFT; Head of Delivery, Services and "
    "Deployment at NAVBLUE (now Skywise); Senior Product Consultant for "
    "Lido Navigation at Lufthansa Systems; Business Development Manager at "
    "FlightAware. MBA from SDA Bocconi (with coursework at Wharton), BBA "
    "from George Washington University. Licensed private pilot with an "
    "instrument rating."
)

STYLE_RULES = """STYLE RULES — these matter as much as the content:
- Write in longer, more developed sentences rather than short punchy
  fragments. Let ideas breathe and build, the way someone with deep
  domain knowledge naturally explains something.
- Use contractions naturally (don't, it's, that's, isn't) — this is
  professional writing, not stiff corporate-speak.
- Tone is measured and fact-forward, not heavily opinionated. Let the
  facts and their implications do the work rather than declaring strong
  verdicts. Light, earned commentary is fine; loud hot-takes are not.
- AVOID these AI-writing tells entirely:
  - "in today's rapidly evolving landscape" or any variant of that phrase
  - "it's worth noting that"
  - "moreover," "furthermore," or other stiff formal transitions
  - excessive em dashes (—) used as a crutch for every aside; use them
    sparingly, like a careful human writer would
  - overly balanced "on one hand / on the other hand" hedging that avoids
    saying anything concrete
  - listy parallel structure in prose (e.g. three clauses in a row all
    shaped the same way for rhetorical effect)
- You MAY reference Vincent's real professional background at a general
  level (e.g. "having spent years on the bid-management side of aviation
  tech deals," "from time spent running global delivery teams," "as a
  pilot, this is the kind of tool I'd actually want in the cockpit") since
  those roles are real and verified above.
- You must NEVER invent a specific anecdote, named deal, customer, dollar
  figure, date, or direct quote and attribute it to Vincent's personal
  experience. Only the general nature of his work (listed above) is fair
  to reference — never fabricate a specific story that sounds plausible
  but isn't something he's confirmed actually happened. If in doubt, stay
  general rather than specific."""

POSTS_DIR = os.path.join(os.path.dirname(__file__), "..", "content", "posts")
API_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-sonnet-4-6"


def get_recent_posts(limit=60):
    """Pull title/date/summary from existing posts so we can avoid repeats
    and recognize genuine follow-ups vs. duplicate coverage."""
    files = sorted(glob.glob(os.path.join(POSTS_DIR, "*.md")), reverse=True)[:limit]
    posts = []
    for f in files:
        with open(f, "r", encoding="utf-8") as fh:
            content = fh.read()
        title_match = re.search(r'^title:\s*"?(.*?)"?\s*$', content, re.MULTILINE)
        date_match = re.search(r'^date:\s*(\S+)\s*$', content, re.MULTILINE)
        summary_match = re.search(r'^summary:\s*"?(.*?)"?\s*$', content, re.MULTILINE)
        if title_match:
            posts.append({
                "title": title_match.group(1),
                "date": date_match.group(1) if date_match else "unknown",
                "summary": summary_match.group(1) if summary_match else "",
            })
    return posts


def build_prompt(recent_posts):
    history_clause = "No posts published yet, so any qualifying story is fine."
    if recent_posts:
        lines = [
            f'- "{p["title"]}" (published {p["date"]}): {p["summary"]}'
            for p in recent_posts
        ]
        history_clause = (
            "Posts already published on this blog (most recent first):\n"
            + "\n".join(lines)
        )

    today = datetime.date.today()
    week_ago = today - datetime.timedelta(days=7)

    return f"""You write a daily blog post for a blog about: {THEME}

{VOICE}

{STYLE_RULES}

TODAY'S DATE: {today.isoformat()}

FRESHNESS REQUIREMENT — STRICT:
Pick ONE specific, genuinely newsworthy story that broke or was reported in
the last 7 days (on or after {week_ago.isoformat()}). Use web search and
check the actual publish date of your sources before choosing a story. Do
not use older news just because it's relevant — if you can't find something
genuinely new from the last 7 days, search again with different terms
rather than falling back to stale news.

NO-REPEAT RULE:
{history_clause}

Do NOT cover a topic/company/story already listed above UNLESS there has
been a genuinely major new development since that post (e.g. a deal that
was rumored is now signed, a beta has now gone GA, a deployment had a
significant new outcome). If you do cover a follow-up like this:
- Say explicitly in the post that this is an update to a story covered
  before, and briefly note what's new vs. what was already known.
- Otherwise, pick a different, fresh topic entirely.

Prefer concrete news (a product launch, an AI deployment, a partnership or
deal, a notable contract) over generic commentary.

Write the post in your own words — do not quote source text directly beyond
a very short phrase here and there. Aim for 400-600 words. Structure: a short
intro hook, 2-3 sections with subheadings (use ## markdown), and a short
closing thought with your own take as an industry insider. End with a
"## Sources" section listing the names of the publications/companies
referenced (no need for full URLs).

Respond with ONLY a single JSON object as your final message — no preamble,
no explanation of your research process, no markdown code fences, nothing
before or after the JSON. Your very last message must start with {{ and end
with }}, in exactly this shape:
{{
  "title": "string, specific and concrete, no clickbait",
  "summary": "one sentence, plain text, for the post list preview",
  "tags": ["2 to 4 short lowercase tags"],
  "body_markdown": "the full post body in markdown, NOT including the title as a heading"
}}"""


def call_claude(prompt):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        sys.exit("ERROR: ANTHROPIC_API_KEY environment variable is not set.")

    response = requests.post(
        API_URL,
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
        json={
            "model": MODEL,
            "max_tokens": 4000,
            "messages": [{"role": "user", "content": prompt}],
            "tools": [{"type": "web_search_20250305", "name": "web_search"}],
        },
        timeout=120,
    )
    response.raise_for_status()
    data = response.json()

    # When web search is used, the model may emit several text blocks
    # (research notes between tool calls) before its final answer. Only the
    # LAST text block is the actual answer we want.
    text_blocks = [block["text"] for block in data.get("content", []) if block.get("type") == "text"]
    if not text_blocks:
        sys.exit(f"ERROR: No text content in model response:\n{json.dumps(data, indent=2)}")

    full_text = text_blocks[-1].strip()

    # Strip accidental code fences if the model adds them anyway.
    full_text = re.sub(r"^```json\s*|\s*```$", "", full_text.strip())

    try:
        return json.loads(full_text)
    except json.JSONDecodeError:
        pass

    # Fallback: the model may have added a sentence of commentary before or
    # after the JSON object. Pull out the largest {...} block and try that.
    match = re.search(r"\{.*\}", full_text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass

    sys.exit(f"ERROR: Could not parse JSON from model output:\n{full_text}")


def slugify(title):
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug).strip("-")
    return slug[:80]


def write_post(post):
    today = datetime.date.today().isoformat()
    slug = slugify(post["title"])
    filename = f"{today}-{slug}.md"
    path = os.path.join(POSTS_DIR, filename)

    tags_yaml = "[" + ", ".join(f'"{t}"' for t in post.get("tags", [])) + "]"
    summary = post.get("summary", "").replace('"', "'")

    front_matter = (
        "---\n"
        f'title: "{post["title"]}"\n'
        f"date: {today}\n"
        f"tags: {tags_yaml}\n"
        f'summary: "{summary}"\n'
        "draft: false\n"
        "---\n\n"
    )

    os.makedirs(POSTS_DIR, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(front_matter + post["body_markdown"].strip() + "\n")

    print(f"Wrote post: {path}")
    return path


def main():
    recent_posts = get_recent_posts()
    prompt = build_prompt(recent_posts)
    post = call_claude(prompt)

    for field in ("title", "summary", "tags", "body_markdown"):
        if field not in post:
            sys.exit(f"ERROR: model response missing required field '{field}'")

    write_post(post)

    # Expose title/summary to later GitHub Actions steps (e.g. email step).
    gh_output = os.environ.get("GITHUB_OUTPUT")
    if gh_output:
        with open(gh_output, "a", encoding="utf-8") as fh:
            fh.write(f"post_title={post['title']}\n")
            fh.write(f"post_summary={post.get('summary', '')}\n")


if __name__ == "__main__":
    main()
