# Episode 004 — Holding Pattern

**Subtitle:** When the agent writes the code for free, the bottleneck does not vanish — it moves to verification, and then it keeps climbing upstream until it lands in the one chair only a human can sit in: deciding what "correct" even means.
**Topics:** verification, AI-assisted development, testing, theory of constraints, specifications, engineering leadership
**Published:** 2026-06-20
**Summary:** Last week was the cost of agentic coding. This week is the upside — told honestly. Agents now write most of the code, and for free, which means generation stopped being the thing that gates how fast you ship. So what gates it now? The answer is verification — proving the code is actually right — and the good news, the real upside, is that verification is far more automatable than people think. Agents can write the tests, run the fuzzers, triage their own pull requests. But here is the twist that makes this episode: every time you automate a stage of verification, the bottleneck does not disappear. It climbs one step upstream. And it keeps climbing until it reaches the one node in the whole pipeline that has no machine answer — deciding what the software is supposed to do in the first place. That is where the work goes now. Not typing. Not even reviewing. Owning the spec.
**Target length:** ~30 minutes (~5,000 words at solo pacing).
**Voice:** Host of Land the Plane — first person, opinionated essay format, weekly cadence with a news segment up top.

---

## Show open

Welcome to Land the Plane. This is your weekly half hour about software engineering, AI-assisted development, and what it actually takes to lead engineering teams in twenty twenty-six. I am your host. This is episode four. Thanks for being here.

Same shape as always. A few things that landed this week, up top. Then a longer piece — one argument, usually opinionated. Then one or two things you can actually do before next week.

Last week I made you a promise. I said we had spent three episodes on what the agent costs us, and that this week I would turn the lens around and talk about the upside — what genuinely gets better, what this lets a small team do that a small team never could before. I am keeping that promise. This is the upside episode. But I am going to tell it honestly, which means it has a sting in the tail. Let us get into it.

---

## This week on the radar

Four things on the radar before the main piece.

One. The generation numbers got loud this quarter. In April, the chief executive of Google said that seventy-five percent of new code at the company is now AI-generated. Microsoft has put its number somewhere around twenty to thirty percent. A survey out of Sonar pegged it at forty-two percent of all code being AI-generated or AI-assisted across the industry. And the wildest one — a batch of Y Combinator startups from earlier this year, where roughly a quarter of the companies reported that ninety-five percent of their codebase was AI-generated. Now, I want you to hold these numbers loosely, because "AI-generated code" is a slippery, self-reported, undefined phrase, and a chief executive quoting a percentage on an earnings call is marketing, not measurement. But even discounted hard, the direction is unmistakable. Generation is no longer the expensive part. Typing the code is no longer the thing standing between you and shipping.

Two — and this is the counterweight, so listen to it next to the first one. Veracode put out their Spring twenty twenty-six security report, and it is the most clarifying number I have seen all year. They have been testing AI-generated code for security across two years of model releases — two years of bigger, smarter, supposedly revolutionary models. And the share of generated code that passes a basic security check has stayed flat. Flat at about fifty-five percent. Which means roughly forty-five percent of AI-generated code ships with a known vulnerability in it. And here is the part that should stop you cold. The models got dramatically better at writing code that works. They did not get one bit better at writing code that is safe. Veracode's own framing is that these models optimize for usefulness and plausibility — not for security. Sit with that word. Plausibility. The code looks right. It compiles, it runs, it passes the demo. And nearly half the time it is carrying a hole. The functional correctness raced ahead. The correctness that actually matters stayed exactly where it was.

Three. On the genuinely hopeful side — because the upside is real and I promised it to you. Anthropic's Frontier Red Team published work on an agent that does not write code. It verifies it. The agent reads a codebase, infers what the code is supposed to do, writes property-based tests to check that, runs them, and reflects on the results to confirm whether it has found a real bug. They pointed it at a hundred popular Python packages. Fifty-six percent of the bug reports it filed were valid — and when they ranked the findings, eighty-six percent of the top-scored ones were real. It found genuine bugs in NumPy, in SciPy, in Pandas — the libraries that the entire data science world is built on, code that has been read by thousands of humans. Patches got merged. Read that as what it is. The same agentic technology that writes the code can be turned around and pointed at verifying it. The robot that flies the plane can also, it turns out, help inspect the plane.

