# Paywall Close Guard Specifications

## Close Guard Lifecycle Architecture

```
[Paywall View Mounted]
       │
       ├──► Check User Entitlement State
       │       │
       │       ├───► Entitled / Paid ────────────────► Show Close Button Instantly (Zero Ad Requests)
       │       │
       │       └───► Free / Unsubscribed ────────────► Hide & Disable Close Button
       │                                                      │
       │                                              Start Loading 1 Close Ad
       │                                                      │
       │                                      ┌───────────────┴───────────────┐
       │                                      ▼                               ▼
       │                                [Ad Loaded]                     [Ad Failed]
       │                                      │                               │
       │                                      └───────────────┬───────────────┘
       │                                                      │
       │                                             Reveal Close Button
       │                                                      │
       ▼                                                      ▼
[User Purchases / Restores]                   [User Taps Close / Back Gesture]
       │                                                      │
       ├──► Dismiss View Instantly                            ├──► Is Ad Loaded?
       └──► Suppress Ad Presentation                          │       ├──► Yes ──► Show Ad ──► Dismiss
                                                              │       └──► No  ─────────────► Dismiss
```

---

## Technical & Interaction Contract Rules

### 1. Unified State & Back Navigation Binding
- **Initial Mount State**: `closeButtonVisible = false`, `closeButtonEnabled = false`, `closeAdState = loading`.
- **Preload Scope**: Load **exactly one** full-screen ad instance scoped exclusively to the active paywall instance.
- **Hardware & Gesture Back Interception**: Intercept both the on-screen close button and system/hardware back navigation gestures through the same handler:
  - While `closeAdState == loading`: Block both the on-screen button and back navigation gestures from dismissing the screen prematurely.
  - While `closeAdState == loaded`: When the user attempts to close (via button tap or back gesture), present the full-screen ad and dismiss the view upon completion.
  - While `closeAdState == failed`: When the user attempts to close, immediately dismiss the view without presenting an ad.

### 2. Purchase & Restoration Overrides
- **In-Flight Purchase**: If the user completes a purchase or restoration transaction while the paywall view is mounted:
  - Immediately dismiss the view or allow unimpeded exit.
  - Discard/ignore any completed or in-flight close ad instances. **Never** show an ad to a user who just purchased or restored entitlements.
- **Pre-existing Entitled User**:
  - Skip ad loading entirely.
  - Set `closeButtonVisible = true` and `closeButtonEnabled = true` immediately on view mount.

### 3. Trapping Prevention
- If the ad loading operation fails, times out, or encounters a network error, transition `closeAdState` to `failed` and enable the close controls immediately.
- The user must never be trapped on a paywall screen due to ad loading delays or failures.
