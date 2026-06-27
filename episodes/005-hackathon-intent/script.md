# Episode 005 — Touch and Go

**Subtitle:** When agents do the typing, the hackathon stops being a build race and becomes a pure intent exercise — the best laboratory you have for discovering what is worth building, and a factory for demos that look done and are not. Those turn out to be the same fact.
**Topics:** hackathons, AI-assisted development, intent, specification, cross-functional teams, psychological safety, engineering leadership
**Published:** 2026-06-27
**Summary:** Last week the argument was that the bottleneck in agentic development climbs upstream until it lands on intent — deciding what correct means. This week we test that claim in the most concrete place it shows up: the hackathon. When the agent does the building, the forty-eight-hour clock stops measuring who can build fastest and starts measuring who knows what is worth building. The room fills with non-engineers holding running software. And every beautiful demo carries the same quiet defect — it proves only that someone could describe it plausibly, not that it is right. The hackathon became the best intent laboratory we have and a factory for plausible-but-unvalidated demos, and the uncomfortable part is that those are the same fact.
**Target length:** ~30 minutes (~5,000 words at solo pacing).
**Voice:** Host of Land the Plane — first person, opinionated essay format, weekly cadence with a news segment up top.

---

## Show open

Welcome to Land the Plane. This is your weekly half hour about software engineering, AI-assisted development, and what it actually takes to lead engineering teams in twenty twenty-six. I am your host. This is episode five. Good to have you here.

Same shape as always. A few things that landed this week, up top. Then one longer argument — usually opinionated. Then a couple of things you can actually do before next week.

Last week I left you with a promise. I said the most valuable thing an engineer does now is not type and not even review — it is to specify intent. To say clearly, precisely enough to be checked against, what correct means. And I said the real question for this week was what it actually looks like to get good at that.

I am not going to answer that from theory today. I am going to answer it from a room. Because I spent this week in that room — a week of hackathon-style projects, small groups, short clocks, people from all over the org. And the room taught me the answer faster than any framework could. Let us get into it.

---

## This week on the radar

Four things on the radar before the main piece.

One. The hackathon went fully agentic, at scale, in public. GitLab ran an AI hackathon this spring — opened in February, judged in March — co-sponsored by Google Cloud and Anthropic, with roughly seven thousand developers and sixty-five thousand dollars in prizes. And look at the tagline they put on the whole thing. You Orchestrate. AI Accelerates. Read that as a job description, because that is what it is. The grand prize winner was a project called LORE that ran on eight agents coordinated by a router. Eight. A single person at a hackathon now arrives with a team of agents and spends the weekend conducting, not typing. The format that was always our purest test of who can build something fast just quietly changed what it is testing.

Two. And here is the tell, the small detail that gives the whole game away. At an AWS agent hackathon in San Francisco late last year — two hundred and fifty developers, more than fifty projects in a day — one of the standout builds was a tool called Udon Cat, and what it does is run a security scanner over the output of a language model before that output ever leaves your browser. Sit with that. The hackathon is now producing tools whose entire job is to verify the output of the same kind of agent that everyone in the room is building with. The format started growing its own antibodies. Even inside the party, somebody already smelled the problem. Hold that thought, because it is the whole back half of this episode.

Three. The data caught up to the vibe this quarter. Anthropic put out its twenty twenty-six Agentic Coding Trends report in January, and two numbers in it matter for us. The first — AI is now involved in around sixty percent of coding work. The second, and this is the one nobody quotes — only zero to twenty percent of tasks are fully handed off to the agent. They have a name for the space between those two numbers. They call it the delegation gap. People are using agents on almost everything and trusting agents to finish almost nothing. And the report's own framing of why is the sentence I want stapled to this episode — the bottleneck is no longer writing the code. It is clarity about what to build. That is not my opinion this week. That is the tooling vendor's own telemetry.

