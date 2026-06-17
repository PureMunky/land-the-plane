# Episode 003 — Pilot Monitoring

**Subtitle:** When the agent writes the first draft, your job stops being to fly the plane and starts being to watch the instruments — and watching is the harder job.
**Topics:** code review, AI-assisted development, automation complacency, engineering leadership
**Published:** 2026-06-13
**Summary:** The agent writes the code now, which means the load-bearing human act has quietly moved from writing to reviewing. But review just changed shape underneath us. The line-by-line nitpicking we called "code review" is becoming the bot's job — and the bot is better at it. What's left for the human is the part a model structurally cannot do: understand what it's approving, and be willing to say, out loud, "I don't get this, walk me through it." This episode argues that code review was never really about catching typos. It was a social act of distributed understanding — and in the agentic era it becomes the load-bearing wall of the whole system.
**Target length:** ~30 minutes (~5,000 words at solo pacing).
**Voice:** Host of Land the Plane — first person, opinionated essay format, weekly cadence with a news segment up top.

---

## Show open

Welcome to Land the Plane. This is your weekly half hour about software engineering, AI-assisted development, and what it actually takes to lead engineering teams in twenty twenty-six. I am your host. This is episode three. Thanks for being here.

Same shape as always. We open with a few things that landed in the world of agentic engineering in the last week or so. Then a longer piece — an argument, usually opinionated — about something underneath the news. And we close with one or two things you can actually do this week.

Two weeks ago I teased this one and then dodged it. So here it is. When the agent writes the first draft of the code, what exactly is a human reviewing now — and how is that different from what code review used to be. There is a real practice forming. I want to walk through it. Let us get into it.

---

## This week on the radar

Four things I want to put on your radar before the main piece.

One. In March, Anthropic shipped a code review feature inside Claude Code, and the framing in the announcement is the whole reason we are doing this episode. The line was, quote, code review has become a bottleneck. Sit with that. The company building the thing that writes the code is telling you the slow part is now the looking-at-it part. And they put numbers on it. After they turned the feature on internally, the share of pull requests that got a substantive review comment went from sixteen percent to fifty-four percent. Read that the honest way. Before the bot, almost five out of six pull requests were getting waved through with nobody saying anything real about them. That was the baseline. That was normal. We will come back to that number, because it is the quiet scandal underneath this whole topic.

Two. GitHub said its Copilot code review crossed sixty million reviews by March, up roughly ten times in under a year, and that it now accounts for more than one in five code reviews happening on GitHub. More than one in five. So if you are picturing the reviewer on your team as a person, update the picture. Increasingly the first reviewer — sometimes the only reviewer — is a model. The machine writes the draft, and then a different machine reviews it, and somewhere at the end of that there is supposed to be a human. We are going to ask some hard questions about that human.

Three. The DORA report from last year — the big annual research on how software teams actually perform — has a finding that I cannot stop quoting. Their conclusion about AI is that it does not fix your system and it does not break your system. It amplifies whatever your system already is. And the specific warning, paraphrasing closely, is that AI-generated code often passes code review just fine — and by the time you notice the architectural rot, it is already embedded throughout your codebase. Passes review. That is the trap in one sentence. The code does not fail loudly at the gate. It fails quietly, months later, everywhere at once.

And four — for the honest counterweight, because I do not want to only sell you alarm. Simon Willison, who is about as credible a working voice on this as exists, has said openly that something like ninety-five percent of the code he uses is now model-generated, and that for routine tasks he has stopped reviewing every line. And he asks the uncomfortable question out loud — is it even responsible to ship code you have not fully read. I want to honor that tension instead of pretending it away. Because the answer this industry is quietly converging on is, we are going to ship code no single human has fully read. That is not a hypothetical. That is Tuesday. The question is what we do about it, and that is the episode.

That is the week. Now let us go.

---

## Cold open

Here is a scene. See if you have lived it.

It is four fifty on a Friday. There is one pull request between you and the weekend. You open it. Fourteen hundred lines. The agent wrote all of it on Wednesday, you kicked off the run, you went to a meeting, and it came back with a service that, by every signal on the screen, works. The tests are green. The linter is happy. The little robot reviewer has already left five comments, and they all got addressed. Continuous integration is a wall of check marks. The thing is, by every dashboard, done.

