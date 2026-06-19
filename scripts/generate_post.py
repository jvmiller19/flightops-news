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

    return f"""You
