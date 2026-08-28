# Funnel Preloading, Delegate Contracts & Freshness Rules

## High-Probability Intent Preloading

```
                    [User Enters High-Intent Step]
            (e.g., Choice Popup Mounted or Feature Screen Mounted)
                                   │
                                   ▼
                    Initiate 1 Ad Preload Request
                                   │
                   ┌───────────────┴───────────────┐
                   ▼                               ▼
       [User Taps Action (Ready)]       [User Taps Action (Loading)]
                   │                               │
                   ▼                               ▼
            Show Ad Instantly          Show Action Loading State
                                                   │
                                                   ▼
                                       Show Ad as Soon as Loaded
```

---

## Technical & Callback Contract Rules

### 1. Callback & Delegate Lifecycle Handling
Handle the standard lifecycle events deterministically:
- `onAdLoaded`: Marks placement slot as ready, captures creation timestamp, and resolves load promises.
- `onAdFailedToLoad`: Transitions slot to failed state, enables UI fallback/collapse, and clears active operation promises.
- `onAdDisplayed`: Acquires presentation lease lock and displays transition overlays.
- `onAdFailedToDisplay`: Releases presentation lease lock, dismisses transition overlays, and allows uninterrupted user flow.
- `onAdDismissed`: Releases presentation lease lock, resets action counters, and triggers user navigation or screen completion.

### 2. Strict Post-Dismissal Preloading Rules
- **Default Prohibition**: Do **NOT** automatically call load/preload operations inside `onAdDismissed()` or `onAdClosed()` callbacks.
- **Human Developer Explicit Opt-In Only**:
  - AI agents are **strictly forbidden** from autonomously adding post-dismissal eager preloads.
  - An eager preload in dismissal callbacks is only permitted when the **human developer explicitly instructs and opts in** for a specific placement (e.g., rapid repeating core loops).
- **Reasoning**: Preloading ads after a funnel completes wastes network bandwidth, memory, and ad freshness if the user navigates away or closes the app.

### 3. High-Probability Choice Popups (e.g., "Watch Ad vs Unlock")
- Preload the full-screen or rewarded ad immediately upon mounting the choice popup.
- The time the user spends reading the options acts as a natural loading buffer.
- If the user selects the ad option while loading is in progress, display a visual button loading indicator until the load completes, then present the ad immediately.
- Do **not** automatically preload a replacement ad upon dismissal; the choice popup lifecycle concludes once dismissed.

### 4. Feature Screen Intent Preloading
- When mounting a feature view where executing the primary action triggers an ad:
  - Initiate ad preloading upon view mounting.
  - If the human developer explicitly opts in for repeating executions, configure the reload cycle accordingly.

### 5. Freshness Validation & Silent Eviction
- All cached ad instances track their creation/load timestamp.
- **Mandatory Verification**: Prior to calling any presentation routine, verify that `currentTime - loadedAt < maximumAge` (e.g., 4 hours).
- **Eviction Protocol**: Discard expired ad instances silently without presenting them to the user. Presenting expired ads yields zero monetization value and degrades user trust.

---

## Mandatory Post-Implementation Reporting Artifact

Whenever ads are implemented, refactored, or configured by an agent, the agent must generate a dedicated delivery artifact (e.g., `ad_lifecycle_spec.md`) documenting:

### 1. Inventory & Placement Table
| Placement Identifier | Format | Trigger Condition / Interval | Eligibility Gate | Post-Dismissal Reload |
| :--- | :--- | :--- | :--- | :--- |
| `[Identifier]` | FullScreen / Native / Banner | `[Interval / Mount / Action]` | `[Entitlement Check]` | `[None / Developer Opt-In]` |

### 2. Exact Placement Lifecycle Behavior
For each configured placement, explicitly detail:
- **Trigger**: When load or preload is initiated.
- **Presentation**: When the ad is displayed to the user.
- **Visual Transition**: Which loading spinner, popup, or resume splash overlay is used.
- **Dismissal Handling**: Exact actions taken upon dismissal (navigation, counter reset, or developer-approved reload).

### 3. Dynamic Verification Checklist
An extensible checklist verifying:
- [ ] Central presentation lease acquired before show and released on dismiss.
- [ ] Paywall close guard blocks close while loading, shows ad on loaded, and bypasses on purchase.
- [ ] System/hardware back navigation is intercepted on paywall screens.
- [ ] No background network requests initiated during app background state.
- [ ] Native/banner views render layout-matched skeleton shimmer placeholders with zero CLS.
- [ ] Post-dismissal preloads only exist where the human developer explicitly opted in.
- [ ] *[User-Specific Additions]*: Custom verification items derived from user feedback to confirm instructions took effect.
