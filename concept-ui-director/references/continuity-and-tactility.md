# Continuity, Materials & Tactility

The interface must feel *physically crafted* and continuous, not like a slideshow of disconnected rectangles.

---

## 1. Continuity: Objects Persist Across Edges

**The element you touch becomes the screen you arrive at.**

When a list card opens into a detail view, the card transforms fluidly into the detail surface (matched geometry / shared element transition). The user's spatial focus stays anchored to one continuous object.

### Specify Per Navigation Edge

Every navigation transition in `.uispec/navigation.md` defines its continuity contract:

| Edge (From $\to$ To) | Persisting Element | Becomes | Transition Physics | Reverse Landing |
|---|---|---|---|---|
| **Feed Card $\to$ Detail** | Card container, thumbnail, headline | Hero header & full-bleed media | Matched geometry, 280ms spring | Card collapses back into exact scroll position |
| **Telemetry Tile $\to$ Inspector** | Metric sparkline & badge | Expanded historical chart | Morphing path transition | Chart condenses smoothly back to tile |
| **Action Trigger $\to$ Sheet** | Primary button target | Floating bottom sheet container | Scale expand with spatial detent | Sheet slides down, button returns to rested state |

---

## 2. Material Hierarchy & Atmospheric Lighting

Materials establish physical depth and spatial relationships without visual clutter:

```
[Layer 3: Interactive Floating Chrome]  → Translucent Glass / Vibrancy (`backdrop-filter: blur(20px)`)
[Layer 2: Elevated Surface Container]   → Surface Fill with Specular Rim Highlight (`inset 0 1px 0 rgba(255,255,255,0.1)`)
[Layer 1: Canvas Base]                 → Rich Atmosphere / Mesh Gradient / Deep Graphite Fills
```

- **Material Rules**:
  - *Class 1 (Instrumental Precision)*: Opaque crisp planar surfaces with 1px hairlines. No blur lag.
  - *Class 2 (Tactile Humanist)*: Warm paper texture fills with soft 0.06 opacity border washes.
  - *Class 3 (High-Contrast Editorial)*: Pure flat planes, stark solid fills, zero gradients.
  - *Class 4 (Spatial Depth)*: Multi-layered glass blur (`backdrop-filter: blur(24px)`), dynamic mesh vibrancy, and floating specular highlights.
  - *Class 5 (Industrial Monolith)*: Matte obsidian with exposed technical grid hairlines.
  - *Class 6 (Sensory Luxury)*: Brushed titanium or midnight obsidian with 0.5px champagne/platinum hairlines.

---

## 3. Tactility & Press Response

Different elements have different physical mass and mechanical properties:

| Element Class | Physical Touch Response | Implied Material |
|---|---|---|
| **Primary Action Button** | 0.96x scale compression on `:active` with tactile spring rebound | Solid, substantial mass |
| **Interactive Metric Tile** | 0.98x scale compression + subtle surface luminance boost | Responsive instrument gauge |
| **List Row** | Background surface tint wash (no scale shift) | Surface plane, zero vertical mass |
| **Draggable Card** | 1:1 finger tracking with momentum and edge rubber-banding | Physical floating token |
| **Mechanical Detent Toggle**| Snaps with resistance at 50% threshold | Detented mechanical switch |
| **Non-Interactive Display**| Zero physical or visual response on touch | Static display read-out |

---

## 4. Sensory Haptics Protocol (`UIFeedbackGenerator`)

Tactile feedback confirms physical reality:

- **Selection Detent (`UISelectionFeedbackGenerator`)**: Fires on rotary knobs, slider ticks, and segment switches.
- **Light / Medium Impact (`UIImpactFeedbackGenerator(style: .light | .medium)`)**: Fires on button tap-up when an action successfully triggers.
- **Rigid / Heavy Impact (`UIImpactFeedbackGenerator(style: .rigid | .heavy)`)**: Fires on destructive or irreversible state commits (e.g. archiving a critical item).
- **Notification Feedback (`UINotificationFeedbackGenerator`)**: Fires on workflow completion (`.success`) or error (`.error`).
- *Rule*: Haptics fire strictly on actual outcome commit, never on touch-down before completion.
