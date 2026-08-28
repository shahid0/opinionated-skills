# Concept & Creative Commitment

The concept is the soul of the interface. The creative philosophy gives it beauty, expression, and form.

---

## 1. What a Concept Is

One sentence naming what the interface **is** — not what it does.

- *"Lets users track sleep"* is a feature list.
- *"A bedside instrument you read in the dark without your glasses"* is a concept: it forces the UI Design Class (Instrumental Precision), large scale typography, high-contrast monochrome values, tactile detents, and why there is no dashboard, all at once.

A concept is doing its job when it **answers questions you did not ask it**. If you have to consult taste or default to generic templates to resolve a layout question, the concept is too weak.

---

## 2. A Concept Must Forbid Things

A concept that rules nothing out is a generic mood board. For every concept, write the forbidden list — and make it specific enough to sacrifice real options:

- *Bedside instrument* forbids: dashboards, complex multi-column charts on primary surfaces, two-handed interactions, decorative animations that delay viewing, more than one primary numeric value.
- *Field notebook* forbids: generic onboarding tours, cartoon empty-state illustrations, celebration confetti, anything that implies the app is a participant rather than a quiet canvas.

---

## 3. Commit the UI Design Class

Every concept must declare its **UI Design Class** (see `ui-design-classes.md`):

1. **Class 1: Instrumental Precision** (75% visual telemetry / 25% text)
2. **Class 2: Tactile Humanist** (60% spatial grouping / 40% text)
3. **Class 3: High-Contrast Editorial** (65% layout geometry / 35% text)
4. **Class 4: Spatial / Translucent Depth** (80% depth & materials / 20% text)
5. **Class 5: Industrial Monolith** (85% telemetry & schematics / 15% text)
6. **Class 6: Sensory Luxury** (70% material finish & poise / 30% text)

---

## 4. Propose 2–3 Rival Concepts & STOP (The Human Choice Gate)

Always present 2–3 concepts that are genuinely distinct — not the same idea at three intensities. Each proposal gets:

```markdown
### Rival Concept A: [Name]
- **The Sentence**: [What the interface IS in 1 punchy sentence]
- **UI Design Class**: [Class 1–6 with target visual ratio]
- **What It Forbids**: [3 to 5 real, painful losses]
- **The Visual Journey**:
  - *1st Seen*: [Primary visual anchor / telemetry beacon]
  - *Next Noticed*: [Supporting data / sparkline grid]
  - *Attention Lands*: [Primary action trigger]
- **The Signature Moment**: [The single physical / emotional peak interaction]
```

### 🛑 Mandatory Human Selection Stop
**The Director MUST STOP HERE AND END THE TURN.** Never commit silently. The human user must review the rival pitches and explicitly pick the winning concept before any `.uispec/` contracts or code can be written.

---

## 5. The Fit Test

Applied to every concept before commitment, and again at verification:

> **Could this same design be applied to an unrelated product with only the labels swapped?**

If yes, it is a template. Reject it and design again. Structural uniqueness, purposeful composition, and custom visual telemetry must make the design inseparable from this specific product.

---

## 6. The Ultimate Evaluation

Every decision derived from the concept must pass the ultimate test:

> **"Does this make the experience clearer, more beautiful, more intuitive, or more memorable?"**

If yes, pursue it boldly — even if it requires stretching design system constraints.

---

## 7. Writing It to `.uispec/concept.md` (Post-Approval Only)

```markdown
# Concept & Creative Commitment

Status: committed <date>. Chosen from 3 rivals; see restraint-log.md.

## What this is
<one sentence defining what the interface IS>

## UI Design Class
<Class 1–6> (Target Visual-to-Text Ratio: NN%)

## Why this and not the alternatives
<two or three sentences naming the rivals and the trade-offs>

## This concept forbids
- <specific, real loss>
- ...

## The Signature Moment
<the single emotional and physical peak moment a person would describe to someone else>

## Decisions this concept already made
| Question | Answer the concept & design class force |
|---|---|
| Primary visual anchor | ... |
| Surface & Material logic | ... |
| Typography pairing | ... |
```
