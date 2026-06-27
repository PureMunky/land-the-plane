# Research brief — Hackathons as the intent laboratory (Ep. 005)

Sourcing note: several primary hosts (arxiv, simonwillison.net, x.com,
Anthropic's resources site) were blocked to the fetcher this session, so a few
quotes are corroborated from search snippets, not character-verified against the
page. Each is flagged **[snippet-only]**. The Lahiri abstract and the hackathon
event facts below were retrieved verbatim. Verify any **[snippet-only]** quote
against the linked page before reading it on air.

## A. Current state (last ~3 months)

- **The agentic hackathon is now the default format.** GitLab's AI Hackathon ran
  Feb 9–Mar 25 2026, co-sponsored by Google Cloud and Anthropic, ~7,000
  developers, $65K prizes. Grand prize "LORE" used 8 agents + a router.
  Tagline: "You Orchestrate. AI Accelerates."
  <https://about.gitlab.com/blog/gitlab-ai-hackathon-2026-meet-the-winners/>
- **AWS AI Agent Hackathon (SF, Cybersecurity Awareness Month / late 2025):**
  "Over 250 developers gathered on a foggy autumn day... to build 50+ projects."
  Standout: "Udon Cat," a browser extension to "vibe code securely" by running
  Semgrep on LLM output *before it leaves the browser window* — i.e. the format
  itself is now producing verification tooling for its own output. Semgrep
  write-up, Nov 2025.
  <https://semgrep.dev/blog/2025/what-a-hackathon-reveals-about-ai-agent-trends-to-expect-2026/>
- **"Vibe coding" hackathons as their own genre.** The AI Vibe Coding Hackathon
  2026 published full judges' scores and AI analysis for **all 250 projects**
  (<https://vibe.yaps.gg/>). HackerRank's "Orchestrate" (May 2026): 12,885 people,
  48 countries, building AI support-triage agents in 24h
  (<https://www.hackerrank.com/blog/what-12885-developers-taught-us-about-building-with-ai/>).
  Calendar of upcoming ones: <https://vibecoding.app/events/hackathons>.
- **The shift from "can we build it" to "do we know what to build."** Anthropic's
  *2026 Agentic Coding Trends Report* (Jan 2026): developers use AI in **~60%**
  of work but can fully delegate only **0–20%** of tasks (the "delegation gap");
  **~27%** of AI-assisted work is tasks "that wouldn't have been done otherwise."
  Reported framing: "The bottleneck is no longer writing code — it's clarity
  about what to build" **[snippet-only]**.
  <https://resources.anthropic.com/2026-agentic-coding-trends-report>
- **Skepticism / failure mode (the sting in the tail).** Convergent evidence that
  agentic demos are plausible, not validated:
  - Q1 2026 GuardMint/Kingbird audit of 200+ vibe-coded apps: **183 (91.5%)** had
    ≥1 vulnerability traceable to AI hallucination or missing security context.
    Flag the methodology: commercial vendor, app-level prevalence (not line-rate),
    sampling criteria unpublished. Credibility is in the *convergence*, not this
    one number. <https://www.softwareseni.com/91-5-percent-of-vibe-coded-apps-have-vulnerabilities-and-what-the-q1-2026-research-actually-shows/>
  - Academic corroboration: *"Understanding the (In)Security of Vibe-Coded
    Applications,"* arXiv 2606.23130 (real-world corpus, Claude Code etc.);
    *"Is Vibe Coding Safe? Benchmarking Vulnerability of Agent-Generated Code,"*
    arXiv 2512.03262 — reports **>80% of functionally correct solutions** carried
    exploitable vulnerabilities. <https://arxiv.org/abs/2512.03262>
  - "The Real Cost of Vibe Coding": tech debt accrues faster because generation
    outpaces validation; "the prototype that 'worked' often needs a massive
    rebuild before it can handle real users."
    <https://hatchworks.com/blog/gendd/cost-of-vibe-coding/>

## B. Deeper-context concepts

- **Intent formalization (Lahiri, Microsoft Research RiSE, March 2026).** The
  spine of the episode's intellectual argument and the direct sequel hook.
  Verbatim from the abstract (verified on the MSR page):
  > "The gap between informal natural language requirements and precise program
  > behavior — the *intent gap* — has always plagued software engineering, but
  > AI-generated code amplifies it to an unprecedented scale."
  > "intent formalization — the translation of informal user intent into a set of
  > checkable formal specifications — is the key challenge that will determine
  > whether AI makes software more reliable or merely more abundant."
  And the validation point (verbatim): *"The central bottleneck is validating
  specifications: since there is no oracle for specification correctness other
  than the user..."* — this *is* your validation-vs-verification distinction:
  verification checks code against a spec; only the user can validate the spec.
  <https://www.microsoft.com/en-us/research/publication/intent-formalization-a-grand-challenge-for-reliable-coding-in-the-age-of-ai-agents/>
  The famous line **[snippet-only, verify before air]**:
  > "LLM-generated code is plausible by construction — it looks right, compiles,
  > and often passes a few tests — but it is not correct by construction."
- **Vibe coding vs. vibe engineering (Simon Willison, Oct 7 2025).** The line that
  separates "demo" from "done" at the practitioner level. **[snippet-only]**:
  > "Vibe coding is irresponsibly building software through dice rolls, not caring
  > what code is produced... I propose 'vibe engineering'!"
  His golden rule (earlier post, Mar 19 2025): *"I won't commit any code to my
  repository if I couldn't explain exactly what it does to somebody else."*
  <https://simonwillison.net/2025/Oct/7/vibe-engineering/>
- **Steve Yegge, the opposing take [snippet-only]:** "you can do 10 different
  spikes in an hour and you don't even have to be an engineer to do that" — and on
  done-ness: "How good are your tests? How good is your verification suite? Does
  it meet the customer's needs? That's all that matters." Good tension to stage
  against Willison. <https://steve-yegge.medium.com/the-future-of-coding-agents-e9451a84207c>
- **Project Aristotle (Google, 2012–2015).** The enabling-conditions thread, if
  you use it. Studied 180+ teams; **psychological safety** was the #1
  differentiator of effective teams — above individual talent, seniority, the
  "who." Ties cleanly: a hackathon manufactures psychological safety + flat
  authority by design, which is exactly the soil where speaking intent clearly
  becomes possible. <https://rework.withgoogle.com/intl/en/guides/understand-team-effectiveness>
- **Democratization, with honest limits.** Anthropic's report: legal, design, and
  ops teams "building data pipelines and workflow automation without engineering
  as a prerequisite"; the line between "people who code" and "people who don't"
  is "becoming more permeable." No hard adoption % for non-engineers could be
  confirmed — treat "anyone can build" as directional, not measured. Gartner's
  oft-cited "80% of tech products built outside IT by 2026" is a prediction, not
  an observation — flag it as such if used.
  <https://resources.anthropic.com/2026-agentic-coding-trends-report>

## C. The surprising / fresh angle

The hackathon was always a verification machine in disguise, and agents quietly
broke that. The classic 48-hour format had a built-in validator: the clock. If a
small team couldn't get the thing *working* by Sunday, the idea failed honestly,
in public, on stage. Building was hard, so "it runs" was real signal — a working
demo was earned evidence that the intent was buildable and roughly coherent.
Agents collapse the cost of "it runs" to near zero, which means a working demo no
longer certifies anything except that someone could describe it plausibly. The
hackathon didn't just get faster; it lost the one cheap test it used to apply for
free. Now the only scarce thing left in the room is knowing what's worth building
and saying it clearly — which is precisely Lahiri's intent gap, wearing a
lanyard. The fresh, slightly uncomfortable claim: the agentic hackathon is the
best laboratory we have for intent-driven work *and* a factory for
plausible-but-unvalidated demos, and those are the same fact, not two facts.

---

**Connective tissue.** One spine threads all of this: *agents removed
construction as the bottleneck, so the hackathon — the purest construction
contest we had — turns into a pure intent exercise.* What stays scarce is
upstream (knowing what to build, specifying it clearly) and the conditions that
let a group do that fast: psychological safety and flat authority (Aristotle).
What gets cheap and dangerous is "it runs," because a demo that's plausible by
construction is not correct, validated, or done (Lahiri's intent gap; the 91.5%
security data; Willison's "explain it to someone" line). The episode lands when
you let the listener feel the same move twice: the hackathon is the best
intent-laboratory we've ever had *because* it strips construction away — and that
same stripping is exactly what mass-produces demos that look finished and aren't.
