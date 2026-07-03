# Episode 006 — Cleared to Land

**Subtitle:** For five episodes the bottleneck has been climbing upstream. This week it arrives at the one place it cannot climb past — intent, the single node in the whole pipeline that has no machine oracle. When agents can build anything and check almost anything except whether it was the right thing, the job collapses to one thing: saying what you meant, well enough to be checked, and keeping the saying.
**Topics:** intent layer, spec-driven development, AI-assisted development, verification, validation, engineering leadership, agentic workflows
**Published:** 2026-07-04
**Summary:** The plane finally lands. For five episodes the constraint has been moving upstream — from psychological safety to people to review to verification to last week's four-day build that produced a beautiful, unvalidated demo. This week it reaches the top of the pipeline and stops, because there is nowhere left to go. Intent is the one node no machine can grade. Agents now build the code and increasingly check the code, and the whole industry is racing to give the specification an oracle — Spec Kit, Kiro, Tessl — but every one of those tools still terminates at a human saying "yes, that is what I meant." So the engineer's job collapses to three verbs: specify intent, capture it, validate it. And the captured intent — the conversation, the pivots, the rejected paths — becomes the one artifact a human still uniquely owns.
**Target length:** ~30 minutes (~5,000 words at solo pacing).
**Voice:** Host of Land the Plane — first person, opinionated essay format, weekly cadence with a news segment up top.

---

## Show open

Welcome to Land the Plane. This is your weekly half hour about software engineering, AI-assisted development, and what it actually takes to lead engineering teams in twenty twenty-six. I am your host. This is episode six. Glad you are here.

You know the shape by now. A few things that landed this week, up top. Then one longer argument. Then a couple of things you can actually do before next week.

And this week the longer argument is one I have been walking toward since episode one. Five episodes ago I told you the planes were not landing. Today I want to tell you what it actually takes to land one. Let us get into it.

---

## This week on the radar

Four things on the radar, and all four of them are the same story from four angles, which almost never happens, so pay attention.

One. GitHub shipped Spec Kit version zero point eleven, on June sixteenth. If you have not looked at Spec Kit since I mentioned it back in episode one, look again, because it grew up. The whole thing is built around a loop — you write a specification, then a plan, then a task list, and only then does the agent write code. Each of those is a plain Markdown file that feeds the next one. And the news in this release is reach. It now drives more than thirty different coding agents from the same spec — Copilot, Claude Code, Cursor, Gemini, Codex, whatever you have got. Think about what that means. The specification is now the portable thing. The agent is the interchangeable thing. That is a complete inversion of how we have thought about tooling for forty years, and GitHub just shipped it as a point release like it was nothing.

Two. Amazon made its spec-driven tool, Kiro, generally available on May seventh. Kiro is spelled K I R O. And Kiro is interesting for one specific reason that is going to matter in the main piece. It does not just turn your spec into code. It tries to test your spec. It generates property-based tests aimed at the specification itself — an attempt to build a machine that can check whether your spec holds together. Hold that thought. Somebody built a robot to grade the requirements. We are going to ask, in about twenty minutes, whether that robot can possibly work.

Three. The counterweight, and it is a good one. There is a company called Tessl — T E S S L — that raised something like a hundred and twenty-five million dollars on the purest version of this bet. Spec is the source. The code gets stamped, literally, generated from spec, do not edit. The boldest possible claim. And in January, Tessl quietly pivoted. Rebranded. Changed what it was selling. Its core framework reportedly still is not generally available after the better part of a year in private beta. I am not dunking on them — this is hard. But keep them in frame as the honest counterweight to the two items before. The idea that intent is the source of truth is shipping in some places and stalling in others, and anyone who tells you this is a solved paradigm is selling something.

Four. And here is the one that actually matters, the one underneath the other three. In March, a researcher at Microsoft Research named Shuvendu Lahiri published a paper with the driest possible title — Intent Formalization — and inside it is the single most important sentence I have read about our job this year. He writes that there is, quote, no oracle for specification correctness other than the user, end quote. Sit with that. Every other stage of building software, we are learning to automate. We can generate the code. We can increasingly test the code. But the question of whether the specification itself was right — whether you asked for the correct thing — Lahiri is telling you there is no machine that can answer that. Ever. Only the person whose intent it was. That is not a tooling gap. That is a wall. And this whole episode is about what you do when you finally hit it.

