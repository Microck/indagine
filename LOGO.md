# Logo Prompts for Indagine

**Project Context**: Indagine is a meta-agent system for debugging other AI agents when they fail. It analyzes traces and tool behavior, classifies root cause using a shared failure taxonomy, and proposes diff-first fixes.

**Suggested Vibe**: Technical, investigative, forensic, crisp

**Signature Ingredients**:
- Artifacts: traces, tool calls, failure taxonomy tags, diff hunks (+/-), diagnosis + fix
- Actions: analyze, classify, pinpoint, propose fixes
- Metaphor: forensic light over a diff
- Avoid: generic circuit boards, generic "AI brain" icons, generic shield/lock motifs

---

## Color Palette

| Role | Color | Hex | Rationale |
|------|-------|-----|-----------|
| Primary | Deep Obsidian | `#1A1F2E` | Serious base for investigation, like a lab notebook / terminal background |
| Secondary | Amber Insight | `#F59E0B` | The "aha" highlight where the root cause is found |
| Accent | Electric Teal | `#14B8A6` | The fix emerging cleanly from the analysis |
| Neutral | Slate Whisper | `#64748B` | Supporting UI/docs tone without feeling generic |

**Palette Story**: Obsidian is the unknown failure. Amber is the moment a diagnosis clicks. Teal is the patch/fix that follows.

---

## Prompt 1: Abstract Geometric - Taxonomy to Lens
```
abstract geometric logo for Indagine, three stacked tag shapes flowing into a circular lens icon, sharp minimalist geometry, flat Amber Insight #F59E0B on white, centered, balanced negative space, Swiss design --ar 1:1 --stylize 70 --seed 41 --no gradient --no drop shadow --no bevel --no 3D --no reflection --no photo --no texture --no background scene --no glow --no complex lighting
```

Concept: Turns the failure taxonomy (tags) into investigation (lens) without generic "AI" symbolism.

---

## Prompt 2: Monoline - Bracketed Trace
```
monoline logo for Indagine, continuous single stroke forming nested brackets like a call stack trace icon with a single focal dot, precise geometry, flat Deep Obsidian #1A1F2E on white, centered, badge-ready --ar 1:1 --stylize 64 --seed 112 --no gradient --no drop shadow --no bevel --no 3D --no reflection --no photo --no texture --no background scene --no glow --no complex lighting
```

Concept: Brackets and nesting read as traces/call stacks and feel developer-native.

---

## Prompt 3: Negative Space - Diff Hunk Reveal
```
negative-space logo for Indagine, solid square mark with a crisp plus/minus diff hunk revealed as negative space inside, bold reduction, flat Deep Obsidian #1A1F2E with Electric Teal #14B8A6 cutout accent, centered on white, balanced negative space, modernist --ar 1:1 --stylize 68 --seed 77 --no gradient --no drop shadow --no bevel --no 3D --no reflection --no photo --no texture --no background scene --no glow --no complex lighting
```

Concept: Diff-first fixes represented directly as a minimal plus/minus motif.

---

## Prompt 4: Lettermark - I as Tool Call + Fix
```
lettermark logo for Indagine, stylized capital I built from two vertical bars with a small offset dot like a tool-call marker, pixel-clean corners, refined proportions, flat Electric Teal #14B8A6 on white, centered, balanced negative space, Paul Rand style --ar 1:1 --stylize 66 --seed 203 --no gradient --no drop shadow --no bevel --no 3D --no reflection --no photo --no texture --no background scene --no glow --no complex lighting
```

Concept: A simple I monogram that hints at tool calls and trace markers.

---

## Prompt 5: Pictorial Symbol - Lens + Diff Marks
```
pictorial logo for Indagine, minimal magnifying glass where the lens contains two tiny diff marks (one plus, one minus) aligned like a code review hunk, bold reduction, two-color Deep Obsidian #1A1F2E with Amber Insight #F59E0B highlight, centered on white, balanced negative space, Sagi Haviv style --ar 1:1 --stylize 72 --seed 88 --no gradient --no drop shadow --no bevel --no 3D --no reflection --no photo --no texture --no background scene --no glow --no complex lighting
```

Concept: Investigation (lens) plus fix intent (diff) in one favicon-friendly icon.

---

## Prompt 6: Emblem/Badge - Diagnosis Stamp
```
emblem logo for Indagine, circular stamp badge containing a small lens icon above a simplified checklist line (diagnosis) and a single highlighted check (fix), stamp-ready, flat Deep Obsidian #1A1F2E with Amber Insight #F59E0B accent, centered on white, refined proportions --ar 1:1 --stylize 70 --seed 156 --no gradient --no drop shadow --no bevel --no 3D --no reflection --no photo --no texture --no background scene --no glow --no complex lighting
```

Concept: A "case closed" badge for forensic diagnosis workflows.

---

## Prompt 7: Tech-minimal - Classify Card Grid
```
tech-minimal logo for Indagine, grid-aligned set of small cards where one card is highlighted like a selected taxonomy category, precise geometry, flat Slate Whisper #64748B with Amber Insight #F59E0B highlight, centered on white, architectural minimal --ar 1:1 --stylize 63 --seed 301 --no gradient --no drop shadow --no bevel --no 3D --no reflection --no photo --no texture --no background scene --no glow --no complex lighting
```

Concept: Classification is the product's signature move; the grid makes it explicit.

---

## Recommended Prompt (Recommended)

**Use**: Prompt 5

**Why**:
- Directly communicates "investigate + propose a diff" without generic security/AI imagery
- Reads well at small sizes (lens silhouette is instantly recognizable)
- Works cleanly in 1-2 colors and stays production-ready

**Runner-ups**:
- Prompt 2: best if you want ultra-minimal, developer-first trace iconography
- Prompt 6: best if you want an enterprise badge feel for docs and slides
