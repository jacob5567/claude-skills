#!/usr/bin/env python3
"""Scan text for pattern-matchable signs of AI writing.

Sign numbers match references/signs.md. Signs that need judgement
(1.8 paired headings, 2.5 rule of three, 2.6 elegant variation) are not
checked here; read for those yourself.

Usage:
    check_ai_signs.py FILE [FILE ...]     # .txt, .md or .html; "-" reads stdin
    check_ai_signs.py FILE --summary      # counts per sign only
"""

import argparse
import html
import re
import sys
from collections import defaultdict


def rx(*parts):
    return re.compile(r"\b(?:" + "|".join(parts) + r")\b", re.IGNORECASE)


# Sentence-level signs: (number, name, pattern)
SENTENCE_SIGNS = [
    ("1.1", "Undue significance / legacy", rx(
        r"(?:is|was|are|stands as|serves as) an? (?:testament|reminder)", r"testament to",
        r"(?:crucial|pivotal|vital|significant|key) (?:role|moment|turning point)",
        r"(?:underscor|highlight)\w* (?:its|the|their) (?:importance|significance)",
        r"reflect\w* (?:the |a )?broader", r"(?:ongoing|enduring|lasting) (?:legacy|impact|influence|relevance)",
        r"setting the stage for", r"marking (?:a|the)", r"shaping the",
        r"(?:represents?|marks?|marked) a (?:shift|turning point)", r"evolving landscape",
        r"focal point", r"indelible mark", r"deeply rooted",
        r"generated (?:\w+ )?debate", r"broader reflection", r"forms? part of the wider",
        r"(?:the )?distinction (?:matters|is important) because")),
    ("1.2", "Canned notability", rx(
        r"independent coverage", r"(?:local|national|international|regional) media(?: outlets)?",
        r"(?:music|business|tech|industry) outlets", r"trade publications",
        r"(?:cited|profiled) (?:in|by)", r"(?<!has been )(?<!have been )featured (?:in|by)", r"leading expert",
        r"(?:active|strong) (?:social media|digital|online) presence")),
    ("1.3", "Superficial -ing analysis", re.compile(
        r",\s+(?:thereby\s+)?(?:highlighting|underscoring|emphasi[sz]ing|ensuring|reflecting|"
        r"symboli[sz]ing|contributing to|cultivating|fostering|encompassing|enhancing|showcasing)\b"
        r"|\bvaluable insights?\b|\b(?:align|resonate)s? with\b", re.IGNORECASE)),
    ("1.4", "Promotional tone", rx(
        r"boasts?", r"boasting", r"vibrant", r"rich (?:cultural|culture|heritage|history|tradition)",
        r"profound", r"exemplif(?:y|ies|ied)", r"commitment to", r"natural beauty", r"nestled",
        r"in the heart of", r"groundbreaking", r"renowned", r"diverse (?:array|range)",
        r"breathtaking", r"stunning", r"world-class", r"seamless(?:ly)?", r"state-of-the-art",
        r"unparalleled", r"must-visit")),
    ("1.5", "Vague attribution", rx(
        r"industry reports?", r"observers (?:have )?(?:noted|cited|said|say|note)",
        r"experts (?:argue|say|believe|agree|suggest|note)", r"some critics", r"critics argue",
        r"several sources", r"studies (?:show|suggest|have shown)", r"research (?:shows|suggests)",
        r"widely (?:regarded|considered|recogni[sz]ed|seen)", r"many believe")),
    ("1.6", "Challenges formula", rx(
        r"despite (?:its|these|this|the|their) [\w\s,-]{0,60}challenges", r"despite these challenges",
        r"faces? (?:several|many|numerous|significant|a number of) challenges",
        r"continues? to thrive", r"future (?:outlook|prospects)", r"challenges and legacy")),
    ("1.7", "Title-defining lead", rx(r"refers to", r"is a curated (?:list|compilation)",
                                      r"is the chronological list")),
    ("1.9", "Shaped-discussion claims", rx(
        r"(?:has|have|had) shaped (?:the )?(?:conversations?|discussions?|debates?)",
        r"in public discussions?", r"sparked (?:\w+ )?(?:conversations?|discussions?|debates?)")),
    ("1.10", "Identified-by-source framing", rx(
        r"(?:identifies|identified|lists|listed|describes|described) (?:\w+ ){1,4}as (?:an?|the|one)",
        r"(?:was|is|were|are) identified by", r"is listed (?:in|on|as)", r"profile lists",
        r"biography records")),
    ("2.1", "AI vocabulary", rx(
        r"additionally", r"bolster(?:ed|s|ing)?", r"crucial", r"delv(?:e|es|ed|ing)",
        r"emphasi[sz]ing", r"enduring", r"garner(?:ed|s)?", r"intricate", r"intricacies",
        r"interplay", r"key", r"landscape", r"meticulous(?:ly)?", r"pivotal",
        r"underscor(?:e|es|ed|ing)", r"tapestry", r"testament", r"valuable", r"vibrant",
        r"enhanc(?:e|es|ed|ing)", r"foster(?:s|ed|ing)?", r"highlighting", r"showcas(?:e|es|ed|ing)",
        r"robust", r"realm", r"navigat(?:e|ing) the", r"embark(?:s|ed)?", r"multifaceted",
        r"deep dive", r"highlights?", r"leverag(?:e|es|ed|ing)", r"causal", r"empirical", r"correlat\w*")),
    ("2.2", "Copula avoidance", rx(
        r"serv(?:es|ed|ing) as", r"stands? as", r"stood as", r"functions? as", r"operates? as",
        r"represents", r"boasts", r"features", r"ventured into", r"began (?:his|her|their) career as")),
    ("2.3", "Vague association", rx(r"associated with", r"in connection (?:with|to)", r"connected (?:with|to)",
                                    r"in association with")),
    ("2.4", "Negative parallelism", re.compile(
        r"\bnot only\b.{0,80}\bbut\b"
        r"|\b(?:it'?s|it is|this is|that'?s|isn'?t|is not|aren'?t|are not|wasn'?t|was not) (?:just|merely|simply|only) (?:a |an |the |about )?\w+"
        r"|\b(?:it|this|that) (?:isn'?t|is not|wasn'?t|was not) [^.;:]{1,40}[,;:]\s*(?:it|this|that)(?:'s| is| was)\b"
        r"|\bnot [^.,;]{1,40},?\s+but\b"
        r"|\bno \w+, no \w+(?:,| or)? (?:just|only)\b"
        r"|\brather than\b", re.IGNORECASE)),
    ("4.1", "Chat leftovers", rx(
        r"i hope this helps", r"hope this helps", r"certainly!", r"great question",
        r"let me know if", r"would you like me to", r"here is an? ", r"here'?s an? ",
        r"in this (?:section|article|post),? (?:we|i) will", r"feel free to", r"happy to help",
        r"of course!", r"you'?re absolutely right", r"is there anything else",
        r"more detailed breakdown", r"(?:check|verify|confirm)\b.{0,60}\bbefore (?:publishing|publication|submitting|submission)",
        r"delete this (?:section|note|comment)")),
    ("4.2", "Knowledge-cutoff / gap speculation", rx(
        r"as of my (?:last|latest) (?:update|knowledge|training)", r"specific details",
        r"not widely (?:documented|disclosed|known|reported|available)",
        r"based on (?:the )?available information", r"maintains a low profile",
        r"limited (?:public )?information", r"information is limited",
        r"(?:as of|up to) my last (?:knowledge|training) (?:update|cutoff)", r"not publicly available",
        r"in the (?:provided|available) (?:sources|search results|information)", r"search results",
        r"keeps? (?:\w+ )?personal details private", r"does not by itself establish",
        r"does not establish", r"should not be confused with")),
    ("4.3", "Placeholders", re.compile(
        r"\[(?:your|insert|describe|add|enter|company|name|date|link)[^\]]*\]|\bINSERT_\w+|\b\d{4}-XX-XX\b"
        r"|\{\{\s*\w+\s*\}\}|\bLorem ipsum\b|\b(?:INSERT|PASTE)_[A-Z_#]+|\bSOURCE_PUBLISHER\b"
        r"|\((?:add|insert) your [^)]*\)|\(if available\)|\bexample\.com\b|\[year\]", re.IGNORECASE)),
    ("4.4", "Refusal / model self-reference", rx(
        r"as an ai(?: language model)?", r"as a large language model", r"i cannot (?:offer|provide|give)[^.]{0,60}but i can",
        r"i'?m (?:sorry|unable), but (?:i|as)")),
    ("4.6", "Customer-service tone", rx(
        r"(?:i|we) have carefully reviewed", r"carefully reviewed", r"(?:any )?inconvenience (?:this|i|we) may have caused",
        r"please point them out", r"i will (?:try|do my best) to resolve", r"unsubstantiated speculation")),
    ("5.1", "Didactic disclaimers", rx(
        r"it'?s (?:important|worth|crucial|essential) (?:to )?(?:note|noting|remember|consider|mention|mentioning)",
        r"it is (?:important|worth|crucial|essential)", r"worth noting", r"may vary", r"keep in mind")),
    ("5.2", "Section summaries", re.compile(
        r"^\W*(?:in summary|in conclusion|overall|ultimately|to sum up|in short|all in all|conclusion\s*$)\b",
        re.IGNORECASE)),
]

