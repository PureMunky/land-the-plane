# Pilot Monitoring

*When the agent writes the first draft, your job stops being to fly the plane and starts being to watch the instruments — and watching is the harder job.*

*Published 2026-06-13. The audio version of this piece is
[Land the Plane episode 3](./episode.mp3); this post covers the same
ground for people who'd rather read.*

---

## This week on the radar

Four things from the last little while.

**The vendors are saying the quiet part out loud: review is the bottleneck.**
In March, Anthropic shipped
[code review inside Claude Code](https://claude.com/blog/code-review), and the
framing is the whole reason for this piece: *"code review has become a
bottleneck."* The company building the thing that writes the code is telling
you the slow part is now the looking-at-it part. And they put numbers on it:
after turning it on internally, the share of pull requests getting a
substantive review comment went from **16% to 54%**
([InfoQ](https://www.infoq.com/news/2026/04/claude-code-review/)). Read that
honestly — before the bot, nearly five out of six PRs were waved through with
nobody saying anything real. That was the *baseline*. That's the quiet scandal
under this whole topic.

**More than one in five reviews on GitHub are now done by a machine.**
GitHub says Copilot code review crossed
[60 million reviews by March 2026](https://github.blog/ai-and-ml/github-copilot/60-million-copilot-code-reviews-and-counting/),
up ~10x in under a year, and now accounts for more than **one in five** code
reviews on the platform — averaging 5.1 comments per review. So if you picture
"the reviewer" as a person, update the picture. Increasingly the first
reviewer — sometimes the only one — is a model. The machine writes the draft,
a different machine reviews it, and somewhere at the end there's supposed to be
a human.

**DORA: AI doesn't fix or break your system — it amplifies it.** The
[DORA 2025 report](https://dora.dev/dora-report-2025/) has the line I can't
stop quoting: AI-generated code often passes code review just fine, and *"by
the time you notice the architectural rot, it's embedded throughout your
codebase"*
([Swarmia summary](https://www.swarmia.com/blog/dora-2025-report-ai-readiness/)).
*Passes review.* That's the trap in one sentence. The code doesn't fail loudly
at the gate. It fails quietly, months later, everywhere at once.

**The honest counterweight.**
[Simon Willison](https://simonwillison.net/tags/ai-assisted-programming/) — as
credible a working voice as exists — has said openly that ~95% of the code he
uses is model-generated, that for routine tasks he's stopped reviewing every
line, and he asks the uncomfortable question: is it even *responsible* to ship
code you haven't fully read
([Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/when-ai-writes-almost-all-code-what))?
I want to honor that tension, not pretend it away. Because the answer the
industry is quietly converging on is: *we're going to ship code no single human
has fully read.* That's not hypothetical. That's Tuesday. The question is what
we do about it.

---

## Cold open: the button at 4:50 on a Friday

It's 4:50 on a Friday. One pull request between you and the weekend. You open
it. Fourteen hundred lines. The agent wrote all of it on Wednesday — you kicked
off the run, went to a meeting, and it came back with a service that, by every
signal on the screen, works. Tests green. Linter happy. The robot reviewer left
five comments and they all got addressed. CI is a wall of checkmarks. By every
dashboard: done.

And your cursor is hovering over the green **Approve** button.

Be honest about the next ten seconds. Are you going to read fourteen hundred
lines at 4:50 on a Friday? You're not. You'll scroll, let your eye snag on a
function name you recognize, nod, scroll more, see the tests are green, see the
bot already looked — and click. And it'll be fine. It's almost always fine.
That's exactly what makes it dangerous.

Here's what just happened, in the language of a different industry. You didn't
*fly* that plane — the autopilot did. Your job, in that moment, was to *monitor*
the autopilot: to be the human who notices when the confident, tireless,
usually-correct machine is confidently, tirelessly wrong. And there's a whole
field of research — paid for in actual wreckage — about what happens to people
in that seat. The seat where the machine does the work and the human is just
supposed to watch.

It turns out we're terrible at it. Not because we're lazy — because of how
attention works. When a system is right ninety-nine times, the human stops
truly checking on the hundredth. The watching decays into the *feeling* of
watching. And the whole safety case quietly comes to rest on a person who's no
longer really there.

That's the seat you're in when you review agent-written code. This piece is
about how to actually sit in it.

---

## Review was never about the typos

Kill an assumption first, because everything depends on it.

When you picture code review, you picture *catching things*: a missing null
check, an off-by-one, a confusing name. The line-by-line hunt for the defect.
That's what most of us mean by review, what most tools optimized for, and what
we spent fifteen years making lighter and more drive-by. LGTM. Approve. Move
on.

Here's the thing: that version of review — the defect hunt — is the part the
machine is now genuinely *better at than you*.

The Anthropic numbers are specific in a way that matters. On PRs over a
thousand lines, their reviewer found issues **84%** of the time, ~7.5 per
change; on PRs under fifty lines it spoke up only **31%** of the time. It scales
attention with risk. And engineers marked **fewer than 1%** of its findings as
incorrect. A tireless reviewer that reads every line of a 1,400-line change at
4:50 on a Friday without getting bored or hungry or having a weekend to get to.
On the narrow task of finding the defect in the diff, you won't beat that — and
you should stop trying.

And this isn't new. It's a *return*. In 1976, Michael Fagan at IBM formalized
the [software inspection](https://graphite.com/blog/the-ancient-origins-of-code-review):
a rigorous, slow, multi-person, multi-pass read with defined roles. It worked
extraordinarily well — Fagan inspections caught on the order of **82%** of
defects, far more per thousand lines than testing. Then we mostly *stopped*,
because humans were the expensive, slow part, and we spent two decades making
review lighter to get them out of the bottleneck. We went from the Fagan
inspection to the GitHub thumbs-up, and called the lightweight thing "modern
code review."

Now the rigorous, every-line inspection is coming back — rebuilt in silicon.
What Anthropic and GitHub shipped isn't really new; it's the Fagan inspection
reborn as a machine that doesn't get tired. We're getting 1976's rigor back, for
free, exactly when we'd lost the ability to provide it ourselves. That's
genuinely good news. Say it plainly before complicating it.

So if the bot has taken back the defect hunt, what's review *for* now?

The answer is the thing that was always underneath the typo-catching. Go back to
1971: Gerald Weinberg, *The Psychology of Computer Programming*, and the idea of
[egoless programming](https://en.wikipedia.org/wiki/Egoless_programming). His
actual point — the one we flattened into etiquette — was that the value of
review was *social*. The group developed a shared understanding of the code. No
one person was the only one who knew how a thing worked. The defects were real,
but the deeper product was **distributed understanding**: a team that had all
looked at the thing, argued about it, and now carried a shared model of it
around in their heads.

That's what review was for. Not the typo. The typo was the *occasion*. The
understanding was the *point*. We never had to separate them, because the same
act produced both — you read the code line by line and caught the bug and built
the understanding in one motion.

The agent just pulled those two apart. It took the defect hunt and does it
better than you. It left you holding the other half: the understanding. Which it
*cannot* do for you, no matter how good it gets, because the understanding has
to live in a human head to be worth anything. The whole point of it is that a
person has it.

So: code review was never really about the typos. It was about a team of humans
understanding their own system. The machine took the typos. You still have to do
the understanding. And almost nobody has reorganized their idea of review around
that split yet.

---

## The seat we're bad at sitting in

The human's job is shifting from catching the bug to understanding the change.
The problem: the seat where you watch a machine work and stay sharp enough to
catch it when it's wrong is a seat human beings are *measurably, predictably
bad at sitting in.* We've known it for decades — just not in our industry.

The term is **automation complacency** (or automation bias). The foundational
synthesis is
[Parasuraman & Manzey (2010)](https://journals.sagepub.com/doi/10.1177/0018720810376055),
pulling together human-factors work, much of it from aviation. The finding is
brutally consistent: give a person a reliable automated system to monitor, and
they monitor it *less.* Not because they're told to relax — because reliability
itself breeds complacency. The better the autopilot, the less the human watches,
so the rare moment it's wrong is precisely the moment the human has checked out.
The system's strength *manufactures* the human's weakness. You can't have a
highly reliable automated partner and an alert human monitor for free; the
alertness has to be actively, unnaturally maintained against the grain of how
attention works.

That's the science of the 4:50-on-Friday Approve button. It's not a character
flaw. You're a normal human exhibiting a documented response to a reliable
machine — working properly toward a catastrophe, because the one time in fifty
that it matters is the one time you're not looking.

And you can't even trust your *own* sense of how carefully you looked. That's
the [METR study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
from July 2025: experienced open-source developers using AI *believed* they were
~20% faster. They were actually ~19% *slower* — wrong about their own experience
by nearly forty points. Now sit that next to review. If you can't trust an
engineer's gut about whether AI made them faster, why trust their gut about
"yeah, I reviewed it, it's fine"? *I reviewed it* is not data. It's a feeling.
And the feeling is exactly what complacency corrupts first.

Now the shape of the work. [GitClear](https://www.gitclear.com/ai_assistant_code_quality_2025_research)
looked at ~211 million lines: cloned (copy-pasted) code is up (8.3% → 12.3%),
refactoring is sharply down (25% → under 10%), and churn — code rewritten within
two weeks — is up (3.1% → 5.7%). More code, more duplication, thrown away
faster. And [AI-assisted PRs run ~18% larger](https://jellyfish.co/blog/ai-assisted-pull-requests-are-18-larger/).

Here's where a thirty-year-old number becomes the most relevant fact in this
whole piece. In 2009, the
[SmartBear/Cisco study](https://static0.smartbear.co/support/media/resources/cc/book/code-review-cisco-case-study.pdf) —
2,500 reviews, millions of lines, for a long time the largest ever — found that
human defect detection falls off a cliff past about **400 lines**. The sweet
spot is 200–400 lines, reviewed slowly
([summary](https://mikeconley.ca/blog/2009/09/14/smart-bear-cisco-and-the-largest-study-on-code-review-ever/)).
Four hundred lines is roughly the ceiling of what a person can review *well.*

Put the two facts in one sentence. Humans top out, on a good day, around 400
lines. The agent routinely drops 1,400-line changes on you. We've built a
pipeline that generates work in exactly the size and shape human review is
known — measured, since 2009 — to be worst at. We didn't just speed up the
writing; we sped it up into a form factor that *defeats the reading.* A
thousand-line PR isn't one review. Functionally it's a defect-laundering
machine, because everyone knows nobody's really reading all of it, and the green
button gets pressed anyway.

That's the DORA warning made mechanical: the code passes review not because it's
good but because the review, at that size and speed and level of complacency,
*isn't actually happening.* It's being performed. The practitioner writing has a
phrase for it I think is exactly right — AI
[*"accelerates the rubber-stamp effect, creating the illusion of rigor while
hollowing out collaborative learning."*](https://medium.com/analysts-corner/code-reviews-rubber-stamps-%EF%B8%8F-or-real-quality-gates-dab98cca0a81)
The **illusion of rigor**: green checks, a bot's five comments, an Approve from
a human who scrolled. It has the complete outward form of rigor. And underneath,
no human understands the change. It doesn't announce itself, because everything
about it looks like success.

---

## The one thing the machine cannot do

If you're slightly worried now, good — but worry without a move is just anxiety.
Here's the move.

If the bot catches defects better than you, the seat makes you complacent, and
the work arrives in a size built to defeat you, then trying to out-read the
machine is a losing game. Don't try to be a better defect hunter than the
tireless one. Instead, do the one thing in this system a machine structurally
*cannot* do.

Understand the change. And when you don't — **say so, out loud, to another
human.**

That's the whole irreducible core of human review in the agentic era. Not "did I
find the bug" — the bot found the bug. The question is: *do I actually
understand what this code does, why it exists, whether it should exist, and
whether it's solving the right problem — and if I don't, am I willing to be the
person in the room who says so.*

Notice how different that is from the old job. The old reviewer's core skill was
*vigilance.* The new one's is closer to *honesty under social pressure*: the
willingness to look at 1,400 lines the tests pass on and the bot blessed and
your tired Friday brain wants to approve, and type — *I don't understand what's
happening in this module, walk me through it.* Or, *why does this exist at all.*
Or, *I see what it does, I don't see why, and I'm not approving until someone can
tell me.*

That's a **vulnerability act.** Saying "I don't understand this" is admitting,
in front of your peers, that you don't know something — about code a machine
wrote, that everyone else is also quietly pretending to understand. Whether you
*can* do that depends entirely on whether it's *safe* to. Which is where the
last two episodes were pointing.

Run all three together, because they're one argument. [Episode
one](../001-intent-layer/post.md): psychological safety became the critical
path, because catching bad agent output requires someone able to say *this is
wrong* without punishment. [Episode two](../002-invest-in-people/post.md): that
safety grows out of trust, built off the keyboard in real human time. **Episode
three is where it all gets spent.** Code review is the specific, concrete event
where the safety and the trust either show up and do their job — or don't. It's
a person, looking at a diff, deciding whether to admit they don't understand it.
The whole edifice of trust and safety exists to make one sentence sayable: *I
don't understand this. Explain it to me.*

And here's why it's load-bearing, not just nice. The only failure mode AI review
genuinely *cannot* catch is a human silently approving code no one in the room
understands. The bot can find your null pointer. It cannot find three engineers
clicking Approve while privately having no idea why the change works. There's no
linter for collective pretending, no CI check for *nobody actually understands
this.* That gap — between the team's real understanding and the code now running
in production — is invisible to every automated system you can buy, because they
all look at the *code*, and the gap is in the *people.* It only becomes visible
at 2 a.m., in the incident, when "who understands this system?" turns out to
have the answer: *nobody.* The machine wrote it, the machine reviewed it, the
humans rubber-stamped it, and now it's on fire and there's no one to ask.

There's one more cost, the one I think we'll regret most, because it compounds
quietly. Back to Weinberg's real point: distributed understanding. Review always
did a second thing we barely noticed because it came free — it *taught people.*
The junior learned by being reviewed; the senior learned the junior's corner by
reviewing it. Every review was a small, two-way transfer of knowledge. For a lot
of how engineers actually grow, that was the main event. When bug-finding moves
to the bot, the transfer doesn't move with it. Defect detection survives — it's
better than ever. But the **learning loop** gets cut. You won't feel it this
quarter. You'll feel it in two years, when you have a group of people who ship a
great deal of code, understand a shrinking fraction of it, and have stopped
teaching each other — because the occasion for teaching got automated into a
checkmark.

So, the thesis, plainly: code review was never about catching typos. It was the
social act where a team came to understand its own system and taught itself in
the process. The machine took the typos — gladly, and it's welcome to them.
What's left is the part that was always the actual point, and it's now the
**load-bearing wall** of the whole enterprise: whether a human, in
psychological safety, built on trust, is willing to look at what the agent wrote
and say out loud, before clicking the button — *I understand this,* or, *I
don't, and I'm not approving until I do.*

---

## What to do this week

1. **Replace one Approve with "I don't understand."** Find the review where
   you'd normally just click Approve — tests green, bot already looked, you're
   tired — and instead write one comment that begins *I don't understand.* Why
   does this function exist? What happens here when the input is empty? Walk me
   through this part. You don't have to find a bug; that was never the point.
   The point is to convert a private, complacent skim into a public act of
   actually trying to understand — the only thing that breaks the rubber stamp,
   and the only thing the machine can't do for you. Notice how unnatural it
   feels. That feeling is the complacency you've been swimming in.

2. **Put a ceiling back on size.** You're fighting 2009's math with 2026's
   tooling. If the agent hands you a thousand-line change, that's not a review,
   it's a rubber stamp with extra steps. Make the agent land its work in pieces
   a human can hold — a few hundred lines, the size the research says you can
   genuinely review. Yes, more PRs. Good. The friction is the feature. A
   reviewable change is one that fits in a person's head; if it doesn't fit,
   you're not reviewing it, you're performing a review of it — and that
   difference is the gap that shows up at 2 a.m.

3. **(Managers) Stop measuring review by speed.** Time-to-merge, review
   turnaround, throughput — in the agentic era, optimizing those is optimizing
   for the rubber stamp. You'll get a beautiful dashboard and a codebase no one
   understands. Measure the harder thing instead: *can the person who approved
   it explain it?* And protect the learning loop on purpose — put two humans on
   the review of consequential agent-written changes, not for throughput, for
   the *transfer.* So understanding stays distributed, somebody still teaches
   somebody, and in two years you have a team and not just a queue of approvals.

Back to the cold open: 4:50 on a Friday, fourteen hundred green lines, the
cursor on the button. The agent flew the plane all week, beautifully, and now
it's on final approach and handing you the controls for the one thing it can't
do — know whether anyone actually understands where it's taking you. That's the
seat you're in. Not the one who writes it. The one who has to genuinely
understand it before it lands, and be brave enough to say when you don't.

The autopilot will fly forever. It will never once tell you it's lost. That part
— noticing, and saying so out loud — is on you.

Land the plane. But read the instruments first.

---

## Sources

- Anthropic, *Code Review for Claude Code* — https://claude.com/blog/code-review
- InfoQ, on Claude Code review (16% → 54%) — https://www.infoq.com/news/2026/04/claude-code-review/
- IT Pro, "Anthropic says code review has become a bottleneck" — https://www.itpro.com/software/development/anthropic-says-code-review-has-become-a-bottleneck-this-new-claude-code-feature-aims-to-solve-that
- GitHub, "60 million Copilot code reviews and counting" — https://github.blog/ai-and-ml/github-copilot/60-million-copilot-code-reviews-and-counting/
- DORA 2025 report — https://dora.dev/dora-report-2025/
- Swarmia, DORA 2025 AI-readiness summary — https://www.swarmia.com/blog/dora-2025-report-ai-readiness/
- Simon Willison, AI-assisted programming — https://simonwillison.net/tags/ai-assisted-programming/
- Pragmatic Engineer, "When AI writes almost all the code" — https://newsletter.pragmaticengineer.com/p/when-ai-writes-almost-all-code-what
- Addy Osmani, "Code Review in the Age of AI" — https://addyo.substack.com/p/code-review-in-the-age-of-ai
- Intercom, "AI is approving our pull requests" — https://www.intercom.com/blog/ai-is-approving-our-pull-requests-heres-how-we-made-it-safe/
- CodeRabbit, "AI vs Human Code Generation" — https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report
- GitClear, 2025 AI code quality research — https://www.gitclear.com/ai_assistant_code_quality_2025_research
- Jellyfish, "AI-assisted PRs are 18% larger" — https://jellyfish.co/blog/ai-assisted-pull-requests-are-18-larger/
- SmartBear/Cisco code review study (PDF) — https://static0.smartbear.co/support/media/resources/cc/book/code-review-cisco-case-study.pdf
- Mike Conley, SmartBear/Cisco study summary — https://mikeconley.ca/blog/2009/09/14/smart-bear-cisco-and-the-largest-study-on-code-review-ever/
- Parasuraman & Manzey, "Complacency and Bias in Human Use of Automation" (2010) — https://journals.sagepub.com/doi/10.1177/0018720810376055
- Automation bias (overview) — https://en.wikipedia.org/wiki/Automation_bias
- METR, early-2025 AI experienced-developer study — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- Egoless programming (Weinberg) — https://en.wikipedia.org/wiki/Egoless_programming
- Graphite, "The ancient origins of code review" (Fagan inspections) — https://graphite.com/blog/the-ancient-origins-of-code-review
- Analyst's Corner, "Code Reviews: Rubber Stamps or Real Quality Gates" — https://medium.com/analysts-corner/code-reviews-rubber-stamps-%EF%B8%8F-or-real-quality-gates-dab98cca0a81
