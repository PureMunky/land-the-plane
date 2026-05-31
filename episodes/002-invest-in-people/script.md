# Episode 002 — Crew Rest

**Subtitle:** Why time with other humans is the maintenance schedule for the part of the work AI can't run.
**Published:** 2026-05-30
**Summary:** Engagement just hit a fifteen-year low, the loneliest people in the building are the ones at the center of it, and the agent on your screen feels like company without being any. This episode argues that as agents absorb the typing, the scarce input shifts from individual output to the relational capital between people — and that capital gets built off the keyboard, in rest and unhurried human time, not at it. Time with other humans isn't a wellness nicety. It's the maintenance schedule for the one part of the system AI can't run.
**Target length:** ~30 minutes (~5,000 words at solo pacing).
**Voice:** Host of Land the Plane — first person, opinionated essay format, weekly cadence with a news segment up top.

---

## Show open

Welcome to Land the Plane. This is your weekly half hour about software engineering, AI-assisted development, and what it actually takes to lead engineering teams in twenty twenty-six. I am your host. This is episode two. Thanks for being here.

Same shape as always. We start with a few things that landed in the world of agentic engineering in the last week or so. Then a longer piece — an argument, usually opinionated — about something underneath the news. And we close with one or two things you can actually do this week.

Last week we talked about intent, agents, and why psychological safety quietly became the critical path. This week is the other half of that coin. It is about the people. Let us get into it.

---

## This week on the radar

Four things I want to put on your radar before the main piece.

One. Gallup published the State of the Global Workplace report for twenty twenty-six in April. The headline number is grim. Global employee engagement fell to twenty percent in twenty twenty-five. That is the lowest it has been since twenty twenty. Gallup puts a price tag on the disengagement of roughly ten trillion dollars in lost productivity. Now, treat that number as directional, not precise — it is a model, not a measurement. But the direction is the point. More than one in five employees say they feel lonely at work. Among workers under thirty-five it climbs toward twenty-six percent. We are going to spend most of this episode on that word, lonely, because I think it is more load-bearing than it looks.

Two. There is a new academic review out this year in the Journal of Management. The title is, All the Lonely People. It synthesizes two hundred thirty-three separate empirical studies on loneliness at work. And it makes a distinction I want you to carry through the whole episode. Isolation and loneliness are not the same thing. Isolation is objective — it is being physically alone. Loneliness is subjective — it is the feeling that your relationships are deficient. Which means you can be deeply lonely in a crowded office. You can be lonely in a Slack with four hundred people in it. The number of humans near you does not fix it. The quality of the connection does.

Three. Amy Edmondson — the Harvard professor who put psychological safety on the map, and who we leaned on heavily last week — has been talking about AI specifically over the last few months. Her framing is that AI is a two-edged sword. Her line is that only in environments where people feel safe do they speak openly, experiment, and treat AI as an opportunity rather than a threat. And the sharp question she keeps asking is this. Will people on your team feel safe admitting they do not understand a recommendation the AI just made? Hold that question. It is the bridge between this episode and the last one.

And four — for balance, because I do not want to only bring you doom. Anthropic published its Agentic Coding Trends report this year, and there is a number in it that complicates the easy story. Developers are now using AI in roughly sixty percent of their work. But they fully hand off — fully delegate, no human in the loop — only somewhere between zero and twenty percent of tasks. And here is the pattern. The harder and more design-dependent the work, the more the humans stay in it. The more they collaborate, the more they keep judgment in human hands. So the tool is not actually forcing anyone into isolation. I want to be honest about that up front. The tool is not the villain here. The temptation is. The option is. We will get to why that distinction matters.

That is the week. Now let us go.

---

## Cold open

Here is a scene. See if any of it lands.

It is Thursday. You have had a great week, by one definition of great. You and your agent have been heads-down since Monday. You shipped a service. You cleared a backlog that had been sitting there for a month. The diffs are beautiful. The tests are green. Every morning you sat down, opened the laptop, described what you wanted, and watched it get built. The agent answered instantly, every time. It never pushed back. It never needed anything from you. It never had a bad day. It was, by every measure available on your screen, the best colleague you have ever had.

