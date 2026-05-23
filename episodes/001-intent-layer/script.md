# Episode 001 — When the Planes Don't Land

**Subtitle:** Intent, agents, and the coming reshape of engineering work.
**Published:** 2026-05-23
**Summary:** Karpathy moves to Anthropic, GitHub Spec Kit reframes the
source of truth, and Thoughtworks warns about cognitive debt. The main
piece argues that as agents take over the typing, three things get
load-bearing in a way they never were before — capturing intent
explicitly, refusing to pay the cargo cult tax, and treating
psychological safety as a throughput argument rather than a soft skill.
**Target length:** ~30 minutes (~5,200 words at solo pacing).
**Voice:** Host of Claude Cast — first person, opinionated essay format,
weekly cadence with a news segment up top.

---

## Show open

Welcome to Claude Cast. This is your weekly half hour about software
engineering, AI-assisted development, and what it actually takes to
lead engineering teams in twenty twenty-six. I am your host. This is
episode one. Thanks for being here.

The shape of this show, every week, is going to be the same. We start
with a quick look at what landed in the world of agentic engineering in
the last seven days. Then a longer piece — usually an argument, usually
opinionated — about something underneath the news that I think matters.
And we close with one or two things you can actually do this week.

Let us get into it.

---

## This week on the radar

Four things from the last little while that I want to put on your
radar, before the main piece.

One. Andrej Karpathy — the man who, in February of twenty twenty-five,
posted the tweet that named vibe coding, and who was one of the
founding members of OpenAI — joined Anthropic in May. Fortune broke
the story on the nineteenth. I do not have inside information about
why. But the symbolic arc is something. The person who coined the
loose, exuberant, no-code-review mode of working with language models
has gone to work at the company building the most opinionated, most
review-disciplined coding agent product in the market. That tells you
something about where the center of gravity is moving. Not away from
agentic coding. Toward agentic coding with more deliberate guardrails.

Two. Visual Studio Magazine ran a piece on May twelfth about GitHub
Spec Kit — the open source spec-driven development toolkit GitHub
released late last year — and the headline literally calls it, quote,
an antidote to piecemeal vibe coding, end quote. Spec Kit is built
around the line, from, code is the source of truth, to, intent is the
source of truth. We will come back to that line. It is going to be the
spine of the main piece this week.

Three. The Thoughtworks Technology Radar volume thirty-four came out in
April. The phrase they introduced — and which I think we are all going
to be using for the next two years — is cognitive debt. The gap
between the volume of code your team is producing with agents and the
amount of that code your team actually understands. Their warning,
which is sharp, is that coding agents will generate bad code, then use
that bad code as context to generate more bad code, and that humans
are dangerously tempted to step out of the loop. Worth a read.

And four. Harvard Business Review and MIT Technology Review have both
published, in the last few months, on something I have been hearing
about privately for a year. Psychological safety is eroding in AI-
heavy teams. ManpowerGroup put a number on it. AI usage at work is up
thirteen percent year over year. Employee confidence in the technology
is down eighteen percent. People are using the tools more and trusting
them less. And in a lot of teams, saying that out loud feels like
heresy. We are going to come back to this in the main piece too.

That is the week. Now let us go.

---

## Cold open

Picture a scene a lot of you are going to recognize.

It is a Tuesday afternoon. Somewhere — an office, a home setup, a
coffee shop — an engineer is sitting at their desk. On the main screen,
a coding agent is doing something. A controller refactor, maybe. It
has been about four minutes since the human last typed. The agent is
working its way through a Kubernetes operator, reading files, proposing
edits, running tests, reading the test output, proposing more edits.
Once in a while a notification chirps and a small light on a side
keypad changes color. The agent has a question.

And in that pause — that little gap between rounds, where a person is
watching a machine work — there is a thought a lot of us have started
to have.

The diff is not the artifact.

The diff is the exhaust. The artifact is the conversation that
produced it. The reasoning. The false starts. The moment the engineer
said, no, not like that, the constraint here is that the controller
has to be idempotent because we are going to run it from a Tekton task
that retries on failure. That sentence — that piece of intent — never
made it into the codebase. It got compressed into a few lines of Go
and a comment that says, idempotent. And the next person who reads
that comment is going to have no idea why it matters.

That is where this episode starts. Because the question that follows
from this little moment is bigger than it looks.