And your cursor is hovering over the green button. The one that says, Approve.

Now be honest with yourself about the next ten seconds. Are you going to read fourteen hundred lines of code at four fifty on a Friday? You are not. Nobody is. You are going to scroll. You are going to let your eye snag on a function name you recognize, nod at it, scroll some more, see that the tests are green, see that the bot already looked, and you are going to click the button. And it will be fine. It is almost always fine. That is exactly what makes it dangerous.

Because here is what just happened, described in the language of a different industry. You were not the person who flew that plane. The autopilot flew it. Your job, in that moment, was to monitor the autopilot. To be the human who notices when the confident, tireless, usually-correct machine is confidently, tirelessly wrong. And there is a whole field of research, paid for in actual wreckage, about what happens to human beings when you put them in that seat. The seat where the machine does the work and the human is just supposed to watch.

It turns out we are terrible at it. Not because we are lazy. Because of how attention works. When a system is right ninety-nine times, the human stops truly checking on the hundredth. The watching decays into the feeling of watching. And the whole safety case quietly comes to rest on a person who is no longer really there.

That is the seat you are in when you review agent-written code. This episode is about how to actually sit in it. Because the title of the show is Land the Plane, and right now there is an autopilot doing most of the flying, and the question of who is actually watching the instruments is not a metaphor anymore. It is the job.

---

## Act one: review was never about the typos

Let me start by killing an assumption, because the whole episode depends on getting this right.

When you picture code review, I bet you picture catching things. A null check that is not there. An off-by-one. A variable named in a way that will confuse the next person. The line-by-line read where you hunt for the defect. That is what most of us mean by code review, and it is what most tools optimized for, and it is what we have spent fifteen years making lighter and faster and more drive-by. The LGTM. Looks good to me. Approve. Move on.

Here is the thing. That version of review — the defect hunt — is the part the machine is now genuinely better at than you are.

Go back to the Anthropic numbers for a second, because they are specific in a way that matters. On pull requests over a thousand lines, their reviewer found issues eighty-four percent of the time, and when it found them it found around seven and a half per change. On the small pull requests, under fifty lines, it spoke up only thirty-one percent of the time, with barely any findings. So the bot is not noise. It scales its attention with the actual risk. And the engineers on the receiving end marked fewer than one percent of its findings as wrong. Fewer than one percent. A tireless reviewer that reads every line of a fourteen-hundred-line change at four fifty on a Friday without getting bored, without getting hungry, without having a weekend to get to. On the narrow task of finding the defect in the diff, you are not going to beat that, and you should stop trying.

And honestly? This is not new. It is a return. Let me give you the history, because it reframes everything.

In nineteen seventy-six, a man named Michael Fagan, at IBM, formalized something called the software inspection. A rigorous, slow, multi-person, multi-pass read of code, with defined roles and a real process. And it worked extraordinarily well. The data from that era had Fagan inspections catching something like eighty-two percent of defects — finding dramatically more bugs per thousand lines than testing did. For a while, that was the state of the art. Real inspection. Heavyweight, expensive, effective.

And then we mostly stopped doing it. Because it was slow, and humans were the expensive, slow part, and the whole industry spent two decades making review lighter to get the humans out of the bottleneck. We went from the Fagan inspection to the GitHub thumbs-up. We did not decide rigorous inspection was wrong. We decided it was too expensive to do to ourselves. So we stopped, and we called the lightweight thing that replaced it modern code review, and we mostly forgot the old thing had ever existed.

Now look at what is happening. The rigorous, defect-hunting, every-line inspection is coming back — but rebuilt in silicon. The thing Anthropic and GitHub are shipping is not really a new invention. It is the Fagan inspection, reborn as a machine that does not get tired. We are getting the nineteen seventy-six rigor back, for free, at the exact moment we stopped being able to provide it ourselves. That is genuinely good news, and I want to say so plainly before I complicate it.

So if the bot has taken back the defect hunt — and it has — then what is review for now? What is the human actually doing in that seat?

And the answer is the thing that was always underneath the typo-catching, the thing we mistook the typos for. Go all the way back to nineteen seventy-one. Gerald Weinberg, in The Psychology of Computer Programming, gave us the idea of egoless programming. And his whole point — the actual point, the one we flattened into etiquette — was that the value of review was social. It was that the group developed a shared understanding of the code. That no one person was the only one who knew how a thing worked. The defects the group caught were real, sure. But the deeper product of review was distributed understanding. A team of people who had all looked at the thing, argued about the thing, and now carried a shared model of the thing around in their heads.

