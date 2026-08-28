# Spec Format & Emitted Contracts

The emitted spec sheet is a precise, machine-auditable contract for implementers (subagents, `agy` CLI, Cursor, and prompt platforms).

---

## The Core Spec Principle

**If a line cannot be verified against a screenshot or a count, it does not belong in the spec.**

Resolved values, complete string sets, and explicit visual telemetry replace prose and subjective adjectives.

---

## Spec Template (`.uispec/specs/<name>.spec.md`)

```markdown
# Spec: <surface name>

Pass: <n>. Written <date>. Disposable.
Concept: <the one sentence, quoted from .uispec/concept.md>
Contract: .uispec/screens/<name>.md
Content: .uispec/content/<name>.slots.md
UI Design Class: <Class 1–6> (Target Visual Ratio: NN%)

## 1. What this surface is for
- Single Question Answered: <exact question>
- Primary Action Trigger: <exact label, position, height>
- Concept Citation: <which line in concept.md forces this>

## 2. Creative Direction & Resolved Identity
- Design Class: <Class 1–6>
- Color Roles: Surface (`#...`), Elevated (`#...`), Border (`#...`), Accent Primary (`#...`).
- Typography Pairing: Display (`<font>`, `<size>`, `<weight>`) + UI/Mono (`<font>`, `<size>`, `<weight>`).
- Radii & Insets: Inset `24 / 16 below 360pt`, Radii `12pt / 24pt`.
- Depth Tier: <Tier 0–3>.

## 3. Visual Journey & Visual Telemetry Map
- **Visual Journey**:
  1. *First Seen*: [Primary Visual Anchor / Hero Telemetry Ring / Key Status Beacon]
  2. *Next Noticed*: [Supporting Metric Sparklines / Contextual Data Grid]
  3. *Attention Lands*: [Primary Conversion Action Button in Thumb Reach Zone]
- **Visual Telemetry Substitutions**:
  - [Metric 1]: Mapped to [Circular Ring Gauge / 32px Sparkline / Status Beacon]
  - [Metric 2]: Mapped to [Interactive Before/After Contrast Slider]

## 4. Contextual Tips & Guidance
- Target Element: <element key>
- Trigger: First run | Hover | Input Focus
- Exact Copy: "<verbatim string from slot file>"
- Recession Rule: Dismiss on tap | Recedes at 10th use

## 5. Element Inventory & Countable Budget
- Ordered Hierarchy: [Hero Anchor (Tier 1) → Telemetry Grid (Tier 2) → Pinned Action Bar (Tier 3)]
- Text Nodes: NN (Matches slot table exactly)
- Accent Colors: 1
- Container Levels: 3 max
- Decorative Elements: 0 (No unprescribed sparkles/blobs)
- Animating Elements: ≤ 2

## 6. Slot Table
| Slot Key | Source | States / Count | Longest Value | Overflow Rule | Notes |
|---|---|---|---|---|---|
| hero.metric | slot file | 1 | `99.8%` | `grow-container-never-truncate` | Tabular numbers |
| hero.status | slot file | 4 | `Reconciliation active` | `grow-container-never-truncate` | Sizes container |
| list.preview | slot file | 1..40 | 48 chars | `wrap-then-truncate-at-2` | Ellipsis allowed |

- **Growth Region**: `[Name of the single scrollable container]`
- **Pinned Below**: `[Action Bar anchored to safe area]`

## 7. State Matrix
| State | Visual Anchor State | Rendered Text Keys | Telemetry Beacon |
|---|---|---|---|
| **Empty / Initial** | Designed canvas illustration + 1 Nudge CTA | `empty.headline`, `empty.action` | Static Slate |
| **Active / Populated** | Live Ring Gauge + Waveform | `hero.metric`, `hero.status` | Pulsing Emerald |
| **Error / Offline** | Truthful Limit Banner + Retry CTA | `error.message`, `error.retry` | Hazard Amber |

## 8. Motion Table & Spatial Physics
| Element | Trigger | Animated Properties | Duration / Curve | Settled State | On Re-trigger |
|---|---|---|---|---|---|
| Hero Gauge | Mount | `opacity`, `transform: scale(0.96→1)` | 280ms spring | Equals static | Retargets |
| Primary CTA | `:active` | `transform: scale(1→0.96)` | 140ms ease-out | Equals static | Springs back |

- **Fallback Ladder**: Reduced motion = 150ms opacity fade, zero scale/translate; Low power = loops disabled.

## 9. Continuity & Tactility Contract
- **Navigation Edge (From → To)**: Card container transforms to Detail Hero Header via matched geometry (280ms).
- **Tactile Responses**: Primary CTA (0.96x compression + light haptic); List Row (surface wash, zero scale).

## 10. The Signature Moment & Emotional Peak
- What happens: [Description of the single memorable interaction]
- Why it is this one: [Citation from concept.md]

## 11. Verification Matrix
- Mechanical checks: Slots matched (100%), Text nodes (NN), Settled geometry static (Pass), 13ms Glanceability (Pass).

## 12. Deviations from Durable Contract
- [Numbered list of intentional deviations to be synced back to foundations.md]

## 13. Known Gaps — Not in Scope
- [Capabilities not supported by data; explicit instruction NOT to fabricate mock values]
```
