---
title: "United's ATC Warning for Air Taxis Is Really About Whether the Flight Ops Software Stack Can Handle a New Category of Aircraft"
date: 2026-11-23
tags: ["advanced air mobility", "air traffic management", "evtol", "flight ops"]
summary: "United Airlines CEO Scott Kirby's public warning that air traffic control isn't ready for eVTOLs is less a verdict on any single aircraft program and more a signal about the depth of the ATM software infrastructure problem the entire industry still needs to solve."
draft: false
---

United Airlines CEO Scott Kirby doesn't hand out public endorsements of technical risk very often, so when he said this week that the nation's air traffic control system isn't ready for air taxis, it was worth reading carefully. The comment came in the context of the FAA's November 13 ground stop — an event I wrote about last week — and <cite index="37-9">United's CEO expressed concerns about whether the nation's air traffic control system was ready for eVTOLs, and the recent ground stop led him to say the FAA needs to invest more in updating its technology. That framing puts the pressure where it belongs: not on the aircraft, but on the infrastructure sitting underneath it.

## The Real Question Isn't Certification — It's the Software Stack

The aviation press has spent most of the past two years treating eVTOL commercialization as a hardware and certification race. Type certificate timelines, battery density curves, vertiport construction counts — those are the metrics that dominate coverage. But Kirby's warning points at a different problem entirely, and it's one the flight ops software community should recognize immediately: <cite index="37-11">eVTOL commercialization is heavily dependent on ecosystem readiness, certified airspace rules from the FAA, and seamless hub-and-app execution. That last phrase is doing a lot of work. "Hub-and-app execution" isn't a hardware specification — it's a software integration challenge, and it's one that doesn't have a clear owner yet.

The traffic management infrastructure question has been hiding in plain sight. In polling I've cited before, aviation professionals identified traffic management infrastructure as the single biggest barrier to commercial eVTOL launch at 37% — ahead of aircraft certification at 27%, public trust at 20%, and vertiport access at 17%. Kirby is essentially naming that number out loud. What he's describing isn't a runway capacity problem or an ATC staffing problem — it's a data and software architecture problem. The systems that handle routing, sequencing, deconfliction, and real-time replanning for today's commercial jets weren't designed with low-altitude, high-frequency, urban-corridor operations in mind. Adding a new category of aircraft means building new logic layers, not just adding new transponder codes.

## What Flight Ops Software Vendors Are Actually Being Asked to Build

The gap Kirby is identifying is one I find genuinely underappreciated on the vendor side. The assumption embedded in most eVTOL commercialization timelines is that the existing ATM infrastructure will adapt — that SMART, FF-ICE, and the broader NextGen/SESAR evolution will eventually accommodate air taxis the way they accommodated regional jets. That assumption deserves more scrutiny than it's getting.

<cite index="37-8">The technical difficulties in air traffic are a real problem for companies focusing on air taxis. But the deeper issue isn't a single system outage — it's that the flight ops software layer connecting urban air mobility operations to the broader ATM network doesn't exist in production form anywhere. No airline's OCC is built to handle a fleet mix that includes both wide-body intercontinental aircraft and sub-15-minute urban shuttle flights operating under different separation minima. No EFB platform has a certified workflow for pilots transitioning between conventional IFR operations and vertiport arrivals in the same duty day. These aren't unsolvable problems, but they're genuine software architecture problems, and the investment required to solve them is orders of magnitude larger than any individual aircraft program.

## The Honest Timeline Problem

Kirby's warning is calibrated, not alarmist. <cite index="37-10">Neither the FAA's nor United's technical problems reflect a flaw in the aircraft itself. That's an important distinction — this isn't a vote against the technology, it's a vote against the timeline assumptions underneath the commercialization story. From time spent on the product and delivery side of flight ops software, I'd characterize the sequencing problem this way: the flight ops software stack that needs to exist before urban air mobility scales at any meaningful volume will take longer to build, validate, and certify than the industry's current projections assume. The certification path for a new aircraft type is at least visible — EASA and FAA have both published frameworks. The certification path for the software layer connecting that aircraft to the broader airspace system is considerably less defined.

That's the real signal in Kirby's comment. It's not pessimism about eVTOLs. It's a reminder that the most important flight ops software for the next decade might not be an EFB upgrade or a fuel-efficiency tool — it could be the ATM integration layer that doesn't exist yet.

## Sources

- [The Motley Fool — "United Airlines Has Warned Air Traffic Control Isn't Ready for Air Taxis"](https://fool.com/investing/2026/11/22/united-airlines-has-warned-air-traffic-control-isn-t-ready-for-air-taxis-that-s-a-bigger-problem-for-archer-than-its-cash-burn)
- [Aviation Week — Advanced Air Mobility coverage, November 2026](https://aviationweek.com/aerospace/advanced-air-mobility)
- [Urban Air Mobility News — latest headlines, November 2026](https://www.urbanairmobilitynews.com/)