That is what review was for. Not the typo. The typo was the occasion. The understanding was the point. We just never had to separate the two before, because the same act produced both. You read the code line by line, and in the reading you caught the bug and built the understanding at the same time. One motion, two products.

The agent just pulled those two apart. It took the defect hunt — the bug-catching half — and did it better than you can. And it left you holding the other half. The understanding. Which it cannot do for you, no matter how good it gets, because the understanding has to live in a human head to be worth anything. The whole point of the understanding is that a person has it.

So that is move one. Code review was never really about the typos. It was about a team of humans understanding their own system. The machine took the typos. You still have to do the understanding. And almost nobody has reorganized their idea of review around that split yet.

---

## Act two: the seat we are bad at sitting in

OK. So the human's job in review is shifting from catching the bug to understanding the change. Here is the problem. The seat where you watch a machine do the work, and you are supposed to stay sharp enough to catch it when it is wrong — that is a seat human beings are measurably, predictably bad at sitting in. And we have known it for decades, just not in our industry.

The term from the research is automation complacency, sometimes automation bias. There is a foundational paper by two researchers, Parasuraman and Manzey, from around twenty ten, pulling together a pile of human-factors work — a lot of it from aviation. And the finding is brutally consistent. When you give a person a reliable automated system to monitor, they monitor it less. Not because they are told to relax. Because reliability itself breeds the complacency. The better the autopilot, the less the human watches it — and so the rare moment when the autopilot is wrong is precisely the moment the human has checked out. The system's strength manufactures the human's weakness. The two move together. You cannot have a highly reliable automated partner and an alert human monitor at the same time, for free. The alertness has to be actively, deliberately, unnaturally maintained, against the grain of how attention actually works.

This is the science of the four-fifty-on-Friday Approve button. It is not a character flaw. You are not weak for scrolling past the fourteen hundred lines. You are a normal human exhibiting a documented response to a reliable machine. The agent is right so often that your brain has correctly learned it is usually right, and has reallocated your attention elsewhere accordingly. That is your brain working properly. It is just working properly toward a catastrophe, because the one time in fifty that it matters is the one time you are not looking.

And it gets worse, because you cannot even trust your own sense of how carefully you looked. This is the finding from METR last year that I keep coming back to. They took experienced open-source developers, had them work with and without AI assistance, and measured it. The developers using AI believed they were about twenty percent faster. They were actually about nineteen percent slower. They were wrong about their own experience by nearly forty points. Now sit that next to review. If you cannot trust an engineer's gut sense of whether AI made them faster — if the felt experience and the measured reality diverge that hard — then why on earth would you trust an engineer's gut sense of, yeah, I reviewed that, I looked at it, it is fine. The feeling of having reviewed something and the fact of having reviewed it are two different things, and the research says we cannot reliably tell them apart from the inside. I reviewed it is not data. It is a feeling. And the feeling is exactly the thing complacency corrupts first.

Now layer on what the agent is actually handing you to review, because the shape of the work has changed too. There is data from GitClear — they looked at something like two hundred eleven million lines of code — and the trend is ugly in a specific way. Copy-pasted, cloned code is way up. Refactoring — the act of cleaning up and consolidating — is sharply down. And churn, code that gets rewritten within two weeks of being written, is up. So the agent is producing more code, more duplicative code, that gets thrown away faster. And separately, other measurement shops are finding AI-assisted pull requests running noticeably larger — on the order of eighteen percent bigger. More lines, more duplication, less consolidation, arriving faster.

And here is where a thirty-year-old number becomes the most relevant fact in this whole episode. In two thousand nine, SmartBear and Cisco ran what was for a long time the largest study of code review ever done — twenty-five hundred reviews, millions of lines. And one of the cleanest findings was about size. Defect detection in human review falls off a cliff past about four hundred lines. The sweet spot is two to four hundred lines, reviewed slowly. Past that, the human eye saturates, and the defects sail right through. Four hundred lines is roughly the ceiling of what a person can actually review well.

