# Verification & Quality Gates

Two passes. Pass 1 checks mechanical correctness; Pass 2 checks concept, beauty, and glanceability survival.

---

## Pass 1 — The 15 Mechanical Assertions

Run against the rendered component matrix across states:

| # | Assertion | Pass Criteria | Fails When |
|---|---|---|---|
| **1** | **No Undeclared Truncation** | No ellipsis in slots not declared `wrap-then-truncate-at-N`. | Ellipsis appears on values or names. |
| **2** | **Pinned Element Invariant** | Primary CTA and headers occupy identical screen coordinates across all states. | Action button moves on state switch. |
| **3** | **Settled Geometry Equals Static** | Rendered coordinates after animation settle match geometry with motion disabled. | Layout property animated (`height`, `gap`). |
| **4** | **Text Node Count Match** | Rendered text node count equals slot table count. | Filler headings or mock copy rendered. |
| **5** | **Verbatim Slot Strings** | All strings match `.slots.md` character-for-character. | Paraphrased or rewritten copy. |
| **6** | **Accent Color Budget** | Accent colors match declared budget (typically 1). | Palette drift. |
| **7** | **Decorative Element Budget** | Decorative elements equal budget (typically 0 unprescribed). | Extra background blobs, sparkles. |
| **8** | **Concurrent Animating Elements** | Concurrent animating elements $\le 2$. | Everything easing in at once. |
| **9** | **Looping Animations Budget** | Looping animations equal declared count (typically 0). | Decorative pulses or shimmers. |
| **10** | **Single Growth Region** | Only the declared growth region changes height between states. | Unintended layout reflow. |
| **11** | **Worst-Case String Support** | Longest string states render without clipping or overlap. | Text overflow on longest strings. |
| **12** | **Contrast Minimums** | Text meets contrast minimums in supported themes. | Washed out unreadable text. |
| **13** | **Touch Target Minimums** | All interactive targets $\ge 44\times 44\text{pt}$ (iOS) / $\ge 48\times 48\text{dp}$ (Web). | Cramped unclickable targets. |
| **14** | **Reduced-Motion Parity** | Interface renders 100% legible and functional with animations disabled. | State only distinguishable by motion. |
| **15** | **Zero Fabricated Values** | Missing data rendered per spec; never zero or mock lorem ipsum. | Invented placeholder values. |

---

## Pass 2 — Concept, Beauty & 13ms Glanceability Survival

Pass 1 ensures no defects; Pass 2 ensures the design has an idea and beauty.

1. **The 13ms Glanceability Test**:
   - If shown for 100ms, does a user understand system state, primary metric, and primary action without reading sentences?
2. **The Fit Test**:
   - Could this same design be applied to an unrelated product with only the labels swapped? (If yes, it is a template. Redesign).
3. **Show, Don't Tell Audit**:
   - Are progress, health, trends, and relationships communicated via visual telemetry (rings, sparklines, beacons, connectors) rather than text paragraphs?
4. **Intentional Beauty & Atmosphere**:
   - Does the screen feel rich, crafted, and distinctive, or does it look like a generic wireframe? Does it evoke the intended emotional character?
5. **System Freedom vs. Rigid Prison**:
   - Is the composition purpose-built around this screen's goal, or was it forced into a generic 8-card grid?
6. **The Signature Moment**:
   - Does the single memorable interaction land with clarity and physical delight?
7. **Restraint Ledger Audit**:
   - Did the tenth use lose orientation noise? Was nonessential complexity ruthlessly edited out?
