# Holding Pattern

*When the agent writes the code for free, the bottleneck doesn't vanish — it moves to verification, and then it keeps climbing upstream until it lands in the one chair only a human can sit in: deciding what "correct" even means.*

*Published 2026-06-20. The audio version of this piece is
[Land the Plane episode 4](./episode.mp3); this post covers the same
ground for people who'd rather read.*

---

## This week on the radar

Four things from the last little while.

**The generation numbers got loud.** In April, Google's CEO said
[75% of new code](https://devops.com/google-ceo-says-75-of-new-code-is-ai-generated/)
at the company is AI-generated. Microsoft puts its number around
[20–30%](https://www.entrepreneur.com/business-news/ai-is-taking-over-coding-at-microsoft-google-and-meta/490896);
a Sonar survey pegs the industry at ~42% of code AI-generated or
-assisted; and a batch of Y Combinator's W25 startups reported that
**25% of them had 95%-AI-generated codebases.** Hold these loosely —
"AI-generated" is a slippery, self-reported, undefined phrase, and a CEO
quoting a percentage is marketing, not measurement. But discounted hard,
the direction is unmistakable. Generation is no longer the expensive
part. Typing the code is no longer the thing between you and shipping.

**The trust gap didn't move an inch.** Veracode's
[Spring 2026 GenAI Code Security report](https://www.veracode.com/blog/spring-2026-genai-code-security/)
is the most clarifying number I've seen all year. Across *two years* of
bigger, smarter, supposedly revolutionary models, the share of generated
code that passes a basic security check has stayed **flat at ~55%** —
meaning ~45% of AI-generated code ships with a known vulnerability. The
models got dramatically better at writing code that *works*. They got
zero better at writing code that's *safe*. Veracode's framing: these
models "optimize for usefulness and plausibility, not security."
*Plausibility.* The code looks right, compiles, runs, demos — and nearly
half the time it's carrying a hole. (Independent corroboration: an AppSec
study found OWASP-Top-10 vulns in
[25.1% of samples](https://www.veracode.com/blog/spring-2026-genai-code-security/);
Black Duck's 2026 OSSRA reports mean vulnerabilities per codebase up
107% year over year.) Functional correctness raced ahead. The
correctness that *matters* stayed exactly where it was.

**The robot that writes the plane can also inspect it.** Anthropic's
Frontier Red Team published work on an agent that doesn't write code — it
*verifies* it. It reads a codebase, infers what the code is supposed to
do, writes [property-based tests](https://red.anthropic.com/2026/property-based-testing/)
to check that, runs them, and reflects to confirm real bugs. Pointed at
100 popular Python packages, **56% of its bug reports were valid** — and
of its top-ranked findings, **86% were real.** It found genuine bugs in
NumPy, SciPy, and Pandas — code thousands of experts have stared at for
years ([paper](https://arxiv.org/pdf/2510.09907)). Patches merged. The
same agentic technology that writes the code can be turned around and
pointed at proving it.

**The bottleneck became a product category.**
[Opslane's](https://www.opslane.com/) entire pitch is one sentence:
*agents write the code, Opslane proves it works.* It drives a real
browser against your running app, checks each acceptance criterion, and
hands you pass/fail with screenshots —
[before you push](https://www.opslane.com/blog/verification-bottleneck).
A whole company now exists to sit in the gap between "the agent wrote it"
and "I trust it." When a startup category forms around a gap, that's the
market telling you where the pain is. It's not generation. It's *proof.*

---

## Cold open: forty planes, one runway

Picture a small team. Three engineers. A year ago, three engineers was
three pairs of hands, and the software you could produce was bounded by
how fast those three people could type.

Now the same three, today, each running a couple of agents. On a good
morning this team of three is effectively a team of nine or twelve, and
the agents don't tire or break for lunch. By 11 a.m. they've generated
forty pull requests. A quarter's worth of last year's output, sitting
there, green, before lunch.

Here's the scene I want you to see. It's not triumph. It's a holding
pattern.

Those forty PRs can't land — not all at once. There's one runway, and the
runway is **verification**: actually proving each change is correct, is
safe, does what it was meant to, and doesn't quietly break something three
modules over. That runway has throughput. A human can only truly verify so
much in a day. So the planes stack up and circle. Forty changes in the
air; a runway that can clear maybe six a day with real confidence.

The team *feels* incredibly productive — look at all that output. But
watch what actually ships, verified and trusted, and the number barely
moved. They didn't get four times faster. They built a magnificent backlog
of un-landed work and called it velocity.

Nobody warned you about this when they sold you the agent. They said
generation was the bottleneck — they were right, and they removed it. And
the moment they did, you discovered the bottleneck was never really
generation. It only *looked* that way because generation was so slow it hid
everything behind it. Speed up the writing, and the real constraint — the
one that was always there — steps out of the shadow.

The real constraint is *proof.* This piece is about what you do when proof
gates everything. There's an old law that tells you exactly what happens
next — and then a twist the law doesn't prepare you for.

---

## The constraint just moved — it didn't leave

The law first, because it's older than software and merciless.

In 1984, Eliyahu Goldratt's business novel *The Goal* laid out the
[Theory of Constraints](https://www.tocinstitute.org/theory-of-constraints.html).
Almost insultingly simple, which is why people keep failing to apply it:
any system has exactly one bottleneck at a time — one slowest step — and
the total throughput of the whole system is set by that step. Not the
average. The slowest stage. **Speed up a step that isn't the bottleneck
and you produce zero additional throughput.** All you do is pile up
inventory in front of the real constraint. In a factory it's parts
stacking against a wall. In our world it's forty PRs circling the runway.

Now [Amdahl's Law](https://en.wikipedia.org/wiki/Amdahl%27s_law), 1967:
the speedup from making one part of a process faster is hard-capped by the
fraction you *didn't* speed up. If writing code was, say, a quarter of the
total work of shipping software — and the rest was understanding the
problem, verifying the solution, integrating, deploying, fixing what broke
— then making the writing *infinitely* fast attacks only a quarter of the
process. Best case, you get maybe 1.3× overall, and then you slam into the
wall of everything you didn't touch.

This is why teams report a strange, frustrating thing right now. The
generation speedup is real — code genuinely appears in seconds — and yet
the date the feature ships to customers barely moved. No mystery. It's
Goldratt and Amdahl. You made the non-bottleneck infinitely fast, and the
bottleneck didn't care. It watched the inventory pile up.

So where did the bottleneck go? *Nowhere.* That's the point. It was always
verification — the proving, the testing, the gaining of justified
confidence that this code is correct. Verification was always the expensive
part. It was just *hidden*, because when writing took two weeks, the two
days of verifying looked cheap. Now writing takes ten minutes, verifying
still takes two days, and the two days is suddenly the whole story. The
cost didn't increase. It got *unmasked.*

And the economics flip in a way I find genuinely clarifying. When
generating a line cost real human effort, the cost of software lived in
generation. Push the cost of a generated line toward zero — roughly where
we're headed — and the entire remaining cost of software relocates to one
place: **verification.** If making the thing is free, the whole cost of
software becomes the cost of *proving the thing is right.* That's not a
small shift. It's the economic center of gravity of our field picking
itself up and moving from writing to proving.

So: the bottleneck moved from generation to verification. The constraint
didn't leave — it relocated, and got brutally visible. Most of the industry
is right here, staring at the holding pattern, wondering why all that speed
didn't turn into shipping.

The interesting part — almost nobody's talking about it — is what happens
when you actually try to *fix* it.

---

## The good news: verification is more automatable than you think

Here's the upside. The real one.

When people hear "verification is the bottleneck now," they assume it's
permanent, because they picture verification as a human reading code, and
humans read at a fixed speed. If that were true, the small team would be
stuck in the holding pattern forever.

It isn't true. Verification is far more automatable than the writing ever
was. Verification is, at root, *checking work against a standard* — and
checking is a more mechanizable act than creating. It's the whole intuition
behind why some problems are hard to solve but easy to check. Generation is
creative. Verification is, largely, checkable. And checkable things become
machines.

So watch what a serious team does to widen the runway. Not ten more humans
reading diffs — they **industrialize the proving.**

**They write property-based tests.** This is the most important idea here,
so slow down. A normal test says "input 3 → output 6." One example. A
[property-based test](https://www.themoonlight.io/en/review/use-property-based-testing-to-bridge-llm-code-generation-and-validation)
says something stronger: "for *any* number, the output should always be
even" — and the machine generates a thousand random inputs trying to break
the rule. You're not checking examples anymore; you're checking
*invariants* — properties that hold for all inputs. The output of a sort is
always sorted. Reverse a list twice, get the original. Claims about the
*shape* of correctness.

Property-based testing is also the perfect answer to the obvious objection:
*if the agent writes the code and also the tests, isn't that circular — the
fox guarding the henhouse?* Great objection. The researchers even named the
failure mode: the **"cycle of self-deception,"** where the test inherits the
exact wrong assumption the code has, so it passes and everyone feels safe
and the bug sails through. Property tests break the cycle, because to state
a property — *sorting always produces sorted output* — the agent commits to
an independent claim about what correct *means.* It's not memorizing buggy
behavior; it's asserting a truth that must hold no matter what, and then a
fuzzer hammers it with cases the agent never imagined. The invariant lives
*outside* the code's own assumptions. That's what breaks the circle.

Not theoretical: Anthropic's Frontier Red Team result *is* this technique,
run by an agent, at scale — inferring properties, writing tests, finding
real bugs in NumPy, SciPy, Pandas, with 86% of top findings genuine. A
verification machine built from the same agentic parts as the generation
machine. And it works.

It extends to the parts of your system that used to be *unverifiable* —
features with a model inside them, where the output is non-deterministic and
there's no single right answer to assert. A year ago you shipped those on
vibes and prayer. Now there's a discipline for it: **evals.** You write a
graded rubric for what "good" looks like, run the feature against a hundred
cases, and score it automatically on every change. Verification of the
fuzziest software we build, turned into a number you can watch. Even the
unverifiable got verifiable.

And it extends to *triage.* A January study of over
[33,000 agent-authored PRs](https://arxiv.org/pdf/2601.00753) built a
"circuit breaker" that predicts, from cheap signals available the instant a
PR is created — file types, patch size — whether it'll be expensive to
verify, *before a human looks*, accurately enough to be a real gate. So you
let a machine sort the planes: these forty land on autopilot, these six need
a human in the tower, and you spend scarce human verification only where it
warrants.

The runway isn't fixed. You can widen it — dramatically — with the same
automation that created the flood. A small team really can industrialize
verification and capture the leverage the agents promised: not just generate
faster, but *prove* faster, and so *ship* faster. That's the upside, and
it's real. The holding pattern is not a life sentence. You can build more
runway.

But there's one honest caveat that turns this whole piece, and it comes from
1969.

---

## The chair no machine can sit in

In 1969, Edsger Dijkstra wrote one of the most-quoted sentences in our
field, and almost everyone quotes it without feeling its weight:
[*"Program testing can be used to show the presence of bugs, but never to
show their absence."*](https://en.wikiquote.org/wiki/Edsger_W._Dijkstra)

*Never to show their absence.* Read that against everything in the last
section. All that beautiful automated verification — property tests,
fuzzers, browser-driving robots, circuit breakers — every bit of it can
only ever do *one* thing: find bugs. It can show the code is wrong. It can
never prove the code is *right.* A passing test doesn't mean correct; it
means *not yet caught.* Run a million property checks and all you've earned
is a million failures to disprove. Verification bounds your risk. It never
certifies your truth.

And that crack — that one word, *absence* — is where the whole thing comes
apart in the most interesting way. It means the bottleneck has no *bottom.*
Watch: you automate a verification stage, you speed it up — and by
Goldratt's law the constraint doesn't vanish, it moves to the next slowest
stage. So you automate that one. It moves again. **Every verification stage
you mechanize hands the bottleneck one step upstream.** The constraint isn't
sitting still waiting to be solved. It's *climbing.*

So follow it all the way up and ask the real question: where does it stop?
When the constraint has climbed past the writing, the unit tests, the
integration tests, the security scans, the browser checks — where's the one
stage it can climb to and get *stuck*, because no machine can do it?

The answer has a 40-year-old name:
[**verification vs. validation**](https://www.scrum.org/resources/blog/doing-right-thing-right-validation-and-verification).
Verification asks: *are we building the thing right?* Does the code match
the spec? That has a machine answer — you can check code against a spec.
Validation asks: *are we building the right thing?* Does this actually solve
the problem it was meant to? That has *no* machine answer. To check whether
the code does the right thing, you must know what the right thing *is* — and
that lives only in a human head.

Make it concrete. The agent builds a function to calculate a refund. Clean
code. Tests pass. Property checks hold. Security scan green. Every machine
in your pipeline signs off: built right, matches spec, internally flawless.
And it refunds the wrong amount, because the spec said *refund the full
purchase price* and the business needed *minus a restocking fee* that nobody
wrote down. Every verification machine you own says that code is correct.
And it's wrong. Not buggy — *wrong.* It does precisely what it was told and
precisely not what was needed. No test catches it, because the test and the
code were built from the same flawed understanding of correct. The gap isn't
in the code. It's between the code and the world — and machines can't see the
world. Only you can.

Computer scientists have a sharper name for the bottom of this: the
[**oracle problem**](https://dl.acm.org/doi/10.1145/3715107). In testing, an
oracle tells you whether an output is correct. The deep, unfixable
difficulty: for any interesting program, deciding whether an output is
correct is — verbatim — *"akin to guessing the intention of the developer
who wrote the code."* There's no test for intention. No fuzzer for "what did
the human actually want." The machine checks code against spec all day. It
cannot check the spec against your actual desire, because your desire isn't
written anywhere a machine can read. It's in you.

This is the grand challenge Microsoft Research named this March, in a
[paper by Shuvendu Lahiri](https://www.microsoft.com/en-us/research/publication/intent-formalization-a-grand-challenge-for-reliable-coding-in-the-age-of-ai-agents/)
I can't recommend enough. The phrase to leave holding: AI-generated code is
**"plausible by construction, but not correct by construction."** *Plausible
by construction* — the model is built to produce code that *looks* right
(Veracode's exact word from the news: plausibility). The gap between
plausible and correct he calls the **"intent gap,"** which has always
plagued software but which AI
[*"amplifies to an unprecedented scale"*](https://arxiv.org/pdf/2603.17150),
because now you generate plausible code faster than you can ever specify what
correct would mean. And the killer line that closes the loop: *"there is no
oracle for specification correctness other than the user."*

There it is. The chair no machine can sit in. You can automate writing the
code, testing the code, increasingly reviewing the code. What you *cannot*
automate — not because the tech is immature but because it's a logical
impossibility, an oracle problem, a theorem — is deciding what the software
is *supposed to do* in the first place. The constraint climbs and climbs and
comes to rest, finally and permanently, on **specification.** On intent. On a
human saying, with enough precision that it can be checked against, *here is
what correct means.*

So, the thesis, plainly: the agent didn't eliminate the bottleneck. It
relocated it — out of your hands, where it was typing, up through
verification, where it's increasingly the machine's, all the way to the one
node with no machine oracle. The engineer's job isn't moving from writing
code to reviewing code. It's moving from writing code to **specifying
intent.** The most valuable thing you can do in the agentic era is not type,
and not even check. It's to know, precisely, what you actually want — and say
it clearly enough that everything downstream, human and machine, can be
measured against it. The bottleneck became *you.* The good kind. The you that
decides what correct means.

---

## What to do this week

1. **Write the acceptance criteria *before* the agent writes the code.** Not
   after. Most people prompt, look at what comes back, and then try to decide
   if they like it — backwards in the exact way the oracle problem predicts,
   because you're verifying against a standard you never set. Flip it. Spend
   the first twenty minutes writing, in plain specific language, what *done*
   means: what it must do, what it must never do, how you'd know it worked.
   Then generate against that. You've done the one piece of work no machine
   can do for you, at the only point where it's cheap — the beginning.
   *Approve the spec, not just the diff.*

2. **Industrialize your verification on purpose — build runway.** If you're a
   working engineer, this week, *genuinely learn property-based testing.* It's
   the highest-leverage testing skill of the next five years, because it's how
   you state invariants — claims about what must always be true — and
   invariants are exactly what survive when a machine writes both the code and
   the example tests. Stop writing tests that check one input/output; start
   asserting a property and letting the machine try a thousand times to break
   it. Let your agents write those tests too — but *you* decide which
   properties matter, because choosing the property is a small act of
   specification, and that part is yours.

3. **(Managers) Stop measuring generation.** Lines of code, PRs opened, story
   points, agent activity — every one measures *planes in the air,* and planes
   in the air are worthless. They're inventory: the holding pattern in the
   costume of progress. Measure *landed* work — changes specified, verified,
   and trusted in production. Then the counterintuitive step: **take your best
   engineers off the keyboard.** The instinct is to point your strongest people
   at generating more, faster. Exactly wrong. Point them at the top of the
   river — at specification, at deciding what correct means, at writing the
   criteria everything else is measured against. That's now the highest-value
   chair in the building, and it's the one chair you can never automate your
   way out of needing filled.

Back to the holding pattern: three engineers, forty planes circling, one
runway. The agent didn't make you a better pilot. It filled your sky with
traffic and handed you the tower. And the job in the tower was never to fly
the planes. It was to know where each one is supposed to land — and that, it
turns out, is the one thing it could never tell you.

So stop trying to land more planes faster. Get clear on the destination
first. The whole sky is waiting on you to know where it's going.

Land the plane. But decide where it's going first.

---

## Sources

- Google CEO: 75% of new code AI-generated — https://devops.com/google-ceo-says-75-of-new-code-is-ai-generated/
- AI coding at Microsoft, Google, Meta (20–30%) — https://www.entrepreneur.com/business-news/ai-is-taking-over-coding-at-microsoft-google-and-meta/490896
- Veracode, Spring 2026 GenAI Code Security report (~55% pass rate, flat) — https://www.veracode.com/blog/spring-2026-genai-code-security/
- Anthropic Frontier Red Team, property-based testing agent — https://red.anthropic.com/2026/property-based-testing/
- Property-based testing agent (paper) — https://arxiv.org/pdf/2510.09907
- Opslane — https://www.opslane.com/
- Opslane, "the verification bottleneck" — https://www.opslane.com/blog/verification-bottleneck
- Antoine Buteau, "agent coding costs hide in review, not generation" — https://www.antoinebuteau.com/agent-coding-costs-hide-in-review-not-generation/
- Property-based testing to bridge LLM generation and validation ("cycle of self-deception") — https://www.themoonlight.io/en/review/use-property-based-testing-to-bridge-llm-code-generation-and-validation
- Circuit-breaker study, 33,707 agent-authored PRs — https://arxiv.org/pdf/2601.00753
- Goldratt, Theory of Constraints — https://www.tocinstitute.org/theory-of-constraints.html
- Amdahl's Law — https://en.wikipedia.org/wiki/Amdahl%27s_law
- Dijkstra, "testing shows the presence, not the absence, of bugs" — https://en.wikiquote.org/wiki/Edsger_W._Dijkstra
- Verification vs. validation — https://www.scrum.org/resources/blog/doing-right-thing-right-validation-and-verification
- The oracle problem (test oracles) — https://dl.acm.org/doi/10.1145/3715107
- Microsoft Research, "Intent Formalization: A Grand Challenge…" (Lahiri) — https://www.microsoft.com/en-us/research/publication/intent-formalization-a-grand-challenge-for-reliable-coding-in-the-age-of-ai-agents/
- Intent Formalization (paper) — https://arxiv.org/pdf/2603.17150
