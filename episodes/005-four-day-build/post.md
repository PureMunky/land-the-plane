# Touch and Go

*When agents do the typing, a four-day build stops being about whether you can build the thing and becomes a pure intent exercise — the best proof you have of what's worth building, and a factory for demos that look done and aren't. Those turn out to be the same fact.*

*Published 2026-06-27. The audio version of this piece is
[Land the Plane episode 5](./episode.mp3); this post covers the same
ground for people who'd rather read.*

---

## This week on the radar

Four things from the last little while.

**The job is becoming orchestration.** The cleanest name for the shift comes
from [Addy Osmani](https://addyosmani.com/blog/code-agent-orchestra/): *conductor
to orchestrator* — from writing the code yourself to directing a small ensemble
of agents that write it for you
([O'Reilly Radar](https://www.oreilly.com/radar/conductors-to-orchestrators-the-future-of-agentic-coding/)).
The counterintuitive thing the people who've gotten good at this keep reporting:
a few focused agents, each pointed at one narrow slice, reliably beat one agent
told to go do everything. Sit with what that means for a team. The valuable human
skill is no longer typing fast — it's *decomposition and direction:* breaking a
problem into pieces clean enough to hand out, and conducting the result. The big
organized builds this spring made it visual — single projects running on eight
agents coordinated by a router, one person at the podium. The keyboard is
becoming a baton.

**The data caught up to the vibe.** Anthropic's
[2026 Agentic Coding Trends report](https://resources.anthropic.com/2026-agentic-coding-trends-report)
(January) has two numbers that matter. AI is now involved in around **60%** of
coding work — but only **0–20%** of tasks are *fully* handed off to the agent.
The space between them they call the **delegation gap**: people use agents on
almost everything and trust agents to finish almost nothing. And the report's
framing of *why* is the sentence I'd staple to this episode — the bottleneck is
no longer writing code, it's **clarity about what to build.** That's not my
opinion this week. That's the tooling vendor's own telemetry.

**And here's who's picking up the baton.** Vercel's *State of Vibe Coding* data
puts a number on it:
[**63% of the people using these AI app-builders aren't developers**](https://www.hostinger.com/blog/vibe-coding-statistics)
— product, design, marketing, ops, building working software by describing it.
Hold it honestly: it's a survey of people *already reaching for* an AI builder,
not a census of the industry — it tells you who's inside the tent, not that
two-thirds of all software changed hands. (Population-level measured data on
non-engineers *shipping* doesn't exist yet; don't let anyone tell you it does.)
But inside the tent, the composition flipped: the people building are, more and
more, the people who were never allowed to build before. Remember that number
when we get to the main piece — it's the whole story of who walks through the
door.

**The counterweight.** [MIT's 2026 *State of AI in Business*](https://venturebeat.com/data/the-last-mile-data-problem-is-stalling-enterprise-agentic-ai-golden)
produced the most-quoted number in enterprise AI: roughly **95% of GenAI pilots
never reach production.** They demo, they impress, they earn a budget line, and
then they die in the gap between the prototype and the real thing. Put that next
to this quarter's security work — a paper bluntly titled
[*Is Vibe Coding Safe?*](https://arxiv.org/abs/2512.03262) found that **>80% of
the functionally correct solutions** — the ones that would've demoed clean —
still carried an exploitable vulnerability. (A
[commercial audit](https://hatchworks.com/blog/gendd/cost-of-vibe-coding/) put
the vuln rate north of 90%; treat that one as directional, but note it converges
with the academic figure.) Two different failures, the same shape: the thing
runs, the thing demos, and then four times out of five it's either carrying a
hole or it never lands at all. Let's talk about why that's not a coincidence —
and why four days of agentic building is exactly where it gets manufactured.

---

## Cold open: day one, mid-afternoon

It's day one of a four-day build. Small, mixed group — a couple of engineers, a
product person, a designer, and someone from the support side, the one who reads
the angry tickets all day and knows exactly where the product hurts. No
scoreboard, no prize: the only question on the table is *in four days, with
agents doing the construction, what can you actually build — and is it the right
thing?*

A year ago I can tell you precisely what each of them is doing on day one. The
engineers are typing. Everyone else is making slides, writing the pitch, getting
lunch — waiting to be useful at the end.

Now look at the same room this week. By mid-afternoon the support person — who
has never written a line of production code in her life — turns her laptop
around. There's a *running application* on the screen. Not a mockup. Not a
Figma. A thing you can click, that talks to a real data source, that does the
one specific thing she's wanted the product to do for two years and has never
once gotten prioritized. She built it. By describing it. To an agent. In an
afternoon.

And the room has the same two reactions, in the same order, every time. First:
genuine, infectious delight, because something that used to be impossible just
happened and it's wonderful. Then, a beat later, quieter — the reaction this
piece is about. Somebody looks at that beautiful running thing and realizes:
*nobody here can actually tell you if it's right.*

It runs. It demos. It's exactly what she asked for. And not one person in the
room can tell you whether what she asked for was the correct thing to ask for,
or whether the code under that clean demo would survive ten minutes of a real
adversary or a real Monday. That gap — between *it runs* and *it's right* — is
the whole story of what four days became.

---

## The four-day build changed species

Here's a thing about a time-boxed build nobody said out loud, because we never
had to: **the clock was always a verification machine in disguise.**

Think about what four days actually did. We told ourselves it was about energy
and focus and the satisfaction of building something real in a week. But
mechanically, that clock was a *test* — a validator. When a team walked up at the
end and the thing actually ran, that working demo was *earned evidence.* It
proved something specific and expensive: that the idea was real enough, and
understood well enough, that a few humans could construct it with their own hands
in the time they had. The clock made building hard, and because building was
hard, getting it to run *meant* something. *It runs* was a certificate, and the
four-day clock was what made the certificate cost something to obtain.

Now collapse the cost of building to near zero — which is exactly what agentic
workflows did.

When anyone in the room can get a thing running in an afternoon by describing it,
*it runs* stops proving the idea was buildable, because everything is buildable
now. The demo still appears — faster, more often, more polished than ever — but
it no longer certifies what it used to. All it certifies now is that somebody
could *describe* the thing plausibly enough for an agent to produce something
that looks like it. The four-day build didn't just get faster. It lost the one
free test it used to run on every project — the test of construction — and most
people running these haven't noticed the test is gone.

So if building isn't the hard part, what is? This is
[Goldratt](https://www.tocinstitute.org/theory-of-constraints.html) again, from
last week: any system has one bottleneck; speed up a non-bottleneck and you get
nothing but a bigger pile of inventory in front of the real constraint. In a
four-day build, construction used to be the bottleneck — the thing that gated
whether your idea ever became real in the room. We removed it. And the instant
we did, the constraint moved upstream, to the question that was always sitting
behind the building, hidden by how hard the building was:

**What should we build? And do we understand it well enough to say so clearly?**

That's what four days measures now — not whether you can build (everyone can
build) but who showed up knowing which thing was worth building, and who could
describe it precisely enough that the agents produced the *right* thing instead
of merely *a* thing. The four-day build became a pure intent exercise. It's the
most concentrated, fastest-feedback intent laboratory I've ever stood inside: you
have an idea at 9am and by 10 you know whether you could even *say* it clearly —
because if you couldn't, the agent built you the wrong thing and you're staring
at the proof.

And notice what we had to take away to get there. A competition, whatever else
you make of it, at least validates *something* — a judge picks a winner, and a
ranking is a crude external check that one thing came out better than another. We
didn't run a competition. No judge, no prize, no clock pressure forcing anyone's
hand. And because the agents made *it runs* free, there isn't even a construction
barrier left to clear. Strip all of that away and you're left with exactly one
variable still under test: *did this team know what was worth building, and could
they say it clearly.* That's the purest isolation of intent I've ever watched a
working process pull off — and it's also (we'll come back to this hard) the
reason every single thing that comes out the far end is **unvalidated by
construction.** Nothing in that room was measuring whether the thing was *right.*
That was never what the room was for.

And that reframe changes who's good at this.

## The people the keyboard was hiding

For thirty years, the keyboard was a filter. Not a fair one.

If you had a brilliant idea about the product but couldn't write the code, a
build like this wasn't really for you. You could pitch, advise, draw the picture
— but you couldn't put your own hands on the thing and make it real, because
making it real required a skill that took years to acquire and had almost nothing
to do with whether your idea was good. The person who understood the customer
best and the person who could type fastest were almost never the same person, and
we built a whole industry that systematically handed the keys to the second one.

Pull the keyboard out as the filter, and watch who walks through the door.

The support lead from the cold open has the highest-resolution map of the
product's pain of anyone in the building — she lives in it. For her whole career
that map has been trapped behind a wall of syntax she was never going to climb.
This week the wall came down, and the first thing she built was sharper and more
useful than what the engineers built, and it's not close, and it's not a fluke.
It's the obvious result. She had the best intent in the room. She was just never
allowed to express it in running software before. **Intent was always the scarce
thing.** We just couldn't see it, because it stood behind a wall of typing and we
kept mistaking the wall for the work.

This is the democratization story, and the honest version is more interesting
than the hype version. The hype version says *everyone's an engineer now.*
That's not true and not what I saw. What I saw is narrower and more important:
people who deeply understand a problem can now produce a working expression of
the solution without an engineer standing between their intent and the artifact.
And we're not only guessing anymore — remember that
[Vercel number](https://www.hostinger.com/blog/vibe-coding-statistics) from the
news: 63% of the people reaching for these builders aren't developers. Hold it
honestly (it's the people already inside the tent, not the whole industry), but
it confirms the shape. The tooling vendors report the same — legal, design, ops,
building their own small tools without an engineer in the loop. The wilder claims
— *80% of software built outside the technology department* — are
[predictions](https://www.gartner.com/en/newsroom), not measurements; file those
as guesses. But the direction isn't a guess.

And here's where the orchestration shift from the top does its quiet, important
work. A four-day mixed team isn't one engineer typing while everyone else hovers.
It's the support lead conducting a couple of agents on her slice, an engineer
conducting three more on the integration, the designer driving the interface —
every one of them directing, none of them bottlenecked behind a single pair of
hands. The team stops scaling to the size of its keyboard and starts scaling to
the size of its intent. Which is exactly why the *mix* matters now in a way it
couldn't before: you want the most different brains in the room you can find,
because every one of them can actually build.

Here's the part the tooling story leaves out, and it's the part that matters if
you run a team: **none of this works without the conditions, and the conditions
aren't technical.**

Think about what that support person had to do to turn her laptop around. She had
to show a half-built, possibly-wrong thing to a room that included engineers —
the people who, in the old world, held all the status in that room. She had to
risk looking naive, operate as a peer in a group that on the org chart doesn't
treat her as one. The only reason that prototype ever got shown is that the room
was safe enough for her to show it.

You know the research. Google's
[Project Aristotle](https://rework.withgoogle.com/intl/en/guides/understand-team-effectiveness)
went looking for what made some teams dramatically more effective than others,
and the #1 factor — above talent, seniority, experience — was **psychological
safety**: the felt permission to take a risk in front of your peers without being
punished for it. In the old version of these four days, safety was a
nice-to-have that made the week pleasant. In the agentic version it's
*load-bearing,* because the entire value of the exercise now depends on the
person with the best intent feeling safe enough to put their hands on the
keyboard in front of people who outrank them. Strip the safety out and the
support lead makes slides again, her insight stays locked in her head, and your
four days go back to measuring typing speed — the one thing that no longer
matters.

So the agentic build doesn't just reward intent. It rewards **distributed
authority** — flattening the room enough that intent can come from anywhere. The
group that gets something genuinely real out of four days isn't the one with the
best engineers; it's the one that got the clearest intent into the room and was
safe enough to let it drive, no matter who carried it. That's the whole anarchist
case for running a team, compressed into a single week.

Which would be a lovely place to stop. Except for the thing in the cold open:
nobody in the room could tell you if it was right. Let me ruin the party.

## Touch and go

There's a maneuver in aviation called a *touch-and-go.* The aircraft comes down,
the wheels actually kiss the runway — and then, without ever stopping, without
taxiing in, without anyone getting off, the pilot pushes the throttle back up and
takes off again. It's practice. The point of a touch-and-go is that it looks
exactly like a landing right up until the moment it very much isn't. The wheels
touched. Nobody arrived.

That's the demo at the end of four days. And it's the most dangerous artifact
your organization now produces.

Here's why. That instinct from the certificate — *running means done* — is wired
into everyone who watches a demo. It was trained over decades when running was
expensive, and it hasn't updated. So you now have an exercise that manufactures
running demos at near-zero cost, shown to people whose every reflex says a
running demo means the work is basically finished. The demo touches the runway;
everyone files it as a landing; nobody got off the plane.

Remember the numbers, because now they bite. **~95%** of enterprise GenAI pilots
never reach production — they demo, then die in the gap between the prototype and
the real thing. And **>80%** of vibe-coded solutions that *functionally worked*
still carried an exploitable vulnerability. Read those against what a demo
actually shows you. A demo shows you the part that works — the happy path, the
thing on the screen. A demo is *structurally incapable* of showing you the hole,
because if the hole showed up in the demo it wouldn't be a hole, it'd be a bug,
and someone would've fixed it. The demo and the defect live in different rooms.
The better the demo, the more completely it hides the part that doesn't work.

And here's where what we stripped away in Act 1 comes due. No judge, no clock, no
construction barrier — every validator the old version of this exercise leaned on,
we pulled out on purpose, because pulling them out is exactly what made it such a
clean intent lab. But it also means the running thing on the screen passed
through *zero* validation gates to get there. The prototype that worked in the
room routinely needs a near-total rebuild before it can survive real users.
Nobody's lying to you. The room itself is built to manufacture things that look
finished and aren't — deliberately, for good reason — which is exactly why it's
so dangerous to trust what walks out of it.

This is the same crack we ended on last week, and it has the same name. There's a
difference between
[**verification and validation**](https://www.scrum.org/resources/blog/doing-right-thing-right-validation-and-verification):
verification asks *did we build the thing right;* validation asks *did we build
the right thing.* Four days of agentic building is spectacular at producing
things that look verified — it runs, it's clean, it demos. It does almost nothing
about validation, because validation requires knowing what the right thing *was,*
and that lives only in a human head; it can't be inferred from a running screen.

Shuvendu Lahiri at Microsoft Research
[named this exact problem](https://www.microsoft.com/en-us/research/publication/intent-formalization-a-grand-challenge-for-reliable-coding-in-the-age-of-ai-agents/)
this spring, and the line to hold is verbatim: the gap between informal
natural-language requirements and precise program behavior — the **intent gap** —
*"has always plagued software engineering, but AI-generated code amplifies it to
an unprecedented scale."* Amplifies. Not creates. The gap was always there; four
days of agentic building is an intent-gap amplifier, producing more
plausible-looking, less-validated software per hour than any process humans have
invented. And Lahiri's hardest sentence closes the easy escape: *"there is no
oracle for specification correctness other than the user."* No machine, test,
scanner, or agent can tell you whether the spec was right. Only a human can. The
demo can't validate itself, and neither can the thing that built it.

So here's the uncomfortable claim, the center of the whole piece. Four days of
cross-functional agentic building is the best intent laboratory we've ever had —
*and* a factory for plausible, unvalidated demos. **Those aren't two facts to
balance. They're the same fact.** The exact property that makes it a great intent
lab — stripping away the cost of construction so pure intent can express itself
instantly — is the exact property that mass-produces demos that look finished and
aren't. You can't have one without the other. The stripping-away is the gift
*and* the danger, same move, same instant. The thing that lets the support lead
express her insight in an afternoon is the same thing that lets her — and you —
mistake an afternoon of expressed insight for a shipped, validated, safe product.

What do you do with that? Not stop running these — the intent lab is too
valuable. You change what you think the *output* is. The output of four days of
agentic building isn't the software; the software is a touch-and-go and was never
going to taxi to the gate. The real output — the cargo worth carrying out of the
room — is the *intent it discovered.* You now know what's worth building, who
understood it, and you have a running sketch that proves its shape. That's gold.
It's genuinely faster discovery of what matters than any planning process gave
you. But it's *discovery* — the beginning of the work, dressed in the costume of
the end of it.

There's a useful distinction from Simon Willison between *vibe coding* and
[*vibe engineering*](https://simonwillison.net/2025/Oct/7/vibe-engineering/). Vibe coding is what happens in those four days — describe it, watch
it run, feel the magic, don't look too hard at what came out. Vibe engineering is
what has to happen after: the same speed, but with the discipline of someone who
refuses to ship code they couldn't explain to another human, who writes the
tests, who states what correct means and checks against it. The four-day build
gives you vibe coding for free. The shipping is all vibe engineering, none of it
is free, and the demo will lie to you about how much is left. Most of the work is
still in front of you at the exact moment it feels finished.

**The thesis, plainly:** take construction out of the four days and what's left
is pure intent — which is why it's now the best laboratory you have for
discovering what to build and who understands it. But intent is the *input* to
software, not the software. The running demo is a touch-and-go: the wheels kissed
the runway and not one passenger arrived. Mistake it for a landing and you'll
taxi a plane full of vulnerabilities to the gate and call it a delivery. The gift
of those four days is the intent. Keep that. The code was always going to take
off again.

---

## What to do this week

1. **If you run one of these, be clear about what you're actually proving.** The
   point of four days isn't to come out with a product — it's to come out knowing
   something you didn't know on Monday: what's worth building, and whether you can
   say it clearly. So judge it on *that,* not on the cleanest-looking running
   thing. Rewarding the best demo trains your whole org to mistake a plausible
   demo for finished work — the single most expensive instinct you could build
   right now. Judge the *intent:* did this team discover something genuinely worth
   building? Can they state, in plain specific language, what *correct* would mean
   — what it must do, must never do, how you'd know it worked? **The spec they can
   write at the end is the asset; the demo is the wrapping paper.**

2. **Treat every prototype as a question, never an answer.** The demo is the
   agent's *hypothesis* about what you meant. Before any of it goes near a
   customer, do the vibe-engineering pass: write the acceptance criteria the demo
   was secretly assuming — the ones nobody said out loud — and actually validate
   against them. Make the throw-away-or-commit decision *explicitly,* out loud, as
   a real fork: either this was a touch-and-go and we keep the intent and rebuild
   it for real, or we're committing to land it — which means it now has to earn a
   real landing with tests, review, and someone who can explain every line. Never
   let a prototype taxi quietly to the gate because it looked done in the room.
   Looking done in the room is the one thing it's guaranteed to do.

3. **(Managers) Put your non-engineers in the cockpit — on purpose.** The
   democratization isn't a party trick; it's the actual prize, and most of you
   will waste it by keeping the keyboard in the same hands it's always been in.
   The support lead who can now prototype her own idea is worth more to you than a
   marginally faster engineer, because she closed a gap that's cost you for years:
   the distance between the people who understand the problem and the people who
   can express a solution. Build the conditions that let that happen — make the
   room safe enough that the person with the best intent and the lowest status
   will actually turn their laptop around. That safety is load-bearing
   infrastructure now, not culture fluff. And when the four days are over, be the
   adult who says the quiet part: *wonderful — now none of this is shipped yet,
   and here's what landing it actually takes.* Know the difference between a
   touch-and-go and an arrival.

Go back to the room. Day one, mid-afternoon. The support lead turns her laptop
around, there's a running thing that didn't exist that morning, and the whole
room lights up. That light is real — something genuinely changed, and it's good,
and you should feel it. Just remember what you're looking at. The wheels touched
the runway. The work now is to figure out whether this plane should ever land at
all — and if it should, to actually bring it down. Slowly. On purpose. With
somebody in the tower who knows where it was always supposed to go.

That's the intent. That was always the only cargo worth carrying off.

---

## Sign-off

Five weeks on one arc now — psychological safety, the people, the moment of
review, the verification bottleneck, and now the four days where all of it
collides and you can watch it happen at speed. Which lands us at the doorstep of
where this show has been walking the whole time. If the output of the work is
*intent* — if the demo is just intent in a costume, and the real cargo is knowing
what to build and being able to say it — then the next question is what it would
look like to treat intent as the *actual artifact:* capture it, version it, keep
it, build from it on purpose, instead of discovering it by accident in a four-day
build and letting it evaporate on Monday. That's the intent layer. That's where
we go next, and where we've been going since episode one.

Until then — run the experiment, keep the intent, and don't taxi a touch-and-go
to the gate.

---

## Sources

- Addy Osmani — "The Code Agent Orchestra" (conductor → orchestrator) — https://addyosmani.com/blog/code-agent-orchestra/
- O'Reilly Radar — "Conductors to Orchestrators: the future of agentic coding" — https://www.oreilly.com/radar/conductors-to-orchestrators-the-future-of-agentic-coding/
- Anthropic — 2026 Agentic Coding Trends report (the "delegation gap," ~60% AI involvement) — https://resources.anthropic.com/2026-agentic-coding-trends-report
- Vercel "State of Vibe Coding" — 63% of AI app-builder users are non-developers (via Hostinger roundup; self-selected tool users) — https://www.hostinger.com/blog/vibe-coding-statistics
- MIT "State of AI in Business" 2026 — ~95% of GenAI pilots never reach production (via VentureBeat) — https://venturebeat.com/data/the-last-mile-data-problem-is-stalling-enterprise-agentic-ai-golden
- "Is Vibe Coding Safe?" (>80% of functionally correct solutions carried an exploitable vulnerability) — https://arxiv.org/abs/2512.03262
- Hatchworks — the cost of vibe coding (commercial >90% vuln claim, "prototype needs a massive rebuild"; treat as directional) — https://hatchworks.com/blog/gendd/cost-of-vibe-coding/
- Microsoft Research — "Intent Formalization: A Grand Challenge…" (Lahiri; the "intent gap," "no oracle for specification correctness other than the user") — https://www.microsoft.com/en-us/research/publication/intent-formalization-a-grand-challenge-for-reliable-coding-in-the-age-of-ai-agents/
- Goldratt, Theory of Constraints — https://www.tocinstitute.org/theory-of-constraints.html
- Verification vs. validation — https://www.scrum.org/resources/blog/doing-right-thing-right-validation-and-verification
- Google re:Work — Project Aristotle (psychological safety) — https://rework.withgoogle.com/intl/en/guides/understand-team-effectiveness
- Simon Willison — "Vibe engineering" (Oct 7, 2025) — https://simonwillison.net/2025/Oct/7/vibe-engineering/
- Simon Willison — "Vibe coding" / the golden rule (Mar 19, 2025) — https://simonwillison.net/2025/Mar/19/vibe-coding/
