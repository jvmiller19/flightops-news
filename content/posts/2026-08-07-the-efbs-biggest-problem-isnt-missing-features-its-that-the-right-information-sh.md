---
title: "The EFB's Biggest Problem Isn't Missing Features — It's That the Right Information Shows Up at the Wrong Time"
date: 2026-08-07
tags: ["efb", "aviation technology", "flight planning", "cockpit tools"]
summary: "Adventure Pilot's iFly EFB 14.1 uses Dynamic Checklists and phase-aware context to argue that the next wave of EFB competition will be won on information timing, not feature count."
draft: false
---

The EFB market has spent the better part of fifteen years adding features. Charts, weather overlays, NOTAM filters, performance calculators, fuel planning, terrain awareness — the modern EFB is genuinely impressive in scope. What it hasn't always been good at is timing. The information is in there; getting it in front of the pilot at the moment it's actually useful has been a different problem entirely, and one that most platforms have been slow to take seriously.

Adventure Pilot's iFly EFB 14.1 release, announced July 21, is a small but pointed argument that the timing problem is solvable — and that solving it is where the next wave of EFB competition will actually be fought.

## Dynamic Checklists Are a UX Bet, Not a Feature Add

<cite index="18-2,18-3">The 14.1 release introduces several pilot-focused enhancements designed to bring useful information forward at the right time, reduce screen-hunting, and improve confidence from preflight through shutdown.</cite> The headline feature is Dynamic Checklists — <cite index="18-4,18-5,18-6">context-aware cockpit tools that turn traditional checklists into something more adaptive, with checklist items that surface relevant frequencies, runway details, altitude references, and ATC cues based on the current flight situation, and that let pilots jump directly from a checklist row to the related part of the app.</cite>

That last detail is worth dwelling on. The jump-to-context behavior isn't about adding new data — it's about collapsing the cognitive steps between a task and the information supporting it. In a bouncy descent into an unfamiliar airport at night, the number of taps to get from checklist to approach plate to frequency is not a minor UX concern. It's directly relevant to workload and error risk.

<cite index="18-7,18-8">The release also adds VFR Visual Approaches for runway-specific arrival planning, and Turn-Aware Flight Plans that present a more natural view of how a route will unfold in flight, with smoother speed-aware turn paths.</cite> These aren't headline-grabbing AI announcements, but they reflect the same underlying design logic: reduce the gap between what the system knows and what the pilot can actually act on in the moment.

## Where the Incumbents Are Vulnerable

I'd frame the core problem this way: the information is usually there, but it isn't easily accessible, and in real workflows it's often missed entirely. That's an information-surfacing problem, not an information-availability problem, and it's the right thing to be trying to fix.

What pilots have consistently wanted — from my time working across EFB and flight planning products — isn't more features. It's a development philosophy that makes their workflow easier rather than layering more complexity onto it. Every additional feature that requires the pilot to navigate to it, learn it, and remember to use it at the right moment is, in a real sense, a tax on attention. The platforms that have accumulated the most features have also, in some cases, accumulated the most of that tax.

ForeFlight has obvious scale advantages and is pushing hard on AI features — <cite index="25-1">launching Airflow, its aviation AI engine, on July 1, 2026, alongside Clear NOTAMs and a ChatGPT-based AI Connector.</cite> Those are genuinely significant moves. But there's a meaningful difference between AI-driven query and interpretation on one hand, and workflow-state-driven context on the other. iFly's Dynamic Checklists approach is more direct — it cuts to the root of the complexity problem rather than adding a new interface layer on top of it. For actual in-flight utility over the next several years, that direction is where the market should be heading.

Adventure Pilot is a smaller player — GA-focused, priced well below the commercial platforms, and without the data network advantages that Jeppesen ForeFlight or Garmin bring to the table. But smaller players often get to experiment with interaction models that incumbents are reluctant to disrupt in their own products. Whether the legacy charting and EFB platforms can make this architectural shift is a real question, and my honest read is that it would likely require building from scratch rather than retrofitting what already exists. The legacy of those platforms is deep feature investment; rearchitecting around phase-of-flight context is a different kind of engineering problem than adding a new data source.

<cite index="18-9">New Vertical Nav and Horizontal Nav instruments in 14.1 provide additional precision for tracking routes, descents, and approach-style guidance, while MOS weather data adds another source for evaluating conditions in flight</cite> — all of it oriented around the pilot's actual position and task at any given moment, not the preflight briefing.

## The Broader Design Argument

The question this release puts on the table for the commercial EFB market is whether context-awareness is a nice-to-have enhancement or a structural requirement for the next generation of pilot-facing tools. I think it's the latter. The amount of data available to a pilot-facing application has grown enormously over the last decade — real-time weather, traffic, TFR updates, NOTAMs, performance calculations. The bottleneck isn't data access anymore. It's intelligent prioritization and sequencing of that data within the flow of an actual flight.

The broader industry challenge, as I see it, is making existing tools more usable rather than continuing to develop more and more new features that take effort to find, learn, and integrate into a workflow that's already demanding. iFly EFB 14.1 takes direct aim at that challenge. It's a smart direction, and the EFB platforms that follow it — not just for the preflight briefing, but for the descent, the approach, the go-around decision — will have a more durable competitive position than any feature list can provide. iFly EFB 14.1 won't be the last word on this. But it's an honest attempt at framing the right question.

## Sources
- [Piper Flyer Association – iFly EFB 14.1 Announcement](https://www.piperflyer.org/adventure-pilot-announces-ifly-efb-14-1-with-smarter-cockpit-tools-and-expanded-flight-planning-features/)
- [Skyfarer Academy – Jeppesen ForeFlight Airflow / ClearNOTAMs Launch](https://blog.skyfareracademy.com/2026/07/01/ai-powers-new-jeppesen-foreflight-features-clear-notams-chatgpt-connector-and-flight-school-scheduler/)
