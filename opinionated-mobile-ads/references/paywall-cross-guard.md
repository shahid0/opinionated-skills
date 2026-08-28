# Paywall Cross Button Guard Specifications

## Paywall Close/Cross Ad Lifecycle

```
[Paywall Screen Mounted]
       │
       ├──► Check Premium / Subscription Status
       │       │
       │       ├───► User is Premium ──────────────► Show Cross Button Instantly (No Ad Request)
       │       │
       │       └───► User is Free ─────────────────► Hide & Disable Cross Button
       │                                                    │
       │                                            Start Preloading 1 Interstitial Ad
       │                                                    │
       │                                    ┌───────────────┴───────────────┐
       │                                    ▼                               ▼
       │                              [Ad Loaded]                     [Ad Failed]
       │                                    │                               │
       │                                    └───────────────┬───────────────┘
       │                                                    │
       │                                           Show Cross Button
       │                                                    │
       ▼                                                    ▼
[User Purchases Subscription]                     [User Taps Cross Button]
       │                                                    │
       ├──► Reveal Cross Button Instantly                   ├──► Show Preloaded Ad
       └──► Suppress Preloaded Ad (Do NOT Show)             └──► Navigate Away
```

---

## Technical Contract Rules

### 1. State Binding
- **Initial Mount State**: `isCrossButtonVisible = false`, `isCrossButtonEnabled = false`.
- **Preload Scope**: Preload **exactly one** Interstitial ad scoped exclusively to this paywall instance.
- **On Ad Load Success**: Set `isCrossButtonVisible = true`, `isCrossButtonEnabled = true`.
- **On Ad Load Failure**: Set `isCrossButtonVisible = true`, `isCrossButtonEnabled = true` (user must never be trapped on a paywall if an ad fails to load).

### 2. Purchase & Premium Overrides
- **In-Flight Purchase**: If the user completes a purchase while on the paywall screen:
  - Immediately set `isCrossButtonVisible = true` and `isCrossButtonEnabled = true`.
  - Discard/ignore the preloaded ad callback. **Never** show an ad to a user who just purchased.
- **Pre-existing Premium User**:
  - Skip ad preload entirely.
  - Set `isCrossButtonVisible = true` instantly on view mount.
