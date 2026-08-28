# UI Design Classes (Visual Archetypes)

Every concept committed by the director must declare its **UI Design Class**. The Design Class establishes the visual grammar, surface logic, typography pairing, density budget, material physics, and visual-to-text ratio.

---

## The 6 UI Design Classes

```
Class 1: Instrumental Precision      (The Cockpit / Workbench)
Class 2: Tactile Humanist           (The Organic Atelier)
Class 3: High-Contrast Editorial    (The Modern Monograph)
Class 4: Spatial / Translucent Depth (The Volumetric Canvas)
Class 5: Industrial Monolith        (The Utilitarian Instrument)
Class 6: Sensory Luxury             (The High-End Atelier)
```

---

### Class 1: Instrumental Precision (The Cockpit / Workbench)
*Target: Technical tools, analytics engines, developer utilities, creative DAWs, trading terminals.*

- **Visual-to-Text Ratio**: 75% visual telemetry & controls / 25% text.
- **Reference Archetypes**: Linear, Bloomberg Terminal, Ableton Live, Xcode, Raycast.
- **Surface & Color**:
  - Primary Surfaces: Dark graphite (`#0F172A`, `#18181B`, `#09090B`).
  - Hairlines: 1px crisp borders (`rgba(255, 255, 255, 0.08)` or `#27272A`).
  - Accents: 1 high-visibility primary signal (Emerald `#10B981`, Electric Indigo `#6366F1`, or Amber `#F59E0B`).
- **Typography**:
  - Display: Crisp Geometric Sans (Geist, Inter, SF Pro Display) at semibold weight.
  - Numerics & Telemetry: Monospaced tabular digits (JetBrains Mono, SF Mono) for instant scanning.
- **Layout & Density**:
  - High compact density; 8px / 12px grid gutters.
  - Micro-sparklines, compact telemetry pills, and status badges replace verbose descriptions.
- **Material & Motion**:
  - Crisp opaque panels with zero blur lag.
  - Snappy, high-stiffness spring curves (120–180ms).
- **Forbidden**: Soft pastel gradients, giant floating drop-shadows, illustrative marketing fluff, verbose explanatory copy.

---

### Class 2: Tactile Humanist (The Organic Atelier)
*Target: Note-taking, thought organization, reading apps, thoughtful productivity, wellness.*

- **Visual-to-Text Ratio**: 60% spatial grouping & tactile elements / 40% text.
- **Reference Archetypes**: Notion, Things 3, Teenage Engineering (Field system), Apple Notes, Bear.
- **Surface & Color**:
  - Primary Surfaces: Warm off-white / cream (`#FAF9F6`, `#F5F3EF`) or warm charcoal (`#1C1917`).
  - Borders: Soft, whispered contours (`rgba(0, 0, 0, 0.06)` or `#E7E5E4`).
  - Accents: Earthy terracotta (`#EA580C`), olive (`#65A30D`), or warm amber (`#D97706`).
- **Typography**:
  - Display: Expressive Humanist Sans or Modern Serif (Fraunces, New York, Newsreader, Berkeley Mono).
  - Body: Highly legible humanist body (SF Pro Text, General Sans, Literata).
- **Layout & Density**:
  - Balanced, relaxed breathing room (16px / 24px padding).
  - Rounded geometry (16–24pt card radii, pill buttons).
- **Material & Motion**:
  - Paper-like surface textures, tactile detents on toggle, physical drag damping.
  - Natural spring overshoot with soft settle (200–300ms).
- **Forbidden**: Harsh pure black `#000000` against pure white `#FFFFFF`, neon cyberpunk colors, cold 1px wireframes.

---

### Class 3: High-Contrast Editorial (The Modern Monograph)
*Target: Publishing, portfolios, magazines, essays, architectural/design showcases, luxury commerce.*

- **Visual-to-Text Ratio**: 65% typographic scale & layout geometry / 35% text.
- **Reference Archetypes**: The New York Times Magazine, Stripe Press, ReadCV, Kinfolk, SSENSE.
- **Surface & Color**:
  - Primary Surfaces: Stark monochrome void balance (Deep black `#000000` / Stark paper white `#FFFFFF`).
  - Borders: Architectural grid hairlines or pure whitespace separation.
  - Accents: Strictly monochrome with at most 1 intentional, high-fashion accent (e.g. Acid Lime `#CCFF00`, International Klein Blue `#002FA7`).
- **Typography**:
  - Display: Dramatic, oversized Serif or Condensed Grotesque (Playfair, Instrument Serif, GT America, Bodoni).
  - Body: Precision editorial serif or clean Swiss grotesque (Times New Roman, Neue Haas Grotesk).
- **Layout & Density**:
  - Asymmetrical grid compositions; generous open voids; massive typographic scale contrasts.
  - Hero typographic moments that break container boundaries.
- **Material & Motion**:
  - Pure flat planar shifts, curtain reveals, smooth opacity fades without playful bouncy springs.
- **Forbidden**: Playful bouncy physics, rounded cartoon pills, pastel gradients, decorative emoji/sparkles.

