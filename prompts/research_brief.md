# Research brief prompt

Use this prompt to produce a sourced research brief for a Claude Cast
episode. The output of this prompt is the input to
`prompts/draft_script.md`.

Drop it into any frontier LLM with web search. Replace the bracketed
fields. The output is intended to be saved as
`episodes/<slug>/research.md` so the drafting step (and any future
revision) can refer back to it.

---

## Prompt

I am writing a 30-minute solo-host podcast episode for a show called
Claude Cast. The show is about software engineering, AI-assisted
development, and engineering leadership in the agentic era — written
for working engineers and engineering managers. Voice is opinionated,
plain-spoken, allergic to corporate-generic language.

**This week's topic:** `[ONE-SENTENCE TOPIC AND ANGLE]`

**Sub-threads I'd like to weave together if the material supports it:**
- `[THREAD 1]`
- `[THREAD 2]`
- `[THREAD 3]`

I need you to do web research and return a structured brief I can
hand to a script writer. For each of the threads above (and any
additional ones you uncover that are obviously important), please
find:

**A. Current state (last ~3 months)**
- What's actually changed in this space recently? Be specific about
  dates and sources.
- Notable writing from practitioners with names and links — prefer
  people who ship in the space over pundits who don't.
- Specific numbers, claims, or stats from reputable sources. Flag
  anything where the methodology looks shaky.
- Skepticism / counterpoints — who's writing well about the limits or
  failure modes?

**B. Deeper-context concepts**
- Any foundational frameworks, theorems, or historical episodes a
  listener would benefit from knowing? Name them, give a one-line
  explanation, and a source link.
- Quotes worth using. Verbatim, with attribution.

**C. The surprising or fresh angle**
- One thing in the material that is genuinely surprising, fresh, or
  unstated in the obvious framings. This is what separates a good
  episode from a generic one.

Constraints on the response:

- Total length under 1500 words. Prioritize specificity (real names,
  real URLs, real verbatim quotes) over breadth.
- Every claim needs a source link.
- Output as Markdown, structured with `## A.` / `## B.` / `## C.`
  headings and bullet points underneath. The drafter will read it
  directly.
- If you can't find something solid for one of the threads, say so
  honestly — better one thread cut than three padded.
- End with a one-paragraph "connective tissue" suggestion: what spine
  could thread these findings into a single argument? This is
  optional — only include it if you see one.