Four. The counterweight, because there is always one and you should hear it next to the rest. A wave of audits this quarter pointed a hard light at vibe-coded software — applications built fast, by prompt, often by people who could not read the code that came out. One commercial audit out of the first quarter claimed that more than ninety percent of the vibe-coded apps it looked at carried at least one AI-traceable vulnerability. Now, I want you to hold that exact number loosely — it is a vendor, the methodology is not fully public, and a scary percentage is good marketing. But here is why I am not dismissing it. It converges with the academic work. A paper this year titled, plainly, Is Vibe Coding Safe, found that more than eighty percent of the functionally correct solutions — the ones that worked, the ones that would have demoed clean — still carried an exploitable vulnerability. Two completely different methods, one pointing at marketing and one pointing at a conference, landed in the same place. The thing runs. The thing demos. And four times out of five the thing is carrying a hole. Let us talk about why that is not a coincidence — and why the hackathon is exactly where it gets manufactured.

---

## Cold open

Let me put you in the room.

It is hour two of a two-day hackathon. Small group, mixed — a couple of engineers, a product person, a designer, and someone from the support side of the house, the person who reads the angry tickets all day and knows exactly where the product hurts. A year ago, I can tell you precisely what each of those people would be doing at hour two. The engineers would be typing. And everyone else would be doing the thing non-engineers do at hackathons — making the slides, writing the pitch, getting lunch. Waiting to be useful at the end.

Now look at the same room this week. At hour two, the support person — the one who has never written a line of production code in her life — turns her laptop around. And there is a running application on the screen. Not a mockup. Not a Figma. A thing you can click, that talks to a real data source, that does the one specific thing she has wanted the product to do for two years and has never once been able to get prioritized. She built it. By describing it. To an agent. In ninety minutes.

And the whole room has the same two reactions, in the same order, every single time. The first reaction is delight — genuine, infectious delight, because something that used to be impossible just happened in front of them and it is wonderful. And the second reaction, maybe a beat later, quieter, is the one this episode is about. Somebody in the room looks at that beautiful running thing and realizes — nobody here can actually tell you if it is right.

It runs. It demos. It is exactly what she asked for. And not one person in that room can tell you whether what she asked for was the correct thing to ask for, or whether the code under that clean demo would survive ten minutes of a real adversary or a real Monday.

That is the room. That gap between it runs and it is right — that gap is the whole story of what the hackathon became. So let me tell you what actually happened to it.

---

## Act one: the hackathon changed species

Here is a thing about hackathons that nobody ever said out loud, because we never had to. The hackathon was always a verification machine in disguise.

Think about what the forty-eight-hour clock actually did. We told ourselves the clock was about energy, about pressure, about the romance of building something overnight. But mechanically, that clock was a test. It was a validator. When a team walked up at the end and the thing actually ran — when the demo worked and did not crash — that running demo was earned evidence. It proved something specific and expensive. It proved that the idea was real enough, and understood well enough, that a few humans could actually construct it with their own hands in two days. The clock made building hard, and because building was hard, getting it to run meant something. It runs was a certificate, and the forty-eight-hour clock was what made the certificate cost something to obtain.

Now collapse the cost of building to near zero. Which is exactly what agents did.

Watch what happens to the certificate. When anyone in the room can get a thing running in ninety minutes by describing it, it runs stops proving that the idea was buildable, because everything is buildable now. It stops being earned. The demo still appears — it appears faster and more often and more polished than ever — but it no longer certifies what it used to certify. All it certifies now is that somebody could describe the thing plausibly enough for an agent to produce something that looks like it. The hackathon did not just get faster. It lost the one free test it used to run on every single project — the test of construction — and most people running hackathons have not noticed that the test is gone.

So if building is no longer the contest, what is? Go back to last week, because this is Goldratt all over again and I am not going to belabor it. Any system has one bottleneck. Speed up something that is not the bottleneck and you get nothing but a bigger pile of inventory in front of the real constraint. At a hackathon, building used to be the bottleneck — the thing that gated whether your idea ever became real in the room. We removed it. And the instant we removed it, the constraint did what constraints always do. It moved upstream. It moved to the question that was always sitting there behind the building, quietly, hidden by how hard the building was.

What should we build? And do we understand it well enough to say so clearly?