And then on Thursday afternoon you stand up to get a glass of water, and you realize something a little strange.

You have not had a real conversation with another human being since Monday.

Not a standup. Not a thread. A conversation. The kind where somebody disagrees with you and you have to sit with it. The kind where you say, I am stuck, and somebody you trust says, yeah, that part is genuinely hard, let me look. You have been, by the org chart, fully connected all week. Calendar full. Messages flowing. And you are, in the precise clinical sense of the word from that Journal of Management review, lonely.

Now here is the thing I want you to notice. Nothing went wrong. That is what makes it dangerous. The week worked. You shipped. By every dashboard your manager looks at, you had a fantastic week. The cost did not show up anywhere a dashboard can see it. It showed up as a slow, quiet draw-down on something that does not have a meter on it.

This episode is about that meter you cannot see. It is about why time away from the keyboard, with other humans, is not a reward you earn after the work — it is an input to the work. It is about why the relationships you build off the clock are the thing you draw down on when the agent is confidently wrong and somebody has to be brave enough to say so. And it is about a finding that genuinely unsettled me, which is that the people most likely to be lonely in your organization are not the disengaged stragglers. They are the people right at the center.

The title of this episode is, Crew Rest. You will see why.

---

## Act one: rest is a maintenance schedule, not a reward

Let me start with the title.

In aviation, there is a concept called crew rest. Pilots are not allowed to fly indefinitely. There are hard, legally mandated rest periods between duty. You cannot waive them by being a hero. You cannot push through because the schedule is tight. The rule exists because the industry learned, expensively, that a depleted pilot is a hazard to everyone on the plane — and that the pilot is the worst-positioned person to judge their own depletion. So the rest is not discretionary. It is on the maintenance schedule, right next to the engine inspections. It is treated as a safety system. Because it is one.

I want to put engineering rest in that same category. Not as a perk. Not as a thing you earn after you have suffered enough. As a maintenance system that keeps the most expensive component — the human judgment — from failing in a way nobody catches until two A M.

Now, here is where it gets more specific than the usual take-a-break advice, and where the science actually helps.

There is a body of recovery research — a lot of it descends from a psychologist named Sabine Sonnentag — that asks a precise question. What actually makes rest restorative? And the answer is not, time off the clock. Plenty of people take time off the clock and come back just as fried as they left. The two ingredients that consistently drive recovery are psychological detachment — actually mentally leaving the work, not just physically — and positive emotion. Feeling good while you are away, not just being away.

Sit with the first one for a second. Psychological detachment. The problem with the way a lot of us rest now is that we never detach. We close the laptop and keep running the bug in the background of our minds. We are physically at dinner and cognitively still in the codebase. And the agentic workflow makes this worse, not better, because the agent is always available. There is no natural stopping point. The build is never done done. You can always kick off one more run before bed. The thing that used to force detachment — you physically could not work, the office was closed, the compile took twenty minutes so you went and got coffee with somebody — a lot of that friction is gone now. The agent removed it. Which means detachment is no longer something that happens to you. It is something you have to choose.

And here is the part that connects rest to the rest of this episode. The American Psychological Association has this framing of seven different types of rest, and one of them is social rest. Rest that happens with other people — supportive, restorative human time. It is a distinct category from physical rest and mental rest. You cannot sleep your way to it. You cannot get it from a quiet room. You get it from being with people who refill you instead of drawing on you.

But — and this is the nuance the research is very clear about, and I do not want to oversell it — social time only restores you if you are actually detached while you are in it. A break where you go get lunch with a coworker and spend the whole lunch grinding through the incident is not social rest. That is just a meeting with worse posture. The recovery comes from the combination. With other people, and genuinely off the work. Feeling part of a group, the literature says, while not still working through someone.

