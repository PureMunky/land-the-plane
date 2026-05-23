# When the Planes Don't Land

*Intent, agents, and the coming reshape of engineering work.*

*Published 2026-05-23. The audio version of this piece is
[Claude Cast episode 1](./episode.mp3); this post covers the same
ground for people who'd rather read.*

---

## This week on the radar

Four things from the last little while.

**Karpathy joins Anthropic.** Andrej Karpathy — who in
[February 2025](https://x.com/karpathy/status/1886192184808149383)
posted the tweet that named "vibe coding," and who was one of the
founding members of OpenAI — joined Anthropic in May. Fortune broke
the story on the [19th](https://fortune.com/2026/05/19/who-is-andrej-karpathy-vibe-coding-anthropic-openai-rubiks-cube/).
The symbolic arc is the thing: the person who coined the loose,
exuberant, no-code-review mode of working with language models has
gone to the company building the most opinionated, most review-
disciplined coding-agent product in the market. The center of gravity
is moving toward agentic coding with more deliberate guardrails, not
away from it.

**Visual Studio Magazine on Spec Kit.** On
[May 12](https://visualstudiomagazine.com/articles/2026/05/12/github-spec-kit-takes-off-as-antidote-to-piecemeal-vibe-coding.aspx)
the magazine ran a piece on GitHub's open-source spec-driven
development toolkit. The headline literally calls it "an antidote to
piecemeal vibe coding." The line at the heart of
[Spec Kit](https://github.com/github/spec-kit) is the one to
internalize: *from "code is the source of truth" to "intent is the
source of truth."* It's the spine of everything that follows.

**Thoughtworks Radar v34.** Published in
[April 2026](https://www.thoughtworks.com/about-us/news/2026/combat-ai-cognitive-debt-radar-v34),
this is the most prominent institutional pushback. The phrase to
remember is "cognitive debt" — the gap between the volume of code
your team is producing with agents and the amount of that code your
team actually understands. Their warning is sharp: "coding agents
will generate bad code and then use bad code to generate more bad
code," and "humans are dangerously tempted to step out of the loop."

**Psychological safety eroding in AI-heavy teams.** HBR
[in February](https://hbr.org/2026/02/how-to-foster-psychological-safety-when-ai-erodes-trust-on-your-team)
and MIT Tech Review (late 2025) both published on something a lot of
people have been seeing privately. ManpowerGroup put a number on it:
AI usage at work up 13% year over year, employee confidence in the
technology down 18%. People are using these tools more and trusting
them less, and in a lot of orgs, saying that out loud feels like
heresy.

---

## The diff is not the artifact

Picture a scene a lot of you will recognize. It's a Tuesday afternoon.
An engineer is sitting at a desk; on the main screen, a coding agent
is working — refactoring a Kubernetes operator, reading files,
proposing edits, running tests, reading the test output, proposing
more edits. It's been about four minutes since the human typed
anything. Once in a while a notification chirps. The agent has a
question.

In that pause, watching the machine work, there's a thought a lot of
us have started to have.

**The diff is not the artifact.** The diff is the exhaust. The
artifact is the conversation that produced it — the reasoning, the
false starts, the moment the engineer said, *no, not like that, the
controller has to be idempotent because we run it from a Tekton task
that retries on failure*. That sentence — that piece of intent —
never made it into the codebase. It got compressed into a few lines
of Go and a comment that says "idempotent," and the next person who
reads that comment will have no idea why it matters.

That's where this piece starts. The question that follows from this
little moment is bigger than it looks. It's a question about what
happens to software when agents do the typing and humans do the
thinking — and about why most engineering organizations are about to
discover, the hard way, that they've been mistaking the shape of
work for the substance of work for about a decade.

## The Intent Layer

[Simon Willison](https://simonwillison.net/2025/Mar/19/vibe-coding/)
has the cleanest line on Karpathy's coinage I've read: "I won't
commit any code if I couldn't explain what it does to somebody else.
If an LLM wrote the code but you then reviewed it, tested it
thoroughly, and ensured you could explain how it works — that's
software development, not vibe coding."

The practical question that line raises is: where does the
explanation live?

If you're going to be able to explain what the code does and *why
it's structured the way it is*, the explanation can't just live in
your head. In three months you won't remember. In six months,
somebody else will own the code and they certainly won't remember,
because they were never there. The explanation has to live somewhere
durable. And the places we usually put explanations — comments,
commit messages, design docs — were designed for a world where a
human typed the code. They're optimized for the assumption that the
typist already understood it.

That assumption is breaking.

GitHub noticed. In late 2025 they released [Spec
Kit](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/),
an open-source toolkit for spec-driven development. You write a
specification first, then a plan, then tasks; then the agent codes.
The tagline — *from "code is the source of truth" to "intent is the
source of truth"* — is the thing to internalize. Specifications
become first-class. Code is the last mile.

But most of the coverage of Spec Kit misses what I think is the
actual point. The specification isn't the goal. The specification is
one snapshot of the intent. Intent itself is bigger: it includes the
moment three days ago when you decided *against* a different design;
the pivot you made at 3 PM yesterday because a stakeholder said
something offhand in a meeting that turned out to be load-bearing;
the thing you tried for an hour, that didn't work, that you
abandoned and never wrote down — and which the next engineer is
going to try again because there's no record that anyone has been
down that path.

A specification captures intent at a moment. **The Intent Layer is
the continuous record of intent across time.**

People have started building personal versions of this. Call it a
captain's log, an intent log, a decision journal — pick the name.
The shape is the same: a thing that sits next to your agent sessions
and captures the conversation — the prompts, the pivots, the
reasoning — alongside the diffs. So when you look back at a feature,
you don't just see what changed. You see what you were trying to do
when you changed it.

Steve Yegge — now at Sourcegraph, co-authoring a book on vibe coding
with Gene Kim and Dario Amodei — has been building something similar
he calls Beads: a lightweight, agent-readable decision and issue
store. Different name, same shape. The whole industry is converging
on the same recognition: **when the typing gets cheap, the
explaining gets expensive.** The explaining is where the actual
value lives.

The internalization for engineering leaders is this. If your team is
using agentic tools and you don't have any way to capture intent
alongside the output, you're accumulating what Thoughtworks now calls
*cognitive debt*. The first sign of it isn't a bug. The first sign
is a meeting where nobody can answer the question, "why did we do it
this way?"

## The cargo cult tax

The title of this piece is "When the Planes Don't Land," and the
reference is the story everyone in engineering should know but a
surprising number of people don't.

In 1974, Richard Feynman gave the Caltech commencement address. He
told a story about the cargo cults of the South Pacific. After World
War II, American forces had built airstrips on Pacific islands,
brought in massive amounts of equipment and supplies — *cargo* — and
then left. The islanders, having watched all of this, did the
reasonable thing: they built bamboo control towers, fake airstrips,
[coconut-shell headphones](https://en.wikipedia.org/wiki/John_Frum).
They made everything *look* exactly like what the Americans had been
doing. And they waited for the planes to come back. The planes did
not come back.

Feynman's [point](https://calteches.library.caltech.edu/51/2/CargoCult.pdf):
"the first principle is that you must not fool yourself — and you
are the easiest person to fool." His application was to bad
science: practices that follow the forms and rituals of scientific
investigation without the underlying mechanism. The shape of science
without the substance.

There's a footnote to the story I think matters more, and I'd never
thought about it until I was reading some recent anthropology for
this piece. Modern anthropologists read the cargo cults very
differently than Feynman did. They don't read them as primitive
misunderstanding. They read them as **deliberate political
response** — the islanders weren't confused about planes; they were
performing a counter-ritual against colonial missionaries and labor
exploitation. The coconut headphones weren't ignorance. They were a
political statement that we, the outside observers, had categorized
as ignorance because that's how outside observers usually categorize
things they don't understand.

Hold both readings. They both apply to engineering management.

Mike Hadlow's 2014 post
["Coconut Headphones: Why Agile Has Failed"](http://mikehadlow.blogspot.com/2014/03/coconut-headphones-why-agile-has-failed.html)
made the Feynman move on Agile: teams adopt the visible shapes —
standups, sprints, story points, retros, planning poker — without
the underlying mechanism. They get the rituals. They miss the
function. The result is Agile theater. The more general phenomenon
is what I'll call the **cargo cult tax**: what your organization
pays when it adopts the form of a practice without the substance.

Standups that aren't really standups — they're status updates to
managers, performed in front of the team to add the patina of self-
organization. Story points that aren't really estimates — they're a
number a manager will hold against you in a year-end review. PR
templates that aren't really design discipline — they're a checklist
nobody reads, attached to every change, including the one-line CSS
fix. Coconut headphones. The visible shape of engineering rigor; not
engineering rigor.

Here's the thing the existing conversation about cargo cult Agile
misses. **When agents start doing the typing, the cargo cult tax
gets worse, not better.**

The agent doesn't slow down for the theater. The agent doesn't have
a manager whose existence depends on it filling out the PR template.
The agent doesn't lose face shipping a one-line fix without a story
point estimate. The agent produces code at a pace that exposes the
ceremony as the bottleneck it always was. Suddenly the engineers can
ship a small change in 20 minutes if they let the agent run, but the
*system* — the ticket queue, the design doc, the review backlog, the
change advisory board — still takes three days.

In most organizations, the response is going to be to add more
ceremony, not less. Because the ceremony is the thing the
organization can see, and what gets measured gets defended.

Take the generous reading of the cargo cult for a moment. The
islanders weren't confused; they were performing a counter-ritual
for a political reason. Apply that to your engineering org. The
standup-as-theater isn't always cluelessness — it's often a rational
response by a manager who needs *something visible* to defend their
existence to *their* manager. The PR template nobody reads isn't
always a misunderstanding of code review; it's often a CYA artifact
for a compliance auditor.

These rituals serve a real political function. They're rational from
the inside. They're just not engineering function. And the moment
agents come in and make engineering function ten times faster, the
gap between political function and engineering function becomes
impossible to hide.

The companies that win the next five years will be the ones that
look hard at every ceremony in their stack and ask: *is this an
engineering function, or is this a political function?* And if it's
political — is the political function still necessary? And if it
is — can we serve it with one-tenth the ceremony?

That's going to be uncomfortable.

## Anarchist management as a throughput argument

The view on this show — and I'll own it as a view, not a fact — is
what I'll call **anarchist management**. People hear the word
anarchist and they think chaos; that's not what it means here. The
word I'm reaching for is the kind of anarchism that comes out of,
say, [David Graeber](https://en.wikipedia.org/wiki/David_Graeber).
It means: skeptical of unjustified hierarchy; assume authority has
to defend itself, not the other way around; distributed decision
making, autonomy at the edges, leadership that emerges from
competence and consent rather than from a title on a slide.

For most of the last decade that's been an *ideological* commitment
— something a lot of us in management believed because we thought it
was right, and which we had to defend to skeptical leaders who
thought we were being soft, naive, or insufficiently rigorous.

What I want to argue here is that, in the agentic era, anarchist
management stops being an ideology. It becomes a **throughput
argument**. It becomes the only architecture that scales.

Let me show the work.

There's a randomized controlled trial from
[METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/),
published in July 2025, of experienced open source developers using
AI tools. Before the study, the developers forecasted AI would make
them 24% faster. After the study, they *self-reported feeling* 20%
faster. The actual measurement: they were **19% slower**.

Read that again. They felt 20% faster. They were 19% slower. The
gap between perception and reality was about forty percentage
points.

The obvious caveat — and Steve Yegge
[makes it loudly](https://sourcegraph.com/blog/revenge-of-the-junior-developer) —
is that the study used tools available before March 2025. Tooling
has changed. Maybe the result wouldn't replicate today. Fine. But
hold onto what the study showed about *humans*, not about tools:
when people are using AI, they're systematically wrong about how
fast they are. They think they're shipping more. They are sometimes
shipping less.

It follows that the work of telling people the truth about their
output becomes massively more important. And the work of telling
people the truth requires a culture where people *can be told the
truth* — without being punished, without their performance review
getting weird, without it ending their relationship with the person
who delivered the news.

[Charity Majors](https://charity.wtf/category/ai/) put this
beautifully: "writing code was never the bottleneck. Validation is."
Validation, in this context, doesn't just mean tests. It means a
human, with skin in the game, looking at this output and saying
"yes, this is right" or "no, this is wrong." It means the social
act of holding a piece of work to a standard.

And the social act of validation requires what Amy Edmondson calls
[psychological
safety](https://en.wikipedia.org/wiki/Psychological_safety): the
belief that you can speak up — point out a problem, ask a dumb
question, disagree with the agent's plan, push back on the senior
engineer's design — without being punished or humiliated.

If you don't have that, here's what happens in your org over the
next twelve months. Engineers using agents are going to produce a
lot more code. The code is going to look plausible. The code is
going to compile, pass the tests the agent wrote, and ship. And
somewhere downstream, a customer is going to hit an edge case the
agent didn't think about. Or a security review will find something.
Or the on-call engineer at 2 AM will discover that none of this
code actually composes the way the architecture diagram says it
does. In a healthy team, somebody saw that coming and said
something three weeks earlier. In an unhealthy team, three people
saw it coming and *didn't* say anything, because the last time
someone said something they got labeled "not a team player."

That's the throughput argument. **Psychological safety isn't a
nice-to-have. It is the literal critical path of shipping software
when the bottleneck has moved from typing to judgment.**

[Ron Westrum](https://itrevolution.com/articles/westrums-organizational-model-in-tech-orgs/) —
a name every engineering manager should know — wrote about this in
2004. He described three kinds of organizational culture:
*pathological* (power-oriented), *bureaucratic* (rule-oriented), and
*generative* (performance-oriented). The headline finding, which
DORA has validated more recently in software contexts, is that
**the single best predictor of organizational effectiveness is
information flow.** Generative cultures surface bad news quickly.
Pathological cultures punish the messenger. Bureaucratic cultures
route bad news through process until it dies.

Sit with that in the context of agentic engineering. Information
flow is the predictor. The agent is generating information at ten
times the previous rate. If your culture is pathological or
bureaucratic, the agent will overwhelm the human cycles available
to process that information, and your team will be drowning in
produced-but-not-validated code within a quarter. If your culture
is generative — if information flows freely, if people can call out
bad output without consequence, if authority is distributed enough
that any engineer can stop the line — you have a chance.

Will Larson, one of the sharpest people writing about engineering
management right now, has a piece in O'Reilly called
["'Good Engineering Management' Is a Fad"](https://www.oreilly.com/radar/good-engineering-management-is-a-fad/).
The argument isn't that good engineering management doesn't exist.
The argument is that the practices we built around it were
calibrated to a set of constraints that have changed. Managers who
built careers on those practices are being told the foundation is
moving. One of the practices that needs to change most is the
cultural assumption that managers add value by *controlling*.
Because when typing is free, control becomes the slowest part of
the system.

[Camille Fournier](https://skamille.medium.com/things-i-currently-believe-about-ai-and-tech-employment-3e712df1dc51)
has been making a parallel prediction — not that the pyramid
flattens, not that we hire fewer juniors and more seniors, but
something stranger. Teams get smaller overall, and prompt/vibe/
intent skills move *outward* into the rest of the knowledge-worker
population. Marketing teams. Operations teams. The boundary of what
counts as engineering blurs. Which means the discipline engineering
historically supplied — the slow, careful judgment about whether a
thing should actually exist — has to come from somewhere. And if it
doesn't come from the tooling, and it doesn't come from the
diffusing pool of part-time engineers, it has to come from the
managers and the platforms.

The other reason to take psychological safety seriously is that
it's *eroding* in AI-heavy teams. ManpowerGroup's number is the one
to remember: AI usage at work up 13% YoY, employee confidence in
the technology down 18%. People are using the tools more and
trusting them less. In a lot of orgs, saying that out loud feels
like heresy.

That's a cultural failure with direct engineering consequences. The
fix is not more tools. Not more agents. Not more ceremony. The fix
is, very specifically, **leaders who model questioning their own AI
output in public, and who actively reward — in performance reviews
and in promotions — the engineers who flag problems.**

This is what anarchist management as a throughput argument looks
like. Distributed authority isn't ideology — it's the only
architecture that lets information flow at the speed agents produce
it. Autonomy isn't a perk — it's the condition under which judgment
scales. Psychological safety isn't soft — it's the literal mechanism
by which bad agent output gets caught before it ships.

## What to do this week

Three things, if any of this lands.

1. **Name one piece of management theater in your org.** Just one.
   Something you do every week or every sprint that, if you're
   honest, serves a political function and not an engineering
   function. Don't try to kill it. Just name it — out loud, to one
   other person you trust. The first move in dismantling theater is
   admitting it's theater.

2. **Find one decision in your codebase that isn't written down
   anywhere.** One pivot. One rejected design. One constraint that
   informed how something got built. Write it down — in the commit
   message, in a design doc, in a comment, or in a personal log if
   your org doesn't have a good place. Don't worry about
   systematizing. Plant the seed.

3. **Push back on one piece of plausible-looking agent output this
   week.** The next time an agent produces something that looks
   right and you have a small feeling it isn't — say something. To
   yourself, to your team, in the review. Don't let the plausibility
   of the output silence the judgment you have, that the machine
   doesn't. Validation is the bottleneck. You are the validator.
   Don't outsource that to vibes.

Karpathy — the man who named vibe coding in February 2025 —
defected to Anthropic in May 2026. The guy who coined the loose
mode is now at the company building the most opinionated coding-
agent product in the market. I think about that arc a lot. The
pendulum is swinging. The first wave of agentic coding was *let it
rip and see what happens.* The second wave, the one we're entering,
is *let it rip within constraints we deliberately specified.*
Specifications. Plans. Reviews. Intent.

The future I'm betting on is one where the most valuable engineers
and the most valuable engineering managers are the ones who can
articulate intent clearly, capture it durably, validate output
honestly, and run a team where people are safe to tell the truth.
That set of skills doesn't have a single name yet. The closest
might be what some people call the staff engineer archetype, but
the role is evolving and the title is going to lag the function by
a couple of years, like it always does.

In the meantime, the planes are not landing. The agents are typing.
The ceremonies are still happening. And the gap between the shape
of engineering work and the substance of engineering work is the
widest it's ever been.

Don't put coconut shells on your head.

Land the plane.

---

## Sources

- Andrej Karpathy, original "vibe coding" tweet, Feb 2 2025: <https://x.com/karpathy/status/1886192184808149383>
- Karpathy joining Anthropic (Fortune, May 19 2026): <https://fortune.com/2026/05/19/who-is-andrej-karpathy-vibe-coding-anthropic-openai-rubiks-cube/>
- Simon Willison on vibe coding: <https://simonwillison.net/2025/Mar/19/vibe-coding/>
- Simon Willison, Agentic Engineering Patterns: <https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/>
- GitHub Spec Kit announcement: <https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/>
- GitHub Spec Kit repo: <https://github.com/github/spec-kit>
- Visual Studio Magazine on Spec Kit (May 12 2026): <https://visualstudiomagazine.com/articles/2026/05/12/github-spec-kit-takes-off-as-antidote-to-piecemeal-vibe-coding.aspx>
- Thoughtworks Radar v34 (April 2026): <https://www.thoughtworks.com/about-us/news/2026/combat-ai-cognitive-debt-radar-v34>
- METR randomized controlled trial (July 2025): <https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/>
- Steve Yegge, "Revenge of the Junior Developer": <https://sourcegraph.com/blog/revenge-of-the-junior-developer>
- Charity Majors: <https://charity.wtf/category/ai/>
- Will Larson, "'Good Engineering Management' Is a Fad": <https://www.oreilly.com/radar/good-engineering-management-is-a-fad/>
- Camille Fournier on AI and tech employment: <https://skamille.medium.com/things-i-currently-believe-about-ai-and-tech-employment-3e712df1dc51>
- HBR on psychological safety and AI (Feb 2026): <https://hbr.org/2026/02/how-to-foster-psychological-safety-when-ai-erodes-trust-on-your-team>
- Ron Westrum's typology in tech orgs: <https://itrevolution.com/articles/westrums-organizational-model-in-tech-orgs/>
- Feynman, "Cargo Cult Science" (1974): <https://calteches.library.caltech.edu/51/2/CargoCult.pdf>
- Mike Hadlow, "Coconut Headphones: Why Agile Has Failed" (2014): <http://mikehadlow.blogspot.com/2014/03/coconut-headphones-why-agile-has-failed.html>
- John Frum movement background: <https://en.wikipedia.org/wiki/John_Frum>
