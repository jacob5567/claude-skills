# Signs of AI writing: full catalogue and fixes

Source: Wikipedia, *Signs of AI writing* (WikiProject AI Cleanup), checked against the 22 November 2026 revision. The original is a field guide for spotting machine-written text. This version turns it around: each sign comes with what it looks like, the words to watch, and how a human writer would fix it. Signs that only apply to Wikipedia markup (wikitext, citation templates, categories, edit summaries) are left out.

The numbering matches `scripts/check_ai_signs.py`.

## Contents

1. Content signs (1.1–1.10)
2. Language and grammar (2.1–2.6)
3. Style and formatting (3.1–3.10)
4. Text meant for the chat user (4.1–4.6)
5. Older-model habits (5.1–5.2)
6. What human writing does instead
7. Not signs: don't "fix" these
8. How to treat the signs

## 1. Content

### 1.1 Undue emphasis on significance, legacy and broader trends

Ordinary facts get a sentence about why they matter, how they "reflect broader" trends, or their "enduring legacy". Even mundane subjects (a railway station, a fish species) get puffed up.

**Words to watch:** stands/serves as, is a testament/reminder, a crucial/pivotal/vital/significant/key role or moment, underscores/highlights its importance, reflects broader, symbolising its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted, forms part of the wider, "the distinction matters because", "has generated debate about…", "prompted broader reflection on…".

**Fix:** delete the significance sentence, or replace it with a specific fact that shows the point.

- Before: "The institute was established in 1989, marking a pivotal moment in the evolution of regional statistics."
- After: "The institute was set up in 1989. It was Spain's first regional statistics office."

### 1.2 Canned emphasis on notability and media coverage

The text tries to prove importance by listing where something was covered, or by describing the sources themselves.

**Words to watch:** independent coverage, local/national media outlets, trade publications, local/regional/national media outlets, music/business/tech outlets, cited/featured/profiled in, written by a leading expert, maintains an active social media presence, a strong digital presence. (Present-perfect "has been featured in" on its own is fine.)

**Fix:** say what the thing is or did. Cite coverage only as a source for a specific claim.

### 1.3 Superficial analysis

A participle clause gets tacked onto the end of a factual sentence. It interprets the fact without adding any information: "…, highlighting its importance", "…, ensuring…", "…, reflecting…".

**Words to watch:** highlighting, underscoring, emphasising, ensuring, reflecting, symbolising, contributing to, cultivating, fostering, encompassing, enhancing, showcasing, valuable insights, align/resonate with.

**Fix:** cut the clause. If the interpretation matters, give it its own sentence with evidence.

- Before: "The station has 8 tracks and 6 platforms, reflecting its continued relevance in the regional transportation landscape."
- After: "The station has 8 tracks and 6 platforms."

### 1.4 Promotional, advert or travel-brochure language

Neutral subjects are written up like a hotel listing or a press release.