That is the week. Now let us go.

---

## Cold open

Let me put you back at the desk from episode one.

Same engineer. Same Tuesday afternoon. The agent is working — reading files, proposing edits, running tests, reading the output, going again. And a light on the side keypad changes color, because the agent has a question.

But something is different now, a year on, and I want you to notice exactly what. A year ago the engineer watched the agent type and had that first uneasy thought — the diff is not the artifact, the diff is the exhaust. This year the engineer is not watching the typing at all. The typing is boring now. The typing is solved. The agent writes the code, and then the agent writes the tests, and then a second agent reviews the first agent's code and files better comments than most humans would. All of that — the whole machine — hums along without much help.

So what is the human actually doing in that chair?

Watch closely, because it is the whole show. The human is doing exactly one thing the machine never asks for help with. The human is deciding what correct means. Not whether the code matches the spec — a machine can check that now. Whether the spec was right. Whether this feature should exist. Whether the edge case the agent is cheerfully asking about should return an error or an empty list, and which of those answers a real customer at two A M actually needs. The agent can build either one perfectly. It has no idea which one is correct, and it never will, because correct here does not live in the code. It lives in a human head, and it has to be spoken out loud before anything downstream can be checked against it.

That is the chair. That is the job now. Everything the machine can grade, the machine is taking. What is left in the chair is the one thing with no grader but you.

For five episodes I have been telling you the bottleneck was climbing. This is the top of the stairs. Let me show you the room it leads to.

---

## Act one: the stairs run out

Let me collect the whole arc in one breath, because we are at the top of it now and you should be able to see the whole staircase.

Episode four was Goldratt. Any system has exactly one bottleneck, and if you speed up anything that is not the bottleneck, you accomplish nothing but piling inventory in front of the real constraint. And I argued that agents did something specific to the software pipeline — they made generation free, so the bottleneck stopped being writing the code and moved upstream to verification, to proving the code was right. Episode five pushed it one more step. I stood in a four-day build and watched construction become so cheap that the constraint climbed past it entirely, up to intent — knowing what was worth building and being able to say it. And I told you the demo at the end of those four days was a touch-and-go. The wheels kissed the runway. Nobody landed.

So here is the question this episode exists to answer. If the bottleneck keeps climbing — generation, then verification, then intent — where does it stop? Because a constraint that just moves forever is not a useful idea. Goldratt's whole point is that you find the one and you work it.

It stops at intent. And the reason it stops there is the most important thing I am going to say today, so I am going to say it plainly and then spend the rest of the episode earning it.

The bottleneck stops climbing at intent because intent is the only node in the entire pipeline with no oracle above it.

Let me define that word, because it is doing all the work. In testing, an oracle is the thing that tells you whether an output is correct. A unit test is an oracle. A type checker is an oracle. A human reviewer is an oracle. Every stage of building software is a stage where some output gets checked against some oracle. The code gets checked against the tests. The tests get checked against the spec. And here is the chain the whole industry is quietly building right now — you can check the tests against the spec, and you can even, like Kiro is trying to do, build a machine that checks the spec against itself for consistency. Push the oracle up, and up, and up.

And then you get to the top. The spec is checked against — what? Against the intent. Against what the person actually wanted. And there is no oracle there. There is no file, no test, no model, no second agent that holds the correct answer for what you should have wanted, because the correct answer was never written down anywhere in the system. It only ever existed in a human mind. Lahiri says it in one line — there is no oracle for specification correctness other than the user. The staircase of automation runs all the way up the building and then the top step opens onto a room with no floor. The user is the floor. There is nothing under them.

And this is not new. This is the oldest known fact about our field, and we forgot it because typing was loud enough to drown it out. Fred Brooks wrote it down in nineteen eighty-six, in an essay called No Silver Bullet that every one of you should read this weekend. His line — forty years old — is this. The hardest single part of building a software system is deciding precisely what to build. And then he twists the knife. For the truth is, he wrote, the client does not know what he wants. Nineteen eighty-six. Before the web. Before the cloud. Before any of the tools we argue about. The hardest part was always deciding what to build, and it was always hard because the person asking could not fully say what they meant.