So put the two facts in the same sentence and just look at them. Humans top out, on a good day, around four hundred lines. The agent now routinely drops fourteen-hundred-line changes on you. We have built a pipeline that generates work in exactly the size and shape that human review is known — measured, since two thousand nine — to be worst at. We did not just speed up the writing. We sped up the writing into a form factor that defeats the reading. A thousand-line pull request is not one review. Functionally, it is a defect-laundering machine, because everyone involved knows nobody is really reading all of it, and the green button gets pressed anyway.

This is the DORA warning made mechanical. The code passes review not because it is good but because the review, at that size and that speed and that level of complacency, is not actually happening. It is being performed. And the architectural rot DORA warns about gets embedded throughout the codebase precisely because every individual pull request looked fine in the thirty seconds anyone actually gave it. There is a phrase I found for this in the practitioner writing that I think is exactly right — AI accelerates the rubber-stamp effect, creating the illusion of rigor while hollowing out the real thing. The illusion of rigor. Green checks, a bot's five comments, an Approve from a human who scrolled. It looks exactly like rigor. It has the complete outward form of rigor. And underneath, no human understands the change. That is the failure mode. And it does not announce itself, because everything about it looks like success.

---

## Act three: the one thing the machine cannot do

So let me bring this home, because if I have done my job you are now slightly worried, and worry without a move is just anxiety. Here is the move.

If the bot catches the defects better than you, and the seat you are in makes you complacent, and the work arrives in a size built to defeat you — then trying to out-read the machine is a losing game. Do not try to be a better defect hunter than the tireless one. You will lose, and you will burn out losing. Instead, do the one thing in this entire system that a machine structurally cannot do.

Understand the change. And when you do not — say so, out loud, to another human.

That is it. That is the whole irreducible core of human review in the agentic era. Not, did I find the bug. The bot found the bug. The question is, do I actually understand what this code does, why it exists, whether it should exist, and whether it is solving the right problem — and if I do not, am I willing to be the person in the room who says I do not.

Listen to how different that is from the old job. The old reviewer's core skill was vigilance — read carefully, catch the flaw. The new reviewer's core skill is something closer to honesty under social pressure. It is the willingness to look at fourteen hundred lines that the tests pass on and the bot blessed and your tired Friday brain wants to approve, and type the words — I do not understand what is happening in this module, walk me through it. Or, why does this exist at all. Or, I see what it does, I do not see why, and I am not approving until someone can tell me.

I want you to notice what kind of act that is, because it is the thread running through this whole show. That is a vulnerability act. Saying I do not understand this is admitting, in front of your peers, that you do not know something — about code a machine wrote, that everyone else is also quietly pretending to understand. And whether you can do that, whether anyone on your team can do that, depends entirely on whether it is safe to. Which is exactly where the last two episodes have been pointing.

Run the three episodes together, because they are one argument. Episode one — psychological safety became the critical path, because catching bad agent output requires somebody able to say this is wrong without getting punished. Episode two — that safety grows out of trust, and trust is built off the keyboard, in real human time. And now episode three is where it all gets spent. Code review is the exact moment, the specific concrete event, where the safety and the trust either show up and do their job — or do not. It is not abstract anymore. It is a person, looking at a diff, deciding whether to admit they do not understand it. Everything from the first two episodes was building to that one small, hard, human moment. The whole edifice of trust and safety exists to make that one sentence sayable. I do not understand this. Explain it to me.

And here is why this is load-bearing and not just nice. The only failure mode AI review genuinely cannot catch is a human silently approving code that no one in the room understands. Think about it. The bot can find your null pointer. It cannot find the fact that three engineers all clicked Approve while privately having no idea why the change works. There is no linter for collective pretending. There is no continuous integration check for nobody actually understands this. That gap — the gap between the team's real understanding and the code that is now running in production — is invisible to every automated system you can buy, because every automated system is looking at the code, and the gap is in the people. It only becomes visible at two in the morning, in the incident, when something breaks and you discover that the answer to who understands this system is nobody. The machine wrote it, the machine reviewed it, and the humans rubber-stamped it, and now it is on fire and there is no one to ask.