And four. The bottleneck has become a product category. There is a tool called Opslane whose entire pitch is one sentence — agents write the code, Opslane proves it works. It drives a real browser against your running app, checks each acceptance criterion you gave it, and hands you pass or fail with screenshots, before you ever push. A whole company now exists to sit in the gap between "the agent wrote it" and "I trust it." When a startup category forms around a gap, that is the market telling you where the pain actually is. The pain is not generation anymore. It is proof. Let us talk about why.

---

## Cold open

Picture a small team. Three engineers. A year ago, three engineers was three engineers — three pairs of hands, three people typing, and the amount of software you could produce was roughly bounded by how fast those three people could write it.

Now picture the same three engineers today. Each one is running a couple of agents. So on a good morning, this team of three is effectively a team of nine or twelve, and the agents do not get tired and do not take lunch. By eleven A M they have generated forty pull requests. Forty. A whole quarter's worth of last year's output, sitting there, green, before lunch.

And here is the scene I actually want you to see. It is not a scene of triumph. It is a scene of a holding pattern.

Because those forty pull requests cannot land. Not all at once. There is one runway, and the runway is verification — the act of actually proving each change is correct, is safe, does the thing it was supposed to do, and does not quietly break something three modules over. And that runway has a throughput. A human can only truly verify so much in a day. So the planes stack up. They circle. Forty changes in the air, and a runway that can clear maybe six of them a day with any real confidence.

The team feels incredibly productive. Look at all that output. Look at all those planes. But watch what actually ships, what actually gets to production verified and trusted, and the number barely moved. They did not get four times faster. They built a magnificent backlog of un-landed work and called it velocity.

This is the thing nobody warned you about when they sold you the agent. They told you generation was the bottleneck, and they were right, and they removed it. And the moment they removed it, you discovered the bottleneck was never really generation at all. It just looked that way because generation was so slow that it hid everything behind it. Speed up the writing, and the writing stops being the constraint, and the real constraint — the one that was always there — steps out of the shadow and into the light.

The real constraint is proof. And this episode is about what you do when proof becomes the thing that gates everything. Because there is a law here, an old one, that tells you exactly what is going to happen next. And then there is a twist that the law does not prepare you for.

---

## Act one: the constraint just moved — it did not leave

Let me give you the law first, because it is older than software and it is merciless.

In nineteen eighty-four, a physicist named Eliyahu Goldratt wrote a business novel called The Goal, and it laid out something he called the Theory of Constraints. The idea is almost insultingly simple, which is why people keep failing to apply it. Any system — a factory, a pipeline, a team — has exactly one bottleneck at a time. One slowest step. And the total throughput of the entire system is set by that one step. Not by the average speed. By the slowest stage.

And here is the punchline that matters for us. If you go and speed up a step that is not the bottleneck, you produce exactly zero additional throughput. Zero. All you do is pile up inventory in front of the real constraint. You make more half-finished work that sits there and waits. In a factory it is physical parts stacking up against a wall. In our world it is forty pull requests circling the runway.

Now put the other old law next to it. Amdahl's law, from nineteen sixty-seven. Gene Amdahl was thinking about parallel computing, but the shape of the idea is universal. The total speedup you can get from making one part of a process faster is capped — hard capped — by the fraction of the process you did not speed up. Let me make that concrete for software. If writing code was, say, a quarter of the total work of shipping software — and the other three quarters was understanding the problem, verifying the solution, integrating it, deploying it, fixing what broke — then even if you make the writing infinitely fast, instant, free, you have only attacked a quarter of the process. The very best you can do is get a little faster overall. Maybe one-point-three times. And then you slam into the wall of everything you did not speed up.

This is why teams are reporting this strange, frustrating thing right now. The agents are real. The generation speedup is real — it is not hype, the code genuinely appears in seconds. And yet the date the feature actually ships to customers has barely moved. People are confused by that. They feel four times faster and they ship roughly the same. There is no mystery here. It is Goldratt and it is Amdahl. You made the non-bottleneck infinitely fast, and the bottleneck did not care. It just watched the inventory pile up against it.

So where did the bottleneck go? It did not go anywhere. That is the whole point. It was always verification — the proving, the testing, the reviewing, the gaining of justified confidence that this code is correct. Verification was always the expensive part. It was just hidden, because back when writing the code took two weeks, the two days of verifying it looked cheap by comparison. Now writing the code takes ten minutes, and verifying it still takes two days, and suddenly the two days is the whole story. The cost did not increase. It got unmasked.

