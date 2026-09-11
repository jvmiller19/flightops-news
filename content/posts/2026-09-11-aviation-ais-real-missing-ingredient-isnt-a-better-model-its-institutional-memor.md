---
title: "Aviation AI's Real Missing Ingredient Isn't a Better Model — It's Institutional Memory"
date: 2026-09-11
tags: ["aviation ai", "flight operations", "efb", "aviation technology"]
summary: "Aviation AI's capability gap is real but overstated — the harder problem is that the institutional knowledge making AI outputs genuinely useful rarely gets encoded in a form models can actually consume."
draft: false
---

There's a pattern worth naming in how the aviation industry talks about AI readiness. The conversation almost always gravitates toward capability — which model is most accurate, which vendor has the cleanest data pipeline, which demo impressed the most people at the last conference. What it rarely confronts directly is the thing that actually makes AI useful in a live operational environment: the accumulated institutional knowledge of how a specific airline runs its specific operation, embedded in the people who've been doing it for years.

A piece from OAG published this week put it well: aviation AI doesn't have a capability problem anymore. What it lacks is something closer to institutional memory — the judgment behind a recovery decision, the reason a particular departure might need a payload restriction on a hot summer afternoon, the accumulated understanding of which situations call for which responses. That knowledge exists. It's just rarely in one place, and almost never in a form that a model can readily consume.

I think the framing is largely right, though I'd stop short of saying the capability gap is fully closed. Both gaps are real, and they compound each other — a more capable model still hits a ceiling if it's operating without the operational context that would make its outputs trustworthy, and the richest institutional knowledge base in the world doesn't help if the underlying tooling can't reason over it effectively. The honest answer is that the industry needs to close both, and the memory side tends to get less attention because it's harder to put on a roadmap.

## The Cockpit Is Where This Gap Bites Hardest

This might sound like an OCC or planning problem, but I'd argue the flightdeck is actually where the institutional memory deficit shows up most acutely. Dispatch can work from structured data — flight plans, weather feeds, NOTAM packages — that at least lives in documented systems. What pilots carry into the cockpit is something different: a mental model of how their aircraft behaves, how their airline tends to respond to specific disruption scenarios, which ATC facilities are likely to offer alternatives in congested airspace and which won't. That knowledge is real, it's operationally consequential, and almost none of it exists in a form that any AI tool can currently see.

Korean Air's fuel management results are a useful reference point here. The airline achieved a 3.3% reduction in emissions in 2025 despite a 2.6% increase in flight operations — a genuinely meaningful result. But that kind of outcome doesn't come from deploying a general-purpose model against publicly available data. It comes from years of operational learning about how Korean Air's fleet, routes, and crews actually behave, translated into specific interventions that pilots and dispatchers can act on. I'd attribute that result roughly equally to the AI tooling and to the airline's operational discipline in encoding and consistently acting on what the system recommended — neither half works without the other.

The vendors building cockpit AI tools are starting to understand this, even if they don't always frame it that way. The smarter EFB platforms aren't just competing on feature count or data freshness — they're competing on how well they can reflect the operator's own operational context back to the crew at the moment it's relevant. That's a fundamentally different design problem than building a good general-purpose navigation or weather tool.

## Why This Is an Adoption Problem Disguised as a Data Problem

The instinct when confronted with a knowledge gap is to reach for more data. And the aviation industry has done exactly that — investing heavily in data platforms, telemetry pipelines, and connectivity infrastructure over the last several years. That infrastructure matters. But more data doesn't automatically produce institutional memory. What produces institutional memory is the deliberate work of capturing how experienced operators actually make decisions, encoding those patterns in a way models can learn from, and then validating that the outputs reflect operational reality rather than a statistically plausible approximation of it.

That work is slow, expensive, and not particularly glamorous. It requires airline operators to invest time that frontline crews — especially pilots — rarely have spare. It requires vendors to build deployment and knowledge-capture workflows that go well beyond a standard SaaS onboarding. And it requires airlines to treat their own operational knowledge as a strategic asset worth protecting and systematically building, rather than something that walks out the door when experienced crew members retire.

Having spent time on the delivery side of aviation software deployments, I can say that this phase genuinely does get taken seriously by airline customers — at least more often than the industry's reputation for chaotic go-lives might suggest. The problem isn't always indifference; it's that even well-intentioned programs run into a convergence of obstacles that are each individually manageable but collectively exhausting. Data format and standardization issues, crew time constraints, regulatory caution about how AI inputs get documented and validated, cultural friction around asking experienced pilots to articulate knowledge they've spent careers internalizing — all of it piles up at the same moment in a deployment. No single factor dominates; they tend to arrive together.

On the crew side specifically, I don't think pilots are fundamentally unwilling to contribute to the kind of structured knowledge capture that would make these tools more contextually accurate. The more realistic concern is whether the capture process itself is designed well enough to fit into how crews actually work. Ask someone to fill out a lengthy debrief form after a long duty period and you'll get low-quality data fast. Build lightweight, contextually triggered feedback mechanisms into the EFB workflow itself, and the calculus looks different. Willingness is there if the ask is reasonable — and making it reasonable is a product design problem, not just a change management one.

The result when that design work doesn't happen is a tool that crews stop trusting after the first few encounters that don't match their experience. That's the adoption problem underneath what looks like a data problem. And until the industry takes it seriously as a discipline — not just a deployment step — the ceiling on cockpit AI usefulness will stay lower than the technology itself would suggest it needs to be.

## Sources
- [OAG — September 2026: Airline Tech Puts a Price on Memory](https://www.oag.com/blog/airline-tech-puts-a-price-on-memory)
- [Aviation Week — Korean Air Fuel Management Results](https://aviationweek.com/term/artificial-intelligence)
- [Aerospace America — AI, Assurance, and the Future of Aviation Operations](https://aerospaceamerica.aiaa.org/institute/ai-assurance-and-the-future-of-aviation-operations/)
