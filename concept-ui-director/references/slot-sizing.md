# Slot Sizing & Element Budgets

Layout shift and truncation are the same defect: **layout sized to current content instead of worst-case content.**

---

## 1. The 5 Core Sizing Rules

### Rule 1 — Complete String Sets
**Every element whose text varies by state ships its entire string set, and its slot is sized by the longest member.**
- A state-varying container never changes size when state toggles. Content crossfades inside stable geometry.

### Rule 2 — Live Numerics Get Fixed-Width Slots
- Live counters and metrics use monospaced tabular digits (`tabular-nums`) and are sized for the widest possible value (e.g. `$999,999.00` or `99h 59m`).

### Rule 3 — Exactly One Growth Region
- Exactly **one region per screen** may change height (e.g. a scrollable activity list). Pinned controls and primary action bars sit outside flow and never shift position.

### Rule 4 — The 4-Item Overflow Vocabulary
Every text slot declares its exact overflow rule:

| Behaviour | Meaning | When to Use |
|---|---|---|
| `wrap-unbounded` | Wraps to any number of lines; never clipped. | Explanatory copy, notes |
| `wrap-then-truncate-at-N` | Wraps to N lines, ellipsis beyond. | List previews, descriptions |
| `grow-container-never-truncate` | Container expands vertically; text never cut. | Values, amounts, names, durations |
| `stack-when-cramped` | Side-by-side pair converts into a vertical stack. | Label + Value pairs on narrow viewports |

### Rule 5 — Declared Ranges, Not Observed Values
Every repeating collection specifies its minimum and maximum count (e.g. `items.count: 1..40`), and the layout is tested at both extremes.

---

## 2. Element Budgets (Countable & Enforceable)

Countable rules are enforceable; taste is not. Every spec sheet includes resolved counts:

```markdown
## Element Budget
- **Total Rendered Text Nodes**: 12 (Matches slot table exactly; zero invented copy)
- **Accent Colors**: 1 Primary Signal
- **Container Levels**: 3 Max (Canvas → Panel → Control)
- **Icons**: 1 per action row
- **Decorative Elements**: 0 (No unprescribed sparkles, stock vectors, or filler blobs)
```
