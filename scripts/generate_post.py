#!/usr/bin/env python3
"""
Two-phase daily post pipeline:

  research  - picks today's topic, drafts the post, drafts 2-3 pointed
              questions for Vincent, saves a pending draft under .pending/,
              and emails him the summary + questions. Does NOT publish.

  finalize  - checked frequently by a separate workflow. For each pending
              draft: looks for Vincent's email reply (via IMAP on the same
              Gmail inbox used for sending), and if found, asks Claude to
              weave his actual answers into the draft as personal
              commentary, then publishes. Drafts older than 24h with no
              reply are discarded unpublished.

Requires env vars: ANTHROPIC_API_KEY, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME,
MAIL_PASSWORD, MAIL_TO. Optional: IMAP_SERVER (defaults to imap.gmail.com).
"""

import os
import re
import json
import glob
import sys
import smtplib
import imaplib
import email
import email.message
import email.header
import datetime
import requests

THEME = (
    "News and trends in aviation FLIGHT OPERATIONS technology specifically. "
    "IN SCOPE: AI adoption in flight operations, flight planning "
    "optimization, dispatch/OCC (operations control center) transformation, "
    "next-generation aviation software, airline data platforms, "
    "sustainability technology relevant to flight operations, autonomy and "
    "advanced air mobility, and how airlines evaluate or adopt emerging "
    "technology in these areas. Also fair game: notable deals, "
    "partnerships, or product launches in any of the above. "
    "OUT OF SCOPE — do not write about these even if aviation-tech-adjacent: "
    "MRO (maintenance, repair, and overhaul) and aircraft maintenance "
    "technology; customer-facing/passenger technology such as inflight "
    "wifi, entertainment systems, or cabin experience. If your research "
    "surfaces a story in one of the out-of-scope areas, discard it and "
    "search again for something in scope rather than writing about it."
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
- Write in first-person singular when giving Vincent's own commentary or
  referencing past posts (e.g. "as I reported last week," "I think," "in my
  experience") — never first-person plural ("we," "our"). This is a single
  named author's voice, not an editorial "we."
- You MAY reference Vincent's real professional background at a general
  level (e.g. "having spent years on the bid-management side of aviation
  tech deals," "from time spent running global delivery teams") since
  those roles are real and verified above.
- Do NOT explicitly call out that Vincent is a pilot (e.g. "as a pilot,"
  "as someone who flies," "in the cockpit myself"). His aviation background
  is already established by the blog's context — calling it out directly in
  every post is repetitive. It's fine to write with that perspective
  implicitly; just don't name it.
- Be concise. Favor a tighter piece over a longer one — cut anything that
  restates a point already made rather than adding new information.
- You must NEVER invent a specific anecdote, named deal, customer, dollar
  figure, date, or direct quote and attribute it to Vincent's personal
  experience. Only the general nature of his work (listed above) is fair
  to reference — never fabricate a specific story that sounds plausible
  but isn't something he's confirmed actually happened. If in doubt, stay
  general rather than specific."""

# Weekly content structure (Monday=0 ... Friday=4). Each day has a
# distinct angle on the same in-scope theme, not a different topic area.
DAY_THEMES = {
    0: {
        "name": "Industry Signal",
        "guidance": (
            "Pick a major piece of flight-ops-relevant aviation news and "
            "focus on WHY IT MATTERS beneath the surface — the real "
            "underlying shift the announcement represents, not just what "
            "was announced. Example framing: \"Airline X's new AI "
            "initiative is less about AI and more about workflow "
            "redesign.\" Look past the press-release framing to the "
            "operational or strategic substance."
        ),
    },
    1: {
        "name": "Flight Operations Deep Dive",
        "guidance": (
            "Go deep on a specific flight operations discipline: dispatch, "
            "OCC (operations control center), flight planning, NOTAMs, "
            "weather, or optimization. Favor a story that lets you explain "
            "how something actually works operationally, not just that it "
            "happened."
        ),
    },
    2: {
        "name": "Technology / Innovation",
        "guidance": (
            "Focus on the technology itself — AI, automation, data "
            "platforms, startups, or emerging aviation tech relevant to "
            "flight operations. Center the post on what's technically new "
            "or interesting about the approach, not just the business deal "
            "around it."
        ),
    },
    3: {
        "name": "Commercial / Business Angle",
        "guidance": (
            "Take a strategic-thinker's view rather than an operator's "
            "view: what does this news mean for airlines, vendors, or "
            "investors? Focus on competitive dynamics, market "
            "implications, or what smart adoption/investment looks like in "
            "response to this news."
        ),
    },
    4: {
        "name": "Your Perspective",
        "guidance": (
            "Write a stronger opinion piece than usual. Take a clear, "
            "specific point of view on a flight-ops-tech topic or trend, "
            "argued with conviction — not hedged both-sides commentary. "
            "Example framing: \"The aviation industry does not have a "
            "technology problem. It has an adoption problem.\" This is the "
            "one day of the week where the post can be built around "
            "Vincent's take itself rather than around a single news item, "
            "though it should still be grounded in something real and "
            "recent."
        ),
    },
}

REPO_ROOT = os.path.join(os.path.dirname(__file__), "..")
POSTS_DIR = os.path.join(REPO_ROOT, "content", "posts")
PENDING_DIR = os.path.join(REPO_ROOT, ".pending")
API_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-sonnet-4-6"
DRAFT_EXPIRY_HOURS = 24


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

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


def call_claude(prompt, use_web_search=True):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        sys.exit("ERROR: ANTHROPIC_API_KEY environment variable is not set.")

    body = {
        "model": MODEL,
        "max_tokens": 4000,
        "messages": [{"role": "user", "content": prompt}],
    }
    if use_web_search:
        body["tools"] = [{"type": "web_search_20250305", "name": "web_search"}]

    response = requests.post(
        API_URL,
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
        json=body,
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

    # Fallback: the model may have added commentary before/after the JSON,
    # or even duplicated the JSON object (e.g. once fenced, once not). Find
    # the first '{' and walk forward counting brace depth (respecting
    # quoted strings) to get exactly the first complete JSON object, rather
    # than a greedy regex that can span across multiple objects.
    start = full_text.find("{")
    if start != -1:
        depth = 0
        in_string = False
        escape = False
        for i in range(start, len(full_text)):
            ch = full_text[i]
            if in_string:
                if escape:
                    escape = False
                elif ch == "\\":
                    escape = True
                elif ch == '"':
                    in_string = False
            else:
                if ch == '"':
                    in_string = True
                elif ch == "{":
                    depth += 1
                elif ch == "}":
                    depth -= 1
                    if depth == 0:
                        candidate = full_text[start:i + 1]
                        try:
                            return json.loads(candidate)
                        except json.JSONDecodeError:
                            break

    sys.exit(f"ERROR: Could not parse JSON from model output:\n{full_text}")


def slugify(title):
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug).strip("-")
    return slug[:80]


def write_post(post, date_str):
    slug = slugify(post["title"])
    filename = f"{date_str}-{slug}.md"
    path = os.path.join(POSTS_DIR, filename)

    tags_yaml = "[" + ", ".join(f'"{t}"' for t in post.get("tags", [])) + "]"
    summary = post.get("summary", "").replace('"', "'")

    front_matter = (
        "---\n"
        f'title: "{post["title"]}"\n'
        f"date: {date_str}\n"
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


def post_exists_for_date(date_str):
    return bool(glob.glob(os.path.join(POSTS_DIR, f"{date_str}-*.md")))


def send_email(subject, body):
    server = os.environ.get("MAIL_SERVER")
    port = int(os.environ.get("MAIL_PORT", "587"))
    username = os.environ.get("MAIL_USERNAME")
    password = os.environ.get("MAIL_PASSWORD")
    mail_to = os.environ.get("MAIL_TO")

    if not all([server, username, password, mail_to]):
        print("WARNING: mail env vars not fully set, skipping email send.")
        return

    msg = email.message.EmailMessage()
    msg["From"] = username
    msg["To"] = mail_to
    msg["Subject"] = subject
    msg.set_content(body)

    if port == 465:
        with smtplib.SMTP_SSL(server, port) as smtp:
            smtp.login(username, password)
            smtp.send_message(msg)
    else:
        with smtplib.SMTP(server, port) as smtp:
            smtp.starttls()
            smtp.login(username, password)
            smtp.send_message(msg)
    print(f"Sent email: {subject}")


def write_gh_output(values):
    gh_output = os.environ.get("GITHUB_OUTPUT")
    if not gh_output:
        return
    with open(gh_output, "a", encoding="utf-8") as fh:
        for key, val in values.items():
            fh.write(f"{key}={val}\n")


# ---------------------------------------------------------------------------
# Pending draft storage
# ---------------------------------------------------------------------------

def pending_path(date_str):
    return os.path.join(PENDING_DIR, f"{date_str}.json")


def save_pending(draft):
    os.makedirs(PENDING_DIR, exist_ok=True)
    path = pending_path(draft["date"])
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(draft, fh, indent=2)
    print(f"Saved pending draft: {path}")


def load_all_pending():
    drafts = []
    for path in sorted(glob.glob(os.path.join(PENDING_DIR, "*.json"))):
        with open(path, "r", encoding="utf-8") as fh:
            drafts.append((path, json.load(fh)))
    return drafts


def ref_token(date_str):
    return f"[ref:{date_str}]"


# ---------------------------------------------------------------------------
# Phase 1: research
# ---------------------------------------------------------------------------

def build_research_prompt(recent_posts, today):
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

    week_ago = today - datetime.timedelta(days=7)
    day_theme = DAY_THEMES.get(today.weekday())

    day_theme_clause = ""
    if day_theme:
        day_theme_clause = f"""
TODAY'S WEEKLY SLOT — {day_theme['name']}:
{day_theme['guidance']}
This is the angle/lens for today's post, within the overall blog scope
below — not a different topic area. Still pick a real, fresh, in-scope
story; just frame and structure it through today's lens.
"""

    # Friday is the opinion-piece slot, so Vincent gets more questions to
    # give more direct input into the stronger take.
    is_friday = today.weekday() == 4
    question_count = "up to 5" if is_friday else "2 or 3"
    question_count_note = (
        " Since today's post is the Friday opinion piece, lean toward the "
        "higher end of that range (up to 5) so his answers can carry more "
        "of the piece's point of view."
        if is_friday else ""
    )

    return f"""You write a daily blog post for a blog about: {THEME}

{VOICE}

{STYLE_RULES}

TODAY'S DATE: {today.isoformat()}
{day_theme_clause}
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

Write a DRAFT of the post in your own words — do not quote source text
directly beyond a very short phrase here and there. Aim for 300-450 words —
keep it tight, every paragraph should earn its place. Structure: a short
intro hook, 2-3 sections with subheadings (use ##
markdown), and a short closing thought. Leave the closing thought light —
it will be revised afterward to incorporate Vincent's own personal take, so
don't make this draft's ending feel too final or conclusive. End with a
"## Sources" section listing the names of the publications/companies
referenced (no need for full URLs).

Also write {question_count} SHORT, POINTED questions to ask Vincent about
this specific story — designed so his quick answers (multiple choice or a
short free-text answer, a sentence or two at most) can be woven into the
post as his personal commentary. Good questions probe his actual opinion or
experience-informed read on the news (e.g. "Does this deal surprise you, or does it look inevitable given the trend? (Surprising / Inevitable / Mixed)",
"Is this the kind of capability your old delivery teams would have wanted
sooner — yes/no and why in a sentence?"). Avoid generic or vague questions.{question_count_note}

Respond with ONLY a single JSON object as your final message — no preamble,
no explanation of your research process, no markdown code fences, nothing
before or after the JSON. Your very last message must start with {{ and end
with }}, in exactly this shape:
{{
  "title": "string, specific and concrete, no clickbait",
  "summary": "one sentence, plain text, for the post list preview",
  "tags": ["2 to 4 short lowercase tags"],
  "body_markdown": "the full draft post body in markdown, NOT including the title as a heading",
  "questions": ["question 1", "question 2", "... {question_count} total"]
}}"""


def _nth_weekday(year, month, weekday, n):
    """1st, 2nd, 3rd... occurrence of `weekday` (Mon=0) in a given month."""
    d = datetime.date(year, month, 1)
    offset = (weekday - d.weekday()) % 7
    d += datetime.timedelta(days=offset + 7 * (n - 1))
    return d


def _last_weekday(year, month, weekday):
    """Last occurrence of `weekday` (Mon=0) in a given month."""
    if month == 12:
        d = datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
    else:
        d = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
    offset = (d.weekday() - weekday) % 7
    return d - datetime.timedelta(days=offset)


def _observed(date_obj):
    """Federal holidays falling on a weekend are observed on the nearest
    weekday (Saturday -> Friday, Sunday -> Monday)."""
    if date_obj.weekday() == 5:
        return date_obj - datetime.timedelta(days=1)
    if date_obj.weekday() == 6:
        return date_obj + datetime.timedelta(days=1)
    return date_obj


def us_federal_holidays(year):
    """Set of date objects for US federal holidays (observed dates) in a
    given year."""
    fixed = [
        datetime.date(year, 1, 1),    # New Year's Day
        datetime.date(year, 6, 19),   # Juneteenth
        datetime.date(year, 7, 4),    # Independence Day
        datetime.date(year, 11, 11),  # Veterans Day
        datetime.date(year, 12, 25),  # Christmas Day
    ]
    floating = [
        _nth_weekday(year, 1, 0, 3),   # MLK Day - 3rd Monday Jan
        _nth_weekday(year, 2, 0, 3),   # Washington's Birthday - 3rd Monday Feb
        _last_weekday(year, 5, 0),     # Memorial Day - last Monday May
        _nth_weekday(year, 9, 0, 1),   # Labor Day - 1st Monday Sep
        _nth_weekday(year, 10, 0, 2),  # Columbus Day - 2nd Monday Oct
        _nth_weekday(year, 11, 3, 4),  # Thanksgiving - 4th Thursday Nov
    ]
    return {_observed(d) for d in fixed} | set(floating)


def is_us_federal_holiday(date_obj):
    return date_obj in us_federal_holidays(date_obj.year)


def run_research():
    today = datetime.date.today()
    today_str = today.isoformat()

    if is_us_federal_holiday(today):
        print(f"{today_str} is a US federal holiday — skipping research.")
        return
    if post_exists_for_date(today_str):
        print("A post for today already exists — skipping research.")
        return
    if os.path.exists(pending_path(today_str)):
        print("A pending draft for today already exists — skipping research.")
        return

    recent_posts = get_recent_posts()
    prompt = build_research_prompt(recent_posts, today)
    draft = call_claude(prompt, use_web_search=True)

    for field in ("title", "summary", "tags", "body_markdown", "questions"):
        if field not in draft:
            sys.exit(f"ERROR: model response missing required field '{field}'")

    draft["date"] = today_str
    draft["created_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    save_pending(draft)

    questions_text = "\n".join(f"{i+1}. {q}" for i, q in enumerate(draft["questions"]))
    body = f"""Today's draft topic: {draft['title']}

{draft['summary']}

I'd like your take before this publishes. Just reply to this email with
your answers (any format is fine, e.g. "1) B  2) yes, because...") and
I'll weave them into the post:

{questions_text}

If I don't hear back within {DRAFT_EXPIRY_HOURS} hours, I'll skip
publishing today's post rather than guess at your take.

— Auto-generated by flightops.news pipeline {ref_token(today_str)}"""

    send_email(f"Your input needed on today's post — {today_str} {ref_token(today_str)}", body)


# ---------------------------------------------------------------------------
# Phase 2: finalize
# ---------------------------------------------------------------------------

def extract_reply_text(raw_body):
    """Strip quoted original message from a plain-text email reply, keeping
    only what the person actually typed above the quote line."""
    cut_patterns = [
        r"\nOn .{0,100} wrote:\s*\n",
        r"\n-{2,}\s*Original Message\s*-{2,}",
        r"\n>.*",
    ]
    text = raw_body
    for pattern in cut_patterns:
        match = re.search(pattern, text, re.DOTALL)
        if match:
            text = text[:match.start()]
    return text.strip()


def find_reply(date_str):
    """Search the inbox via IMAP for a reply referencing this draft's ref
    token. Returns the extracted reply text, or None if not found."""
    imap_server = os.environ.get("IMAP_SERVER", "imap.gmail.com")
    username = os.environ.get("MAIL_USERNAME")
    password = os.environ.get("MAIL_PASSWORD")
    if not username or not password:
        print("WARNING: mail credentials not set, cannot check for reply.")
        return None

    token = ref_token(date_str)
    try:
        conn = imaplib.IMAP4_SSL(imap_server)
        conn.login(username, password)
        conn.select("INBOX")
        status, data = conn.search(None, f'(SUBJECT "{token}")')
        if status != "OK" or not data[0]:
            # Diagnostic: log recent subjects so we can see why the match
            # failed (e.g. subject encoding) without needing mailbox access.
            _, recent_ids = conn.search(None, "ALL")
            recent_ids = recent_ids[0].split()[-10:] if recent_ids and recent_ids[0] else []
            print(f"No SUBJECT match for token {token!r}. Last {len(recent_ids)} inbox subjects:")
            for msg_id in recent_ids:
                _, hdr_data = conn.fetch(msg_id, "(BODY[HEADER.FIELDS (SUBJECT)])")
                if hdr_data and hdr_data[0]:
                    raw_header = hdr_data[0][1].decode("utf-8", errors="replace").strip()
                    print(f"  {raw_header!r}")
            conn.logout()
            return None

        ids = data[0].split()
        # Most recent matching message first.
        for msg_id in reversed(ids):
            status, msg_data = conn.fetch(msg_id, "(RFC822)")
            if status != "OK":
                continue
            msg = email.message_from_bytes(msg_data[0][1])
            raw_subject = msg.get("Subject", "")
            decoded_parts = email.header.decode_header(raw_subject)
            subject = "".join(
                part.decode(enc or "utf-8", errors="replace") if isinstance(part, bytes) else part
                for part, enc in decoded_parts
            )
            print(f"Inspecting candidate message, subject: {subject!r}")
            # Only treat actual replies (not the original sent email) as input.
            if not subject.lower().startswith("re:"):
                print("  -> skipped, does not start with 'Re:'")
                continue

            raw_body = None
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        raw_body = part.get_payload(decode=True).decode(
                            part.get_content_charset() or "utf-8", errors="replace"
                        )
                        break
            else:
                raw_body = msg.get_payload(decode=True).decode(
                    msg.get_content_charset() or "utf-8", errors="replace"
                )

            if not raw_body:
                print("  -> skipped, no text/plain body found")
                continue
            reply_text = extract_reply_text(raw_body)
            if reply_text:
                print(f"  -> using as reply ({len(reply_text)} chars)")
                conn.logout()
                return reply_text
            print("  -> skipped, extracted reply text was empty after stripping quote")
        conn.logout()
        return None
    except Exception as exc:
        print(f"WARNING: IMAP check failed: {exc}")
        return None


def build_finalize_prompt(draft, reply_text):
    questions_text = "\n".join(f"- {q}" for q in draft["questions"])
    return f"""You are revising a draft blog post to weave in the author's
own personal commentary, which he just gave in response to specific
questions. Do not change the factual reporting or restructure the piece —
only revise it (especially the closing section) so his actual answers below
read as his natural first-person commentary, per the voice and style rules
below.

{VOICE}

{STYLE_RULES}

DRAFT TITLE: {draft['title']}

DRAFT BODY:
{draft['body_markdown']}

QUESTIONS HE WAS ASKED:
{questions_text}

HIS RAW REPLY (verbatim, may be informal or use shorthand like "1) B"):
\"\"\"{reply_text}\"\"\"

Incorporate his actual answers naturally into the post as his own voice —
do not quote his reply verbatim or refer to "questions" or "answers"
explicitly; it should read as commentary he simply included while writing.
Do not fabricate anything beyond what his reply conveys.

Also write a one-line "linkedin_teaser" — a punchy, scroll-stopping single
sentence Vincent could post on LinkedIn to draw attention to this finished
article (not just a restatement of the title; give it a hook, and reflect
his actual take if it sharpens the hook). No hashtags, no emoji.

Respond with ONLY a single JSON object as your final message — no preamble,
no markdown code fences, nothing before or after the JSON. Your very last
message must start with {{ and end with }}, in exactly this shape:
{{
  "title": "string, may be unchanged from the draft",
  "summary": "one sentence, plain text, for the post list preview",
  "tags": ["2 to 4 short lowercase tags"],
  "body_markdown": "the full REVISED post body in markdown, NOT including the title as a heading",
  "linkedin_teaser": "one punchy sentence, no hashtags, no emoji"
}}"""


def run_finalize():
    pending = load_all_pending()
    if not pending:
        print("No pending drafts.")
        return

    now = datetime.datetime.now(datetime.timezone.utc)
    published_any = False

    for path, draft in pending:
        date_str = draft["date"]

        if post_exists_for_date(date_str):
            print(f"Post for {date_str} already exists — removing stale pending draft.")
            os.remove(path)
            continue

        created_at = datetime.datetime.fromisoformat(draft["created_at"])
        age_hours = (now - created_at).total_seconds() / 3600
        if age_hours > DRAFT_EXPIRY_HOURS:
            print(f"Pending draft for {date_str} expired ({age_hours:.1f}h old) — discarding.")
            os.remove(path)
            send_email(
                f"Skipped today's post — no reply received ({date_str})",
                f"I didn't hear back on the {date_str} draft within "
                f"{DRAFT_EXPIRY_HOURS} hours, so I skipped publishing rather "
                f"than guess at your take. Topic was: {draft['title']}",
            )
            continue

        reply_text = find_reply(date_str)
        if not reply_text:
            print(f"No reply yet for {date_str} pending draft.")
            continue

        print(f"Found reply for {date_str}, finalizing post.")
        prompt = build_finalize_prompt(draft, reply_text)
        final_post = call_claude(prompt, use_web_search=False)

        for field in ("title", "summary", "tags", "body_markdown", "linkedin_teaser"):
            if field not in final_post:
                sys.exit(f"ERROR: finalize response missing required field '{field}'")

        write_post(final_post, date_str)
        os.remove(path)
        published_any = True

        send_email(
            f"Published: {final_post['title']}",
            f"Today's post is live, with your input included.\n\n"
            f"Title: {final_post['title']}\n"
            f"Summary: {final_post.get('summary', '')}\n\n"
            f"LinkedIn teaser (copy/paste when you share the post):\n"
            f"{final_post['linkedin_teaser']}\n\n"
            f"It will be live on the site within a few minutes, once the "
            f"deploy workflow finishes.",
        )

        write_gh_output({
            "published": "true",
            "post_title": final_post["title"],
            "post_summary": final_post.get("summary", ""),
        })

    if not published_any:
        write_gh_output({"published": "false"})


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ("research", "finalize"):
        sys.exit("Usage: generate_post.py [research|finalize]")

    if sys.argv[1] == "research":
        run_research()
    else:
        run_finalize()


if __name__ == "__main__":
    main()