This episode is about what happens to software when agents do the
typing and humans do the thinking. It is about why most engineering
organizations are about to discover, the hard way, that they have been
mistaking the shape of work for the substance of work for about a
decade. And it is about why I think the most important management
skill of the next five years is going to be one that a lot of senior
leaders have been actively trained out of.

The title of this episode is, "When the Planes Don't Land." You will
see why in a few minutes.

---

## Act one: the Intent Layer

Let me back up.

In February of last year, Andrej Karpathy posted a tweet that named
something a lot of us were already doing. He called it vibe coding. He
said, quote, there's a new kind of coding I call vibe coding, where you
fully give in to the vibes, embrace exponentials, and forget that the
code even exists, end quote. The internet did its usual thing. Half the
people thought it was the future of software. Half thought it was the
end of craft. And a smaller third group — including Simon Willison —
said something more useful.

Willison's line is the one I keep coming back to. He said, I won't
commit any code if I couldn't explain what it does to somebody else. If
an LLM wrote the code but you then reviewed it, tested it thoroughly,
and ensured you could explain how it works — that is software
development, not vibe coding.

That distinction, between vibing and engineering, is the cleanest one I
have heard. And the practical question it raises is, where does the
explanation live?

If I am going to be able to explain what the code does and why it is
structured the way it is, the explanation cannot just live in my head.
Because in three months I will not remember. And in six months somebody
else will own this code, and they certainly will not remember, because
they were never there. The explanation has to live somewhere durable.
And the place we usually put explanations — comments, commit messages,
design docs — those forms were designed for a world where a human typed
the code. They are optimized for the assumption that the typist already
understood it.

That assumption is breaking.

GitHub noticed. In late twenty-twenty-five they released something
called Spec Kit. The tagline is the thing I want you to hear. From,
code is the source of truth, to, intent is the source of truth. The
whole toolkit is built around the idea that you write a specification
first, then a plan, then tasks, and then the agent codes.
Specifications become first-class artifacts. Code is the last mile.

Visual Studio Magazine — and I love that this is the phrase that made
it into the headline — called Spec Kit an antidote to piecemeal vibe
coding. That framing is exactly right. Spec-driven development is what
you do when you have watched vibe coding produce something that works
on Tuesday and is completely opaque on Friday.

But here is what I think most of the coverage of Spec Kit misses. The
point is not the specification. The point is that the specification is
one snapshot of the intent. The intent itself is bigger. It includes
the moment three days ago when you decided against a different design.
It includes the pivot you made at three PM yesterday when a stakeholder
said something offhand in a meeting that turned out to be load-bearing.
It includes the thing you tried for an hour, that did not work, that
you abandoned and never wrote down — and which the next engineer is
going to try again, because there is no record that anyone has been
down that path.

A specification captures intent at a moment. The Intent Layer is the
continuous record of intent across time.

People have started to build personal versions of this. Call it a
captain's log, an intent log, a decision journal — pick the name you
want. The idea is a thing that sits next to your agent sessions and
captures the conversation — the prompts, the pivots, the reasoning —
alongside the diffs. So when you look back at a feature, you do not
just see what changed. You see what you were trying to do when you
changed it. The diff says, I added a retry loop. The log says, I added
a retry loop because the pipeline was eating transient five-oh-threes
from the registry, and I tried three other approaches first that did
not work because of authentication scoping.

That second one is the one you actually need in six months.

Steve Yegge — who is now at Sourcegraph, co-authoring a book on vibe
coding with Gene Kim and Dario Amodei — has been building something
similar he calls Beads. A lightweight, agent-readable decision and
issue store. Different name. Same shape. The whole industry is
starting to converge on the same recognition. When the typing gets
cheap, the explaining gets expensive. And the explaining is where the
actual value lives.

This is the Intent Layer. Different people are going to build it
different ways. The shape that wins might be Spec Kit. Might be Beads.
Might be a thing I have never heard of. But the function is the same.
Capture intent. Make it durable. Make it survive the moment of
creation.

And here is the part I want senior engineers and engineering managers
to internalize. If your team is using agentic tools and you do not have
any way to capture intent alongside the output, you are accumulating
something I have heard the Thoughtworks Radar call cognitive debt. The
gap between how much code your team is producing and how much your team
actually understands. That gap compounds. And the first sign of it is
not a bug. The first sign of it is a meeting where nobody can answer
the question, why did we do it this way.

---

## Act two: the cargo cult tax

OK. Promised you would find out why this episode is called, when the
planes don't land.

