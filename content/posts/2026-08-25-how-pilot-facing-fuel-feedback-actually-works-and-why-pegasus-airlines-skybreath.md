---
title: "How Pilot-Facing Fuel Feedback Actually Works — and Why Pegasus Airlines' SkyBreathe Deployment Is Worth Understanding"
date: 2026-08-25
tags: ["fuel efficiency", "flight ops", "efb", "sustainability"]
summary: "Pegasus Airlines' SkyBreathe MyFuelCoach deployment illustrates how pilot-facing fuel feedback tools work in practice — and why the crew engagement question matters as much as the data pipeline underneath it."
draft: false
---

There's a meaningful difference between a fuel-efficiency program that lives in the OCC and one that lives in a pilot's hands. The airline industry has spent years building the former — fleet-level optimization engines, route planners that shave kilograms off the planned uplift, dispatch systems that flag cost-index opportunities before departure. What's been slower to develop is the latter: tools that take that same data stream and route it back to the individual on the flightdeck who actually executes the flight.

OpenAirlines' SkyBreathe MyFuelCoach is one of the clearest current examples of that model in production. Pegasus Airlines, the Turkish low-cost carrier, presented its deployment at this year's EMEA Flight Operations IT Conference — and the mechanics of how that system actually works operationally are worth unpacking.

## The Data Loop the Pilot Actually Sees

The core premise of MyFuelCoach isn't optimization in the traditional sense. It doesn't change the flight plan or renegotiate cost index with the dispatcher. What it does is take actual post-flight performance data — comparing what the pilot did against what the plan called for — and translate that into personalized, readable feedback delivered directly to the crew. Think of it as closing the loop that fleet-level fuel analytics have always left open: the data arrives at the OCC, trends get reported in monthly reviews, and somewhere in between the insight and the cockpit, a lot of value dissipates.

SkyBreathe MyFuelCoach routes that insight to the pilot directly, framed in terms of their own flights rather than fleet averages. That distinction matters more than it might sound. Aggregate fuel reports tend to produce aggregate behavior; individualized feedback, when it's specific enough to be actionable, tends to produce different engagement entirely. Pegasus's presentation at the EMEA conference highlighted how the platform strengthened crew engagement and supported more consistent fuel-saving behaviors — which is a real outcome, not just a process improvement.

The data pipeline underneath this is worth understanding. Actual flight data — engine parameters, climb profiles, speed management adherence, APU usage — gets ingested after each flight and reconciled against the original flight plan. The system identifies where performance diverged, scores the flight against a set of fuel-saving techniques, and generates the crew-facing report. None of that is trivial to do at scale across a busy LCC operation, and it requires the kind of ACARS or flight data infrastructure that not every carrier has cleanly in place.

## What the Pegasus Deployment Reveals About Airline Adoption

Pegasus is an interesting operator for this kind of tool. As a high-frequency, point-to-point LCC with a relatively young and uniform fleet, it's exactly the operating environment where per-flight fuel savings stack up fastest and where crew engagement with fuel efficiency can be measured with statistical confidence across enough repetitions to be meaningful. That said, I'd actually expect long-haul carriers to see even greater benefit from pilot-facing coaching tools — longer sectors mean more opportunity to act on fuel-saving techniques mid-flight, and the per-flight savings potential is simply larger. The high-frequency LCC context is tractable, but the long-haul case may ultimately be more compelling.

What the deployment also illustrates is that airlines evaluating pilot-facing sustainability tools are making a distinct procurement decision from the one they make for fleet-level optimization software. The former requires buy-in from flight operations and from crew themselves; it's closer to a training and engagement program than a planning system, even though the underlying data is deeply technical. Getting that adoption right — framing the feedback in a way that feels useful rather than punitive, calibrating the benchmarks to account for factors outside pilot control like ATC routing or weather — is where these tools succeed or fail in practice.

Having spent time on both the product and delivery sides of flight ops software, I can say that crew engagement tends to be consistently underestimated at the procurement stage. It often gets treated as a change-management problem to solve after the contract is signed, rather than a design requirement baked in from the start. That's a mistake, because the data pipeline is genuinely the easier engineering problem. What's harder — and what determines whether the tool actually moves behavior — is designing feedback that a captain on their fourth turnaround of the day will read and act on. Engagement has to be designed in; it doesn't emerge on its own from a well-structured dataset.

## The Broader Trend This Points To

The Pegasus deployment isn't an isolated case — it reflects a broader pattern of airlines wanting sustainability accountability to exist at the crew level, not just the fleet level. Regulators and carbon reporting frameworks are increasingly asking airlines to demonstrate not just what their fleet burned, but what they did operationally to reduce it. Pilot-facing tools are one credible answer to that question, because they create an audit trail of engagement that fleet optimization software alone doesn't produce.

The more important question going forward is how these tools integrate with the broader EFB ecosystem. Right now, most pilot-facing fuel feedback lives in standalone apps or web portals — useful, but separated from the preflight and in-flight tools the crew is already working with. Integration is really what makes these tools real rather than supplementary. A pilot's fuel performance history visible in the same environment where they're reviewing the flight plan and checking NOTAMs — that's the architectural step that would produce genuine, durable adoption. A standalone app can deliver insight; an integrated one changes workflow, and workflow is where habits actually form.

## Sources
- [Aircraft Commerce / EMEA Flight Operations IT Conference — Pegasus Airlines / OpenAirlines SkyBreathe MyFuelCoach presentation](https://aircraftcommerceevents.com/event/2026-airline-aerospace-mro-flight-operations-it-conference-emea/)
- [OpenAirlines SkyBreathe MyFuelCoach product overview](https://www.openairlines.com/skybreathe-myfuelcoach)
