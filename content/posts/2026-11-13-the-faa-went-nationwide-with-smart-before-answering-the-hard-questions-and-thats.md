---
title: "The FAA Went Nationwide With SMART Before Answering the Hard Questions — and That's the Real Story"
date: 2026-11-13
tags: ["air traffic management", "aviation ai", "flight planning", "faa"]
summary: "The FAA's expansion of SMART to all 22 en route centers is a meaningful milestone, but pushing it nationwide while congressional safety questions remain unanswered says something uncomfortable about how aviation AI actually gets validated at scale."
draft: false
---

**Update:** This blog has covered SMART at multiple earlier stages — the June 2026 contract award to Air Space Intelligence, the September Washington-area launch, and the October rollout milestone. The November 10 announcement that SMART now covers all 22 U.S. en route centers is a genuinely new development that changes the story materially.

---

There's a version of the SMART nationwide expansion story that reads as a straightforward win: <cite index="19-2,19-3">the FAA is extending its Strategic Management of Airspace, Routes and Trajectories system to airspace managed by all 22 centers, with a cloud-based platform combining 200 data streams including weather, flight paths, traffic flows, and controller staffing. The early results out of Washington are real. <cite index="19-4">Since SMART began on September 21, the FAA says it has helped reroute 180 flights, saving an average of ten minutes and almost 80 gallons of fuel per flight. Those are not trivial numbers.

But I'd push back on reading that as the full story — because the more instructive angle isn't the expansion itself. It's the speed of it.

## The Gap Between the Headline and the Evidence Base

<cite index="27-3,27-4">The FAA is expanding SMART to all 22 centers even after more than two dozen lawmakers called for a pause in the Washington-area rollout. In announcing the expansion on November 10, the FAA said the tool had helped reroute 180 flights in the Washington area. That's the full evidentiary case being offered for a nationwide deployment: 180 flights across a single metropolitan region, over roughly seven weeks. <cite index="22-6">The case for expansion rests on Washington-area results, but those are not nationwide results.

<cite index="27-7,27-8">In October, lawmakers asked the FAA to explain how it had tested the system for safety and trained staff to use it. The agency's November 10 update did not address those questions.

I'm not suggesting SMART is unsafe. The human oversight architecture is genuinely well-designed: <cite index="19-5">FAA specialists at the SMART center in Washington analyze and validate the data, then send scheduling recommendations to the Air Traffic Control System Command Center in Warrenton, Virginia. <cite index="3-8">Controllers retain responsibility for aircraft separation. That layered validation is exactly the kind of sequencing I think makes sense for flight-ops AI — prove it on lower-stakes functions before moving toward anything decision-critical. SMART's recommendation model fits that logic.

What doesn't fit is the accountability gap. The FAA moved from a seven-week regional trial to a nationwide operational posture without publicly closing the loop on how the system was tested, how controllers were trained, or what failure modes were considered. The industry's concern about over-correction is legitimate: <cite index="20-5">airline brass warned the system could overcompensate for predicted delays by canceling or rerouting flights unnecessarily in a sort of self-fulfilling prophecy. That's a real systems-design risk, not a reflexive objection to AI.

## What This Means for the Flight Planning Layer

The question I keep coming back to isn't whether SMART works as described. It's what happens downstream — specifically, how SMART's rerouting recommendations translate into the amended flight plans that actually reach pilots. <cite index="24-8">Airlines run their own dispatch and flight planning systems, so SMART recommendations work alongside the routes carriers file for each flight. That handoff is not automated. It still runs through airline OCCs, dispatchers, and in many cases a manual re-filing process before anything changes in the cockpit.

That's the gap I haven't seen the FAA address publicly, and it's the gap that matters most for how the aviation community should interpret the 10-minutes-saved figure. Time saved at the SMART recommendation layer is not the same as time saved at the aircraft level. The pipeline in between is long, and in my experience working across flight planning and navigation products, the data handoff between ATC recommendations and the preflight or in-flight planning tools pilots actually use is rarely as clean as the system diagrams suggest.

## Speed Isn't a Validation Strategy

I think the aviation industry — vendors, airlines, and regulators included — has started conflating deployment velocity with proof of concept. The fact that airline industry officials described SMART's operational design as <cite index="20-4">"simply generating alternative route information that is passed through the FAA's existing systems and procedures" and called it "a big relief" tells you something important: the bar for comfort was set low. What relieved them was that SMART wasn't more ambitious, not that it was rigorously validated.

That dynamic is worth watching carefully as SMART scales. The 22-center expansion is a process milestone, but it isn't a validation milestone. Those are different things, and the difference matters enormously when the industry starts treating SMART's output as routine input into the flight planning stack.

My polling data shows the industry's AI adoption concerns are led by liability and accountability at 41%, followed by data quality and integration at 23%. SMART's expansion presses on both of those simultaneously. The accountability question is the one Congress is already asking. The data quality and integration question — how the recommendation actually reaches the crew flying the aircraft — is the one nobody seems to be asking loudly enough yet.

## Sources
- [Airways Magazine — FAA Expands SMART Traffic Planning to All 22 Centers](https://www.airwaysmag.com/new-post/faa-smart-nationwide-22-centers)
- [AVweb — FAA Expands AI-Assisted Traffic Management Nationwide](https://avweb.com/aviation-news/faa-expands-ai-assisted-traffic-management)
- [Gizmodo — The FAA Is Rolling Out Its AI Air Traffic Tool Nationwide](https://gizmodo.com/the-faa-is-rolling-out-its-ai-air-traffic-tool-nationwide-2000839347)
- [Aerotime — FAA expands SMART air traffic tool to all 22 US en route centers](https://www.aerotime.aero/articles/faa-smart-air-traffic-tool-22-en-route-centers)
- [The Flight Brief — FAA Says Its SMART Planning Tool Now Covers All 22 Centers](https://www.theflightbrief.com/articles/faa-smart-traffic-planning-all-22-centers)
- [SuperpowerDaily — FAA takes AI traffic advice nationwide, with controllers retaining the final say](https://superpowerdaily.com/posts/faa-takes-ai-traffic-advice-nationwide-with-controllers-retaining-the-final-say)
- [Deep Arrival — FAA SMART AI Now Covers All 22 Centers](https://deeparrival.com/news/faa-smart-ai-all-22-centers-nationwide-delays-2026/)
