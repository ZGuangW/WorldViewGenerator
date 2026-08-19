---
name: worldview-chronicle-generator
version: 1.0.0
description: 世界观构建, 编年史生成, 世界观设计, 世界观文档, Automated worldview and chronicle generation system for storytelling. Interactively collects world type (fantasy, sci-fi, historical alternate, etc.) and timeline span, then generates a complete worldview chronicle through four modules — world framework, key plots, 16-dimension social portrait, and final integrated chronicle document. Trigger phrases - worldview building, chronicle generation, world design, story worldview, worldbuilding, worldview framework.
tags: [creative-writing, worldbuilding, storytelling, chronicle, lore]
---

# Worldview Chronicle Generation System

An automated four-module pipeline that builds a complete fictional worldview and generates a full-length chronicle document (~100,000 characters by default).

## When to Use This Skill

Activate when the user expresses any of these intents:

- "Help me build a worldview / 帮我构建一个世界观"
- "Design a story world / 设计一个故事的世界观"
- "Generate a chronicle / 生成编年史"
- "Worldview chronicle / 世界观编年史"
- "Build a fantasy/sci-fi world / 构建奇幻/科幻世界观"
- "Worldbuilding / lore creation"
- Any request to create fictional setting, history, lore, or timeline for narrative purposes

## Core Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  Module 1        Module 2        Module 3         Module 4      │
│  World Framework → Key Plots  → Social Portrait → Chronicle    │
│                                                                 │
│  world.md         plots.md        society.md       chronicle.md │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

The system operates as a **sequential pipeline** where each module builds on the previous output. All four modules execute in order, producing independent Markdown files at each stage.

## Execution Protocol

### Phase 0: Requirements Gathering

Collect the following from the user through interactive dialogue. Use your platform's native interaction mechanism (questions, prompts, forms) — adapt to whatever input method is available.

**Required inputs:**

| Input | Description | Examples |
|-------|-------------|----------|
| World type | Genre / setting type | Fantasy, sci-fi, historical, post-apocalyptic, urban fantasy, wuxia, steampunk, cyberpunk, mythic |
| Timeline span | Total years covered | 500 years, 3,000 years, 10,000 years |
| Core theme | Central conflict or motif | Gods vs humanity, civilization cycle, order vs chaos |

**Optional inputs:**

| Input | Description |
|-------|-------------|
| Special lore | Any pre-existing worldbuilding constraints |
| Style preference | Epic / documentary / biographical (default: epic) |
| Target length | Total character count (default: ~100,000) |
| Era emphasis | Specific periods to expand or condense |

**Interaction style:** Ask one or two questions at a time rather than presenting a long form. Start with world type and timeline, then proceed to theme and optional parameters.

---

### Module 1: World Framework

**Goal:** Produce the skeletal structure of the world.

**Process:**

1. Design core world settings:
   - Physical laws and natural rules
   - Supernatural / magic / psionic power system (if applicable)
   - Races / species / civilizations
   - Geographic layout and key regions
2. Write a 300–500 word overview of the world's narrative arc
3. Create a timeline with **8–12 key nodes**, each containing:
   - Node name / era label
   - Year / chronological marker
   - One-sentence event description

**Output file:** `world.md`

```markdown
# World Framework

## Basic Information
- Type: [World type]
- Timeline: [X years]
- Core theme: [Theme]

## Core Settings
[Detailed description of physical laws, power systems, races, geography]

## Overview
[300–500 word narrative overview]

## Timeline

| Node | Year | Event |
|------|------|-------|
| [Node 1] | [Year] | [Event] |
| ... | ... | ... |
```

**Checkpoint:** Display the framework summary and timeline to the user. Ask whether to adjust node count or direction before proceeding.

---

### Module 2: Key Plot Generation

**Goal:** Expand each timeline node into a full narrative episode.

**Input:** Read `world.md` timeline nodes.

**For each node, generate:**

| Component | Length | Content |
|-----------|--------|---------|
| Event narrative | 500–800 words | Full event description with vivid scenes and turning points |
| Key characters | 2–4 characters | Name, identity, motivation, pivotal actions |
| Turning point analysis | 200–300 words | How this event redirected the world's historical trajectory |
| Historical ripple | 100–200 words | Chain reactions and downstream consequences |

**Output file:** `plots.md`

```markdown
# Key Plots

## Node 1: [Name]
**Year:** [Year marker]

**Event Narrative:**
[500–800 words]

**Key Characters:**
- **[Name]**: [Identity], [Motivation], [Pivotal action]

**Turning Point Analysis:**
[200–300 words]

**Historical Ripple:**
[100–200 words]

---

[Repeat for each node...]
```

**Checkpoint:** Show a preview of the first two nodes. Confirm narrative style before continuing.

---

### Module 3: Social Portrait

**Goal:** Generate a panoramic social description for each era node across 16 dimensions.

**Input:** Read `world.md` (timeline) and `plots.md` (events).

**For each era node, generate content across these 16 dimensions:**

#### The 16 Dimensions

