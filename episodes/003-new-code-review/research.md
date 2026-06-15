# Research Brief: The New Shape of Code Review When the Agent Writes the First Draft

Scope note: All claims sourced. Several primary URLs (Anthropic, GitHub,
Pragmatic Engineer, Addy Osmani, Intercom) returned 403/Cloudflare blocks to
automated fetch; their figures are corroborated across multiple independent
secondary reports and are reliable, but pull longer verbatim quotes from a
browser before leaning hard on them. The widely-circulated "LinearB
4.6x/91%" cluster is **unverified** against any primary LinearB report —
cut it or hedge it.

---

## A. Current state (March–June 2026, with key earlier anchors)

**Code review is now explicitly the bottleneck — vendors are saying it out loud.**
- Anthropic shipped **Code Review for Claude Code** on **March 9, 2026**, and
  framed it directly: *"code review has become a bottleneck."* Internal data:
  after deploying it, the share of PRs getting **substantive review comments
  rose from 16% to 54%**, with engineers marking **fewer than 1% of findings
  as incorrect**. On PRs >1,000 lines, **84% get findings (avg 7.5 issues)**;
  on PRs <50 lines, only **31% (avg 0.5)**. It deliberately reviews for
  **correctness only** — logic errors, security, edge cases, regressions — and
  **ignores style/formatting by default**. Avg review ~20 min, ~$15–25/review.
  [claude.com/blog/code-review](https://claude.com/blog/code-review) ·
  [InfoQ](https://www.infoq.com/news/2026/04/claude-code-review/) ·
  [IT Pro](https://www.itpro.com/software/development/anthropic-says-code-review-has-become-a-bottleneck-this-new-claude-code-feature-aims-to-solve-that)
- **GitHub Copilot code review** passed **60 million reviews by March 2026**,
  up **10x** since its **April 2025** launch — now **more than 1 in 5 reviews
  on GitHub**. Surfaces actionable feedback in **71%** of reviews, stays silent
  in 29%, averaging **5.1 comments/review**. Moved to an **agentic
  architecture** that explores the repo and traces cross-file dependencies.
  [github.blog](https://github.blog/ai-and-ml/github-copilot/60-million-copilot-code-reviews-and-counting/)

**The volume/quality problem (use with care on methodology).**
- **CodeRabbit's "AI vs Human Code Generation" report**: AI-generated code
  introduces **~1.7x more issues** than human-written code. Vendor-published —
  directionally useful, flag the conflict of interest.
  [coderabbit.ai/blog](https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report)
- **GitClear 2025** (211M lines analyzed): copy/pasted (cloned) code rose
  **8.3% → 12.3%** (2021→2024), refactored code fell **25% → <10%**, and code
  "churned" (revised within 2 weeks) rose **3.1% → 5.7%**. The cleanest "AI is
  changing the *shape* of code, so review must change shape too" data point.
  [gitclear.com](https://www.gitclear.com/ai_assistant_code_quality_2025_research)
- **Jellyfish**: AI-assisted PRs are **~18% larger** — directly relevant
  because larger PRs defeat review (see SmartBear below).
  [jellyfish.co](https://jellyfish.co/blog/ai-assisted-pull-requests-are-18-larger/)
- **Caution flag:** the *"AI-generated PRs wait 4.6x longer, reviewers spend
  91% more time, fully-AI PRs went 1% → 27.6%"* cluster (attributed to
  "LinearB 2026 benchmarks") appears only in **secondary marketing blogs**. Not
  verified against a primary LinearB report — do not cite as fact.

**DORA 2025** (the institutional anchor): AI **amplifies** the system it's
dropped into. *"AI-generated code often passes code review… by the time you
notice the architectural rot, it's embedded throughout your codebase."* Their
thesis: AI doesn't replace review, it makes review **more critical** and
exposes weak review systems.
[dora.dev/dora-report-2025](https://dora.dev/dora-report-2025/) ·
[Swarmia summary](https://www.swarmia.com/blog/dora-2025-report-ai-readiness/)

**Practitioners worth quoting (named, ship in the space):**
- **Simon Willison** — estimates **~95% of the code he uses** is
  model-generated; openly admits he's **stopped reviewing every line** for
  routine tasks and asks whether shipping unreviewed code to production is
  "responsible." The honest tension, from a credible source.
  [simonwillison.net](https://simonwillison.net/tags/ai-assisted-programming/) ·
  [Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/when-ai-writes-almost-all-code-what)
- **Addy Osmani**, *"Code Review in the Age of AI"* — review shifts from
  line-by-line to intent/architecture.
  [addyo.substack.com](https://addyo.substack.com/p/code-review-in-the-age-of-ai)
- **Intercom**, *"AI is approving our pull requests: here's how we made it
  safe"* — a real team letting AI approve PRs with guardrails.
  [intercom.com](https://www.intercom.com/blog/ai-is-approving-our-pull-requests-heres-how-we-made-it-safe/)

**Skepticism / failure modes:**
- **GitHub's own AI-agent incident**: ~17M agent PRs, **five outages, a kill
  switch** — the review firehose has operational failure modes.
  [danilchenko.dev](https://www.danilchenko.dev/posts/2026-04-11-github-ai-agents-pull-requests/)
- The Register: *"AI-authored code needs more attention, contains worse bugs."*
  [theregister.com](https://www.theregister.com/2025/12/17/ai_code_bugs/)
- **Rubber-stamping** thesis: AI *"accelerates the rubber-stamp effect,
  creating the illusion of rigor while hollowing out collaborative learning"* —
  the loss of review-as-knowledge-transfer is the under-discussed cost.
  [Analyst's Corner / Medium](https://medium.com/analysts-corner/code-reviews-rubber-stamps-%EF%B8%8F-or-real-quality-gates-dab98cca0a81)

## B. Deeper-context concepts (the spine of the argument)

- **Egoless programming — Gerald Weinberg, *The Psychology of Computer
  Programming* (1971).** Review's whole point was the *group* finds defects,
  "ego" detached from the code. Connects to the ep-001/002 psychological-safety
  thread: review was always a social act, not a technical one.
  [Wikipedia](https://en.wikipedia.org/wiki/Egoless_programming)
- **Fagan Inspections — Michael Fagan, IBM (1976).** The original formal review
  found **38 defects/KLOC vs 8 for unit tests**, catching **82%** of total
  defects. The historical baseline that "modern code review" (lightweight,
  tool-based, ~2013) drifted away from — and that AI may be quietly pushing
  back toward.
  [graphite.com/blog](https://graphite.com/blog/the-ancient-origins-of-code-review)
- **SmartBear / Cisco study (2009, 2,500 reviews, 3.2M LOC).** Defect detection
  drops sharply **past 400 lines**; optimal is **200–400 LOC at <400 LOC/hour**,
  yielding **70–90%** defect detection. The killer juxtaposition: humans top
  out at ~400 lines, AI now drops **1,000-line PRs** on them.
  [smartbear PDF](https://static0.smartbear.co/support/media/resources/cc/book/code-review-cisco-case-study.pdf) ·
  [Mike Conley summary](https://mikeconley.ca/blog/2009/09/14/smart-bear-cisco-and-the-largest-study-on-code-review-ever/)
- **Automation bias / automation complacency — Parasuraman & Manzey (2010);
  aviation human-factors.** The documented tendency to under-monitor a trusted
  automated system and miss its failures. The *mechanism* behind LGTM
  rubber-stamping — a known, studied failure mode, not a new one.
  [Parasuraman & Manzey](https://journals.sagepub.com/doi/10.1177/0018720810376055) ·
  [Automation bias (Wikipedia)](https://en.wikipedia.org/wiki/Automation_bias)
- **METR (July 2025):** experienced OSS devs were **19% slower** with AI while
  *believing* they were 20% faster. The perception/reality gap that makes "I
  reviewed it" untrustworthy as self-report.
  [metr.org](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
- **Conway's Law** (optional): AI reviewers can't see org structure or the
  design decisions living in Slack and people's heads — the "business logic
  blindness" limit.

**Quotes worth using (verbatim, attributed):**
- Anthropic: *"code review has become a bottleneck."*
- DORA-adjacent: *"AI-generated code often passes code review… by the time you
  notice the architectural rot, it's embedded throughout your codebase."*
- On rubber-stamping: AI *"accelerates the rubber-stamp effect, creating the
  illusion of rigor while hollowing out collaborative learning."*

## C. The surprising / fresh angle

**AI didn't kill code review — it's quietly reviving the 1976 Fagan
inspection, and inverting who learns.** For a decade "modern code review" got
*lighter* (LGTM, drive-by approvals) because humans were the expensive, slow
part. Now the human is the *only* slow part, so the rigorous, defect-hunting,
multi-pass inspection is being rebuilt — but in silicon. The uncomfortable
corollary: classic review's *real* payload was **knowledge transfer** — the
junior learned by being reviewed, the team built shared mental models
(Weinberg's whole point). When the bug-finding moves to bots, the
**defect-detection survives but the learning loop is severed** — and *that*,
not bug count, is the loss that compounds. The reframe: the human's job in
review is no longer "find the bug" (the bot is better and tireless at that);
it's the one thing the bot structurally *cannot* do — **say out loud, to
another human, "I don't understand this, explain it,"** which is simultaneously
the only reliable defense against rubber-stamping *and* a vulnerability act
that only survives in psychologically-safe teams.

## Connective tissue (the spine)

Code review was never really about catching typos — it was a social act of
distributed understanding, and AI just stripped away the part we mistook for
the whole. The line-nitpicking that defined "modern code review" is now the
bot's job, and it's better at it; what's left for the human is the irreducible
core — intent, architecture, "should this exist," and *do I actually
understand what I'm approving.* But that core can only be exercised in a team
where admitting "I don't get this, walk me through it" is safe (ep 001) and
where the trust to ask is already built (ep 002). So the AI-review era doesn't
make psychological safety a nice-to-have — it makes it the **load-bearing
wall**, because the only failure mode AI review can't catch is a human silently
clicking LGTM on code no one in the room understands.