SIGN_NAMES = {n: name for n, name, _ in SENTENCE_SIGNS}
SIGN_NAMES.update({
    "3.1": "Title Case headings", "3.2": "Boldface in prose", "3.3": "Bold-label bullets",
    "3.4": "Em dashes", "3.5": "Emoji as formatting", "3.6": "Tiny tables",
    "3.7": "Mixed curly and straight quotes", "3.8": "Thematic breaks between sections",
    "3.9": "Markdown in a non-Markdown format", "3.10": "Chatbot artefacts / tracking links",
    "2.1n": "Newer-model vocabulary cluster (mid-2026 onward)", "4.5": "Possible abrupt cut-off",
})

# Mid-2026 vocabulary: ordinary words, so only a cluster of 2+ in one sentence is reported.
NEWER_VOCAB = rx(r"challenge[sd]?", r"clearer", r"dependabl[ey]", r"echoe?d?", r"foster\w*", r"leverag\w*",
                 r"matters", r"multifaceted", r"practical", r"prioriti[sz]\w*", r"quietly", r"steady",
                 r"steadily", r"universally")
ARTEFACT = re.compile(r"contentReference\[[^\]]*\]|oaicite(?::\d+)?|turn\d+(?:search|news|view)\d+|\u21a9"
                      r"|utm_source=(?:chatgpt\.com|openai|copilot\.com|perplexity)|referrer=grok\.com", re.IGNORECASE)
