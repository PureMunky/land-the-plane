# Cleared to Land

*For five episodes the bottleneck has been climbing upstream. This week it arrives at the one place it can't climb past — intent, the single node in the whole pipeline with no machine oracle. When agents can build anything and check almost anything except whether it was the right thing, the job collapses to one thing: saying what you meant, well enough to be checked, and keeping the saying.*

*Published 2026-07-04. The audio version of this piece is
[Land the Plane episode 6](./episode.mp3); this post covers the same
ground for people who'd rather read.*

---

## This week on the radar

Four things — and all four are the same story from four angles, which almost never happens.

**Spec Kit grew up.** GitHub shipped
[Spec Kit 0.11.0 on June 16](https://github.com/github/spec-kit). If you haven't
looked since I mentioned it back in episode one, look again. The whole thing is a
loop — you write a **spec**, then a **plan**, then a **task list**, and only then
does the agent write code, each stage a plain Markdown artifact feeding the next
([docs](https://github.github.com/spec-kit/)). The news in this release is
*reach:* it now drives **30+ coding agents** from the same spec — Copilot, Claude
Code, Cursor, Gemini, Codex. The specification is now the portable thing; the
agent is the interchangeable thing. That's a complete inversion of how we've
thought about tooling for forty years, shipped as a point release like it was
nothing.

**Amazon's Kiro went GA — and tries to test your spec.**
[Kiro reached general availability on May 7](https://kiro.dev/blog/general-availability/),
replacing Amazon Q Developer. The detail that matters for the main piece: Kiro
doesn't just turn your spec into code, it generates
[property-based tests aimed at the *specification itself*](https://kiro.dev/docs/specs/)
— an attempt to build a machine that checks whether your spec holds together.
Somebody built a robot to grade the requirements. We're going to ask whether that
robot can possibly work.

**The honest counterweight: Tessl stalled.** [Tessl](https://tessl.io/) raised
~$125M on the purest version of the bet — spec is the source, code gets stamped
`// GENERATED FROM SPEC – DO NOT EDIT`. In January it
[quietly pivoted and rebranded](https://codemyspec.com/blog/tessl-review), and its
core framework reportedly still isn't GA after most of a year in private beta. I'm
not dunking — this is hard. But keep them in frame: the idea that intent is the
source of truth is shipping in some places and stalling in others. (Martin Fowler's
site now runs a
[three-tool comparison](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
of Kiro, Spec Kit, and Tessl — the establishment blessing that this is a real
category, not a slogan.)

**And the one underneath the other three.** In March, Shuvendu Lahiri at Microsoft
Research published a paper with the driest possible title —
[*Intent Formalization*](https://www.microsoft.com/en-us/research/publication/intent-formalization-a-grand-challenge-for-reliable-coding-in-the-age-of-ai-agents/)
([arXiv](https://arxiv.org/abs/2603.17150)) — containing the single most important
sentence I've read about our job this year: **"there is no oracle for specification
correctness other than the user."** Every other stage of building software, we're
learning to automate. We can generate the code. We can increasingly test the code.
But whether the specification *itself* was right — whether you asked for the
correct thing — Lahiri is telling you there's no machine that can answer that.
Only the person whose intent it was. That's not a tooling gap. It's a wall. This
whole episode is about what you do when you hit it.

---

## Cold open: the same desk, a year later

Put yourself back at the desk from episode one. Same engineer, same Tuesday
afternoon. The agent is working — reading files, proposing edits, running tests,
going again. A light on the keypad changes color: the agent has a question.

Something is different a year on, and notice exactly what. A year ago the engineer
watched the agent *type* and had that first uneasy thought — *the diff isn't the
artifact, the diff is the exhaust.* This year the engineer isn't watching the
typing at all. The typing is boring now. The agent writes the code, then writes
the tests, then a second agent reviews the first agent's code and files better
comments than most humans would. The whole machine hums without much help.

So what is the human actually doing in that chair?

Exactly one thing the machine never asks for help with: **deciding what correct
means.** Not whether the code matches the spec — a machine can check that now.
Whether the spec was *right.* Whether this feature should exist. Whether the edge
case the agent is cheerfully asking about should return an error or an empty list
— and which one a real customer at 2am actually needs. The agent can build either
one perfectly. It has no idea which is correct and never will, because *correct*
here doesn't live in the code. It lives in a human head, and it has to be spoken
out loud before anything downstream can be checked against it.

That's the chair. Everything the machine can grade, the machine is taking. What's
left is the one thing with no grader but you. For five episodes the bottleneck has
been climbing. This is the top of the stairs.

## The stairs run out

Let me collect the whole arc in one breath. Episode four was
[Goldratt](https://www.tocinstitute.org/theory-of-constraints.html): any system
has exactly one bottleneck, and speeding up a non-bottleneck accomplishes nothing
but piling inventory in front of the real constraint. Agents made *generation*
free, so the bottleneck moved upstream to *verification* — proving the code is
right. Episode five pushed one step further: in a four-day build, construction got
so cheap the constraint climbed past it to *intent* — knowing what's worth
building and being able to say it. And the demo at the end was a **touch-and-go:**
the wheels kissed the runway, nobody landed.

So: if the bottleneck keeps climbing — generation, verification, intent — where
does it *stop?* A constraint that just moves forever isn't a useful idea.

It stops at intent. And the reason is the most important thing I'll say today:
**the bottleneck stops climbing at intent because intent is the only node in the
entire pipeline with no oracle above it.**

That word is doing all the work. In testing, an *oracle* is the thing that tells
you whether an output is correct. A unit test is an oracle. A type checker is an
oracle. A human reviewer is an oracle. Every stage of building software checks
some output against some oracle: code against tests, tests against spec. And
here's the chain the industry is quietly building — you can check the tests
against the spec, and you can even (like Kiro) build a machine that checks the
spec against *itself* for consistency. Push the oracle up, and up, and up.

Then you reach the top. The spec is checked against — what? Against the *intent.*
Against what the person actually wanted. And there's no oracle there. No file, no
test, no model, no second agent holds the correct answer for what you *should have
wanted*, because that answer was never written down anywhere in the system. It
only ever existed in a human mind. Lahiri says it in one line: *there is no oracle
for specification correctness other than the user.* The staircase of automation
runs all the way up the building and the top step opens onto a room with no floor.
The user is the floor. There's nothing under them.

And this isn't new — it's the *oldest* known fact about our field, and we forgot it
because typing was loud enough to drown it out. Fred Brooks wrote it down in 1986,
in [*No Silver Bullet*](https://worrydream.com/refs/Brooks_1986_-_No_Silver_Bullet.pdf),
which every one of you should read this weekend. His forty-year-old line: **"The
hardest single part of building a software system is deciding precisely what to
build."** And then the knife: **"For the truth is, the client does not know what he
wants."** 1986. Before the web, before the cloud, before any of the tools we argue
about. The hardest part was always deciding what to build, and it was always hard
because the person asking couldn't fully say what they meant.

For forty years that truth was hidden, because deciding what to build was maybe 20%
of the pain and the other 80% was the brutal labor of construction. When most of
the work is typing, you experience software as a typing problem. Agents deleted the
80%. What got exposed — sitting there the whole time — was Brooks's 20%: the
deciding, the wanting, the saying, which never got easier and is now the entire
visible surface of the job. We didn't invent a new bottleneck. We power-washed
forty years of construction off the top of the oldest one.

That's why the stairs run out here. Not because we've run out of things to automate
below intent — we'll keep automating those for years — but because intent is where
the oracle goes missing, and a bottleneck at a node with no oracle can't be
relieved by a better machine. Only by a better human, saying a clearer thing.

## Everyone is building an oracle for the thing that can't have one

Here's what's fascinating about this exact moment. The whole industry has figured
out that intent is the constraint — you don't ship a spec-driven tool by accident.
And having figured that out, the industry is doing what engineers always do with a
constraint: trying to build a machine to beat it.

Look at what shipped. Spec Kit stages the work — spec, plan, tasks — so intent
gets pinned in writing before a line of code exists. Kiro generates tests against
your spec, trying to catch where it contradicts itself. Tessl bet the whole company
on generating code straight from the spec and treating the code as disposable. And
the intellectual engine under all of it is a talk OpenAI's **Sean Grove** gave last
year,
[*The New Code*](https://the-decoder.com/code-is-just-a-lossy-projection-of-intent-according-to-openai-researcher-sean-grove/).
Grove's framing is the sharpest going: **code is just a lossy projection of
intent.** The intent is the real thing; the code is a lossy compression of it — you
can't recover the full intent by reading the code, the way you can't recover a raw
photo from a JPEG. And the line that should be tattooed on the industry: keeping the
generated code while throwing away the prompt is
[*"like you shred the source and then very carefully version control the binary"*](https://lawwu.github.io/transcripts/8rABwKRsec4.html).

He's right. That's exactly what most teams do. The prompt — the actual source, the
statement of intent — evaporates the moment the code appears, and then we lovingly
commit the code, which is the *build output.* Spec Kit and Kiro and Tessl are all,
in their different ways, attempts to stop shredding the source. That's good. I'm
for all of it.

But watch the top of every one of those tools, because it's the same thing every
time, and it's the tell. Kiro generates tests for your spec — checking that it's
*consistent,* that you didn't say blue in one place and green in another. That's
real, useful **verification:** did we write the spec right. It's structurally
incapable of telling you whether blue was the *correct* color. A perfectly
consistent spec for the wrong product is still the wrong product, and it passes
every property test Kiro can generate, cleanly, forever. The machine can make your
spec *precise.* It cannot make it *correct,* because correct is measured against
something not in the spec — what you actually wanted — the one thing with no oracle.

This is the inversion at the center of the piece. Every one of these tools pushes
the oracle upward — check the code, then the tests, then the spec — and every one,
at the very top, terminates at a human saying *yes, that's what I meant.* You can
formally verify a specification against itself until the heat death of the universe
and never once learn whether the spec was right. **Precision is not correctness.
Verification is not validation.** The tools are spectacular at the first word of
each pair and can do *nothing* about the second.

And the skeptics are right about the failure mode. There's a sharp piece from
Arcturus Labs,
[*Why Spec-Driven Development Breaks at Scale*](http://arcturus-labs.com/blog/2025/10/17/why-spec-driven-development-breaks-at-scale-and-how-to-fix-it/):
a big spec is written in natural language, natural language is imprecise, so a big
spec inherits all the ambiguity of the English it's made of. You haven't escaped
the problem — you've *moved* it. Instead of underspecified code you now have an
underspecified spec, and the agent fills every gap with a plausible guess. The
button with no specified color comes out green today, red tomorrow — both perfectly
valid completions of what you *didn't say.* The formalization burden didn't vanish;
it relocated upstream, to you. Somebody has to decide the button is blue. There's
no one else in the building who can.

And a sharper needle still: this shiny "new paradigm" — write the requirements
carefully first, then build from them — [has a name](https://eu.36kr.com/en/p/3388182127870345).
We used to call it **waterfall.** We spent twenty years learning why it fails —
because you can't know the requirements up front, because building the thing is how
you discover what you wanted, because the client *doesn't know what he wants.*
Spec-driven development done badly is just waterfall with an agent playing the
offshore team that builds exactly what the document said and none of what you meant.

So the spec-driven turn is real and good and *also* walking back toward a wall we
already hit once. The way through — the hinge of the episode — is to stop treating
the spec as a document you write once at the top, and start treating intent as a
living thing you capture continuously.

## The one artifact that is yours

The freshest idea I found this week is small and concrete and points exactly the
right way. In March, Ivan Stetsenko published
[*Lore*](https://arxiv.org/abs/2603.15566), which repurposes git commit messages —
structured trailers — to store the reasoning behind a change so any agent can query
it later. The mechanism is almost aggressively simple. The *concept* is the keeper:
he names the **decision shadow** — everything real about a decision that the diff
throws away. The constraints you worked under. The alternatives you considered and
rejected. The forward-looking context — why you built it loose *here* because you
know a second use case lands next quarter. The diff records *what* changed; the
decision shadow is *why,* and the why is exactly what the diff can't hold.

This is the intent layer I described in episode one, finally showing up as a running
implementation — early and small, but the shape is dead right, and here's why it
matters more than any spec tool. **A spec is a snapshot.** It captures your intent
at the moment you wrote it — the top of the work, which is precisely when you
understand the problem *least,* because you haven't built anything yet. The decision
shadow is captured *continuously,* including at 3pm Thursday when a customer said
something offhand that turned out to be load-bearing and you pivoted the whole
design. That pivot is the single most valuable piece of intent in the project, and
there's no field for it in your spec, no line for it in your diff, and in almost
every team on earth it lives in exactly one place: a Slack thread unfindable in a
month and a human memory gone in six.

So here's the claim, the payoff of the whole arc. In the agentic era, **the captured
intent — the spec plus the decision shadow, the whole living record of what you were
trying to do and why and what you ruled out — is the one artifact that is uniquely,
irreducibly yours.** Think about what the machine has taken: the typing, the
testing, the reviewing, the refactoring, the migrations. Every artifact in your
repo that can be checked against an oracle is being absorbed, because the machine is
very good at everything *with* an oracle. What's left is the node *without* one. The
intent. Which means captured intent isn't documentation anymore — it's the actual
product of your labor. The code is the exhaust. It always was; we just couldn't see
it while we made it by hand.

This reframes the job cleanly, into three verbs. **Specify. Capture. Validate.**

**Specify** is the front. It's Grove's point — the person who communicates most
effectively is becoming the most valuable programmer. Not who types fastest; who can
take a fuzzy human want and sharpen it into something precise enough that an agent
builds the right thing *and* a test can check it. Genuinely hard, genuinely
learnable, and a different skill than the one most of us built careers on. Closer to
writing than typing. Closer to interviewing a stakeholder than closing a ticket.

**Capture** is the middle, and almost everyone skips it. Say the thing, then *keep
the saying.* Don't shred the source and version-control the binary. When you make a
decision, record the shadow — the alternatives, the constraint, the pivot — not in
your head, not in Slack, but in something durable that sits next to the code and
travels with it. This is the boring infrastructural work nobody gets promoted for,
and within a couple of years it will separate the teams that still understand their
own systems from the teams drowning in plausible code no living person can explain.

**Validate** is the top, and it has no shortcut, because there's no oracle but you.
It's the human act of looking at what came out and asking not *did we build it
right* — a machine can answer that — but *did we build the right thing.* That
question has no test and never will;
[Lahiri proved it in a sentence](https://www.microsoft.com/en-us/research/publication/intent-formalization-a-grand-challenge-for-reliable-coding-in-the-age-of-ai-agents/).
It routes through exactly one instrument: a human with judgment and context and skin
in the game, saying *yes, that's what I meant,* or *no, try again.* When people ask
what's left for engineers once agents can build anything — that's the answer. The
thing with no oracle. The
[final approach only a human can fly](https://www.scrum.org/resources/blog/doing-right-thing-right-validation-and-verification).

And here's the sharpest objection, because it's the right one: if specifying intent
is the whole job now, can't the agent do *that* too? Partly yes — and it's coming
fast. Point an agent at your usage data, your mission, and a pile of industry
research and it'll cheerfully generate twenty things you could build next — some
sharp, some things no human in the room would've thought of. But notice what it
produced: **candidates.** It flooded the top of the funnel with *plausible* intent.
It did not — cannot — tell you which of the twenty is the *right* one to build,
because that's a validation question, and validation has no oracle but you. An agent
that generates a hundred ideas doesn't shrink your job. It takes the one thing only
you can do — *choosing, and being able to say why* — and makes it the whole thing.

**The thesis, plainly:** for five episodes the bottleneck climbed — generation,
verification, intent — and here it stops, permanently, because intent is the one
node no machine can grade. The whole industry is racing to build an oracle for it
and will fail, not for lack of trying but because the thing is ungradable by
anything but the user. So the job isn't to build the oracle. **The job is to become
the oracle — and to leave a record of your rulings so the next person can find
them.** Specify the intent, capture the intent, validate against the intent. The
captured intent is the artifact. The code was always just the way it used to be
expensive to make one.

That's what it takes to land the plane. Not a green build. Not a clean demo. A human
in the tower saying *yes — that's where it was always supposed to go. Bring it
down.*

## What to do this week

Three things, mapped to the three verbs so they're easy to remember.

1. **Specify one thing, on purpose, before an agent touches it.** Pick a real task
   and write the intent down first — not a ticket, a *specification:* what it must
   do, what it must never do, and the hardest sentence of all, *how you'd know it
   worked.* If you can't write that last sentence, you've learned the most important
   thing you could: you don't understand the problem yet, and no amount of agent
   horsepower was going to save you from that. The blank space where the acceptance
   criteria go is the real state of your understanding. Look at it honestly before
   you build.

2. **Capture one decision shadow.** Just one, to feel the muscle. Next time you make
   a real call — picked this approach over that one, built it loose because a second
   use case is coming, ruled out the obvious design for a non-obvious reason — write
   the *why.* The alternatives and why you rejected them. Put it somewhere that
   travels with the code; the commit message is a fine place to start, which is the
   whole point of [Lore](https://arxiv.org/abs/2603.15566). You're not building a
   system, you're planting the idea that the reasoning is worth more than the diff —
   because it is. In a year you'll wish you had a hundred of these; be glad you
   started with one.

3. **Validate — don't outsource the ruling to plausibility.** This week an agent
   will hand you something that looks completely finished. It runs, it's clean, it
   passes its own tests, and you'll feel the pull to accept it because it's plausible
   and you're busy and the machine seems so sure. Stop and ask the one question the
   machine can't ask itself: *is this the right thing* — not *is this a working
   thing.* You are the oracle; there is no other one. That's not a burden, it's the
   job surviving. In a world where the machine can build anything, the person who can
   say what's worth building — and mean it, and prove they meant it — isn't obsolete.
   That person is the only one who was never replaceable.

Go back to the desk. The agent is working. The light changes color, because it has a
question. And underneath every question it will ever ask you is the same one: *is
this what you meant?* You're the only thing in the entire system that can answer.
That was always true. It used to be buried under a mountain of typing. The typing is
gone now — and there it is, bare, and yours, and the whole job.

---

## Sign-off

That's episode six — the one the last five were walking toward. Psychological
safety, the people, the review, the verification bottleneck, the four-day
touch-and-go: each was the constraint climbing one more stair, and this week it
reached the top and stopped at the one place it can't climb past. Intent. The node
with no oracle. The only cargo that was ever really yours to carry.

Where we go next is the strangest turn yet: if the machine can build anything and
the job that's left is deciding what's *worth* building, then the next place we point
the agents is at that very question — feed them the usage data, the mission, the
industry research, and let them surface candidate ideas for the humans to weigh.
Agents at the *front* of the funnel, generating the intent instead of just executing
it. It sounds like it breaks everything I said today; I think it does the opposite —
it makes the human oracle matter *more.* Until then — specify the thing, capture the
why, and when the machine asks if this is what you meant, *answer.*

---

## Sources

- GitHub Spec Kit (0.11.0, June 16 2026) — https://github.com/github/spec-kit · docs: https://github.github.com/spec-kit/
- AWS Kiro — general availability (May 7 2026) — https://kiro.dev/blog/general-availability/ · specs & property-based testing: https://kiro.dev/docs/specs/
- Tessl — https://tessl.io/ · pivot/review (self-selected commercial review; treat as directional) — https://codemyspec.com/blog/tessl-review
- Martin Fowler — spec-driven development, three-tool comparison (Kiro/Spec Kit/Tessl) — https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- Shuvendu Lahiri (Microsoft Research) — "Intent Formalization: A Grand Challenge for Reliable Coding in the Age of AI Agents" (March 2026; "no oracle for specification correctness other than the user") — https://www.microsoft.com/en-us/research/publication/intent-formalization-a-grand-challenge-for-reliable-coding-in-the-age-of-ai-agents/ · arXiv: https://arxiv.org/abs/2603.17150
- Sean Grove (OpenAI) — "The New Code" ("code is just a lossy projection of intent"; "shred the source and version control the binary") — https://the-decoder.com/code-is-just-a-lossy-projection-of-intent-according-to-openai-researcher-sean-grove/ · transcript: https://lawwu.github.io/transcripts/8rABwKRsec4.html
- Fred Brooks — "No Silver Bullet" (1986; "the hardest single part… is deciding precisely what to build") — https://worrydream.com/refs/Brooks_1986_-_No_Silver_Bullet.pdf
- Ivan Stetsenko — "Lore: Repurposing Git Commit Messages as a Structured Knowledge Protocol for AI Coding Agents" (March 2026; the "decision shadow") — https://arxiv.org/abs/2603.15566
- Arcturus Labs — "Why Spec-Driven Development Breaks at Scale" — http://arcturus-labs.com/blog/2025/10/17/why-spec-driven-development-breaks-at-scale-and-how-to-fix-it/
- 36Kr — spec-driven development as "the return of waterfall" — https://eu.36kr.com/en/p/3388182127870345
- Simon Willison — agentic engineering patterns / tests-as-specification (Feb 2026) — https://simonw.substack.com/p/agentic-engineering-patterns
- Andrej Karpathy — "Software 3.0" (YC AI Startup School, June 17 2025) — https://www.latent.space/p/s3 · "the hottest new programming language is English" (Jan 2023) — https://x.com/karpathy/status/1617979122625712128
- Goldratt — Theory of Constraints — https://www.tocinstitute.org/theory-of-constraints.html
- Verification vs. validation — https://www.scrum.org/resources/blog/doing-right-thing-right-validation-and-verification
</content>