For forty years that truth was hidden, because deciding what to build was maybe twenty percent of the pain and the other eighty percent was the sheer brutal labor of construction. When most of the work is typing, you experience software as a typing problem. Agents came in and deleted the eighty percent. And what got exposed, sitting there the whole time, was Brooks's twenty percent — the deciding, the wanting, the saying — which never got easier at all, and which is now the entire visible surface of the job. We did not invent a new bottleneck. We power-washed forty years of construction off the top of the oldest one.

That is why the stairs run out here. Not because we ran out of things to automate below intent — we will keep automating those for years. But because intent is where the oracle goes missing, and a bottleneck at a node with no oracle cannot be relieved by a better machine. It can only be relieved by a better human, saying a clearer thing. That is the whole game now. So the interesting question becomes — is the industry facing that, or running from it? And the answer, this quarter, is both at once.

---

## Act two: everyone is building an oracle for the thing that cannot have one

Here is what is genuinely fascinating about this exact moment. The whole industry has figured out that intent is the constraint. You can see it in the tooling — nobody ships a spec-driven tool by accident. And having figured out that intent is the constraint, the industry is doing the thing engineers always do with a constraint. It is trying to build a machine to beat it.

Look at what shipped. Spec Kit stages the work — spec, then plan, then tasks — so that the intent gets pinned down in writing before a line of code exists. Kiro goes further and generates tests against your specification, trying to catch the places where your spec contradicts itself. Tessl bet the whole company on generating the code straight from the spec and treating the code as disposable output. And the intellectual engine under all of it is a talk that an OpenAI researcher named Sean Grove gave last year, called The New Code, which I cannot recommend enough. Grove's framing is the sharpest version of the idea going. He says code is just a lossy projection of intent. The intent is the real thing. The code is a compression of it, and a lossy one — you cannot recover the full intent by reading the code, the same way you cannot recover a raw photo from a JPEG. And he has this line that should be tattooed on the industry. He points out that when we keep the AI-generated code and throw away the prompt that produced it, we are doing something insane — it is, he says, like you shred the source and then very carefully version control the binary.

He is right. That is exactly what most teams are doing right now. The prompt — the actual source, the statement of intent — evaporates the moment the code appears, and then we lovingly commit the code, which is the build output. We have been version-controlling the binary and shredding the source. Grove is right, and Spec Kit and Kiro and Tessl are all, in their different ways, attempts to stop shredding the source. To make the intent a first-class, durable, checkable thing. That is good. I am for all of it.

But watch what happens at the top of every one of those tools, because it is the same thing every time, and it is the tell.

Kiro generates tests for your spec. Great — what do those tests check? They check that your spec is consistent. That it does not contradict itself. That if you said the button is blue in one place you did not say green in another. That is real and useful and it is verification — did we write the spec right. It is structurally incapable of telling you whether blue was the correct color. A perfectly consistent spec for the wrong product is still the wrong product, and it will pass every property test Kiro can generate, cleanly, forever. The machine can make your spec precise. It cannot make it correct, because correct is measured against something that is not in the spec — it is measured against what you actually wanted, and that is exactly the thing with no oracle.

This is the inversion I want you to hold onto, because it is the center of the episode. Every one of these tools is pushing the oracle upward — checking the code, then checking the tests, then checking the spec. And every one of them, at the very top, terminates at a human saying yes, that is what I meant. They can automate the whole staircase and the top step is always, unavoidably, a person. You can formally verify a specification against itself until the heat death of the universe and never once learn whether the specification was right. Precision is not correctness. Verification is not validation. And the tools are spectacular at the first word of each of those pairs and can do nothing — nothing — about the second.

And the skeptics are right about the failure mode, so let me give them their due, because they are the most useful voices in this whole conversation. There is a sharp piece from a group called Arcturus Labs titled, plainly, Why Spec-Driven Development Breaks at Scale. The argument is exactly the one you would fear. A big specification is written in natural language, and natural language is imprecise, so a big spec inherits all the ambiguity of the English it is written in. You have not escaped the problem. You have moved it. Instead of underspecified code you now have an underspecified spec, and the agent fills every gap you left with a plausible guess. The classic example is a button with no color specified — the agent makes it green today and red tomorrow and both are, from the machine's point of view, perfectly valid completions of what you said, because you did not say. The formalization burden did not vanish. It relocated, upstream, to you. Somebody has to decide the button is blue. There is no one else in the building who can.