---

### Class 4: Spatial / Translucent Depth (The Volumetric Canvas)
*Target: Spatial tools, modern media, audio platforms, multi-layered dashboards, next-gen mobile apps.*

- **Visual-to-Text Ratio**: 80% layered depth, materials & visual state / 20% text.
- **Reference Archetypes**: Apple visionOS, iOS 18 Control Center, macOS Sequoia, Arc Browser.
- **Surface & Color**:
  - Primary Surfaces: Layered translucent glass (`backdrop-filter: blur(24px)`), dynamic mesh gradients, subtle specular rim lighting (`inset 0 1px 0 rgba(255,255,255,0.2)`).
  - Backgrounds: Rich deep canvas with atmospheric chromatic lighting.
  - Accents: Vibrancy-boosted chromatic colors with glow falloff.
- **Typography**:
  - Clean, legible Modern Sans (SF Pro, Geist, Plus Jakarta Sans) with optical tracking adjustments.
- **Layout & Density**:
  - Layered z-index planes (Tier 0 canvas $\to$ Tier 1 translucent card $\to$ Tier 2 elevated control).
  - Floating pill controls, continuous lighting reflection across container boundaries.
- **Material & Motion**:
  - Fluid matched-geometry transformations, volumetric depth tilt, interactive specular highlights.
- **Forbidden**: Heavy opaque solid borders, flat dull grays, harsh aliased corners.

---

### Class 5: Industrial Monolith (The Utilitarian Instrument)
*Target: Hardware controllers, developer CLIs, security/telemetry consoles, cybernetic instruments.*

- **Visual-to-Text Ratio**: 85% visual telemetry, status lights & schematics / 15% text.
- **Reference Archetypes**: Teenage Engineering OP-1 / TP-7, Cyberpunk HUD, Vercel CLI, NASA Apollo telemetry.
- **Surface & Color**:
  - Primary Surfaces: Pure obsidian / anodized matte black (`#050505`, `#121212`) or industrial concrete gray (`#E5E5E5`).
  - Borders: Rigid sharp 0–2pt corners, exposed structural grid lines.
  - Accents: High-visibility instrument indicators (Hazard Amber `#FFB000`, Signal Orange `#FF5500`, CRT Green `#00FF66`).
- **Typography**:
  - Primary: Technical Monospace (Dank Mono, Space Mono, IBM Plex Mono) or Industrial DIN.
- **Layout & Density**:
  - Segmented display panels, LED-style dot matrix indicators, visual schematics, live waveform telemetry.
- **Material & Motion**:
  - Immediate, detented mechanical clicks, instant zero-latency transitions, detented knob/slider drag physics.
- **Forbidden**: Soft rounded cards, pastel gradients, decorative lifestyle photography, prose explanations.

---

### Class 6: Sensory Luxury (The High-End Atelier)
*Target: High-end luxury products, bespoke concierge, premium financial services, private membership.*

- **Visual-to-Text Ratio**: 70% visual poise, material finish & micro-motion / 30% text.
- **Reference Archetypes**: Leica, Bang & Olufsen, Apple Watch Hermès, Aman Resorts.
- **Surface & Color**:
  - Primary Surfaces: Deep Midnight (`#0A0A0C`), Brushed Titanium, or Rich Espresso (`#1A1715`).
  - Borders: Whispered 0.5px hairline borders with subtle champagne or platinum sheen.
  - Accents: Champagne Gold (`#D4AF37`), Muted Bronze, or Deep Ruby.
- **Typography**:
  - Elegant Modern Display Serif (Canela, Ogg, Cormorant Garamond) paired with whisper-quiet Geometric Sans.
- **Layout & Density**:
  - Spacious, majestic composition; quiet visual breathing room; deliberate focal pacing.
- **Material & Motion**:
  - Ultra-smooth, perfectly damped physical motion (400–600ms elegant easing).
  - Micro-haptics (rigid/soft impact detents) on primary actions.
- **Forbidden**: Flashy aggressive popups, badge clutter, cheap bright gradients, marketing hype copy.

---

## Design Class Selection Matrix

| Product Domain | Primary Recommended Class | Alternative Class |
|---|---|---|
| Developer Tool / Code / Analytics | **Class 1 (Instrumental Precision)** | **Class 5 (Industrial Monolith)** |
| Knowledge / Notes / Personal Utility | **Class 2 (Tactile Humanist)** | **Class 1 (Instrumental Precision)** |
| Publishing / Portfolio / Editorial | **Class 3 (High-Contrast Editorial)** | **Class 6 (Sensory Luxury)** |
| Media / Music / Next-Gen Consumer App | **Class 4 (Spatial Depth)** | **Class 2 (Tactile Humanist)** |
| Hardware Companion / Security Telemetry | **Class 5 (Industrial Monolith)** | **Class 1 (Instrumental Precision)** |
| Luxury Lifestyle / High-End Finance | **Class 6 (Sensory Luxury)** | **Class 3 (High-Contrast Editorial)** |
