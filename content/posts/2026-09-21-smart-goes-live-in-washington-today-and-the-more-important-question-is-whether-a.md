---
title: "SMART Goes Live in Washington Today — and the More Important Question Is Whether Airlines' Flight Planning Systems Are Ready to Receive It"
date: 2026-09-21
tags: ["faa", "air traffic management", "flight planning", "aviation technology"]
summary: "The FAA's SMART predictive traffic-planning system begins its first operational trial in the Washington area today, and the real test isn't the AI — it's whether the data pipeline connecting SMART's outputs to airline flight planning tools can actually deliver."
draft: false
---

I've covered the SMART program twice before — when the FAA awarded the contract to Air Space Intelligence in June, and again when airlines flagged data-sharing concerns in Senate testimony. Today is a genuinely different moment: the system appears to be going live.

## What's Actually Happening

The FAA is preparing to put SMART, its new predictive traffic-planning software, into operational use in the Washington area — what would be the system's first operational fielding. SMART — Strategic Management of Airspace, Routes and Trajectories — sits under a 12-year, $875-million contract with Air Space Intelligence, and is designed to support both the FAA and airlines with operations, schedules, and reducing delays and cancellations. The first roughly 90-day test will help determine how well the system works before any wider rollout.

The press framing on this has been predictably focused on the ATC side: controllers getting a smarter picture, congestion predicted before it develops. That's real, but it's also not the whole story.

## The Part That Affects Flight Planning Directly

FAA Administrator Bryan Bedford told a House appropriations subcommittee on September 15 that SMART uses AI to predict congestion and conflicts earlier, "adjusting departure times, routes, and timing at designated points enroute." Those aren't abstract ATM outputs — those are the same variables sitting inside every airline's flight plan. Departure time adjustments, reroutes, and enroute timing constraints are precisely what dispatchers and pilots are working from when they file and brief.

SMART is designed to give air traffic managers a more comprehensive picture by combining airline schedules, weather forecasts, airport runway capacity, airspace restrictions, and other operational information. Rather than waiting until congestion has already disrupted flights, it's built to identify potential problems earlier and provide options for resolving them. That earlier identification window is where the cockpit angle becomes interesting. If SMART is generating route alternatives or departure time adjustments ahead of the gate, the downstream question is how quickly those recommendations propagate into the flight planning tools a crew is actually looking at during preflight.

SMART sits inside FMDS — the Flow Management Data and Services platform the FAA selected Air Space Intelligence to build. FMDS is the architectural layer that's supposed to modernize how traffic management data flows between the FAA and airline operations systems. The quality of that data feed, and how cleanly it interfaces with downstream flight planning software, is going to determine whether SMART's earlier-detection capability actually translates into better information on the flightdeck — or stays contained inside the ATCSCC.

When I think about where friction is most likely to surface in the first 90 days, I don't think it's concentrated at any single handoff point. A SMART-generated recommendation has to travel through several stages before it's actionable — a dispatch release update, an ACARS message, a revised clearance from ATC — and any one of those links can introduce latency or data loss. The honest answer is that all of them are candidates, and which one becomes the problem depends heavily on how each airline has wired its operations stack to receive data from FMDS.

## The 90-Day Trial as a Calibration Moment

Reports emerged of concerns from officials at three airlines who wanted to reduce the scope of the project with a "start, crawl, walk, run" approach, and that caution strikes me as reasonable integration prudence rather than airlines simply protecting existing workflow habits. Plugging a new predictive layer into the flow management stack without disrupting the data contracts that airline flight planning vendors rely on is genuinely hard, and the 90-day Washington trial is as much a test of that integration surface as it is a test of the AI. The hesitation reads less like resistance to change and more like organizations that have been through enough large-scale system deployments to know where the surprises tend to hide.

Airlines for America has hailed the advent of SMART as "one of the most exciting and bold initiatives taken on by the FAA in decades." That kind of enthusiasm is worth tempering slightly — not because the system isn't promising, but because the proof will be in what airline flight planning platforms can actually consume from it, and how quickly.

From time spent on the delivery side of aviation software programs, the pipeline between an ATM system's output and what appears in a flight planning tool is where the most implementation surprises tend to surface. The Washington trial starting today is the moment that pipeline gets its first real-world test.

## Sources
- [Airways Magazine](https://www.airwaysmag.com/new-post/faa-smart-first-deployment-washington)
- [Travel Tomorrow](https://traveltomorrow.com/faa-to-launch-new-smart-ai-system-to-help-manage-us-air-traffic/)
- [Aviation Today India](https://aviationtoday.in/air-traffic-controller/faa-set-to-trial-ai-powered-smart-system-to-predict-air-traffic-conflicts-and-congestion/)
- [YourNews](https://yournews.com/2026/09/21/7200221/faa-to-launch-ai-powered-air-traffic-management-system-in-washington/)
- [Archyde](https://www.archyde.com/faa-to-launch-ai-tool-to-manage-us-air-traffic-congestion/)
- [TravelPirates](https://www.travelpirates.com/captains-log/faa-ai-air-traffic-tool-washington-dc-airports)