There is sabbatical research in the same vein — and the finding I love from it is about timing. The people who got the most out of extended leave were not the ones who collapsed into it half-dead. They were the ones who rested proactively, before they were depleted, and who rested in emotional and relational modes — time with people they loved — rather than just sleeping for a week. The benefit persisted after they came back. They were better for months. Rest, done right, is not a debt you pay down. It is a capability you build.

So the first move of this episode is just to reclassify the thing. Time away, with other humans, is not the reward for the work. It is part of the work. It is crew rest. It is on the maintenance schedule. And in a world where the agent will quite happily let you fly twenty hours a day, you are the only one who can ground the plane.

---

## Act two: relationships are the account you draw down on

OK. So rest with people refills the person. Now I want to talk about what it builds between people. Because that is the part that actually shows up in your engineering outcomes.

Let me start with the most-quoted study in this entire space, which you have probably heard of even if you do not know the name. Google ran a research project called Project Aristotle. Over about two years they studied something like one hundred eighty teams across two hundred fifty different attributes, trying to answer one question. What makes a team effective? They expected it to be the mix of talent. The smartest people, the right specialties, the right seniority. That is not what they found. The number one differentiator, above all of it, was psychological safety. The shared belief that the team is safe to take risks in. Safe to be wrong in. Safe to say I do not know in.

And there is a line from the writeup of that study that I think about a lot. The conclusion they drew was that no one wants to put on a, quote, work face, when they get to the office. That nobody does their best work while performing a sanitized version of themselves. The teams that won were the teams where people could show up as people.

Now, psychological safety is the outcome. I want to talk about the input — what actually produces it. And for that I am going to reach for Patrick Lencioni, who wrote a book a lot of managers have on their shelf called The Five Dysfunctions of a Team. He puts trust at the very base of the pyramid. Everything else — healthy conflict, commitment, accountability, results — sits on top of trust. And his definition of trust is the part I want to read carefully. He calls it a willingness to be completely vulnerable with one another. To let down our guard, admit our flaws, and ask for help.

Admit our flaws. And ask for help.

I want you to hold those two phrases up against the agentic workflow, because something quietly alarming happens when you do. Asking for help used to be a social act. When you were stuck, you had to turn to another human, expose that you did not know the thing, and ask. That little moment of vulnerability — multiplied across a thousand small stuck-moments a year — is a huge amount of how trust actually gets built on a team. You ask, they help, you are slightly indebted and slightly closer, and next week it goes the other way. That is the entire flywheel.

The agent removes that moment. Now when you are stuck, you do not turn to a person. You turn to the model. It answers instantly, it never makes you feel dumb, it never remembers that you asked the same thing yesterday. It is, honestly, a better experience than asking a busy senior engineer who sighs before they help you. And so we are, all of us, going to ask the agent instead. Thousands of times a year. And every one of those is a deposit into the trust account that no longer gets made.

This is the muscle that atrophies. The asking-for-help muscle. The being-slightly-vulnerable-with-a-colleague muscle. It does not atrophy because anybody decided relationships do not matter. It atrophies because the single most common occasion for building one — I am stuck, can you help — got quietly intercepted by a tool that does it faster and with less friction.

Now let me connect this to money and speed, because I do not want this to sound like it is only about feelings. Stephen Covey — the son, Stephen M R Covey — wrote a book called The Speed of Trust, and the core economic claim in it is clean. When trust goes down, speed goes down and costs go up. When trust goes up, speed goes up and costs go down. Trust is not a soft thing that is nice to have. It is a literal multiplier on how fast a group of people can move, because a high-trust team does not have to verify everything, document everything defensively, route everything through process, cover itself at every step.

And here is the agentic irony, the one I cannot stop turning over. Agents made typing nearly free. They collapsed the cost of producing code to almost nothing. But the speed of everything that happens between people — agreeing on what to build, trusting a teammate's judgment, accepting a hard piece of feedback, deciding to kill a project — that speed is still entirely governed by trust. We optimized the cheap part to zero and left the expensive part — the human part — exactly where it was. Which means, proportionally, the human part is now almost the entire cost. The relationship is the bottleneck now. Not because it got slower. Because everything around it got instant.