MARKDOWN = re.compile(r"\*\*[^*\n]+\*\*|^\s{0,3}#{1,6}\s|^\s*[-*]\s+\S|\[[^\]\n]+\]\([^)\s]+\)|^\s*```")

SMALL_WORDS = {"a", "an", "the", "and", "or", "but", "nor", "of", "in", "on", "to", "for",
               "with", "at", "by", "from", "as", "vs", "via", "into", "per"}
EMOJI = re.compile("[\U0001F300-\U0001FAFF\U0001F000-\U0001F2FF☀-➿⭐⬆↔-↪]")
BOLD = re.compile(r"\*\*[^*\n]+\*\*|__[^_\n]+__")
BOLD_LABEL = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+(?:\*\*|__)[^*_\n]{1,60}(?::\s*(?:\*\*|__)|(?:\*\*|__)\s*:)")
BREAK = re.compile(r"^\s*(?:-{3,}|\*{3,}|_{3,})\s*$")
HEADING = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$")
SENT_SPLIT = re.compile(r"(?<=[.!?])[\"')\]]?\s+(?=[\"'(\[]?[A-Z0-9])")


def html_to_text(src):
    """Turn HTML into Markdown-ish lines so the line checks still work."""
    src = re.sub(r"(?is)<(script|style|noscript)\b.*?</\1>", "", src)
    src = re.sub(r"(?is)<!--.*?-->", "", src)
    src = re.sub(r"(?i)<h([1-6])\b[^>]*>", lambda m: "\n" + "#" * int(m.group(1)) + " ", src)
    src = re.sub(r"(?i)</h[1-6]>", "\n", src)
    src = re.sub(r"(?i)<li\b[^>]*>", "\n- ", src)
    src = re.sub(r"(?i)<(strong|b)\b[^>]*>(.*?)</\1>", r"**\2**", src)
    src = re.sub(r"(?i)<hr\b[^>]*>", "\n---\n", src)
    src = re.sub(r"(?i)<tr\b[^>]*>", "\n| ", src)
    src = re.sub(r"(?i)</t[dh]>", " | ", src)
    src = re.sub(r"(?i)<(?:br|/p|/div|/section|/article|/tr|/ul|/ol|/blockquote)\b[^>]*>", "\n", src)
    src = re.sub(r"<[^>]+>", "", src)
    return "\n".join(line.strip() for line in html.unescape(src).splitlines())


