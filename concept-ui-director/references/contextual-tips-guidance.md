# Contextual Tips & Progressive Guidance

Tips and guidance exist to help people navigate non-obvious capabilities or domain complexities without creating visual clutter or blocking interaction.

---

## 1. The Core Rule

**Give tips only where truly required. Never block interaction.**

A good tip is like a thoughtful note left by a craftsman: quiet, positioned exactly where hesitation occurs, immediately dismissible, and gone once understood.

---

## 2. When Tips Are Required

Apply tips only for:
1. **Truthful Limits**: When the product intentionally cannot promise or know something (e.g. *"Offline: Changes sync automatically when connected"*).
2. **Non-Obvious Gestures**: When an interaction relies on a gesture that lacks visual chrome (e.g. *"Swipe card left to archive, right to pin"* on first encounter).
3. **Complex Domain Objects**: When terminology has specific operational meaning (e.g. *"Reconciliation runs automatically at midnight UTC"*).
4. **First-Run Empty Orientations**: When a screen has no data yet and requires one clear orientation nudge.

### Never Use Tips For:
- Explaining self-evident buttons (*"Click here to save"*).
- Generic feature tours that pop up on launch.
- Marketing upsells disguised as tips.
- Obstructing modal takeovers that force a "Next" / "Done" click.

---

## 3. Visual & Structural Format

Tips must be **structural and non-blocking**, never modal:

1. **Inline Contextual Callout**:
   - Compact 1-line callout placed directly beneath the relevant control or section.
   - Distinct muted container fill (`rgba(255, 255, 255, 0.04)` or subtle accent wash).
   - Dismiss icon ($\times$) or automatic dismissal upon first successful interaction.
2. **Hover / Focus Micro-Affordance**:
   - Appears instantly on hover/focus after a subtle delay (150ms).
   - Crisp 1-sentence explanation; zero animation lag.
3. **Progressive Disclosure Indicator**:
   - Subtle `?` or `info` beacon that reveals a micro-popover on tap/hover without shifting page geometry.

---

## 4. The Recession Lifecycle (Experience Arc)

Tips participate directly in the **Experience Arc**:

| Experience Stage | Tip Behavior | Goal |
|---|---|---|
| **First Run (1st Use)** | Prominently visible adjacent to the key action or empty state. | Orientation & Confidence |
| **Tenth Use (10th Use)** | Structurally receded or collapsed into a quiet icon/tooltip. | Fast Task Execution |
| **Hundredth Use (100th Use)** | Completely absent. Zero residual tip chrome on screen. | Unencumbered Mastery |

### Reversible Recession
If an error occurs or if the user has not opened the surface for an extended period (>90 days), the contextual tip may reappear once as a helpful reminder.

---

## 5. Specification Contract for the Spec Sheet

Every contextual tip specified in `.uispec/specs/<surface>.spec.md` must declare:

```markdown
## Contextual Tips & Guidance
- **Target Element**: [Element ID / Container Name]
- **Trigger**: [First run | Hover | Input Focus | Error State]
- **Exact Copy**: "[Exact 1-sentence tip text from slot file]"
- **Recession Condition**: [Dismiss on tap | Recedes after 1st success | Collapses to icon at use 10]
- **Blocking**: False (Mandatory)
```
