---
title: "At AIAA Aviation Forum, Airline and Avionics Leaders Show Where AI Is Actually Working — and Where It's Getting Stuck"
date: 2026-06-22
tags: ["ai", "airline operations", "flight ops", "dispatch"]
summary: "Reporting from the AIAA Aviation Forum published June 19, United Airlines, Collins Aerospace, and Reliable Robotics offered a ground-level view of where AI is already embedded in flight ops — and why systems integration, not algorithm maturity, is the real bottleneck."
draft: false
---

The AI-in-aviation conversation has been running hot at the conference circuit level for a couple of years now. Most of it is predictably abstract — frameworks, roadmaps, responsible-AI position papers. What was different about the session that closed out the AIAA Aviation Forum in San Diego last week — and reported on by *Aerospace America* on June 19 — was the degree to which the panelists spoke in specifics. United Airlines, Collins Aerospace, Reliable Robotics, and NASA weren't debating whether AI belonged in aviation. They were describing, in operational terms, where it's already running and what's actually slowing it down.

This is the kind of signal worth paying attention to right now.

## United's Framing: Integration Is the Problem, Not the Algorithm

<cite index="98-2,98-3">At the AIAA Aviation Forum in San Diego, aviation leaders focused on the practical question of how to introduce advanced analytics, automation, and autonomy into live operations — including airlines, new entrants, and future airspace — without breaking the complex system that already moves hundreds of thousands of people every day. Panelists from United Airlines, Reliable Robotics, Collins Aerospace, NASA, and the standards community focused on where AI and autonomy are already changing decision-making in the field and what it will take to certify, integrate, and trust these tools at scale.</cite>

<cite index="98-10,98-13">For United Airlines, AI is already embedded in daily operations, according to Roberta Zimmerman, United's director of Air Traffic Strategy, Data Analytics, and Strategic Vision. Zimmerman explained that United is using AI where it can reduce friction for customers and crew without taking over safety-critical decisions.</cite> <cite index="108-10,108-11">United is also applying AI to crew scheduling — a complex optimization problem shaped by increasingly intricate labor contracts. As Zimmerman put it, the airline is using AI to help translate contractual rules into scheduling logic that can support more effective crew planning.</cite>

That's a meaningful data point. Crew scheduling at a network carrier like United is one of the most computationally dense problems in airline operations — bid periods, reserve rules, FAR 117 fatigue regs, CBA constraints stacked on top of each other. If AI is genuinely helping translate those rules into scheduling logic rather than just surfacing optimization recommendations that dispatchers then have to second-guess, that's real operational value.

<cite index="98-21,98-22,98-23,98-24">For Zimmerman, the real barrier is systems integration, not the maturity of AI algorithms. She pointed to a seemingly trivial change — one airport identifier switch at Palm Beach International — as a massive internal lift. "We have such a vast display of capabilities in the NAS, and we're not going to change the infrastructure overnight," she said. "We are a system of systems, and something very small — the integration of that is a huge impact to make sure that there's no loss of continuity."</cite>

I've been in rooms where airline IT teams spend six months remapping a single airport code change across their OCC, dispatch, and EFB environments. She's right. The algorithms aren't the hard part anymore.

## Collins' Playbook: Start Low-Criticality, Earn Your Way Up

<cite index="58-15,58-16">Collins Aerospace is experimenting with lower-criticality applications like "Galley AI," which uses optical sensing and data to track inventory, open latches, and passenger needs in the cabin. The company deliberately clusters early AI deployments in low-criticality zones while it works through certification questions.</cite>

<cite index="58-18">Collins' innovation program manager Travis Klopfenstein described a shift in language away from "autonomy" toward "increasing automation" — with the goal of optimizing human decision-making rather than replacing it.</cite> He also flagged high-fidelity modeling and simulation — potentially using commercial game engines — as becoming essential not just for operations, but for the eventual certification pathway.

This staged approach is the only realistic one, and any supplier trying to shortcut it is going to get burned. The FAA and EASA aren't going to grant broad operational approvals for AI-driven functions based on a demo. You have to demonstrate the bounded failure modes, and you need simulation data at scale to do that. Collins is playing the long game correctly here.

## Reliable Robotics: Building Your Own Proving Ground

<cite index="58-10,58-11,58-12">Reliable Robotics operates Reliable Airlines, a Part 135 carrier based in Albuquerque that flies daily cargo routes for a major integrator. That airline will be the first operator of the automated system and a key design partner. Bringing pilots, maintainers, operators, and dispatchers into the design process has been "hugely fruitful," according to Reliable's VP of UAS Integration, Brandon Suarez.</cite>

This is a smart structural move that not enough aviation tech companies make. Building or operating your own airline to be the testbed for your automation stack gives you a feedback loop that no contracted pilot study or simulator run can replicate. You see the real edge cases — the weather deviations, the ATC reroutes, the weird MEL items at 2am in ABQ. That operational residency is what ultimately builds the evidentiary base for certification.

## What This Means Commercially

The picture that emerges from San Diego is nuanced but directionally clear: AI is no longer a future roadmap item at major carriers and tier-one avionics suppliers. It's running in production, scoped carefully to problems where the data is clean and the failure modes are tolerable. The bottleneck for the next phase isn't whether the models work — it's whether the underlying data architecture and system integration can support the next tier of applications.

For vendors pitching AI-powered flight planning, dispatch optimization, or crew decision support to airlines right now, that's the conversation you need to be ready for. Don't lead with the algorithm. Lead with how your integration story handles the airport code renaming edge case.

## Sources
- Aerospace America / AIAA Aviation Forum (published June 19, 2026)