So the relationships you build — the time you invest in the people you work with — that is not extracurricular. That is you funding the account that the whole team draws down on every time something is genuinely hard. Every honest code review. Every this-is-not-good-enough. Every I-think-we-are-building-the-wrong-thing. Those withdrawals are only possible if somebody made the deposits. And the deposits get made off the keyboard. In the lunch. On the walk. In the unhurried hour where you are just two humans, not two roles.

---

## Act three: the loneliness accelerant

Before I give you the finding that genuinely got under my skin, I want to make sure you do not file loneliness under soft, the way our industry files most things about humans. So let me put a hard number on it.

In May of twenty twenty-three, the United States Surgeon General put out an advisory called, Our Epidemic of Loneliness and Isolation. Eighty-one pages. And the anchor finding is one of those facts that, once you hear it, you cannot unhear. The mortality risk of chronic social disconnection is comparable to smoking up to fifteen cigarettes a day. Lonely people have a roughly twenty-nine percent higher risk of heart disease and a thirty-two percent higher risk of stroke. The advisory names workplaces directly as a domain where, in their words, performance, productivity, and engagement are diminished.

Read that again, because it is wild. We have spent two decades building elaborate wellness programs and ergonomic chairs and standing desks to protect engineers from repetitive strain and back pain. And the data says the disconnection — the not-having-real-relationships — is carrying a health risk on the order of a pack-a-day habit. We took the small physical risks seriously and we put a fruit bowl in the kitchen for the big relational one. The thing we have been treating as the soft, optional, nice-to-have layer is, by the numbers, one of the most dangerous things in the building.

OK. Now the finding that inverts what you would assume.

Go back to that Gallup report from April. You would assume loneliness at work is concentrated at the bottom — the disengaged, the checked-out, the people on their way out the door. That is not what the data says. The data says leaders report the highest engagement, twenty-six percent, and the highest thriving, forty-three percent — and also the highest loneliness, thirty-one percent. The people at the center of the network. The most connected by org chart. The ones in every meeting, on every thread, copied on everything. They are the loneliest people in the building.

Read that next to the distinction from the Journal of Management review and it snaps into focus. Loneliness is not about how many people are near you. It is about whether the connections are real. And the people at the center have the most connections and the fewest real ones, because every one of their interactions has an agenda attached. Everyone who talks to them wants something, or is performing for them, or is managing up. The org chart connects you to everyone and bonds you to no one.

Now drop an agent into that life. Here is the trap, and this is the central claim of this episode, so I am going to say it as plainly as I can.

An agent gives you the sensation of collaboration while delivering none of its value.

Think about what a real collaborator does. They answer your question — yes. But they also push back. They also need something from you sometimes. They also remember that you were short with them last week. They also catch the thing you got wrong, because they have skin in the game and a reputation on the line. They also, occasionally, just want to talk to you because they like you. The friction and the need and the memory and the reciprocity — that is not a bug in human collaboration. That is the part that builds the trust. That is the part that catches the error.

The agent has none of it. It answers instantly. It never pushes back socially. It never needs anything. It never remembers a slight. It is pure, frictionless responsiveness. And that feels wonderful. It feels like the best colleague you ever had. But it is the exact profile of an interaction that feels deeply social and is, functionally, completely solitary. It scratches the itch of collaboration without doing any of the things collaboration is for.

That is what I mean when I say AI is a loneliness accelerant disguised as a collaborator. It is not that the agent isolates you by force — remember, the Anthropic data says people keep humans in the loop on the hard stuff. It is subtler and worse than force. It removes the felt need for other people. It satisfies the surface symptom of wanting company while the underlying thing — real connection, real trust, real relationship — quietly starves. You do not notice you are starving because you feel full. That is the whole problem. Hunger you would fix. Fullness you ignore.