And once you see it this way, the economics flip in a way I find genuinely clarifying. When generating a line of code cost real human time and effort, the value and the cost of software lived in the generation. That is where the money went. But push the cost of generating a line down toward zero — which is roughly where we are headed — and every bit of the remaining cost of software relocates to one place. Verification. If making the thing is free, then the entire cost of software becomes the cost of proving the thing is right. That is not a small shift in where the work is. That is the entire economic center of gravity of our field picking itself up and moving from one place to another. From writing, to proving.

So that is act one, and it is just the setup. The bottleneck moved from generation to verification. The constraint did not leave. It relocated, and it got brutally visible. Most of the industry is right here, right now, staring at the holding pattern and wondering why all that speed did not turn into shipping.

The interesting part — the part almost nobody is talking about — is what happens when you actually try to fix it.

---

## Act two: the good news — verification is more automatable than you think

Here is the upside. The real one. The one I promised you.

When most people hear "verification is the bottleneck now," they assume the bottleneck is permanent, because they picture verification as a human reading code, and humans read at a fixed speed, and so they conclude we are simply stuck — capped forever by how fast a person can review. And if that were true, this would be a bleak episode. The small team would be doomed to a holding pattern forever.

But it is not true. And this is the genuinely hopeful turn. Verification is far more automatable than the writing ever was. Think about what verification actually is. It is checking work against a standard. And checking is a fundamentally easier, more mechanizable act than creating. We have known this in computer science forever — it is the whole intuition behind why some problems are hard to solve but easy to check. Generation is creative. Verification is, in large part, checkable. And checkable things can be turned into machines.

So watch what a serious team does to widen that runway. They do not hire ten more humans to read diffs. They industrialize the proving.

They write property-based tests. This is the most important idea in this whole act, so let me slow down on it. A normal test says "when I put in three, I should get back six." One example. A property-based test says something much stronger — it says "for any number I put in, the output should always be even," and then the machine generates a thousand random inputs and tries to break that rule. You are not checking examples anymore. You are checking invariants — properties that must hold for all inputs. The output of a sort is always sorted. Reversing a list twice always gives you back the original. These are claims about the shape of correctness itself.

And property-based testing happens to be the perfect answer to the most obvious objection to all of this. Someone is shouting it at their phone right now — if the agent writes the code and the agent also writes the tests, isn't that circular? Isn't that the fox guarding the henhouse? It is a great objection. The researchers even have a name for the failure mode — they call it the cycle of self-deception, where the test inherits the exact same wrong assumption that the code has, so the test passes and everyone feels safe and the bug sails right through, because the code and its test agreed with each other about being wrong.

Property-based tests break that cycle, and here is why. When the agent has to state a property — sorting always produces sorted output — it is committing to an independent claim about what correct means. It is not memorizing the buggy behavior. It is asserting a truth that has to hold no matter what, and then a fuzzer hammers it with a thousand cases the agent never thought about. The invariant is a claim that exists outside the code's own assumptions. That is what breaks the circle.

And this is not theoretical. Go back to that Anthropic Frontier Red Team result from the news. That is exactly this technique, run by an agent, at scale. The agent inferred properties, wrote the tests, ran them, and found real bugs in NumPy and SciPy and Pandas — libraries that thousands of expert humans have stared at for years. Eighty-six percent of its top findings were genuine. That is a verification machine, built out of the same agentic parts as the generation machine, and it works.

It goes further than tests. The same logic extends to the parts of your system that used to be unverifiable. Think about the features you are shipping now that have a model inside them — the ones where the output is not deterministic, where there is no single right answer to assert. A year ago those felt impossible to test, so most teams just shipped them on vibes and prayer. Now there is a whole discipline forming around it, called evals — you write a graded rubric for what a good response looks like, and you run the feature against a hundred cases and score it, automatically, every time you change something. That is verification, of the fuzziest, most slippery kind of software we build, turned into a number you can watch. Even the unverifiable got verifiable.

