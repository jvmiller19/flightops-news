---
title: "The November 13 FAA Ground Stop Wasn't a Surprise — It Was a Warning"
date: 2026-11-16
tags: ["faa", "atc", "infrastructure", "flight ops"]
summary: "A faulty router during a copper-to-fiber upgrade halted every US departure for four hours on November 13 — and the real story isn't the router. It's the infrastructure it was sitting on."
draft: false
---

On the evening of November 13, the FAA issued a nationwide ground stop that halted all US departures for just over four hours. More than 15,000 flights were delayed or canceled that day, with disruption spilling into Saturday as airlines worked to reposition aircraft and crew. Flights inbound from Europe were caught mid-ocean. The ripple effects lasted days.

The stated cause: a newly installed router, part of an ongoing upgrade from copper to fiber telecommunications, began flooding the FAA's network with roughly a thousand connection attempts every four to five seconds. That behavior disrupted aircraft communication feeds and radar data across multiple Air Route Traffic Control Centers, forcing controllers to call a full stop until the network could be stabilized. As of Friday the 14th, the FAA had not confirmed the root cause of the router's behavior.

Transportation Secretary Sean Duffy was quick to clarify that the FAA's SMART AI advisory tool — which had been deployed to some facilities — was not involved. Air Space Intelligence, the contractor behind SMART, confirmed the same. That clarification was necessary because SMART had been in the news, and the instinct to blame the newest, most visible piece of technology was predictable. But the actual failure was in infrastructure that predates SMART by decades.

## What Actually Failed

The FAA's communications backbone is a patchwork of legacy systems, many of which were designed in an era when today's traffic volumes were unimaginable. STARS and ERAM — the radar and flight data processing platforms at the core of ATC operations — are themselves replacements for older systems, but they sit on top of telecommunications infrastructure that in many facilities is still transitioning away from copper. The upgrade program underway is not optional maintenance. It is an overdue structural replacement.

The irony of this particular failure is that it happened during the upgrade, not because of deferred maintenance. A contractor introducing a misconfigured router into a fragile network produced a cascade that the system had no tolerance for. That's not an argument against upgrading. It's an argument for how little margin exists in the current architecture. A network with modern, redundant, well-monitored infrastructure absorbs a misconfigured router. This one didn't.

The House Transportation and Infrastructure Committee announced it would review the failure. That review is warranted, but the question it needs to answer isn't "who misconfigured the router." It's why the FAA's communications network in 2026 has so little fault tolerance that a single misbehaving device at a remote site can ground the entire country.

## The Trend Line Points in One Direction

This is not an isolated incident. The January 2023 NOTAM system failure — which also resulted in a nationwide ground stop — was traced to a corrupted database file during a routine maintenance update. The same pattern: an infrastructure system with no meaningful redundancy, a routine operation, a cascade failure, and a country-wide halt.

The volume of IFR operations in US airspace has grown steadily for years. The complexity of that traffic — more carriers, more routes, more data dependencies between systems — has grown with it. The infrastructure underneath has not kept pace. At some point, the gap between the load the system is carrying and the resilience it was designed for produces failures. We are past that point.

I've spent time on the vendor side of aviation software, working with carriers and operators who depend on FAA systems as foundational inputs to their own operations — flight planning, dispatch, crew scheduling, all of it assumes a functioning ATC backbone. What became clear from that work is how deeply the fragility of FAA infrastructure propagates downstream. When the FAA stops, it isn't just controllers who are affected. Every flight ops software platform, every EFB, every dispatch system that depends on real-time airspace data is suddenly operating against a blank or stale picture. The operators absorb that uncertainty in silence, because there's no alternative.

## This Needs to Be Treated as Urgent

The FAA modernization program has been underfunded and politically deprioritized for most of the past two decades. NextGen, the last major infrastructure modernization effort, was supposed to be complete years ago and remains unfinished in many respects. The copper-to-fiber upgrade program is real and ongoing, but it is proceeding at a pace that reflects bureaucratic budget cycles, not operational risk.

The November 13 ground stop cost airlines and passengers tens of millions of dollars in a single afternoon. That figure is real, but it understates the actual cost — which includes the erosion of confidence in US airspace reliability, the downstream operational chaos that cascaded through airline networks over three days, and the compounding risk that each additional failure represents for a system that is asked to handle more traffic, more complexity, and more data dependencies every year.

Upgrading FAA infrastructure needs to be treated as an urgent national priority, not a line item that gets trimmed in budget negotiations. The current pace of investment is not matched to the pace of risk accumulation. If it isn't addressed deliberately, the November 13 ground stop won't be the last one. It will be one of the smaller ones we look back on.

## Sources
- [CNN — November 13, 2026: Some US flights resume after hours-long ground stop](https://www.cnn.com/2026/11/13/us/live-news/flights-ground-stop-faa)
- [CNBC — FAA lifts ground stop after more than four hours, but flight cancellations will stretch into the weekend](https://www.cnbc.com/2026/11/13/faa-ground-stop.html)
- [AvWeb — FAA Rules Out SMART AI System as Cause of Nationwide Ground Stop](https://avweb.com/aviation-news/faa-nationwide-ground-stop-lifts-smart-ai/)
- [Aviation Stream — FAA Nationwide Ground Stop: What Happened on 13 November](https://aviationstream.com/news/faa-nationwide-ground-stop-november-2026-explained/)
- [Wikipedia — 2026 FAA nationwide ground stop](https://en.wikipedia.org/wiki/2026_FAA_nationwide_ground_stop)