def is_title_case(heading):
    words = re.findall(r"[A-Za-z][\w'’-]*", heading)
    rest = [w for w in words[1:] if w.lower() not in SMALL_WORDS]
    caps = [w for w in rest if w[0].isupper() and not w.isupper()]
    return len(rest) >= 2 and len(caps) == len(rest)


def scan(text, markdown_ok=True):
    """Return {sign: [(line_no, snippet, match)]}.

    markdown_ok=False (plain text, or the raw source of an HTML file) reports Markdown syntax as 3.9.
    """
    hits = defaultdict(list)
    lines = text.splitlines()

    # Skip YAML front matter and fenced code blocks.
    skip = set()
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                skip.update(range(0, i + 1))
                break
    fence = False
    if not markdown_ok:
        for i, line in enumerate(lines):
            m = MARKDOWN.search(line)
            if m:
                hits["3.9"].append((i + 1, line.strip(), m.group(0).strip()))
    for i, line in enumerate(lines):
        a = ARTEFACT.findall(line)
        if a:
            hits["3.10"].append((i + 1, line.strip(), ", ".join(sorted(set(a)))))

    for i, line in enumerate(lines):
        if line.lstrip().startswith(("```", "~~~")):
            fence = not fence
            skip.add(i)
        elif fence:
            skip.add(i)

    has_curly = any(c in text for c in "“”‘’")
    has_straight = bool(re.search(r"[\"']", text))
    breaks = []
    table = []

    def flush_table():
        body = [r for r in table if not re.match(r"^\s*\|?[\s:|-]+\|?\s*$", lines[r])]
        if table and len(body) <= 4:  # header + up to 3 rows
            hits["3.6"].append((table[0] + 1, lines[table[0]].strip(), f"{len(body) - 1} data rows"))
        table.clear()

    for i, line in enumerate(lines):
        if i in skip:
            continue
        n = i + 1
        stripped = line.strip()

        if stripped.startswith("|"):
            table.append(i)
            continue
        flush_table()

        if BREAK.match(line):
            breaks.append(n)
            continue
        m = HEADING.match(line)
        if m and is_title_case(m.group(1)):
            hits["3.1"].append((n, stripped, m.group(1)))
        if BOLD_LABEL.match(line):
            hits["3.3"].append((n, stripped, "bold label"))
        else:
            for b in BOLD.findall(line):
                hits["3.2"].append((n, stripped, b))
        if "—" in line:
            hits["3.4"].append((n, stripped, f"{line.count(chr(0x2014))} em dash(es)"))
        e = EMOJI.findall(line)
        if e:
            hits["3.5"].append((n, stripped, "".join(e)))
        if has_curly and has_straight and re.search("[“”‘’]", line):
            hits["3.7"].append((n, stripped, "curly quote"))

        prose = re.sub(r"^\s*(?:#{1,6}|[-*+>]|\d+[.)])\s+", "", line)
        for sentence in SENT_SPLIT.split(prose):
            if not sentence.strip():
                continue
            for num, _, pattern in SENTENCE_SIGNS:
                found = pattern.findall(sentence) if num != "5.2" else pattern.findall(sentence.strip())
                if found:
                    words = sorted({(f if isinstance(f, str) else f[0]).strip().lower() for f in found})
                    hits[num].append((n, sentence.strip(), ", ".join(words)))
            newer = sorted({w.lower() for w in NEWER_VOCAB.findall(sentence)})
            if len(newer) >= 2:
                hits["2.1n"].append((n, sentence.strip(), ", ".join(newer)))
    flush_table()

    # 4.5: the last line of prose ends without closing punctuation.
    for i in range(len(lines) - 1, -1, -1):
        line = lines[i].strip()
        if not line or i in skip or BREAK.match(line) or line.startswith("|"):
            continue
        if not HEADING.match(line) and len(line.split()) >= 6 and not re.search(r"[.!?:;)\]\"'”’*_>]$", line):
            hits["4.5"].append((i + 1, line, "no closing punctuation"))
        break

    if len(breaks) >= 2:
        for n in breaks:
            hits["3.8"].append((n, "---", "thematic break"))
    return hits


