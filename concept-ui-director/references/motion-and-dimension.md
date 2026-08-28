# Motion, Dimension & Spatial Physics

Motion serves two masters: **communication** (explaining spatial causality) and **delight** (creating tactile satisfaction and brand personality).

---

## 1. The Core Motion Invariants

### Invariant 1: Settled Geometry Equals Static Geometry
**Every animation's settled geometry must be 100% identical to the static layout geometry.**
- Motion may animate only GPU-composited properties: `transform: translate3d / scale / rotate`, `opacity`, `filter: blur`, and `clip-path`.
- **Never animate layout-participating properties**: `height`, `width`, `margin`, `padding`, `gap`, `font-size`.
- This eliminates layout shift and ensures the interface renders identically with motion disabled.

### Invariant 2: Interaction Precedes Animation
- The primary action is interactive at frame one.
- Animations must be **interruptible and retargetable** mid-flight without stutter or reset.

---

## 2. Depth Tiers (0 to 3)

The director explicitly declares the depth tier in the spec sheet:

| Tier | Name | Visual Behavior | Optimal Design Class |
|---|---|---|---|
| **Tier 0** | **Flat Plane** | Fill and border only. Zero depth, zero shadows. | Class 1 (Instrumental) / Class 3 (Editorial) |
| **Tier 1** | **Layered Depth** | Stacked planes, directional shadows, bounded scroll parallax. | Class 2 (Humanist) / Class 6 (Luxury) |
| **Tier 2** | **Perspective & Tilt** | Pointer/gyro tilt ($\le 8^\circ$), dynamic specular lighting highlights. | Class 4 (Spatial) / Class 5 (Industrial) |
| **Tier 3** | **Volumetric Scene** | Real 3D camera, mesh geometry, shaders, spatial particles. | Class 4 (Spatial) *(Requires explicit opt-in)* |

---

## 3. Motion Budgets (Countable & Enforceable)

```
motion focal point            : 1 per transition (directs the eye)
concurrent animating elements : 2 max
looping animations            : 0 by default (permitted only for live activity beacons)
entrance sequence duration    : ≤ 450ms total to fully settled and interactive
stagger delay between items   : 30ms – 60ms
```

---

## 4. Fallback Ladder (Graceful Degradation)

| Condition | Fallback Behavior |
|---|---|
| **Reduced Motion (`prefers-reduced-motion`)** | Translation and scale become subtle 150ms opacity fades. Parallax and tilt disabled. Settled geometry remains 100% identical. |
| **Low Power Mode** | Looping activity pulses stop. Tier drops to Tier 1. Complex blurs disabled. |
| **Coarse Pointer (Mobile / Touch)** | Hover-dependent perspective tilts disabled; touch press scale active. |
| **Slow Device / Low Frame-rate** | Motion sequence skips to end state immediately; never plays slowly. |

---

## 5. Motion Table for the Spec Sheet

```markdown
## Motion Table
| Element | Trigger | Animated Properties | Duration / Curve | Settled State | On Re-trigger / Interruption |
|---|---|---|---|---|---|
| Hero Card | Mount | `opacity (0→1)`, `transform: translateY(12px→0)` | 280ms cubic-bezier(0.2, 0.8, 0.2, 1) | Equals static | Retargets from current position |
| Primary CTA | `:active` | `transform: scale(1→0.96)` | 140ms ease-out | Equals static | Springs back with slight overshoot |
```
