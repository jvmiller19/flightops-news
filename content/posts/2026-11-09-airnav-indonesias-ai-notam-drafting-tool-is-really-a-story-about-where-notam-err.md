---
title: "AirNav Indonesia's AI NOTAM Drafting Tool Is Really a Story About Where NOTAM Errors Come From in the First Place"
date: 2026-11-09
tags: ["notam", "aviation ai", "flight planning", "apac aviation"]
summary: "Indonesia's air navigation service provider and Telkom University showcased an LLM-powered NOTAM drafting application at a USTDA international forum this week — and the upstream angle is more interesting than the AI headline."
draft: false
---

The conversation about AI and NOTAMs has largely focused on the consumption side: how do pilots and dispatchers make sense of dense, often cryptically formatted NOTAM text before a flight? That's a real problem, and there's been genuine momentum on that front from startups like Skymerse and from the FAA's own data infrastructure work. But there's a companion problem that gets almost no attention — and AirNav Indonesia just walked into an international forum this week and put it on the table.

<cite index="19-2,19-3">At the Aviation Safety and Security Reverse Trade Mission organized by USTDA, running from October 26 through November 6 in Arlington, Virginia, AirNav Indonesia introduced NOTAM-AI — an AI-based NOTAM drafting application developed jointly with Telkom University. <cite index="19-7">The collaboration combines operational aviation requirements with AI language technology. The underlying architecture is LLM-based: <cite index="24-2">the application accepts natural-language inputs and processes them into NOTAM format in compliance with ICAO standards.

The USTDA forum itself is worth noting as context. This is a US government trade development body convening aviation safety stakeholders from multiple countries — the fact that an Indonesian ANSP brought an AI-native internal tool to that stage signals something about where APAC aviation infrastructure is heading, even if the tool itself is still relatively early.

## The Upstream Problem Nobody Is Talking About

All the energy in the NOTAM-AI space has been directed at the reader's end of the problem: how do we help a pilot or dispatcher understand what a NOTAM actually means, filter out the noise, and carry relevant context from preflight into the flight itself? Those are legitimate challenges, and I think the work happening on that side is important.

But there's a reason NOTAM text is so hard to parse: a lot of it was drafted under time pressure, by humans working from manual templates, in a format that hasn't fundamentally changed since the teletype era. The ambiguity and inconsistency that AI comprehension tools are trying to decode didn't appear by accident — it was introduced at the authoring stage. <cite index="24-1">NOTAM drafting requires precision because the information must conform to international aviation formats and standards, and that conformance is something human authors get wrong with enough regularity that it creates systemic downstream noise for everyone receiving the data.

What AirNav Indonesia is proposing is intervention at the source. <cite index="20-5">The AI application understands natural-language input from the NOTAM originator and transforms it into an ICAO-compliant NOTAM format. If that works reliably, it doesn't just speed up the drafting process — it removes a category of downstream interpretation errors before they propagate across the global NOTAM network. That's a structurally different value proposition from what a comprehension tool offers.

## What Makes This More Than a Regional Curiosity

It's easy to file this under "interesting APAC experiment" and move on. I'd push back on that framing. <cite index="22-5,26-7,26-8">The collaboration between AirNav Indonesia and Telkom University has been underway since 2025, with a formal cooperation agreement and soft launch held at AirNav Indonesia's headquarters in Tangerang in July 2025. This isn't a proof-of-concept announced at a tradeshow — it's a working tool that an operational ANSP has been developing internally, now being introduced to an international audience for the first time.

The ICAO NOTAM reform agenda has been moving slowly for years, and the burden of compliance has largely fallen on the receiving end — the EFB platforms, the flight planning tools, the AI startups trying to make NOTAM text legible. What AirNav Indonesia's project represents, if it scales, is a different reform vector: address the quality problem at the point of origination, not just at the point of consumption. Those two approaches aren't mutually exclusive, but the industry has been almost exclusively investing in the second while largely ignoring the first.

From my own time working with flight planning and navigation data systems, the data quality problem always goes deeper than it looks. Improving how downstream tools interpret imperfect data is valuable, but it's inherently remedial work. If the signal coming out of the authoring system is cleaner to begin with, the entire stack benefits — EFBs, dispatch platforms, flight planning tools, everything that ingests NOTAM data as an operational input. That's the case AirNav Indonesia is implicitly making, and it's a more systemic argument than the press framing of "AI for aviation safety" quite captures.

## Sources
- [Selular.id — Telkom University dan AirNav Kembangkan NOTAM Berbasis AI untuk Penerbangan](https://selular.id/2026/11/telkom-university-dan-airnav-kembangkan-notam-berbasis-ai-untuk-penerbangan/)
- [Bisnis.com — Telkom University dan AirNav Kembangkan NOTAM Berbasis AI](https://market.bisnis.com/read/20261105/192/2018790/telkom-university-dan-airnav-kembangkan-notam-berbasis-ai)
- [iNews.id — Tingkatkan Akurasi Navigasi Penerbangan, Telkom University dan AirNav Kembangkan NOTAM AI di AS](https://www.inews.id/techno/telco/tingkatkan-akurasi-navigasi-penerbangan-telkom-university-dan-airnav-kembangkan-notam-ai-di-as)
- [IndoTelko — Telkom University dan AirNav kembangkan AI untuk penyusunan NOTAM](https://www.indotelko.com/read/1793882514/telkom-university-dan-airnav-kembangkan-ai-untuk-penyusunan-notam)
- [InfoEkonomi.id — Inovasi Anak Bangsa: Telkom University & AirNav Hadirkan Aplikasi Berbasis AI untuk Keselamatan Penerbangan](https://infoekonomi.id/2026/11/inovasi-anak-bangsa-telkom-university-airnav-hadirkan-aplikasi-berbasis-ai-untuk-keselamatan-penerbangan/)
- [InternationalMedia.id — Telkom University-AirNav Inovasi NOTAM Berbasis AI untuk Keselamatan Penerbangan](https://www.internationalmedia.id/2026/11/telkom-university-airnav-inovasi-notam.html)