And here is where this becomes an engineering problem and not just a human one, which is the through-line of this whole show. Last week the argument was that psychological safety is the critical path — that catching bad agent output requires a team where people can say, this is wrong, without getting punished for it. This week is the foundation underneath that. You cannot have psychological safety on a team with no relationships. Safety is not a policy you announce. It is not a value on a wall. It is a thing that grows in the soil of actual human trust, built over actual human time. You cannot install it. You have to grow it. And it grows off the keyboard.

So run the two episodes together. The agent generates plausible, confident, sometimes-wrong output at ten times the old rate. Catching the wrong output requires somebody with judgment to say so out loud. Saying it out loud requires psychological safety. Psychological safety requires trust. Trust requires relationship. Relationship requires unhurried human time. And unhurried human time is the exact thing the agentic workflow quietly deletes, because the agent removed every natural occasion for it — the asking for help, the waiting on the build, the closing of the office, the I-am-stuck. The chain of dependencies runs straight from your two A M incident all the way back to whether you ever go to lunch with anybody anymore.

That is the argument. The scarce input is no longer output. The scarce input is the relational capital between people. And it is the one input on the whole system that you cannot buy more compute to fix.

The thesis of this episode is this. In the agentic era, time with other humans is not the thing you do instead of the work. It is the maintenance schedule for the one part of the work that AI cannot run.

---

## Close

Let me land this somewhere you can actually act on.

I have made three moves this episode. Rest with people is a maintenance system, not a reward — it is crew rest, and you are the only one who can ground the plane. Relationships are the account every hard moment on a team draws down on, and the deposits get made off the keyboard. And the agent is a loneliness accelerant that feels like company while starving you of the real thing, which means the trust your whole engineering process depends on is exactly the thing most quietly at risk.

Here is what I would ask you to do this week.

First. Take one piece of rest with actual psychological detachment in it, and make it social. Not a quiet evening doom-scrolling alone — that is not rest, the research is clear, that is just a different screen. Have one meal, one walk, one coffee, with a human being, where the deal you make with yourself is that you are not going to talk shop and you are not going to check the build. Detached, and with people. That is the combination that actually refills you. Treat it like an engine inspection. Put it on the schedule. Do not skip it because the sprint is tight. The sprint is always tight.

Second. Find the one stuck-moment this week where you would normally turn to the agent, and turn to a person instead. Not because the agent would give you a worse answer — it might give you a better one. Do it because the point was never just the answer. The point is the deposit. You ask, they help, the account grows a little. Pick the colleague you would like to trust more in six months, and go be slightly, deliberately, vulnerable with them today. That is how the muscle comes back. You have to use it on purpose now, because the workflow will not make you anymore.

Third — and this one is mostly for the managers, but everyone should hear it. If you are at the center of the network — lots of meetings, lots of threads, copied on everything — assume you are at risk for exactly the loneliness that Gallup found, and assume your most senior people are too. Being central is not the same as being connected. So make one real connection this week that has no agenda attached. No agenda. Nothing you want from them. Just time with a person you respect, because the relationship itself is the point. The most connected people in your org are the ones starving, and they are also the ones whose judgment your hardest decisions depend on. Feed that.

Go back to the cold open. The week where everything shipped and nothing went wrong and you still, somehow, ended up depleted and alone. The cost that did not show up on any dashboard. That is the most dangerous kind of cost there is — the kind the system cannot see and therefore cannot defend against. You are the only instrument that reads that meter. So read it.

The agent will let you fly forever. It will never tell you to land. That part is on you.

Land the plane. And then, for the love of everything, go get lunch with somebody.

---

## Sign-off

That is episode two of Land the Plane. Last week, the machine in the room. This week, the people in the room. If you have a colleague who has been heads-down with an agent for a week straight, this is the episode to send them — and then maybe go get that coffee.

Next week, I want to come back to something I teased and then dodged — the new shape of code review when the agent writes the first draft. What exactly is the human reviewing for now, and how is it different from what review used to be. There is a real practice forming. I want to walk through it.

Until then. Rest on purpose. Make the deposit. Talk to a human. And keep the planes landing.

Thanks for listening. This has been Land the Plane.
