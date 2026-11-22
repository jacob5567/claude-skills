---
name: de-ai-writing
description: 'Rewrite text to remove signs of AI writing from Wikipedia''s field guide: puffery, em dashes, "not just X", AI vocabulary. Use to de-AI, humanise or check copy, docs or sites before publishing.'
---

# De-AI writing

Rewrite content so it reads as if a knowledgeable person wrote it. Do this by removing the patterns catalogued in Wikipedia's *Signs of AI writing* (WikiProject AI Cleanup). The full catalogue is in `references/signs.md`, with words to watch and a before/after fix for each sign. Read it before the first rewrite in a session; it's the source of truth for what counts as a sign. Its last section, "How to treat the signs", explains why a single flagged word proves little and why AI detectors aren't to be trusted.

Use this skill whenever someone wants content de-AI'd, humanised, made to "sound less like ChatGPT/AI" or "less robotic", cleaned of AI tells, or checked for signs of AI writing before publishing. That covers blog posts, web copy, FAQs, emails, essays, LinkedIn posts, product pages, docs, and whole websites or repos of content. Also use it to polish a draft the user says came from an AI.

## Why this works the way it does

The Wikipedia guide makes a point worth keeping in mind: the signs are symptoms. Language models drift toward the most statistically common phrasing, so specific facts get smoothed into generic, important-sounding statements. Swapping a flagged word for a synonym, or an em dash for an en dash, hides the symptom and leaves the problem. The aim is text that says specific things plainly. When you fix a sentence, fix what it's doing (puffing something up, hedging, correcting a misconception nobody raised), not just the word that tripped the scanner.

## Workflow

1. **Get the text.** It might be pasted text, a file, a folder of files, or a built website. For a codebase or site, find where the copy actually lives (data files, CMS exports, templates) and edit it there, not in generated output.

2. **Scan it.** If you can run code, use the bundled scanner to get a baseline:
   ```bash
   python3 scripts/check_ai_signs.py <file(s)>      # .txt, .md or .html; "-" reads stdin
   python3 scripts/check_ai_signs.py <file> --summary
   ```
   It lists each matching line under its sign number. It only catches the signs a pattern can match. Rule of three, elegant variation, uniform sentence length, puffed-up structure and summary endings need your own reading, and so do links: check that each one resolves to what it claims. Without code execution, make the same pass by hand using `references/signs.md`.

3. **Rewrite.** Go sentence by sentence through everything flagged, then read the whole piece once more for the signs that need judgement. Rules for the rewrite:
   - **Keep every fact, number, name, date, link and claim.** De-AI'ing changes how things are said, never what is said. If a sentence was only padding, delete it. If it carried a fact, keep the fact.
   - **Keep the author's voice and conventions**: person (I/we/you), spelling (UK/US), tone, formatting (Markdown, HTML, JSX, plain text), and any length limits (SEO titles about 60 characters, meta descriptions about 155, button labels).
   - **Never change quotations** of real people or sources, titles of works, or legal text.
   - **Em dashes**: rewrite with commas, colons, parentheses or full stops. Don't swap in another dash. One or two in a long piece is fine. Don't overshoot: turning every dash into a full stop gives a run of short, same-length sentences, which newer models produce and the guide counts as a sign in itself. Vary the sentence length.
   - **Contrasts** ("not X but Y", "rather than", "not just… it's"): state the positive claim on its own, unless a reader really would assume the opposite.
   - **Unknowns**: if the original says something isn't known, keep that honesty. Say it once, concretely, along with what the reader should do ("Hours aren't posted; call ahead"). Don't pad it with speculation.
   - **Plain words**: is/has instead of serves as/boasts. Used, tried, moved, to, before.
   - **Clean up leftovers**: strip `utm_source=chatgpt.com` and similar tracking parameters from links, delete citation markup like `contentReference[oaicite:1]`, and convert stray Markdown to the target format.
   - **Don't over-correct.** Perfect grammar, a formal register, a single transition word and an unsourced claim are *not* signs (see section 7 of the reference). Leave clean sentences alone.

4. **Re-scan and re-read.** Run the scanner again and aim for zero hits. A hit you keep on purpose is fine: a quotation, a proper noun like "Key Largo", or a word used literally ("landscape" for a painting). Note it in your report.

5. **Report briefly.** Give the rewritten text (or confirm which files you edited). Then add a short note with the sign counts before and after, two or three representative before/after examples, and anything you left in on purpose. Keep the note short; the rewrite is the deliverable.

## Quick reference

The signs in brief (details and fixes are in `references/signs.md`):

| # | Sign | Typical tells |
|---|------|---------------|
| 1.1 | Undue significance / legacy | stands as, testament, pivotal role, reflects broader, enduring legacy |
| 1.2 | Canned notability | featured in, independent coverage, active social media presence |
| 1.3 | Superficial -ing analysis | "…, highlighting/ensuring/reflecting…", valuable insights |
| 1.4 | Promotional tone | vibrant, nestled, in the heart of, boasts, world-class, seamless |
| 1.5 | Vague attribution | experts say, observers note, studies show, widely regarded |
| 1.6 | Challenges formula | "Despite its…, faces challenges… Despite these challenges…" |
| 1.7 | Title-defining lead | "X refers to…" |
| 1.8 | Paired headings | Awards and recognition, Challenges and legacy |
| 1.9 | Shaped-discussion claims | has shaped conversations/debate about |
| 1.10 | Identified-by-source framing | is listed in, profile lists her as, was identified by |
| 2.1 | AI vocabulary | additionally, crucial, delve, enhance, foster, key, landscape, robust, tapestry; newer: leverage, quietly, dependable, multifaceted (in clusters) |
| 2.2 | Copula avoidance | serves as, functions as, represents, features/offers (for "has") |
| 2.3 | Vague association | associated with, in connection with |
| 2.4 | Negative parallelism | not only…but, it's not X it's Y, no X no Y just Z, rather than |
| 2.5 | Rule of three | stacked triplets used for rhythm |
| 2.6 | Elegant variation | synonym cycling for one noun |
| 3.1–3.8 | Formatting | Title Case headings, bold everywhere, **Label:** bullets, em dashes, emoji, tiny tables, mixed curly quotes, --- between sections |
| 3.9–3.10 | Leftover markup | Markdown in email/HTML, oaicite markup, utm_source=chatgpt.com |
| 4.1–4.3 | Chat leftovers | I hope this helps, let me know, "not widely documented", "should not be confused with", [Your Name] |
| 4.4–4.6 | Chat leftovers | as an AI language model, text cut off mid-sentence, "I have carefully reviewed" |
| 5.1–5.2 | Older habits | it's important to note, may vary, In conclusion, Overall |

## Example

**Input**
> Nestled in the heart of the city, our café stands as a testament to the town's rich cultural heritage — it's not just a coffee shop, it's a gathering place. Additionally, the menu boasts a diverse array of pastries, showcasing our commitment to quality. While specific details about opening hours are not widely documented, it's important to note that hours may vary.

**Output**
> Our café is on the main square, in a building that has been a bakery since 1911. People come for the coffee and stay for hours. We bake about twenty kinds of pastry each morning. Opening hours change with the seasons, so check our Instagram before you visit.

The details "1911", "twenty kinds" and "Instagram" would come from the user. If those facts aren't available, ask, or write the plain version without them: "Our café is on the main square. We bake pastries every morning. Hours change with the seasons, so check before you visit." Never invent facts to replace puffery.