That is the new contest. That is what a hackathon actually measures now. Not who can build — everyone can build. It measures who showed up knowing which thing was worth building, and who could describe it precisely enough that the agents produced the right thing instead of merely a thing. The hackathon became a pure intent exercise. It is the most concentrated, fastest-feedback intent laboratory I have ever stood inside. You have an idea at nine in the morning and by ten you know whether you could even say it clearly, because if you could not, the agent built you the wrong thing and you are staring at the proof.

And that reframe changes who is good at this. Which is act two.

---

## Act two: the people the keyboard was hiding

For thirty years, the keyboard was a filter. Not a fair one. A filter.

If you had a brilliant idea about the product but you could not write the code, the hackathon was not really for you. You could pitch, you could advise, you could draw the picture — but you could not put your own hands on the thing and make it real, because making it real required a skill that took years to acquire and that had almost nothing to do with whether your idea was good. The person who understood the customer best and the person who could type the fastest were almost never the same person, and we built a whole industry that systematically handed the keys to the second one.

Pull the keyboard out as the filter, and watch who walks through the door.

The support lead from the cold open. She has the highest-resolution map of the product's pain of anyone in the building. She lives in it. For her entire career that map has been trapped, because the distance between knowing what is wrong and being able to build what is right was a wall of syntax she was never going to climb. This week the wall came down, and the first thing she built was sharper and more useful than what the engineers built, and it is not close, and it is not a fluke. It is the obvious result. She had the best intent in the room. She was just never allowed to express it in running software before. Intent was always the scarce thing. We just could not see it, because it was standing behind a wall of typing and we kept mistaking the wall for the work.

This is the democratization story, and it is real, and I am not going to oversell it, because the honest version is more interesting than the hype version. The hype version says everyone is an engineer now. That is not true and it is not what I saw. What I saw is narrower and more important. People who deeply understand a problem can now produce a working expression of the solution without an engineer standing between their intent and the artifact. The tooling vendors are reporting the same thing from their side — people in legal, in design, in operations, building their own small tools without engineering as a prerequisite. Be careful with the bigger claims floating around — you will hear that eighty percent of software will soon be built outside of the technology department, and that is a Gartner prediction, not a measurement, so file it as a guess. But the direction is unmistakable, and I watched it happen in a room with my own eyes.

Here is the part the tooling story leaves out, though, and it is the part that actually matters if you run a team. None of this works without the conditions. And the conditions are not technical.

Think about what that support person had to do to turn her laptop around. She had to be willing to show a half-built, possibly-wrong thing to a room that included engineers — the people who, in the old world, held all the status in that room. She had to risk looking naive. She had to operate as a peer in a group that, on the org chart, does not treat her as one. The only reason that prototype ever got shown is that the room was safe enough for her to show it.

You already know the research here, and it is the spine of half of this show. Google's Project Aristotle went looking for what made some teams wildly more effective than others, and the number one factor — above talent, above seniority, above experience — was psychological safety. The felt permission to take a risk in front of your peers without being punished for it. In the old hackathon, psychological safety was a nice-to-have. It made the weekend pleasant. In the agentic hackathon it is load-bearing, because the entire value of the format now depends on the person with the best intent feeling safe enough to put their hands on the keyboard in front of people who outrank them in the old hierarchy. Strip the safety out and the support lead makes slides again, and her two-year-old insight stays locked in her head, and your hackathon goes back to measuring typing speed — which is the one thing that no longer matters.

So the agentic hackathon does not just reward intent. It rewards distributed authority — flattening the room enough that intent can come from anywhere. The team that wins is not the team with the best engineers. It is the team that got the clearest intent into the building and was safe enough to let it drive, no matter who was carrying it. That is the whole anarchist case for how you run a team, and the hackathon just compressed the proof of it into forty-eight hours.

Which would be a lovely place to stop. An uplifting episode. Everyone can build, the best ideas win, flatten your hierarchy, go in peace.

Except for the thing in the cold open. Except that nobody in the room could tell you if it was right. Let me ruin the party.

---

## Act three: touch and go