It goes further still. There is a tool I mentioned, Opslane, that drives a real browser against your running application and checks each acceptance criterion before you push — actual end-to-end proof, automated. And there is a study from January, looking at over thirty-three thousand pull requests written by agents, where the researchers built what they called a circuit breaker. It predicts, from cheap signals available the instant a pull request is created — the file types, the size of the change — whether that change is going to be expensive to verify. Before a single human looks at it. They got it accurate enough to be genuinely useful as a triage gate. So now you are not even verifying everything by hand. You are letting a machine sort the planes — these forty can land on autopilot, these six need a human in the tower — and you are spending your scarce human verification on exactly the changes that warrant it.

So the runway is not fixed. You can widen it, dramatically, with the same kind of automation that created the flood in the first place. A small team really can industrialize verification and actually capture the leverage the agents promised — not just generate faster, but prove faster, and therefore ship faster. That is the upside, and it is real, and I do not want a single skeptical bone in your body to miss it. The holding pattern is not a life sentence. You can build more runway.

But — and you felt this coming, because there is always a but — there is one honest caveat that turns this entire episode, and it comes from nineteen sixty-nine.

---

## Act three: the chair no machine can sit in

In nineteen sixty-nine, Edsger Dijkstra wrote one of the most quoted sentences in our field, and almost everyone quotes it without feeling the weight of it. He said — and this is verbatim — program testing can be used to show the presence of bugs, but never to show their absence.

Never to show their absence. Read that against everything I just told you in act two. All that beautiful automated verification — the property tests, the fuzzers, the browser-driving robots, the circuit breakers — every bit of it can only ever do one thing. It can find bugs. It can show you the code is wrong. It can never, ever prove the code is right. A test that passes does not mean correct. It means "not yet caught." You can run a million property checks and all you have earned is a million failures to disprove. Verification, all of it, bounds your risk. It never certifies your truth.

And that crack — that one word, absence — is where the whole thing comes apart in the most interesting possible way. Because it means the bottleneck I have been describing does not actually have a bottom. Watch what happens when you automate a stage of verification. You speed up that stage. And by Goldratt's law, the constraint does not vanish — it moves to the next slowest stage. So you automate that one too. And it moves again. Every verification stage you successfully mechanize just hands the bottleneck one step upstream to the next one. The constraint is not sitting still waiting to be solved. It is climbing.

So follow it all the way up the river and ask the real question. Where does it stop? When the constraint has climbed past the writing, past the unit tests, past the integration tests, past the security scans, past the browser checks — where is the one stage it can climb to and get stuck, because there is no machine that can do it?

The answer has a forty-year-old name, and once you have the name you cannot unsee it. It is the difference between verification and validation. Verification asks — are we building the thing right? Does the code match the specification? That question has a machine answer, because you can check code against a spec. But validation asks a different question — are we building the right thing? Does this software actually do what it was supposed to do, solve the problem it was meant to solve, behave the way a human actually needed it to? And that question has no machine answer. Because to check whether the code does the right thing, you need to know what the right thing is. And the only place that lives is in a human head.

Let me make that concrete, because it is easy to nod at and miss. Imagine the agent builds you a function to calculate a refund. It is clean code. It has tests, and they pass. The property checks hold. The security scan is green. Every machine in your pipeline signs off — this code is built right, it matches its spec, it is internally flawless. And it refunds the wrong amount, because the spec it was built against said to refund the full purchase price, and the business actually needed it to subtract a restocking fee that nobody wrote down. Every verification machine you own says that code is correct. And it is wrong. Not buggy — wrong. It does precisely what it was told and precisely not what was needed. No test on earth catches that, because the test and the code were both built from the same flawed understanding of what correct meant. The gap is not in the code. The gap is between the code and the world, and machines cannot see the world. Only you can.

Computer scientists have an even sharper name for the bottom of this. They call it the oracle problem. In testing, an oracle is the thing that tells you whether a given output is correct. And the deep, unfixable difficulty is that for any interesting program, deciding whether an output is the correct output is — in the words of the research, verbatim — akin to guessing the intention of the developer who wrote the code. Guessing the intention. There is no test for intention. There is no fuzzer you can point at "what did the human actually want." The machine can check the code against the spec all day long. It cannot check the spec against your actual desire, because your actual desire is not written down anywhere a machine can read it. It is in you.

