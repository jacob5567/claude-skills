# claude-skills

Two Agent Skills for Claude, packaged as a plugin marketplace so they install straight from this repo and pick up updates without re-uploading a ZIP.

| Plugin | What it does |
|---|---|
| [`adhd`](plugins/adhd/skills/adhd/SKILL.md) | Shapes every reply for a reader with ADHD: the next action comes first, steps are numbered, progress is restated each turn, time estimates are concrete, and tangents wait their turn. |
| [`de-ai-writing`](plugins/de-ai-writing/skills/de-ai-writing/SKILL.md) | Rewrites text to remove the signs of AI writing catalogued in Wikipedia's [*Signs of AI writing*](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) guide. Includes a scanner, `scripts/check_ai_signs.py`, that flags matching sentences in Markdown, HTML or plain text. |

## Install

### claude.ai and Claude Desktop

Plugins need a paid plan.

1. Open **Customize → Plugins → Add → Add marketplace → Add from a repository**.
2. Enter `jacob5567/claude-skills`.
3. Install `adhd`, `de-ai-writing`, or both.

Plugins added here also show up in Cowork and Claude Code.

### Claude Code

```
/plugin marketplace add jacob5567/claude-skills
/plugin install adhd@claude-skills
/plugin install de-ai-writing@claude-skills
```

To get updates automatically, open `/plugin`, go to **Marketplaces**, select `claude-skills` and turn on auto-update. Third-party marketplaces have it off by default. The plugins have no `version` field, so each commit to `main` counts as a new version.

### Upload as a ZIP instead

Zip the skill folder itself (for example `plugins/adhd/skills/adhd/`) so that `adhd/SKILL.md` is at the top of the archive, then upload it under **Customize → Skills → Upload a skill**. You'll need to upload it again after each change.

## Credits

Neither skill started here:

- `adhd` comes from the skill shared in [this r/ClaudeAI post](https://www.reddit.com/r/ClaudeAI/comments/1v8o1jn/whoever_created_the_adhd_skill_god_bless_you/).
- `de-ai-writing` comes from [this r/claudeskills post](https://www.reddit.com/r/claudeskills/comments/1wpbkmy/a_free_claude_skill_to_deai_your_written_content/).

Changes made in this repo:

- Both descriptions are shortened to fit claude.ai's 200-character limit.
- `adhd` was renamed from `i-have-adhd`.
- `de-ai-writing` gets a rewritten scanner script. Its sign catalogue is updated against the 22 November 2026 revision of the Wikipedia guide, which adds newer signs such as identified-by-source framing, chatbot citation artefacts, tracking links, and mid-2026 vocabulary.
