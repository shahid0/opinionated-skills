# Navigation, Interval Triggers & Exit Screen Ads

## Action Counting & Interval Trigger Workflow

```
[Eligible User Action / Navigation Event]
                   │
                   ├───► Is Route in Exclusion List? ──► Suppress Action Count & Ad Presentation
                   │
                   └───► Valid Eligible Action
                             │
                             ├───► Enqueue Sequential Operation Tail (Prevent Race Conditions)
                             │
                             ├───► Increment Placement Action Counter (count = count + 1)
                             │
                             ├───► Is Due? (count >= triggerInterval)
                             │       │
                             │       ├──► NO:
                             │       │      └──► Is Ad Ready in Memory?
                             │       │             ├──► Yes ──► Proceed with User Action
                             │       │             └──► No  ──► Trigger Eager Preload (Action Buffer)
                             │       │
                             │       └──► YES:
                             │              └──► Is Ad Ready & Presentation Lease Free?
                             │                     ├──► Yes ──► Show Full-Screen Ad
                             │                     │            ├──► Reset Action Counter to 0
                             │                     │            └──► Eagerly Reload Next Ad Post-Dismissal
                             │                     └──► No  ──► Trigger Preload & Continue User Action
```

---

## Technical Contract Rules

### 1. Per-Placement Interval Configuration
- Define dedicated trigger intervals per placement identifier (e.g., bottom navigation switch interval = 3, mode switch interval = 2, feature completion interval = 1).
- Actions are tracked independently per placement identifier.

### 2. Sequential Concurrency Control
- Wrap all action increments and trigger checks in sequential operation queue tails.
- Multiple rapid user taps are serialized so counter increments and presentation eligibility evaluations cannot suffer from race conditions or duplicate shows.

### 3. Route & Context Exclusion Policy
- Suppress counter increments and ad presentation when:
  - Navigating into onboarding or welcome flows.
  - Navigating into initial profile setup or authentication views.
  - Navigating into loading or splash flows.
  - Switching between sub-tabs within the same shell container (reserving navigation interstitials for major route transitions).
  - Navigating into any monetization, paywall, or subscription view.

### 4. Eager Preloading & Post-Show Reload Strategy
- **Startup Eager Preload**: Preload all enabled interstitial placements during application startup.
- **Action Buffer Preload**: When an action occurs and `count < interval`, if the placement slot is not currently ready, initiate an eager preload so it is primed well before the counter reaches the threshold.
- **Post-Show Immediate Reload**: Immediately after an interstitial is presented and dismissed (`onDismissed`), reset the action counter to zero and initiate a background preload for the next opportunity.

### 5. App Exit Screen Flow
- When a back gesture or exit intent occurs from the root navigation level:
  - Query candidate interstitial placements in priority order for an available ready ad.
  - If a ready ad exists and the presentation lease is available, present it and reset that placement's counter.
  - Upon completion (or if no ad was ready), proceed with navigating to the exit screen or handling application exit.
