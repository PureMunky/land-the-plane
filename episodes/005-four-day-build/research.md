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


---

# SUPPLEMENT — the four-day cross-functional build reframe

(Episode is now: a cross-functional team — engineers AND non-engineers —
given four days and an agentic workflow to PROVE what can be built. No
scoreboard, no prize. Spine unchanged: agents do construction, so the only thing
tested is intent; the running demo is a "touch-and-go," plausible-by-
construction, not validated.)

## 1. Real (measured) data on non-engineers building — and the honest limit

- **63% of vibe-coding / AI-app-builder users are non-developers** — Vercel's
  *State of Vibe Coding* report, surfaced via Hostinger's 2026 stats roundup.
  Breakdown: UIs 44%, full-stack apps 20%, personal software 11%.
  <https://www.hostinger.com/blog/vibe-coding-statistics> (cites Vercel).
  **Honest limit to state on air:** this is a survey of people *already using v0
  / AI builders* — self-selected tool users, not a population sample. It shows
  the mix of who's inside the tent, NOT "63% of all software is now built by
  non-engineers." Don't let it become that.
- **Scale context (real, but old-style "citizen developer" framing):** estimates
  put no-code/low-code "citizen developers" at ~100M+ vs ~27.7M professional
  developers worldwide — directionally real, but these figures predate agents and
  conflate spreadsheet-style building with shipping software. Use as color, not
  proof. <https://www.hostinger.com/blog/ai-app-builder-statistics>
- **Qualitative, credible:** Anthropic's *2026 Agentic Coding Trends Report* —
  legal/design/ops "building data pipelines and workflow automation without
  engineering as a prerequisite." This is the cleanest source for the
  cross-functional claim. <https://resources.anthropic.com/2026-agentic-coding-trends-report>
- **Bottom line for the writer:** solid *measured* population-level adoption of
  non-engineers shipping production software does NOT exist yet. What exists is
  (a) vendor telemetry on tool-user mix (Vercel 63%) and (b) qualitative reports.
  Say that plainly; lean on the *four-day build as the proof-of-concept* rather
  than overclaiming a measured trend.

## 2. Multi-agent orchestration in practice (the "you orchestrate" shift)

- **Best named practitioner source: Addy Osmani.** "The Code Agent Orchestra —
  what makes multi-agent coding work" and "Conductors to Orchestrators: The
  Future of Agentic Coding" (O'Reilly Radar). Frame: the engineer's role moves
  from implementer to *orchestrator*; claims "three focused agents consistently
  outperform one generalist agent working three times as long" **[verify exact
  wording before quoting — snippet-derived]**.
  <https://addyosmani.com/blog/code-agent-orchestra/> ,
  <https://www.oreilly.com/radar/conductors-to-orchestrators-the-future-of-agentic-coding/>
- **Patterns vocabulary (useful for the build narrative):** sequential, parallel
  (fan-out/fan-in), hierarchical (manager + workers), handoff/routing, loop. The
  hierarchical "manager of agents" pattern is exactly the human-conducts-many
  posture the four-day team adopts. <https://www.augmentcode.com/guides/multi-agent-orchestration-architecture-guide>
- **Tie to the reframe:** orchestration is what makes a *mixed* team viable in
  four days — a PM can conduct agents on one slice while an engineer conducts
  agents on another. The human contribution is direction and judgment, not typing.

## 3. The prototype-to-production / "demo isn't done" gap (strengthens touch-and-go)

- **Strongest citable number: MIT's finding that only ~5% of GenAI pilots reach
  scale / production** across industries — the canonical "most prototypes never
  land" stat. Use this as the hard backbone of the touch-and-go act.
  (MIT NANDA "State of AI in Business" / GenAI Divide; widely cited 2025–26.)
  Reported via <https://venturebeat.com/data/the-last-mile-data-problem-is-stalling-enterprise-agentic-ai-golden> ;
  verify the exact 95%/5% phrasing against the MIT report before air.
- **Mechanism quotes (named, snippet-derived):** "the prototype that 'worked'
  often needs a massive rebuild before it can handle real users"; tech debt
  accrues faster than anyone can validate it.
  <https://hatchworks.com/blog/gendd/cost-of-vibe-coding/>