**Words to watch:** boasts a, vibrant, rich (culture/heritage/history), profound, enhancing, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking, renowned, featuring, diverse array, breathtaking, stunning, world-class, seamless, state-of-the-art. (The last five come from the guide's examples rather than its word list.) The guide notes this tone is less common in newer models' output, but it's still common in marketing copy.

**Fix:** replace the adjective with the fact that would earn it, or drop it.

- Before: "Nestled in the heart of the old town, the café boasts a diverse array of pastries."
- After: "The café is on the main square and sells about twenty kinds of pastry."

### 1.5 Vague attributions and overgeneralised opinions

Opinions get pinned on unnamed authorities, or one source is presented as many.

**Words to watch:** industry reports, observers have cited, experts argue, some critics argue, several sources (when there are one or two), studies show, widely regarded, "such as" before what is actually a complete list.

**Fix:** name the source, state the claim as your own view, or cut it.

The guide marks its examples here as older-model habits, but they still turn up.

### 1.6 Formulaic "challenges and future prospects" endings

"Despite its [praise], X faces several challenges… Despite these challenges, X continues to thrive…", often in a closing "Challenges and legacy" or "Future outlook" section.

**Fix:** if a problem is real, state it plainly where it belongs. Drop the optimistic wrap-up.

### 1.7 Leads that define the title as a thing

"X refers to…", "The List of Y is a curated compilation of…" or "is the chronological list of…" for topics or lists.

**Fix:** start with the subject itself. "A catchment area is the area a hospital draws patients from."

### 1.8 "X and Y" headings, "Awards and recognition"

Paired headings built to sound complete. A bare "Recognition" section is the same habit, and the guide calls "Awards and recognition" nearly ubiquitous in AI text. Paired headings also appear in human writing, so keep a heading only if the section needs it.

### 1.9 Claims that the subject shaped discussion

The text says the subject "has shaped conversations about" something, often followed by a rule-of-three list of topics.

**Words to watch:** has/have shaped conversations/discussions/debate about, in public discussions, sparked discussions about.

**Fix:** say who discussed what, where, or cut it.

### 1.10 Undue emphasis on being identified or listed by a source

One of the most common signs as of late 2026. Instead of stating a fact, the text reports that a source "identifies", "lists" or "describes" the subject as something.

**Words to watch:** identifies/lists/describes [X] as, was identified by [source] as, is listed in, professional profile lists, biography records that.

**Fix:** state the fact and cite the source for it. "Her LinkedIn profile lists her as head of design" → "She is head of design at ExampleCorp."

## 2. Language and grammar

### 2.1 High density of "AI vocabulary"

One or two of these words is normal. Several in one piece of text is one of the strongest tells.

- **2023 to mid-2024 set:** additionally (especially opening a sentence), boasts, bolstered, crucial, delve, emphasising, enduring, garner, intricate/intricacies, interplay, key (adjective), landscape (abstract), meticulous, pivotal, underscore, tapestry, testament, valuable, vibrant.
- **Mid-2024 to 2025 set:** align with, bolstered, crucial, emphasising, enhance, enduring, fostering, highlighting, pivotal, showcasing, underscore, vibrant.
- **Mid-2025 to mid-2026:** emphasising, enhance, highlighting, showcasing.
- **Mid-2026 onward:** challenge, clearer, dependable, echoed, foster, leverage, matters, multifaceted, practical, prioritise, quietly, steady, universally. These are ordinary words, so only a cluster of them means anything. This era also leans on full stops and commas and on sentences of a similar 8 to 20 words.
- **Not tied to an era, but common:** robust, deep dive, showcase and highlight (as verbs). Grok in particular likes causal, empirical, correlate and underscore.

The era lists aren't hard cutoffs. Watch for context too: "underscore" can mean a literal underline or film music.

**Fix:** use the ordinary word or cut it. "Additionally" → start the sentence without it, or use "Also". "Crucial" → "important", or explain why. "Landscape" → name the actual thing. Don't just swap in a synonym: as the guide warns, the word is a symptom and the padding is the problem.

### 2.2 Avoiding "is", "are" and "has"

A plain verb gets dressed up.

**Words to watch:** serves as, stands as, marks, functions as, operates as, represents, boasts / features / maintains / offers (meaning "has"), refers to, "ventured into politics as a candidate" (was a candidate), "began his career as" (was). The guide marks these examples as dating from older models.

**Fix:** use is/are/has. "Gallery 825 serves as LAAA's exhibition space. The gallery features four separate spaces" → "Gallery 825 is LAAA's exhibition space. It has four galleries."

### 2.3 Vague connection or association

"was associated with leadership of", "in connection with/to", "connected with/to", "in association with", "particularly/widely associated with", where the actual relationship is known. The guide lists this among the most common signs as of late 2026.

**Fix:** state the relationship. "In 2017 she was CEO of ExampleCorp."

### 2.4 Negative parallelisms

The text corrects a misconception nobody raised:

- "Not only … but also …", "It's not just X, it's Y", "This isn't A, it's B"
- "Not X, but Y", "X is not a mirror but a portal"
- "No X, no Y, just Z"
- "Y rather than X" (overused; fine occasionally)

**Fix:** state the positive claim alone. "It's not just a coffee shop, it's a gathering place" → "People stay for hours." Keep a contrast only when a reader really would assume the opposite.

### 2.5 Rule of three

Triplets of adjectives or short phrases used to sound thorough: "fast, reliable, and secure"; "learn, connect, and grow".

**Fix:** keep lists that really are lists of facts. Otherwise pick the one item that matters, or two. Vary the rhythm.

### 2.6 Elegant variation

Cycling through synonyms to avoid repeating a noun ("the artist… the painter… the creative… the visionary").

**Fix:** repeat the plain noun, or use a pronoun.

## 3. Style and formatting

### 3.1 Title Case headings

"Impact Of Technology And Digitalization".

**Fix:** use sentence case, unless house style says otherwise.

### 3.2 Overuse of boldface

Key phrases bolded throughout, "key takeaways" style.

**Fix:** bold nothing in body prose, or at most a term where it's defined.

### 3.3 Inline-header vertical lists

Bullets that start with a bold label and a colon: "**Scalability:** The system…".

**Fix:** turn them into prose, a plain list without labels, or a real table if the data is tabular.

### 3.4 Overuse of em dashes

LLMs use em dashes where people use commas, colons, parentheses or full stops, often spaced " — " for punch. Claude in particular uses more of them than professional writers do.

**Fix:** rewrite the sentence with ordinary punctuation. Don't swap in an en dash or a hyphen, because that keeps the pattern. One or two in a long piece is fine.

Don't overshoot, either. Newer models are tuned to avoid em dashes and lean on commas and full stops instead, and the guide calls that "its own sign". Text with every dash turned into a full stop reads as a run of short, same-length sentences. Vary the sentence length.

### 3.5 Emoji as formatting

Emoji in front of headings or bullets.

**Fix:** remove them.

### 3.6 Unusual small tables

Two- or three-row tables that would read better as one sentence.

### 3.7 Curly quotes and apostrophes

A mix of curly (“ ” ’) and straight quotes.

**Fix:** match the surrounding text's convention. (Word processors also produce curly quotes, so this alone proves nothing.)

### 3.8 Thematic breaks between every section

`---` between every section.

**Fix:** remove them unless the format needs them.

### 3.9 Markdown where the format doesn't use it

Asterisks for bold, `#` headings, `*` bullets, `[text](url)` links or triple-backtick code fences pasted into an email, a CMS field, a Word document or HTML. Also wrong heading levels: the title repeated as a top-level heading, or several top-level headings. The guide calls a stray code-fence wrapper one of the most unambiguous signs.

**Fix:** convert to the target format's own formatting, or to plain text.

### 3.10 Chatbot artefacts and tracking links

Leftovers from the chat interface: `contentReference[oaicite:1]` and similar citation markup, "↩" footnote arrows, and links carrying `utm_source=chatgpt.com`, `utm_source=openai`, `utm_source=copilot.com` or `referrer=grok.com`. Links may also be broken (404s with no archived copy), or DOIs and ISBNs may be invalid or point to an unrelated source.

**Fix:** delete the markup. Strip the tracking parameters from links. Check every link and reference; replace or remove any that don't resolve to what they claim. (A tracking parameter shows someone used a chatbot to find the link, not necessarily to write the text.)

## 4. Text meant for the chat user

### 4.1 Collaborative communication left in

"I hope this helps", "Certainly!", "Of course!", "You're absolutely right!", "Great question", "Let me know if…", "Would you like me to…", "Is there anything else…", "Here is a…", "a more detailed breakdown", "In this section, we will discuss…", reminders to "check/verify… before publishing", and instructions left in comments ("Delete this section before submission").

**Fix:** delete it.

### 4.2 Knowledge-cutoff disclaimers and speculation about gaps

"As of my last knowledge update…", "Up to my last training update…", "While specific details are limited…", "not widely documented/disclosed/available", "not publicly available", "based on available information", "in the provided sources / search results", "maintains a low profile", "keeps personal details private", followed by guesses about what the missing information "likely" is.

A newer variant (from mid-2026) is the corrective framing: "does not by itself establish", "should not be confused with", "should be treated as… rather than…". It hedges against a claim nobody made.

**Fix:** if something really is unknown, say so once, concretely, and tell the reader what to do: "Opening hours aren't posted; call ahead." Never pad the gap with speculation.

### 4.3 Placeholders

"[Your Name]", "[Your Email Address]", "[Year]", "[Describe the section]", "(Add your channel URL here)", "(If available)", "INSERT_SOURCE_URL", "PASTE_URL_HERE", "SOURCE_PUBLISHER", links to example.com, and dates like "2025-XX-XX".

**Fix:** fill them in or remove them.

### 4.4 Refusals and model self-reference

"As an AI language model…", "As a large language model…", "I cannot offer medical advice, but I can…", "I'm sorry, but…". Rare now, but unambiguous.

**Fix:** delete it, along with anything the refusal was hedging.

### 4.5 Abrupt cut-offs

Text that stops mid-sentence or mid-list because the output ran out. (A bad copy-paste does the same.)

**Fix:** finish the thought or cut back to the last complete sentence.

### 4.6 Customer-service tone in replies

In emails, comments and replies: "I have carefully reviewed…", apologising for any inconvenience the writer "may have" caused, "please point them out to me, and I will try to resolve them", dismissing a concern as "unsubstantiated speculation", or headed sections inside a short reply.

**Fix:** answer the point directly, the way the person would in conversation.

## 5. Older-model habits (still worth avoiding)

### 5.1 Didactic disclaimers

"It's important to note/remember/consider", "It is worth noting", "may vary", "keep in mind".

**Fix:** state the thing. "Hours may vary" → "Hours change in winter."

### 5.2 Section summaries

Paragraphs that end by restating themselves; openers like "In summary", "In conclusion", "Overall", "Ultimately"; a section headed "Conclusion".

**Fix:** end on the last new fact.

## 6. What human writing does instead

From the guide's "Signs of human writing":

- Plain is/has sentences: "there is a", "it has a".
- Plain words: wrote (not authored), moved (not relocated), used (not utilised), tried (not attempted), died (not passed away), before (not prior to), to (not in order to).
- Definite statements where they're true: "is the only", "was the first", "one of the best".
- Ordinary hedges and intensifiers: "very", "perhaps", "tends to".
- Some ordinary wordiness: "as a result of", "in order to", "the fact that". People write these; models tend to avoid them.
- Sentences of uneven length.
- Specific, unusual facts. AI text drifts to the generic ("a revolutionary titan of industry"); human text keeps the odd detail ("inventor of the first train-coupling device").

## 7. Not signs: don't "fix" these

The guide lists these as unreliable indicators. Changing them wastes effort and can make the text worse:

- Perfect grammar.
- Mixing casual and formal registers.
- "Bland" or formal prose in general.
- "Fancy" prose or long words in general (only the specific words in 2.1 are tells).
- A single transition word on its own.
- Unsourced content.
- Correct formatting.

Quoted material (a real person's words, a title, a source) is never rewritten to remove signs.

## 8. How to treat the signs

The guide describes itself as "observations, not rules", and says some signs may not apply outside Wikipedia. Many also turn up in editorials, blogs and marketing copy written by people. Keep these points in mind:

- **The signs point to a problem; they aren't the problem.** The guide says not to "merely treat these signs as the problems to be fixed". Fix what the sentence is doing: puffing up, hedging, saying nothing.
- **Count clusters, not single words.** One or two flagged words can be chance. Many, repeated, is a strong tell.
- **Don't trust AI detectors.** The guide says not to rely on them alone: they have real error rates and are thrown off by paraphrasing and formatting. Untrained people do little better than chance; experienced readers do much better.
- **Models differ.** Broader-context puffery is more typical of ChatGPT and Grok. Gemini and Claude tend to be more concise, and newer models avoid em dashes and over-use full stops instead.