There is one more cost here, and it is the one I think we will regret most, because it compounds quietly. Go back to Weinberg, to the real point of review — distributed understanding, the team building a shared model. There was always a second thing review did that we barely noticed because it came for free. It taught people. The junior engineer learned by being reviewed. The senior learned the junior's corner of the system by reviewing it. Every review was a small transfer of knowledge across the team, in both directions. That was not a side effect. For a lot of how engineers actually grow, that was the main event.

When the bug-finding moves to the bot, that transfer does not move with it. The bot does not learn your junior, and your junior does not learn from the bot the way they learned from a senior who took twenty minutes to explain why this pattern and not that one. The defect detection survives — it is fine, it is better than ever. But the learning loop, the thing that was quietly turning your team into a team, gets cut. And you will not feel that this quarter. You will feel it in two years, when you look around and realize you have a group of people who ship a great deal of code and understand a shrinking fraction of it, and have stopped teaching each other entirely, because the occasion for teaching — here, let me review this with you — got automated into a green check mark.

So here is the thesis, as plainly as I can put it. Code review was never about catching typos. It was the social act where a team came to understand its own system and taught itself in the process. The machine just took the typos — gladly, and it is welcome to them. What is left is the part that was always the actual point, and it is now the load-bearing wall of the entire enterprise. Whether a human, in psychological safety, built on trust, is willing to look at what the agent wrote and say out loud, before clicking the button — I understand this, or, I do not, and I am not approving until I do.

---

## Close

Let me land this somewhere you can act on, starting tomorrow.

Three moves. Here they are.

First, and this is the whole episode in one habit. Find the review this week where you would normally just click Approve — the one where the tests are green and the bot already looked and you are tired — and instead of approving, write one comment that begins, I do not understand. I do not understand why this function exists. I do not understand what happens here when the input is empty. Walk me through this part. You do not have to find a bug. That is not the point and it never was. The point is to convert your private, complacent skim into a public act of trying to actually understand — which is the only thing that breaks the rubber-stamp, and the only thing the machine cannot do for you. Do it once on purpose this week, and notice how unnatural it feels. That feeling is the complacency you have been swimming in. Now you can see it.

Second, put a ceiling back on size, because you are fighting two thousand nine's math with twenty twenty-six's tooling. If the agent hands you a thousand-line change, that is not a review, it is a rubber stamp with extra steps, and everyone knows it. Make the agent land its work in pieces a human can actually hold — a few hundred lines, the size the research says you can really review. Yes, it is more pull requests. Good. The friction is the feature. A reviewable change is one a person can fit in their head. If it does not fit, you are not reviewing it, you are performing a review of it, and the difference is exactly the gap that shows up at two A M.

Third — and this one is for the managers, though everyone should hear it. Stop measuring review by speed. Time-to-merge, review turnaround, throughput — in the agentic era, optimizing those is optimizing for the rubber stamp. You will get a beautiful dashboard and a codebase no one understands. Measure the thing that actually matters instead, even though it is harder to count. Can the person who approved it explain it. And protect the learning loop on purpose, because it is not coming back by accident. Put two humans on the review of the consequential agent-written changes — not for throughput, for the transfer. So the understanding stays distributed, so somebody still teaches somebody, so in two years you have a team and not just a queue of approvals.

Go back to the cold open. Four fifty on a Friday, fourteen hundred green lines, the cursor on the button. The agent flew the plane all week, beautifully, and now it is on final approach and it is handing you the controls for the one thing it cannot do — know whether anyone actually understands where it is taking you. That is the seat you are in. Not the one who writes it. The one who has to genuinely understand it before it lands, and be brave enough to say when you do not.

The autopilot will fly forever. It will never once tell you it is lost. That part — noticing, and saying so out loud — is on you.

Land the plane. But read the instruments first.

---

## Sign-off

That is episode three of Land the Plane. Three weeks now on one arc — the machine in the room, the people in the room, and now the moment where the two meet, over a diff, and somebody has to be honest about what they understand. If there is a person on your team who has been clicking Approve a little too fast lately — and there is, and it might be you — this is the episode to send them.

Next week I want to turn the lens around. We have spent three episodes on what the agent costs us. Next time, the other side — what genuinely gets better, what this lets a small team do that a small team never could before, and how to chase that without walking straight back into everything we just talked about. The upside, told honestly. That is where we are headed.

Until then. Understand what you approve. Say it out loud when you do not. And keep the planes landing.

Thanks for listening. This has been Land the Plane.