And there is an even sharper needle, from a tech outlet that pointed out something nobody in the spec-driven camp wants to hear. This shiny new paradigm — write the requirements carefully first, then build from them — has a name. We used to call it waterfall. Listen to the stakeholder, write the requirements document, hand it down to construction. We spent twenty years learning why that fails — because you cannot know the requirements up front, because building the thing is how you discover what you actually wanted, because the client, as Brooks said, does not know what he wants. And spec-driven development, done badly, is just waterfall with an agent playing the role of the offshore team that builds exactly what the document said and none of what you meant.

So the spec-driven turn is real and it is good and it is also walking straight back toward a wall we already hit once. The way through — and this is the hinge of the whole episode — is to stop treating the spec as a document you write once at the top and start treating intent as a living thing you capture continuously. Which is act three.

---

## Act three: the one artifact that is yours

Let me tell you about the freshest idea I found this week, because it is small and concrete and it points exactly the right direction.

In March a researcher named Ivan Stetsenko published a paper on something he calls Lore. The mechanism is almost aggressively simple — it repurposes git commit messages, using structured trailers, to store the reasoning behind a change so that any agent can query it later. But the concept underneath it is the thing I want you to keep. He names something called the decision shadow. The decision shadow is everything real about a decision that the diff throws away. The constraints you were working under. The alternatives you considered and rejected. The forward-looking context — the reason you built it loose here because you know a second use case is coming next quarter. The diff records what changed. The decision shadow is why, and the why is exactly what the diff cannot hold.

This is the intent layer I described in episode one, finally showing up as a running implementation, and I want to be honest that it is early and small. But the shape is dead right, and here is why it matters more than any spec tool. A spec is a snapshot. It captures your intent at the moment you wrote it, at the top of the work, which is precisely the moment you understand the problem least, because you have not built anything yet. The decision shadow is captured continuously, all the way through, including at three PM on Thursday when a customer said something offhand that turned out to be load-bearing and you pivoted the whole design. That pivot is the most valuable single piece of intent in the entire project, and there is no field for it in your spec, and there is no line for it in your diff, and in almost every team on earth right now it lives in exactly one place — a Slack thread that will be unfindable in a month, and a human memory that will be gone in six.

So here is the claim I want to leave you with, and it is the payoff of the whole arc. In the agentic era, the captured intent — the spec plus the decision shadow, the whole living record of what you were trying to do and why and what you ruled out — is the one artifact that is uniquely, irreducibly yours. Think about what the machine has taken. It took the typing. It is taking the testing. It is taking the reviewing, the refactoring, the boilerplate, the migrations. Every artifact in your repository that can be checked against an oracle is being absorbed into the machine, because the machine is very good at everything with an oracle. What is left — the only thing left — is the node with no oracle. The intent. And that means the captured intent is not just documentation anymore. It is the actual product of your labor. The code is the exhaust. It always was. We just could not see it while we were busy making it by hand.

And this reframes the whole job, cleanly, into three verbs. Specify. Capture. Validate.

Specify is the front of the job. It is Grove's point — that the person who communicates most effectively is becoming the most valuable programmer. Not the person who types fastest. The person who can take a fuzzy human want and sharpen it into something precise enough that an agent builds the right thing and a test can check it. This is genuinely hard and genuinely learnable and it is a different skill than the one most of us built our careers on. It is closer to writing than to typing. It is closer to interviewing a stakeholder than to closing a ticket.

Capture is the middle, and it is the part almost everyone is skipping. Say the thing, and then keep the saying. Do not shred the source and version-control the binary. When you make a decision, record the shadow — the alternatives, the constraint, the pivot. Not in your head. Not in a Slack thread. In something durable that sits next to the code and travels with it. This is the boring infrastructural work that nobody gets promoted for and that will, within a couple of years, separate the teams that can still understand their own systems from the teams drowning in plausible code that no living person can explain.

And validate is the top, and it is the one with no shortcut, because there is no oracle but you. Validate is the human act of looking at what came out and asking not did we build it right — a machine can answer that now — but did we build the right thing. That question has no test. It never will. Lahiri proved it in a sentence. It routes through exactly one instrument, which is a human being with judgment and context and skin in the game, saying yes, that is what I meant, or, no, that is not it, try again. When people ask what is left for engineers to do when the agents can build anything, that is the answer. The thing with no oracle. The final approach that only a human can fly.