In nineteen seventy-four, Richard Feynman gave the commencement address
at Caltech. And he told a story that has become one of the load-bearing
metaphors for how I think about engineering work. He talked about the
cargo cults of the South Pacific. After World War Two, American forces
had built airstrips on Pacific islands, brought in massive amounts of
equipment and supplies — what the locals called cargo — and then left.
The islanders, having watched this happen, did a perfectly reasonable
thing. They built bamboo control towers. They built fake airstrips.
They put coconut shells on their heads as headphones. They made
everything look exactly like what the Americans had been doing. And
they waited for the planes to come back.

The planes did not come back.

Feynman's point — and the line everyone quotes — was, the first
principle is that you must not fool yourself, and you are the easiest
person to fool. His application was to bad science. People who follow
the forms and rituals of scientific investigation without the
underlying mechanism. The shape of science, without the substance.

There is a footnote to this story that I think actually matters more,
and I had never thought about it until I was reading some recent
anthropology for this episode. Modern anthropologists read the cargo
cults very differently than Feynman did. They do not read them as
primitive misunderstanding. They read them as deliberate political
response. The islanders were not confused about planes. They were
performing a counter-ritual against colonial missionaries and labor
exploitation. The coconut headphones were not ignorance. They were a
kind of political statement that we, the outside observers, had
categorized as ignorance because that is how outside observers usually
categorize things they do not understand.

I want you to hold both readings in your head. Because both apply to
engineering management.

Mike Hadlow wrote a famous post in twenty-fourteen called, Coconut
Headphones: Why Agile Has Failed. His argument was that teams adopt the
visible shapes of Agile — standups, sprints, story points, retros,
planning poker — without the underlying mechanism that made those
shapes work in the first place. They get the rituals. They miss the
function. The result is what some people call Agile theater. And what I
have been calling, more generally, the cargo cult tax.

The cargo cult tax is what your organization pays when it adopts the
form of a practice without the substance. Standups that are not really
standups — they are status updates to managers, performed in front of
the team to add the patina of self-organization. Story points that are
not really estimates — they are a number a manager will hold against
you in a year-end review. PR templates that are not really design
discipline — they are a checklist that nobody reads, attached to every
change, including the one-line CSS fix.

These are coconut headphones. They are the visible shape of engineering
rigor. They are not engineering rigor.

Now. Here is where it gets interesting. And here is the part I think
the existing conversation about cargo cult Agile misses.

When agents start doing the typing, the cargo cult tax gets worse. Not
better.

Here is why. The agent does not slow down for the theater. The agent
does not have a manager whose existence depends on it filling out the
PR template. The agent does not lose face if it ships a one-line fix
without a story point estimate. The agent will produce code at a pace
that exposes the ceremony as the bottleneck it always was. Suddenly you
have a team where the engineers can ship a small change in twenty
minutes if they let the agent run, but the system — the ticket queue,
the design doc, the review backlog, the change advisory board — still
takes three days.

And the response, in most organizations, is going to be to add more
ceremony. Not less. Because the ceremony is the thing that the
organization can see. And what gets measured gets defended.

I want to take the more generous reading of the cargo cult for a
second. Remember — the anthropologists say the islanders were not
confused. They were performing a counter-ritual. They had a political
reason. Apply that to your engineering org. The standup as theater is
not always cluelessness. It is often a rational response by a manager
who needs something visible to defend their existence to their manager.
The PR template that nobody reads is not always a misunderstanding of
code review. It is often a CYA artifact for a compliance auditor who is
going to ask, do you have a code review process, and needs to be able
to point at a thing.

These rituals serve a real political function. They are rational from
the inside. They are just not engineering function.

And the moment agents come in and make engineering function ten times
faster, the gap between political function and engineering function
becomes impossible to hide. Your team can ship. Your team is not
shipping. The bottleneck is no longer the typing. It is the
institution.

The companies that win the next five years are going to be the ones
that look hard at every ceremony in their stack and ask, is this an
engineering function, or is this a political function. And if it is
political, is the political function still necessary. And if it is, can
we serve it with one-tenth the ceremony.

That is going to be uncomfortable.

---

## Act three: anarchist management as a throughput argument

The view on this show — and I will own it as a view, not a fact — is
what I call anarchist management. People hear the word anarchist and
they think chaos. That is not what it means here. The word I am
reaching for is the kind of anarchism that comes out of, say, David
Graeber. It means, skeptical of unjustified hierarchy. It means, assume
authority has to defend itself, not the other way around. It means,
distributed decision making, autonomy at the edges, leadership that
emerges from competence and consent rather than from a title on a
slide.

