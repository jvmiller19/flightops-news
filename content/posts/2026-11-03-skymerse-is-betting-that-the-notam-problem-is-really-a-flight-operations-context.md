---
title: "Skymerse Is Betting That the NOTAM Problem Is Really a Flight Operations Context Problem"
date: 2026-11-03
tags: ["notams", "flight planning", "ai", "efb"]
summary: "Notamify's relaunch as Y Combinator-backed Skymerse signals a broader shift: the industry's NOTAM comprehension challenge isn't just about plain-language translation — it's about carrying operational context from preflight planning all the way to the cockpit."
draft: false
---

NOTAMs have been a punchline in aviation for decades — dense, coded, relentlessly unreadable, and issued in volumes that make genuine comprehension nearly impossible at scale. The industry has known this for a long time. What's changed recently is that multiple vendors are attacking the problem simultaneously, from different angles, and one of the more interesting entrants just significantly widened its ambition.

## From Decoder to Flight Ops AI

<cite index="35-1,35-2">Notamify, the AI NOTAM interpretation tool, has expanded into Skymerse — a Y Combinator-backed "autopilot for flight operations" built on a foundation of 3.6 million interpreted NOTAMs, with new airport suitability assessment and a native iPhone app. The pivot is meaningful. <cite index="35-3">The company describes Skymerse as "one AI system for flight operations," carrying operational context from planning and dispatch in the operations center through to real-time support in the cockpit.

That framing — context continuity from planning through to the flightdeck — is the interesting part. A standalone NOTAM decoder is useful; a system that understands which NOTAMs are operationally relevant *to this specific flight, for this crew, at this point in the sequence* is a different product entirely. Most EFB platforms today still present NOTAMs as a flat list filtered by route proximity, which is better than nothing but still leaves the relevance-ranking problem to the pilot. The gap between "here are the NOTAMs along your route" and "here is what actually matters for your specific operation right now" is where comprehension failures happen.

## How the NOTAM Problem Actually Works

It's worth understanding why NOTAM comprehension is so hard before evaluating what any of these tools are actually solving. A typical international pre-flight briefing for a widebody flight might include hundreds of NOTAMs across departure, en route, destination, and alternates. Many are template-issued, repetitive, or structurally irrelevant to the filed route. The encoding format — inherited from teletype-era constraints — compresses information into abbreviations that even experienced crews have to mentally parse. The cognitive load of sorting operationally critical information from routine filler isn't trivial, and it compounds under time pressure at the gate.

The underlying data quality problem is also real. <cite index="22-4">The Weather Company addressed the adjacent issue in September 2025 when it released smart NOTAMs, using AI to categorize and summarize aviation notices for pilots and dispatchers. That was a dispatch-side product. More recently, <cite index="28-1,28-2,28-3">AirNav Indonesia signed a new AI and cybersecurity cooperation agreement in October 2026 building on a 2024 memorandum, with its NOTAM AI Generator prototype having begun in 2024 and received a soft launch in 2025 — though as of early October its deployment status remains exploratory. At the EFB layer, <cite index="36-3">Jeppesen ForeFlight introduced Graphical NOTAMs in FliteDeck Pro in April 2026, translating dense NOTAM text into map-linked visual information for airline and business aviation pilots. <cite index="36-7,36-8">Graphical NOTAMs show a closed taxiway directly on the airport diagram, primarily for airline and business aviation pilots, while ClearNOTAMs generates plain-language text summaries aimed at individual pilots in the flight-planning workflow.

That layered approach — visual map overlay for the spatial problem, plain-language text for the comprehension problem — is actually a sensible decomposition. The two tools solve different parts of the same underlying challenge.

## The Context Layer Is the Hard Part

What Skymerse is attempting is structurally harder than any of those individual features, because it's asserting that the real problem isn't NOTAM translation — it's operational context. <cite index="35-6">For airlines, the pitch is an "autopilot for flight operations" that carries operational context from the dispatch desk to the cockpit. That means the system needs to understand not just what a NOTAM says, but what it means given the specific aircraft, the specific route, the crew's current operational state, and the real-time environment around the flight.

From my time on the product and delivery side of flight ops software, I'd say that contextual presentation is genuinely the unsolved problem in this space. The data pipeline to get NOTAMs into an EFB has been solved for years. What hasn't been solved is surfacing the right NOTAM, at the right moment, in the right workflow context — without adding cognitive load to a crew that already has plenty to manage. That's an AI problem, but it's also a UX problem and a workflow integration problem. Getting all three right simultaneously is why most attempts at "smart" NOTAM tools have stayed in the useful-but-supplemental category rather than changing how crews actually brief.

<cite index="35-4,35-5">ClearNOTAMs is one piece of a broader trend — multiple EFB providers have now added NOTAM-interpretation features, which means the translation capability is becoming table stakes. The differentiation question shifts to: which platform can actually embed that context into a crew's natural workflow rather than delivering it as a parallel lookup they have to consciously choose to use?

Skymerse's Y Combinator backing and its claim to carry context from planning through to the cockpit is an architectural argument, not just a product feature. Whether the data model underneath it is actually rich enough to support that claim at commercial airline scale — across different fleet types, different regulatory environments, and different dispatch-to-crew data pipelines — is the question I'd be asking if I were evaluating it. The NOTAM interpretation piece is tractable. The operational context continuity piece is significantly harder, and that's where this story gets interesting.

## Sources

- [Skymerse / Notamify — Skyfarer Academy](https://blog.skyfareracademy.com/2026/07/31/notamify-becomes-skymerse-the-y-combinator-backed-push-to-build-an-autopilot-for-flight-operations/)
- [The Weather Company — Wikipedia](https://en.wikipedia.org/wiki/The_Weather_Company)
- [AirNav Indonesia NOTAM AI Deployment — Streamline Feed](https://streamlinefeed.co.ke/news/airnav-indonesia-notam-ai-deployment-status-unclear)
- [Jeppesen ForeFlight ClearNOTAMs — Skyfarer Academy](https://blog.skyfareracademy.com/2026/07/10/jeppesen-foreflight-simplifies-flight-planning-with-ai-powered-clearnotams/)
