# Discovery Interview & Interactive Discovery

Concepts and creative directions cannot be generated from thin air. This interview actively probes the user's mind to uncover their true intent, physical context, emotional stakes, and aesthetic taste.

---

## 1. The Hard Interactive Discovery Gate (`ask_question`)

**NEVER SKIP INTERACTIVE DISCOVERY. NEVER GUESS OR ASSUME USER INTENT.**

On Turn 1 of any new surface or redesign task, the Director **MUST ALWAYS** invoke `ask_question` to present structured multiple-choice questions across these dimensions:

### Dimension 1: Physical Situation & User Context
- **Option A**: *Focused Desk / Workstation* (Unhurried, mouse/keyboard precision, large screen space, deep focus).
- **Option B**: *Mobile in Transit / One-Handed* (Walking, glare, hurried, thumb-reach ergonomics critical, distraction).
- **Option C**: *Bedside / Dim Light / Low Energy* (Late night/early morning, drowsy, dark mode critical, high contrast, zero cognitive friction).
- **Option D**: *High-Velocity Operational Cockpit* (Urgent monitoring, high throughput, zero tolerance for decorative delay).

### Dimension 2: The Single Question
- **Option A**: *"What is my status right now?"* (Instant status telemetry & live progress).
- **Option B**: *"What single action do I take next?"* (Task execution & workflow trigger).
- **Option C**: *"What happened while I was away?"* (Activity summary & timeline delta).
- **Option D**: *"How am I performing over time?"* (Trends, sparklines, comparative analytics).

### Dimension 3: Visual Archetype & UI Design Class
- **Option A**: *Instrumental Precision (Class 1)* — Dark graphite, 1px hairlines, tabular monospaced figures, micro-telemetry (Linear/Xcode).
- **Option B**: *Tactile Humanist (Class 2)* — Warm cream/charcoal, 16–24pt rounded radii, paper craft, physical detents (Notion/Things 3).
- **Option C**: *High-Contrast Editorial (Class 3)* — Stark monochrome void balance, oversized display serif, Swiss grid (NYT/Stripe Press).
- **Option D**: *Spatial / Translucent Depth (Class 4)* — Layered glass blur, dynamic mesh gradients, liquid physics (Apple visionOS/iOS 18).
- **Option E**: *Industrial Monolith (Class 5)* — Obsidian matte, sharp 0–2pt corners, high-vis neon indicators, schematics (Teenage Engineering).
- **Option F**: *Sensory Luxury (Class 6)* — Whispered 0.5px borders, champagne/midnight contrast, micro-haptics (Leica/Hermès).

### Dimension 4: Visual Expression & Density
- **Option A**: *Compact Visual Telemetry* (Dense graphs, micro-gauges, maximum scanability, minimal text).
- **Option B**: *Expressive & Atmospheric* (Rich backgrounds, lighting, depth, emotional hero moments, generous breathing room).
- **Option C**: *High-Speed Utilitarian* (Crisp, direct, zero delay, instantaneous state recognition).

---

## 2. The 6 Core Discovery Inquiries

1. **Who opens this, where, and in what state?** (Physical situation, lighting, noise, time pressure, emotional state).
2. **What one question do they open it to answer?** (Forces the single primary visual anchor).
3. **What happens if they do not use it for a month?** (Distinguishes an instrument from a habit from an appliance).
4. **What can this product genuinely not know or not promise?** (The truthful limit — often the richest source of distinctive craft).
5. **What would make them tell a friend about it?** (Locates the Signature Moment before pixels are drawn).
6. **What must be true or the design has failed?** (The non-negotiable invariant).

---

## 3. Handling Content-as-Brief

Common scenario: the user pastes a resume, spreadsheet, or raw feature list.
- **Classify as CONTENT**: Extract the *shape* (cardinality, maximum text length, state counts) for slot sizing.
- **Never derive DIRECTION from CONTENT**: A resume with "enterprise banking" does not mean the UI should look like a 1990s bank. Direction comes strictly from the committed concept and design class.

---

## 4. No Fast-Path Bypass Rule

There is **zero tolerance for skipping discovery**. If a user provides a brief 1-line prompt:
- **Do NOT guess or proceed with silent assumptions.**
- **Do NOT start writing `.spec.md`, `.slots.md`, or component code.**
- **MUST ALWAYS run `ask_question` and pitch 2–3 rival concepts first.**