This is the grand challenge that Microsoft Research named just this March, in a paper I cannot recommend enough, by a researcher named Shuvendu Lahiri. The phrase he uses is the one I want you to leave this episode holding. He says AI-generated code is plausible by construction, but not correct by construction. Plausible by construction. The model is built to produce code that looks right — Veracode's word from the news, plausibility, the exact same word. And the gap between plausible and correct — Lahiri calls it the intent gap — has always plagued software, but AI amplifies it to an unprecedented scale, because now you can generate plausible code faster than you can ever specify what correct would have meant. And his killer line, the one that closes the loop on this whole episode — there is no oracle for specification correctness other than the user.

There it is. That is the chair no machine can sit in. You can automate writing the code. You can automate testing the code. You can, increasingly, automate reviewing the code. What you cannot automate — not because the technology is immature but because it is a logical impossibility, an oracle problem, a theorem — is deciding what the software is supposed to do in the first place. The constraint climbs and climbs and climbs, and it comes to rest, finally and permanently, on specification. On intent. On a human being saying, with enough precision that it can actually be checked against, here is what correct means.

So here is the thesis, as plainly as I can say it. The agent did not eliminate the bottleneck. It relocated it — out of your hands, where it was typing, up through verification, where it is increasingly the machine's, and all the way up to the one node in the pipeline that has no machine oracle. The job of an engineer is not moving from writing code to reviewing code. It is moving from writing code to specifying intent. The most valuable thing you can do in the agentic era is not type, and it is not even check. It is to know, precisely, what you actually want — and to be able to say it clearly enough that everything downstream, human and machine, can be measured against it. The bottleneck became you. The good kind of you. The you that decides what correct means.

---

## Close

Let me land this somewhere you can act on, starting Monday.

Three moves.

First — and this is the whole episode compressed into one habit — write the acceptance criteria before you let the agent write the code. Not after. Before. Most people prompt the agent, look at what comes back, and then try to decide if they like it. That is backwards, and it is backwards in the exact way the oracle problem predicts, because you are trying to verify against a standard you never set. Flip it. Spend the first twenty minutes writing down, in plain specific language, what done means — what this thing must do, what it must never do, how you would know it worked. Then let the agent generate against that. You have just done the one piece of work no machine can do for you, and you did it at the only point in the process where it is cheap — the beginning. Approve the spec, not just the diff.

Second, industrialize your verification on purpose — build runway. If you are a working engineer, this week, learn property-based testing. Genuinely. It is the highest-leverage testing skill of the next five years, because it is how you state invariants — claims about what must always be true — and invariants are exactly what survive in a world where a machine writes both the code and the example tests. Stop writing tests that check one input and one output. Start writing tests that assert a property and let the machine try a thousand times to break it. Let your agents write those tests too — but you decide which properties matter, because choosing the property is a tiny act of specification, and that part is yours.

Third — and this one is for the managers. Stop measuring generation. I mean it. Lines of code, pull requests opened, story points moved, agent activity — every one of those metrics measures planes in the air, and planes in the air are worthless. They are inventory. They are the holding pattern wearing the costume of progress. Measure landed work — changes that are specified, verified, and trusted in production. And then take the hardest, most counterintuitive step of all. Take your best engineers off the keyboard. The instinct is to point your strongest people at generating more, faster. Exactly wrong. Point them at the top of the river — at specification, at deciding what correct means, at writing the criteria everything else gets measured against. That is now the highest-value chair in the building, and you want your best person sitting in it, because it is the one chair you can never automate your way out of needing filled.

Go back to the holding pattern. Three engineers, forty planes circling, one runway. The agent did not make you a better pilot. It filled your sky with traffic and then handed you the tower. And the job in the tower was never to fly the planes. It was to know where each one is supposed to land — and that, it turns out, is the one thing it could never tell you.

So stop trying to land more planes faster. Get clear on the destination first. The whole sky is waiting on you to know where it is going.

Land the plane. But decide where it is going first.

---

## Sign-off

That is episode four of Land the Plane. Four weeks now on one arc — psychological safety, then the people, then the moment of review, and now the constraint that runs underneath all of it, climbing upstream until it lands on the one thing only a human can own. Intent. What we actually meant.

Which is, not coincidentally, exactly where this show has been heading the whole time. Because if the most valuable thing an engineer does is specify intent clearly enough to be checked against — then the real question for next time is, what does it actually look like to get good at that. To treat intent as the primary artifact, and the code as the thing that falls out the bottom. That is where we go next. The intent layer. See you there.

Until then. Decide what correct means. Say it before you build it. And keep the planes landing.

Thanks for listening. This has been Land the Plane.
