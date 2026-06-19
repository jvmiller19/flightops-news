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

POSTS_DIR = os.path.join(os.path.dirname(__file__), "..", "content", "posts")
API_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-sonnet-4-6"


def get_recent_titles(limit=15):
    """Pull titles from existing posts so we don't repeat topics."""
    files = sorted(glob.glob(os.path.join(POSTS_DIR, "*.md")), reverse=True)[:limit]
    titles = []
    for f in files:
        with open(f, "r", encoding="utf-8") as fh:
            content = fh.read()
        match = re.search(r'^title:\s*"?(.*?)"?\s*$', content, re.MULTILINE)
        if match:
            titles.append(match.group(1))
    return titles


def build_prompt(recent_titles):
    avoid_clause = ""
    if recent_titles:
        joined = "; ".join(recent_titles)
        avoid_clause = (
            f"\n\nPosts already published recently (do NOT repeat these topics, "
            f"pick something different): {joined}"
        )

    return f"""You write a daily blog post for a blog about: {THEME}

Pick ONE specific, genuinely newsworthy story or development from roughly the
last few days that fits this theme. Prefer concrete news (a product launch,
an AI deployment, a partnership or deal, a notable contract) over generic
commentary. Research it using web search before writing.{avoid_clause}

Write the post in your own words — do not quote source text directly beyond
a very short phrase here and there. Aim for 400-600 words. Structure: a short
intro hook, 2-3 sections with subheadings (use ## markdown), and a short
closing thought. End with a "## Sources" section listing the names of the
publications/companies referenced (no need for full URLs).

Respond with ONLY a single JSON object, no markdown code fences, no preamble,
in exactly this shape:
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

    text_parts = [
        block["text"] for block in data.get("content", []) if block.get("type") == "text"
    ]
    full_text = "\n".join(text_parts).strip()

    # Strip accidental code fences if the model adds them anyway.
    full_text = re.sub(r"^```json\s*|\s*```$", "", full_text.strip())

    try:
        return json.loads(full_text)
    except json.JSONDecodeError:
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
    recent_titles = get_recent_titles()
    prompt = build_prompt(recent_titles)
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