def sort_key(sign):
    return tuple(int(re.sub(r"\D", "", p) or 0) for p in sign.split(".")) + (sign,)


def clip(s, width=140):
    return s if len(s) <= width else s[: width - 1] + "…"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+", help='files to scan; "-" reads stdin')
    ap.add_argument("--summary", action="store_true", help="print counts per sign only")
    args = ap.parse_args()

    grand = 0
    for path in args.files:
        if path == "-":
            text, label = sys.stdin.read(), "<stdin>"
        else:
            with open(path, encoding="utf-8", errors="replace") as f:
                text, label = f.read(), path
        is_html = label.lower().endswith((".html", ".htm")) or (
            path == "-" and bool(re.search(r"(?i)<(?:html|body|p|div)\b", text)))
        is_md = label.lower().endswith((".md", ".markdown", ".mdx")) or label == "<stdin>"
        hits = defaultdict(list)
        if is_html:
            for k, v in scan(text, markdown_ok=False).items():  # raw source: Markdown, artefacts
                if k in ("3.9", "3.10"):
                    hits[k].extend(v)
            text = html_to_text(text)
        for k, v in scan(text, markdown_ok=is_md or is_html).items():
            if not (is_html and k == "3.10"):
                hits[k].extend(v)
        total = sum(len(v) for v in hits.values())
        grand += total
        print(f"== {label}: {total} hit(s) across {len(hits)} sign(s)")
        for sign in sorted(hits, key=sort_key):
            items = hits[sign]
            print(f"  {sign} {SIGN_NAMES[sign]} ({len(items)})")
            if args.summary:
                continue
            for n, snippet, match in items:
                print(f"    L{n}: {clip(snippet)}")
                print(f"          [{match}]")
        print()

    if len(args.files) > 1:
        print(f"Total: {grand} hit(s)")
    print("Not checked (read for these yourself): 1.8 paired headings, 2.5 rule of three, "
          "2.6 elegant variation, uniform sentence length, broken links and references, "
          "puffed-up structure, summary endings mid-paragraph.")


if __name__ == "__main__":
    main()