| # | Dimension | Core Focus |
|---|-----------|-----------|
| 1 | Political Landscape | Governance type, power structure, ruling factions, legal system, foreign relations |
| 2 | Demographics | Races / groups, population trends, inter-group relations, settlement patterns |
| 3 | Economy & Trade | Economic form, key industries, trade networks, currency, wealth disparity |
| 4 | Technology | Tool level, key innovations, knowledge transmission, tech-social interplay |
| 5 | Arts & Culture | Literary/art forms, masterpieces, aesthetic paradigms, cultural identity |
| 6 | Social Stratification | Class hierarchy, mobility channels, class relations, survival strategies |
| 7 | Daily Life | Food/clothing/housing/transport, labor patterns, leisure, gender roles |
| 8 | Marriage & Family | Marriage forms, family structure, gender power, wedding/funeral rites |
| 9 | Beliefs & Customs | Religious systems, deity pantheons, rituals, folk beliefs |
| 10 | Intellectual Currents | Philosophical systems, core values, schools of thought, intellectual change |
| 11 | Collective Psychology | Social mood, collective fears/dreams, identity, conformity pressure |
| 12 | Public Order | Crime, judiciary, private vs public justice, underground order |
| 13 | Information Flow | Media, communication networks, censorship, information monopoly |
| 14 | Existential Risks | Natural disasters, war, supernatural threats, resource scarcity |
| 15 | Era Aesthetics | Beauty ideals, body culture, architecture, fashion, rhetoric |
| 16 | Ecology & Nature | Environment, resource cycles, human-nature relationship |

#### Dimension Interdependencies

Ensure logical coherence across dimensions:

- **Economy → Stratification → Politics** (base structure → superstructure)
- **Beliefs → Intellectual Currents → Aesthetics** (spiritual unity)
- **Risks → Order → Information** (order maintenance triangle)
- **Demographics → Family → Daily Life** (social reproduction chain)
- **Technology → Economy → Arts** (technological diffusion chain)

**Output file:** `society.md`

```markdown
# Social Portraits

## [Era Name] ([Year Range])

### Political Landscape
[Content]

### Demographics
[Content]

### Economy & Trade
[Content]

### Technology
[Content]

### Arts & Culture
[Content]

### Social Stratification
[Content]

### Daily Life
[Content]

### Marriage & Family
[Content]

### Beliefs & Customs
[Content]

### Intellectual Currents
[Content]

### Collective Psychology
[Content]

### Public Order
[Content]

### Information Flow
[Content]

### Existential Risks
[Content]

### Era Aesthetics
[Content]

### Ecology & Nature
[Content]

---

[Repeat for each era node...]
```

**Checkpoint:** Show one era's portrait as preview. Ask about depth and emphasis before proceeding.

---

### Module 4: Chronicle Integration

**Goal:** Synthesize all three source files into a single, cohesive chronicle document.

**Input:** Read `world.md`, `plots.md`, `society.md`.

**Length rules:**
- User-specified: generate within ±10% of target
- Default: ~100,000 characters (Chinese) / ~50,000 words (English)

**Integration principles:**

1. Use `world.md` as the narrative skeleton — ensure logical flow
2. Use `plots.md` as narrative flesh — enrich character arcs and dramatic tension
3. Use `society.md` as world backdrop — enhance immersion and verisimilitude
4. **Organic fusion, not concatenation** — weave source material into seamless prose
5. Add transitional passages where the source files have narrative gaps
6. Maintain consistent narrative voice (epic / documentary / biographical — user chooses, default: epic)
7. Chapter division follows timeline nodes — each chapter centers on one key period

**Output file:** `chronicle.md`

```markdown
# [World Name] Chronicle

## Preface
[World overview, chronicle purpose — 200–300 words]

## Chapter 1: [Era / Event Name]
[Integrated narrative from all three source files]

## Chapter 2: [Era / Event Name]
[Integrated narrative from all three source files]

...

## Epilogue
[Concluding reflection — 300–500 words]

---

*Generated by Worldview Chronicle Generation System*
*Date: [YYYY-MM-DD]*
```

---

## File Structure

### Input / Output Files

```
project-directory/
├── world.md         # Module 1 output: Framework + timeline
├── plots.md         # Module 2 output: Node narratives
├── society.md       # Module 3 output: 16-dimension social portraits
└── chronicle.md     # Module 4 output: Integrated chronicle
```

### Skill Resources

```
worldview-chronicle-generator/
├── SKILL.md                              # This file — main entry point
├── references/
│   └── social-dimensions-guide.md        # Detailed 16-dimension reference
└── scripts/
    └── validate.py                      # Project validation + word count
```

---

## Interaction Guidelines

### Pacing

- Present one module at a time; do not dump all four modules at each interaction
- After each module, pause for user confirmation before proceeding
- If the user wants changes at any checkpoint, revise the current module before moving on

### Style Control Commands

| User says | Effect |
|-----------|--------|
| "More epic" / "更史诗感" | Increase grand narrative, tragic heroism, mythic resonance |
| "More documentary" / "更纪实感" | Add archival, historiographic, field-report tone |
| "More literary" / "更文学性" | Deepen psychological description and scene painting |
| "Emphasize [era]" / "调整时期侧重" | Expand or condense specific periods |
| "Length X" / "字数X" | Set target character/word count |

### Quality Standards

- Each timeline node should feel distinct in tone and era atmosphere
- Characters must have clear motivations and consequences
- Social dimensions must be internally consistent within each era
- The final chronicle should read as a unified narrative, not a patchwork
- Avoid info-dumping — weave worldbuilding into narrative naturally

### Language Adaptation

- Generate in the user's language (Chinese or English)
- Match vocabulary density and prose style to the target language
- Chinese: default ~100,000 characters for full chronicle
- English: default ~50,000 words for full chronicle

## Implementation Notes

- This skill does not require any specific platform, tool, or connector — it operates entirely through text generation and file I/O
- All output is Markdown for maximum portability
- The agent should use standard file system operations (read / write / edit) to manage output files
- No external APIs, databases, or services required
- Works in any agent environment with basic file system access