And I can hear the smart objection, because it is the right one. If specifying intent is the whole job now, cannot the agent do that too? And the honest answer is — partly, yes, and it is coming faster than you think. Point an agent at your usage data, at your mission, at a pile of industry research, and it will happily generate you twenty things you could build next. Some of them sharp. Some of them things no human in the room would have thought of. That is real, and it is close, and it is going to change what the front of the job feels like. But look hard at what it produced. It produced candidates. It flooded the top of the funnel with plausible intent. It did not, and it cannot, tell you which of those twenty is the right one to actually build — because that is a validation question, and validation has no oracle but you. An agent that generates a hundred ideas does not shrink your job. It takes the one thing only you can do — choosing, and being able to say why — and makes it the whole thing.

So here is the thesis, plainly, and then I will land it. For five episodes the bottleneck climbed — generation, verification, and now intent — and here it stops, permanently, because intent is the one node no machine can grade. The whole industry is racing to build an oracle for it and the whole industry is going to fail, not for lack of trying but because the thing is mathematically ungradable by anything but the user. So the job is not to build the oracle. The job is to become the oracle, and to leave a record of your rulings so the next person can find them. Specify the intent. Capture the intent. Validate against the intent. The captured intent is the artifact. The code was always just the way it used to be expensive to make one.

That is what it takes to land the plane. Not a green build. Not a clean demo. A human in the tower saying, yes — that is where it was always supposed to go. Bring it down.

---

## Close

Let me hand you three things to do this week, and they map to the three verbs, so they are easy to remember.

First — specify one thing, on purpose, before you let an agent touch it. Pick a real task this week and force yourself to write the intent down first. Not a ticket. A specification — what it must do, what it must never do, and the single hardest sentence, which is how you would know it worked. If you cannot write that last sentence, you have just learned the most important thing you could learn, which is that you do not actually understand the problem yet, and no amount of agent horsepower was going to save you from that. The blank page where the acceptance criteria should go is the real state of your understanding. Look at it honestly before you build.

Second — capture one decision shadow. Just one, this week, to feel the muscle. The next time you make a real call in a codebase — you picked this approach over that one, you built it loose because a second use case is coming, you ruled out the obvious design for a reason that is not obvious — write down the why. The alternatives you rejected and why you rejected them. Put it somewhere that travels with the code — the commit message is honestly a fine place to start, which is the whole point of that Lore idea. You are not building a system. You are planting the idea that the reasoning is worth more than the diff, because it is, and in a year you will wish you had a hundred of these and you will be glad you started with one.

Third — and this is the hard one, the validate one. This week, an agent is going to hand you something that looks completely finished. It will run. It will be clean. It will pass its own tests. And you are going to feel the pull to accept it, because it is plausible and you are busy and the machine seems so sure. Do not outsource the ruling to the plausibility. Stop, and ask the one question the machine cannot ask itself — is this the right thing, not is this a working thing. You are the oracle. There is no other one. That is not a burden. That is the job surviving. In a world where the machine can build anything, the person who can say what is worth building, and mean it, and prove they meant it — that person is not obsolete. That person is the only one who was never replaceable.

Go back to the desk. The agent is working. The light on the keypad changes color, because it has a question. And the question, underneath every question it will ever ask you, is the same one. Is this what you meant? You are the only thing in the entire system that can answer. That was always true. It used to be buried under a mountain of typing, and the typing is gone now, and there it is — bare, and yours, and the whole job.

---

## Sign-off

That is episode six of Land the Plane, and it is the one the last five were walking toward. Psychological safety, the people, the review, the verification bottleneck, the four-day touch-and-go — every one of them was the constraint climbing one more stair, and this week it reached the top and stopped at the one place it cannot climb past. Intent. The node with no oracle. The only cargo that was ever really yours to carry.

Where we go from here is the strangest turn yet. If the machine can build anything, and the job that is left is deciding what is worth building — then the next place we point the agents is at that very question. Feed them the usage data, the mission, the industry research, and let them surface candidate ideas for the humans to weigh. Agents at the front of the funnel, generating the intent instead of just executing it. It sounds like it breaks everything I said today. I think it does the opposite — I think it makes the human oracle matter more, not less. That is next week.

Until then. Specify the thing. Capture the why. And when the machine asks if this is what you meant — answer. This has been Land the Plane.
</content>