There is a maneuver in aviation called a touch-and-go. The aircraft comes down, the wheels actually kiss the runway — and then, without ever stopping, without taxiing in, without anyone getting off, the pilot pushes the throttle back up and takes off again. It is a practice maneuver. The point of a touch-and-go is that it looks exactly like a landing right up until the moment it very much is not one. The wheels touched. Nobody arrived.

That is the agentic hackathon demo. And it is the most dangerous artifact your organization now produces.

Here is why. Go back to the certificate from act one — the way it runs used to be earned evidence that the thing was real. That instinct is still wired into every person who watches a demo. When you see software run, some deep part of your brain marks it as done. That instinct was trained over decades when running was expensive, and the instinct has not updated. So now you have a format that manufactures running demos at near-zero cost, shown to people whose every reflex says a running demo means the work is basically finished. The demo touches the runway. Everyone in the room files it as a landing. And nobody got off the plane.

Remember the numbers from the radar. More than eighty percent of the vibe-coded solutions that functionally worked still carried an exploitable vulnerability. Read that against what a demo shows you. A demo shows you the eighty percent — the part that works, the happy path, the thing on the screen. A demo is structurally incapable of showing you the hole, because if the hole showed up in the demo it would not be a hole, it would be a bug, and somebody would have fixed it. The demo and the defect live in different rooms. The whole point of a demo is to show the part that works, which means the better the demo, the more completely it hides the part that does not.

This is the same crack we ended on last week, and it has the same name, so let me say it precisely. There is a difference between verification and validation. Verification asks — did we build the thing right. Validation asks — did we build the right thing. The agentic hackathon is spectacular at producing things that look verified — it runs, it is clean, it demos. It does almost nothing about validation, because validation requires knowing what the right thing actually was, and that knowledge lives only in a human head, and it cannot be inferred from a running screen.

The researcher Shuvendu Lahiri, at Microsoft Research, named this exact problem in a paper this spring that I cannot recommend enough, and the line I want you to hold is verified and verbatim. The gap between informal natural-language requirements and precise program behavior — he calls it the intent gap — has always plagued software engineering, but AI-generated code, he says, amplifies it to an unprecedented scale. Amplifies it. Not creates it. The gap was always there. But the agentic hackathon is an intent-gap amplifier, because it produces more plausible-looking, less-validated software per hour than any process humans have ever invented. And Lahiri's hardest sentence is the one that closes the door on the easy escape — there is, he writes, no oracle for specification correctness other than the user. There is no machine, no test, no scanner, no agent that can tell you whether the spec was right. Only a human can. The demo cannot validate itself, and neither can the thing that built it.

So here is the uncomfortable claim, and it is the center of the whole episode. The agentic hackathon is the best intent laboratory we have ever had — and a factory for plausible, unvalidated demos. And those are not two separate facts you have to balance. They are the same fact. The exact property that makes it a great intent lab — that it strips away the cost of construction so that pure intent can express itself instantly — is the exact property that mass-produces demos that look finished and are not. You cannot have one without the other. The stripping-away is the gift and the stripping-away is the danger. Same move. Same instant. The thing that lets the support lead express her insight in ninety minutes is the same thing that lets her, and you, mistake ninety minutes of expressed insight for a shipped, validated, safe product.

What do you do with that? You do not stop hackathoning — God, no, the intent lab is too valuable. You change what you think the output is. The output of an agentic hackathon is not the software. The software is a touch-and-go; it was never going to taxi to the gate. The real output — the thing worth carrying out of the room — is the intent it discovered. You now know what is worth building, and you know who understood it, and you have a running sketch that proves the shape of it. That is gold. That is genuinely faster discovery of what matters than any planning process ever gave you. But it is discovery. It is the beginning of the work, dressed up in the costume of the end of the work.

There is a useful distinction making the rounds, from the writer Simon Willison, between vibe coding and what he calls vibe engineering. Vibe coding is what happens in the room — describe it, watch it run, feel the magic, do not look too hard at what came out. Vibe engineering is what has to happen after — the same speed, but with the discipline of someone who refuses to ship code they could not explain to another human, who writes the tests, who states what correct means and checks against it. The hackathon gives you vibe coding for free. The shipping is all vibe engineering, and none of it is free, and the demo will lie to you about how much of it is left. Most of the work is still in front of you at the exact moment it feels finished.