For most of the last decade that has been an ideological commitment.
Something a lot of us in management believed because we thought it was
right, and which we had to defend to skeptical leaders who thought we
were being soft, or naive, or insufficiently rigorous.

What I want to argue in the rest of this episode is that, in the
agentic era, anarchist management — distributed authority, autonomy,
psychological safety, authentic communication — stops being an
ideology. It becomes a throughput argument. It becomes the only
architecture that scales.

Let me show my work.

There is a study from METR — that is the Model Evaluation and Threat
Research organization — published in July of twenty twenty-five. They
ran a randomized controlled trial of experienced open source developers
using AI tools. Before the study, the developers forecasted AI would
make them twenty-four percent faster. After the study, they self
reported feeling twenty percent faster. The actual measurement: they
were nineteen percent slower.

Read that again. They felt twenty percent faster. They were nineteen
percent slower. The gap between perception and reality was about forty
percentage points.

Now, the obvious caveat — and Steve Yegge makes it loudly — is that the
study used tools available before March of twenty twenty-five. Tooling
has changed. Maybe the result would not replicate today. Fine. But hold
onto what the study showed about humans, not about tools. When people
are using AI, they are systematically wrong about how fast they are.
They think they are shipping more. They are sometimes shipping less.

What follows from that? It means the work of telling people the truth
about their output becomes massively more important. And the work of
telling people the truth requires a culture where people can be told
the truth. Without being punished. Without their performance review
getting weird. Without it ending their relationship with the person who
delivered the news.

Charity Majors put this beautifully. She said, writing code was never
the bottleneck. Validation is. Validation, in this context, does not
just mean tests. It means a human, with skin in the game, looking at
this output and saying, yes this is right, or, no this is wrong. It
means the social act of holding a piece of work to the standard.

And the social act of validation requires what Amy Edmondson calls
psychological safety. Which means: the belief that you can speak up —
point out a problem, ask a dumb question, disagree with the agent's
plan, push back on the senior engineer's design — without being
punished or humiliated.

If you do not have that, here is what happens in your org over the next
twelve months. Engineers using agents are going to produce a lot more
code. The code is going to look plausible. The code is going to
compile, pass the tests the agent wrote, and ship. And somewhere
downstream, a customer is going to hit an edge case the agent did not
think about. Or a security review is going to find a thing. Or the on-
call engineer at two A M is going to discover that none of this code
actually composes the way the architecture diagram says it does. And in
a healthy team, somebody on the inside saw that coming and said
something three weeks earlier. And in an unhealthy team, three people
saw it coming and did not say anything, because the last time someone
said something they got labeled, not a team player.

That is the throughput argument. Psychological safety is not a nice to
have. It is the literal critical path of shipping software when the
bottleneck has moved from typing to judgment.

Ron Westrum — and this is a name every engineering manager should know
if you do not already — wrote about this back in two thousand four. He
described three kinds of organizational culture. Pathological, which is
power oriented. Bureaucratic, which is rule oriented. And generative,
which is performance oriented. The headline finding from his research,
which the DORA folks have validated more recently in software contexts,
is this. The single best predictor of organizational effectiveness is
information flow. Generative cultures surface bad news quickly.
Pathological cultures punish the messenger. Bureaucratic cultures route
bad news through process until it dies.

Now sit with that for a second in the context of agentic engineering.
Information flow is the predictor. The agent is generating information
at ten times the previous rate. If your culture is pathological or
bureaucratic, the agent is going to overwhelm the human cycles
available to process that information, and your team is going to be
drowning in produced-but-not-validated code within a quarter. If your
culture is generative — if information flows freely, if people can call
out bad output without consequence, if authority is distributed enough
that any engineer can stop the line — then you have a chance.

Will Larson, who I think is one of the sharpest people writing about
engineering management right now, published a piece called, Good
Engineering Management Is a Fad. The argument is not that good
engineering management does not exist. The argument is that the
practices we built around it were calibrated to a set of constraints
that have changed. Managers who built their careers on those practices
are being told the foundation is moving. And one of the practices that
needs to change the most is the cultural assumption that managers add
value by controlling. Because when the typing is free, control becomes
the slowest part of the system.

