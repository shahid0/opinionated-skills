# Visual-First Glanceability & Cognitive Science

Visual communication is processed significantly faster than text. Understanding this cognitive architecture allows the director to build interfaces that feel effortless, intuitive, and instantly understandable.

---

## 1. The Cognitive Science: 13ms Scene Recognition

- **MIT Neuroscience (Potter et al., 2014)**: The human visual cortex identifies the concept of an image and extracts meaning from visual scenes in as little as **13 milliseconds**.
- **Serial Text vs. Parallel Visual Processing**: Reading text requires slow, serial phonological decoding (200–300ms per eye fixation). Visual scenes, spatial layouts, colors, and shapes are processed in parallel via pre-attentive iconic memory before conscious focus begins.
- **Dual-Coding Theory (Allan Paivio)**: Visual information creates dual memory traces in the brain (a visual representation + a verbal label). Pairing visual anchors with concise text labels produces maximum recall, instant scanability, and the lowest cognitive load.

---

## 2. The Visual-First Mandate ("Show, Don't Tell")

Whenever information or state needs to be communicated, apply the transformation ladder:

```
[Level 1: Passive Text Description]  ❌ BANNED
  └─ "The server backup has completed 78% of the data transfer and is currently healthy."

[Level 2: Text + Icon Key-Value]     ⚠️ MINIMAL
  └─ Status: Healthy | Backup: 78%

[Level 3: Visual Telemetry & Anchor]  ✅ REQUIRED
  └─ [ ◉ 78% Ring Gauge ] with Emerald Status Beacon & Pulsing Throughput Waveform
```

### Visual Telemetry Substitutions

| What Needs Communicating | ❌ Text Explanation (Banned) | ✅ Visual Solution (Mandatory) |
|---|---|---|
| **Completion / Progress** | "75% completed, 3 items left" | Circular progress ring or segmented bar with filled beads |
| **System Health** | "System is operational and running normally" | Pulsing status beacon (Emerald `#10B981`) + live micro-waveform |
| **Trend / Velocity** | "Increased by 14% over last 7 days" | 32px inline sparkline with direction vector $\nearrow$ |
| **Comparison** | "Version A had 12 errors while Version B had 2" | Interactive Before/After split card or side-by-side bar contrast |
| **Relationship / Hierarchy** | "Project X contains Module Y and Submodule Z" | Visual tree node connecting lines or spatial nested containers |
| **Active Mode / State** | "Currently in Recording Mode" | Edge-glow chromatic vignette + recording timeline cursor |
| **Threshold / Capacity** | "Storage is almost full (92% used)" | Horizon fill gauge transitioning from Emerald $\to$ Amber at 80% |

---

## 3. Pre-Attentive Visual Encoding

Guide the user's eye subconsciously within the first 500ms using the 4 pre-attentive visual channels:

1. **Form (Geometry & Size)**:
   - Make the primary focal element 2x to 3x larger in scale than secondary elements.
   - Use distinct container shapes (e.g. pill vs card vs circle) to signal distinct operational types.
2. **Color & Intensity**:
   - Reserve primary accent saturation for the **one hero element** or active signal.
   - Muted/neutral fills for secondary structures so the eye naturally settles on the primary outcome.
3. **Spatial Position & Proximity (Gestalt Law of Proximity)**:
   - Items with a causal relationship (Cause $\to$ Effect) are placed with tight grouping or visual connector lines.
   - Pinned actions anchor in the ergonomic bottom 30% Thumb Zone.
4. **Motion (Physical Feedback)**:
   - Movement signals state transitions instantly without requiring a read of confirmation copy.

---

## 4. Visual-to-Text Ratio Budgeting

Every emitted spec sheet must calculate and declare its **Visual-to-Text Ratio**:

$$\text{Visual Ratio} = \frac{\text{Area of Visual Telemetry, Imagery, Controls \& Void}}{\text{Total Screen Area}} \times 100\%$$

- **Class 1 (Instrumental Precision)**: 75% Visual / 25% Text
- **Class 2 (Tactile Humanist)**: 60% Visual / 40% Text
- **Class 3 (High-Contrast Editorial)**: 65% Visual / 35% Text
- **Class 4 (Spatial Depth)**: 80% Visual / 20% Text
- **Class 5 (Industrial Monolith)**: 85% Visual / 15% Text
- **Class 6 (Sensory Luxury)**: 70% Visual / 30% Text

---

## 5. The 13ms Glanceability Test (Verification)

During verification pass 2, evaluate the rendered UI against this test:

> **If shown for 100ms, does a person understand the system state, primary metric, and primary action without reading a single sentence?**

If they must read a paragraph to understand what is happening, the visual communication has failed. Return to the director to replace prose with visual telemetry.