- **Security as the sharpest face of "plausible not validated":** GuardMint Q1
  2026 — 91.5% of 200+ vibe-coded apps had ≥1 vulnerability (flag: commercial,
  app-level prevalence); arXiv 2512.03262 "Is Vibe Coding Safe?" — >80% of
  *functionally correct* solutions carried exploitable vulns. The phrase to land:
  *functionally correct and still wrong.* <https://arxiv.org/abs/2512.03262>

## 4. Verification chores (results)

- **(a) Lahiri "plausible by construction... not correct by construction":**
  CONFIRMED in substance, NOT page-verified (arxiv/MSR blocked by egress policy
  this session). Search snippets render it as:
  > "LLM-generated code is plausible by construction—it looks right, compiles,
  > and often passes a few tests—but it is not correct by construction."
  Note: snippet uses *tight em-dashes* (no surrounding spaces). The MSR
  publication page (which DID load) carries only the abstract and does not
  contain this sentence. **Action: confirm dash/word fidelity against
  arXiv 2603.17150v1 from an unblocked network before reading verbatim.**
  <https://www.microsoft.com/en-us/research/publication/intent-formalization-a-grand-challenge-for-reliable-coding-in-the-age-of-ai-agents/>
- **(b) Willison URL + golden rule:**
  - "Vibe engineering" post — URL CONFIRMED, dated **7 Oct 2025**:
    <https://simonwillison.net/2025/Oct/7/vibe-engineering/>. He contrasts vibe
    coding ("fast, loose and irresponsible... no attention paid to how the code
    actually works") with vibe engineering (seasoned pros who "stay proudly and
    confidently accountable for the software they produce") **[snippet-only —
    verify wording]**.
  - Golden rule — from the earlier post "Not all AI-assisted programming is vibe
    coding," dated **19 Mar 2025**:
    <https://simonwillison.net/2025/Mar/19/vibe-coding/>. Your wording ("I won't
    commit any code to my repository if I couldn't explain exactly what it does
    to somebody else") matches third-person snippet paraphrases closely but is
    **not page-verified**. Confirm before quoting verbatim.

## A. Keep vs. swap, given the reframe

- **SWAP / DROP (competition framing now off-topic):**
  - The GitLab AI Hackathon beat (7,000 devs, $65K prizes, grand-prize winners)
    — leaderboard/prize energy. Drop, or demote to a one-line aside.
  - HackerRank "Orchestrate" (12,885 people, scored contest) and the "all 250
    judged projects" / vibe.yaps.gg scoreboard — pure competition. Drop.
  - "48-hour clock as built-in validator" framing from the old fresh-angle —
    rebuild around "four days, no scoreboard" (see B).
- **KEEP (reframe-neutral spine material):**
  - Lahiri intent-gap + "plausible vs correct by construction" — core.
  - Anthropic delegation gap (~60% AI use, 0–20% full delegation; ~27% net-new
    work) — supports "intent is what's left."
  - Willison vibe-coding vs vibe-engineering + golden rule — the practitioner
    "demo vs done" line.
  - Security data (GuardMint 91.5%, arXiv >80%) + MIT 5%-reach-scale — the
    touch-and-go evidence.
  - AWS "Udon Cat / vibe code securely" — keep ONLY reframed as "the format
    spawns its own verification tooling," not as a hackathon-winner story.
  - Project Aristotle (psychological safety) — fits BETTER now: a no-scoreboard,
    four-day cross-functional build is engineered psychological safety + flat
    authority. Promote it.

## B. One fresh fact the reframe opens up

Removing the scoreboard removes the only validator the old hackathon had left.
A competition still tested *something* real — relative ranking; a judge declared
a winner, which is a crude external validation signal. Strip the prize and the
clock-pressure, and a four-day agentic build has **zero** built-in validation: no
judge, and (because agents made "it runs" free) no construction barrier either.
What you're left with is the purest possible isolation of the intent variable —
the build *only* tests "did we know what was worth building and say it clearly?"
That's the gift and the trap in one: it's the cleanest intent laboratory
precisely because nothing else is being measured, which is exactly why every
output is a touch-and-go — plausible, unranked, unvalidated, and easy to mistake
for a landing. The competition framing hid this; "no scoreboard" makes the
missing validator impossible to ignore.