So the thesis, plainly. When you take construction out of the hackathon, what is left is pure intent — which is why it is now the best laboratory you have for discovering what to build and who understands it. But intent is the input to software, not the software. The running demo is a touch-and-go: the wheels kissed the runway and not one passenger arrived. Mistake it for a landing and you will taxi a plane full of vulnerabilities to the gate and call it a delivery. The hackathon's gift is the intent. Keep that. The code was always going to take off again.

---

## Close

Let me land this somewhere you can act on, starting Monday.

Three moves.

First — if you run a hackathon, change what you reward. Stop scoring the demo. I mean it the same way I meant stop measuring generation last week. If you hand the prize to the cleanest-looking running thing, you are rewarding the best touch-and-go, and you are training your whole org to mistake a plausible demo for finished work — which is the single most expensive instinct you could possibly build right now. Score the intent instead. Did this team discover something genuinely worth building? Can they now state, in plain specific language, what correct would mean for it — what it must do, what it must never do, how you would know it worked? Reward the team that left the room with the clearest specification, not the prettiest screen. The spec is the asset. The demo is the wrapping paper.

Second — for everyone who builds. Treat every prototype that comes out of one of these as a question, never an answer. The demo is the agent's hypothesis about what you meant. Before any of it goes near a customer, do the vibe-engineering pass — sit down and write the acceptance criteria the demo was secretly assuming, the ones nobody said out loud, and then actually validate against them. And make the throw-away-or-commit decision explicitly, out loud, as a real fork in the road. Either this was a touch-and-go and we keep the intent and rebuild it for real — or we are committing to land it, which means it now has to earn a real landing: tests, review, someone who can explain every line. What you must never do is let a prototype taxi quietly to the gate because it looked done in the room. Looking done in the room is the one thing it is guaranteed to do.

Third — and this is for the managers, and it is the most important one. Put your non-engineers in the cockpit. On purpose. The democratization is not a party trick — it is the actual prize, and most of you are going to waste it by keeping the keyboard in the same hands it has always been in. The support lead who can now prototype her own idea is worth more to you than a marginally faster engineer, because she closed a gap that has cost you for years — the distance between the people who understand the problem and the people who can express a solution. Build the conditions that let that happen. Make the room safe enough that the person with the best intent and the lowest status will actually turn their laptop around. That safety is now load-bearing infrastructure, not company culture fluff. And then, when the hackathon is over, be the adult who says the quiet part — wonderful, now none of this is shipped yet, here is what landing it actually takes. Be the one who knows the difference between a touch-and-go and an arrival.

Go back to the room. Hour two. The support lead turns her laptop around, and there is a running thing on the screen that did not exist ninety minutes ago, and the whole room lights up. That light is real. Something genuinely changed, and it is good, and you should feel it.

Just remember what you are looking at. The wheels touched the runway. The work now is to figure out whether this plane should ever land at all — and if it should, to actually bring it down. Slowly. On purpose. With somebody in the tower who knows where it was always supposed to go.

That is the intent. That was always the only cargo worth carrying off.

---

## Sign-off

That is episode five of Land the Plane. Five weeks on one arc now — psychological safety, the people, the moment of review, the verification bottleneck, and now the room where all of it collides in forty-eight hours and you can watch the whole thing happen at speed.

Which lands us, finally, right at the doorstep of where this show has been walking the whole time. If the output of the work is intent — if the demo is just intent wearing a costume, and the real cargo is knowing what to build and being able to say it — then the obvious next question is what it would look like to treat intent as the actual artifact. To capture it, version it, keep it, build from it on purpose, instead of discovering it by accident at a hackathon and letting it evaporate on Monday. That is the intent layer. That is where we go next, and it is where we have been going since episode one.

Until then. Run the experiment. Keep the intent. And do not taxi a touch-and-go to the gate. This has been Land the Plane.