Camille Fournier has been making a parallel prediction. Not that the
pyramid flattens. Not that we hire fewer juniors and more seniors.
Something stranger. That teams get smaller overall, and that prompt and
vibe and intent skills move outward, into the rest of the knowledge-
worker population. Marketing teams. Operations teams. The boundary of
what counts as engineering blurs. Which means the discipline that
engineering historically supplied — the slow, careful judgment about
whether a thing should actually exist — has to come from somewhere.
And if it does not come from the agentic tooling, and it does not come
from the diffusing pool of part-time engineers, it has to come from the
managers and the platforms.

The other reason to take psychological safety seriously: it is eroding
in AI-heavy teams. Harvard Business Review and MIT Tech Review both
published on this in early twenty twenty-six. The number that stuck
with me — from ManpowerGroup — is that AI usage at work went up
thirteen percent year over year while employee confidence in the
technology dropped eighteen percent. People are using these tools more
and trusting them less. And in a lot of orgs, saying that out loud — I
do not actually trust this output, or, I think we are shipping too fast
— feels like heresy. Like you are not on the bus.

That is a cultural failure that has direct engineering consequences.
And the fix is not more tools. It is not more agents. It is not more
ceremony. The fix is, very specifically, leaders who model the act of
questioning their own AI output in public, and who reward — actively
reward, in performance reviews and in promotions — the engineers who
flag problems.

This is what I mean by anarchist management as a throughput argument.
Distributed authority is not ideology. It is the only architecture that
lets information flow at the speed agents produce it. Autonomy is not a
perk. It is the condition under which judgment scales. Psychological
safety is not soft. It is the literal mechanism by which bad agent
output gets caught before it ships.

---

## Close

I want to land this somewhere actionable.

I have been pointing at a few things in this episode. The Intent Layer
— the idea that what we need to capture is the reasoning, not just the
diff. The cargo cult tax — the ceremony your organization charges you
for in exchange for political cover. And the throughput argument — that
the things we used to call soft skills are now the load-bearing
mechanism of engineering output.

Here is what I would ask you to do this week, if any of this lands.

First. Name one piece of management theater in your org. Just one.
Something you do every week, or every sprint, that, if you are honest,
serves a political function and not an engineering function. Do not try
to kill it. Just name it. Out loud, to one other person you trust.
Because the first move in dismantling theater is admitting it is
theater.

Second. Find one decision from a recent change in your codebase that
is not written down anywhere. One pivot. One rejected design. One
constraint that informed how something got built. Write it down. Put it
in the commit message, or a design doc, or a comment, or a personal log
if your org does not have a good place. Do not worry about
systematizing. Just plant the seed of the idea that intent is the thing
worth recording.

Third — and this is the hardest one. The next time an agent produces
something that looks plausible and you have a small feeling that it is
not quite right, say something. To yourself, to your team, in the
review. Do not let the plausibility of the output silence the judgment
that you have, that the machine does not. Validation is the bottleneck.
You are the validator. Do not outsource that to vibes.

Karpathy — the man who named vibe coding in a tweet in February of
twenty twenty-five — defected to Anthropic in May of twenty twenty-six.
The guy who coined the loose mode is now at the company building the
most opinionated coding-agent product in the market. I think about that
arc a lot. The pendulum is swinging. The first wave of agentic coding
was, let it rip and see what happens. The second wave, which is the
one we are entering, is, let it rip within constraints we deliberately
specified. Specifications. Plans. Reviews. Intent.

The future I am betting on is one where the most valuable engineers and
the most valuable engineering managers are the ones who can articulate
intent clearly, capture it durably, validate output honestly, and run a
team where people are safe to tell the truth. That set of skills does
not have a single name yet. The closest thing might be what some people
call the staff engineer archetype, or what some people call the
technical leader, but the role is going to evolve, and the title is
going to lag the function by a couple of years, like it always does.

In the meantime, the planes are not landing. The agents are typing. The
ceremonies are still happening. And the gap between the shape of
engineering work and the substance of engineering work is the widest it
has ever been.

Do not put coconut shells on your head.

Land the plane.

---

## Sign-off

That is episode one of Claude Cast. If any of this resonated — or if
any of it made you mad — both are useful signals. The way to find us
next week is the same way you found us this week. Subscribe in whatever
podcast app you are using. Tell one other person who works in
engineering.

Next week, we are going to do a piece on what I am starting to think of
as the new code review. When the agent writes the first draft, what is
the human reviewing for, and how is that different from what code
review used to be. There is a real practice forming around this. I want
to walk through it.

Until then. Capture intent. Validate honestly. Name your theater. And
keep the planes landing.

Thanks for listening. This has been Claude Cast.
