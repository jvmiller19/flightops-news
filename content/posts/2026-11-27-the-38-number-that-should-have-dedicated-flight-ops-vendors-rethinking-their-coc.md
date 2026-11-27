---
title: "The 38% Number That Should Have Dedicated Flight Ops Vendors Rethinking Their Cockpit Strategy"
date: 2026-11-27
tags: ["flight ops software", "efb", "aviation ai", "cockpit tools"]
summary: "A recent industry poll finding that 38% of aviation professionals now rate airlines building in-house as the best source of flight ops software is a more consequential market signal than the vendor community seems to have absorbed — especially on the cockpit side."
draft: false
---

The conventional read on who builds the best flight operations software has always been straightforward: specialized vendors win on depth, airlines win on institutional knowledge, and big tech wins on infrastructure. What's changed is the size of the gap. A recent industry poll asked aviation professionals directly — and 46% said dedicated vendors, while 38% said airlines building in-house. That's not a comfortable margin. That's a warning sign for the vendor community that deserves a more honest reckoning than it's getting.

## The Vendor Assumption That Needs Re-Examining

For most of the past two decades, the working assumption in flight ops software was that purpose-built vendors had an almost structural advantage on the cockpit side. They could amortize development costs across dozens of operators, iterate on UX through feedback from thousands of pilots, and keep the navigation data infrastructure current in ways no single airline IT team could match. That logic still holds in some domains — certified aeronautical data publishing, for instance, is genuinely hard to replicate in-house, and there's a reason the chart and navigation data layer has remained dominated by a small number of specialized players.

But the assumption breaks down when you look at pilot-facing application design and what I'd call the information-timing problem: not whether the data is available in the EFB, but whether it shows up in the right format, at the right phase of flight, without creating cognitive noise for a crew already managing workload. That problem doesn't get solved by the vendor who has the most features. It gets solved by the team that has sat with its own pilots long enough to know which features actually change behavior and which ones get ignored after the first week.

The SITA eWAS+ launch this week — pairing weather and operational data in a single EFB layer for pilots — is a good illustration of a dedicated vendor trying to solve exactly this problem. <cite index="28-1">Pilots can make more confident decisions with eWAS+, which pairs weather and operational data for a full picture at every phase of flight. <cite index="28-2">It builds on SITA eWAS, used by more than 40,000 pilots at more than 60 airlines for over 12 years. That installed base is real. But the fact that a twelve-year-old product needed a significant rearchitect to combine weather with operational context is itself telling — the original design left that integration on the table for over a decade.

## Why Airlines Building In-House Are Gaining Ground on the Cockpit

The 38% figure isn't coming from nowhere. When I look at the dynamics that have actually shifted in the last few years, two things stand out.

First, the data-quality gap that once firmly favored vendors has narrowed. The underlying aeronautical data layer — NOTAMs, charts, weather — has become more accessible via API from a wider range of sources, which means an airline's internal team doesn't need to build a global data-publishing operation from scratch. They can compose from best-in-class feeds and focus their development energy on the layer that actually differentiates the cockpit experience: the workflow logic, the phase-of-flight context, the way information surfaces when a crew needs it rather than when the system thinks they might.

Second, and this is the part I think vendors are underestimating, airline-built tools carry a qualitatively different relationship with their pilot community. The feedback loop is direct, iterative, and embedded in real operations — not mediated through a customer success manager and a quarterly release cycle. That intimacy produces different design decisions. The captain who finds the fuel-uplist flow confusing walks down the hall and says so. That doesn't happen with an external vendor platform.

From time working on delivery and product roles across multiple aviation software vendors, I've watched the same gap emerge repeatedly: the data pipeline gets built, the integration gets certified, the platform goes live — and then behavior doesn't change the way the original business case projected, because the tool wasn't designed around the actual cognitive moment where the decision gets made. Airlines building their own tools are, increasingly, getting this right.

## What the Dedicated Vendors Need to Do Differently

None of this means the 38% figure signals an inevitable platform shift toward airline-built software. The certification overhead alone — keeping a commercial EFB platform compliant across EASA, FAA, CAAC, and a dozen other regulatory environments — is a genuine moat that most airline IT organizations don't want to maintain. The vendor community still has structural advantages that are real and durable.

But the right response to that 38% number isn't to dismiss it as airlines being overconfident about their internal capabilities. The right response is to treat it as evidence that the vendor community has left genuine gaps in the cockpit-side experience — in information timing, in feedback design, in the kind of crew-centric UX thinking that only comes from deep pilot engagement — and that airlines are filling those gaps themselves because no one else did.

I'd argue that where dedicated vendors are most at risk is precisely in the pilot-facing analytics and decision-support layer: the tools that sit between raw data and cockpit action. That's where airline-built products are increasingly competitive, and that's where vendors who keep competing on feature count rather than workflow quality are going to continue losing ground — regardless of how mature their underlying data infrastructure is.

The EFB market is heading toward $6 billion by 2035, and there's enough growth for multiple business models to coexist. But the competitive frontier has shifted. It's no longer about who has the most comprehensive data platform. It's about who understands the cockpit workflow well enough to make the data actually useful when it counts.

## Sources
- [AAV News in Brief – 26 November 2026 (SITA eWAS+ launch)](https://asianaviation.com/posts/aav-news-in-brief-26-november-2026)
- [Y Combinator Airlines Startups 2026 (Skymerse profile)](https://www.ycombinator.com/companies/industry/Airlines)
- [Spherical Insights – Top 20 EFB Market Companies 2026–2035](https://www.sphericalinsights.com/blogs/top-20-companies-in-the-global-electronic-flight-bag-efb-market-2026-2035-spherical-insights-analysis)
