---
name: mobile-ads-monetization
description: >-
  Opinionated monetization architecture and ad orchestration strategy. Use when designing,
  auditing, or implementing deterministic ad placements, presentation concurrency leasing,
  full-coverage paywall close guards with hardware back interception, interval-based navigation triggers,
  exit screen flows, primed memory resume lifecycles, high-probability intent preloading,
  callback delegate contracts, mandatory lifecycle reporting artifacts, ad freshness validation,
  and layout-stable native and banner view leasing with zero cumulative layout shift.
---

# Mobile Ads Monetization & View Orchestration Architecture

## Overview

This skill provides an opinionated blueprint for integrating, preloading, managing, and rendering full-screen, inline banner, and native advertisements. It eliminates ad management anti-patterns by enforcing deterministic funnel-tied preloading, centralized presentation concurrency leasing, full-coverage paywall close guards, primed in-memory resume lifecycles, dynamic interval action triggers, exit screen flows, strict callback/delegate preloading constraints, layout-stable view leasing, and mandatory post-implementation reporting artifacts with extensible verification checklists.

---

## Prerequisites & Trigger Conditions

Activate this skill when:
- Designing or implementing ad monetization strategies and placement orchestration.
- Building paywall screens with close/cross button and hardware back navigation ad guards.
- Setting up interval-based navigation, tab bar, mode switch, or app exit interstitial triggers.
- Managing in-memory primed resume ad lifecycles across application foreground/background state transitions.
- Preloading ads based on high-probability user intent popups or feature screen lifecycles.
- Managing ad callback/delegate lifecycles (`onLoaded`, `onFailed`, `onDisplayed`, `onDismissed`).
- Integrating inline banner and native ads with exclusive view leasing and zero cumulative layout shift.
- Generating post-implementation lifecycle specification artifacts and developer checklists.
- Auditing ad presentation to prevent collisions, stale asset display, or serving ads to paid/entitled users.

---

## Step-by-Step Operational Workflow

### Phase 1: Placement Catalog & State Discovery

1. **Catalog Definition**: Define placement identifiers, ad formats (full-screen, resume, banner, native), enabled flags, and per-placement trigger intervals in a centralized registry.
2. **Entitlement & Eligibility Gate**: Check active user subscription, entitlements, and ad-free statuses prior to initiating any load or presentation operation.
3. **Presentation Lease Registry**: Register with the centralized presentation lease coordinator to guarantee single-presentation mutual exclusion.

---

### Phase 2: Core Execution & Placement Patterns

#### 1. Callback & Delegate Handling Rules (Strict Preload Constraints)
- **Callback / Delegate Lifecycle**: Handle the standard lifecycle events:
  - `onLoaded`: Marks placement slot as ready and captures creation timestamp.
  - `onFailedToLoad`: Transitions slot to failed state, enables UI fallback/collapse, and clears active operation promises.
  - `onDisplayed`: Acquires presentation lease and displays transition overlays.
  - `onFailedToDisplay`: Releases presentation lease, dismisses transition overlays, and allows uninterrupted user flow.
  - `onDismissed`: Releases presentation lease, resets action counters, and triggers user navigation or screen completion.
- **Strict Post-Dismissal Preload Rule**:
  - **Default Rule**: Do **NOT** initiate an ad preload inside `onDismissed()` or `onAdClosed()` callbacks.
  - **Human Developer Explicit Opt-In Only**: AI agents must **never** autonomously inject post-dismissal eager preloads. Only the human developer may explicitly opt in when a workflow guarantees an immediate repeat action within the same screen lifecycle (e.g., rapid repeating core loops).
- *Detailed Reference*: [Funnel Preloading & Freshness Rules](./references/funnel-preloading-and-freshness.md)

#### 2. Full-Coverage Paywall Close Guard Protocol
- **Mount State**: Upon mounting a paywall or premium screen:
  - If user is already subscribed/entitled, reveal the close button immediately without initiating an ad request.
  - If user is free/unsubscribed, hide and disable the close button and begin loading one full-screen close ad instance.
- **Hardware & Gesture Back Interception**: Intercept both the on-screen close button and system/hardware back navigation gestures through the unified close guard handler:
  - While loading: Close actions and back navigation are blocked.
  - When loaded: Close actions display the full-screen ad, then complete screen dismissal.
  - When failed: Close actions dismiss the screen immediately without presenting an ad (never trap the user).
- **Purchase & Restore Override**: Any completed purchase or restoration immediately dismisses the view without presenting any close ad.
- *Detailed Reference*: [Paywall Close Guard Specifications](./references/paywall-close-guard.md)

#### 3. Navigation, Interval Triggers & Exit Screen Ads
- **Interval-Based Counting**: Track action counters per placement against configured trigger intervals (e.g., trigger every $N$ eligible events).
- **Sequential Concurrency Queue**: Process action increments through sequential operation queueing to prevent race conditions during rapid taps.
- **Route Hierarchy Exclusions**: Suppress action increments and ad triggers during onboarding, initial profile setup, loading/splash flows, internal shell tab transitions, and navigation into monetization views.
- **Eager Preloading Strategy**:
  - Proactively preload all enabled full-screen placements at startup.
  - While action counts progress toward the trigger threshold, initiate an eager preload if the placement is not ready so that it is guaranteed primed when due.
  - When explicitly configured, reload the placement post-dismissal upon successful ad presentation.
- **Exit Screen Presentation**: When handling back navigation from the root view, query candidate placements for an available ready ad to present before routing to the exit flow.
- *Detailed Reference*: [Navigation & Interval Triggers](./references/navigation-and-interval-triggers.md)

#### 4. Primed Memory Lifecycle (Resume Ads)
- **Startup Priming**: Preload the resume ad at application start to keep an instance primed in memory.
- **Zero Background Loading**: Strictly avoid initiating network ad requests while the application is in the background state.
- **Foreground Presentation**:
  - When returning to the foreground, verify that no other full-screen ad or modal flow holds the presentation lease.
  - Validate ad freshness; if expired, evict the instance and trigger a fresh reload.
  - Display a brief transition overlay (resume splash) to mask visual lag, present the primed ad, dismiss the overlay, and eagerly reload a replacement instance post-dismissal.
  - If unready upon foregrounding, continue into the app without blocking the user and trigger a preload.
- *Detailed Reference*: [Lifecycle & Resume Ads](./references/lifecycle-and-resume-ads.md)

#### 5. High-Probability Intent Preloading & Freshness
- **Intent Buffering**: Preload full-screen or rewarded ads upon mounting high-intent views (e.g., choice popups or ad-gated feature screens) leveraging user decision time as natural loading buffer.
- **Action Loading States**: If user triggers the action before load completion, display a visual button loading indicator until the ad is ready to present.
- **Freshness Validation**: Verify cached asset timestamps against maximum age limits prior to presentation. Expired assets are discarded silently without presentation.
- *Detailed Reference*: [Funnel Preloading & Freshness Rules](./references/funnel-preloading-and-freshness.md)

#### 6. Native & Banner View Leasing & Layout Stabilization
- **Exclusive View Leasing**: Each mounted view ad acquires a single-handle lease tied to its specific placement identifier. Simultaneously mounted views must use distinct placement identifiers.
- **Async Generation Counter**: Use an incrementing generation counter on view reload or unmount to discard out-of-order async completions and release unused leases immediately.
- **Zero-Shift Skeleton Placeholders**: Display dimension-accurate animated skeleton/shimmer placeholders matching layout variants (small, medium, large) to prevent Cumulative Layout Shift (CLS).
- **Graceful Collapse**: If ad loading fails or user gains ad-free entitlement, collapse the container cleanly to zero height without leaving blank boxes or visual artifacts.
- *Detailed Reference*: [Native & Banner View Specifications](./references/native-and-banner-views.md)

#### 7. Presentation Lease & Concurrency Lock
- A central presentation lease coordinator manages a single active presentation lock.
- Any presentation trigger must acquire the lease prior to display and release it upon ad dismissal.
- Concurrent triggers (such as foreground resume firing while a feature interstitial is active) are skipped or deferred.
- Display a brief loading popup or overlay before presenting full-screen ads to eliminate black frames or visual hitching.

---

### Phase 3: Post-Implementation Reporting Artifact

Whenever an agent implements, refactors, or configures ads, it **MUST generate a comprehensive delivery artifact** to clearly communicate the implementation to the developer:

1. **Inventory & Placement Map**: A table of all ad placements, formats, triggers, and eligibility conditions.
2. **Exact Lifecycle Behavior Breakdown**: For each placement, explicit documentation of:
   - When the load/preload operation is initiated.
   - When the ad presentation is triggered.
   - Which transition overlays/loaders are displayed.
   - How callbacks (`onLoaded`, `onFailed`, `onDismissed`) are handled.
3. **Developer Opt-In Audit Log**: Clear identification of any placement where post-dismissal preloading was explicitly requested and enabled.
4. **Extensible Verification Checklist**: A structured checklist of testable assertions (presentation locks, back gesture trapping prevention, zero background calls, zero CLS skeletons, purchase overrides). The checklist must be dynamically updated with any specific requirements or feedback requested by the user.

---

## Phase 4: Verification & Quality Gates

1. **Entitlement Gate**: Confirm entitlement checks precede all ad load requests and presentation attempts.
2. **Presentation Concurrency Gate**: Verify that presentation lease acquisition prevents overlapping full-screen ads.
3. **Paywall Trap Gate**: Confirm that both on-screen close button and system/hardware back navigation resolve gracefully on ad failure or purchase.
4. **Route Filter Gate**: Verify navigation policies exclude onboarding, setup, internal shell tabs, and monetization paths.
5. **Dismissal Preload Gate**: Verify no unauthorized post-dismissal preloads exist without documented developer opt-in.
6. **Layout Shift Gate**: Confirm native and banner containers display matching skeleton placeholders and collapse cleanly on failure.
7. **Lease Release Gate**: Verify view leases are released immediately when view components unmount or reconfigure.

---

## Failure Modes & Recovery Matrix

| Failure Scenario | Root Cause | Recovery Operational Action |
| :--- | :--- | :--- |
| User trapped on paywall screen | Close ad failed or timed out without triggering UI state change | Ensure failure callbacks set state to failed and permit direct dismissal. Never trap the user. |
| Double ad collision on app resume | Resume ad triggered while full-screen interstitial was already active | Acquire central presentation lease lock before presentation; skip resume ad if lease is held. |
| Navigation ad shown on paywall | Destination route was not filtered out of navigation policy | Enforce route exclusion check before incrementing action counters or triggering ads. |
| Unauthorized post-dismissal ad load | Agent added automatic preload in dismissal callback | Remove post-dismissal load; require explicit human developer opt-in before enabling eager reload. |
| Stale/zero revenue ad presented | Ad instance cached past its maximum freshness lifespan | Check timestamp age prior to presentation. Evict expired ads silently and request fresh instance. |
| Memory leak or orphan ad view handle | View unmounted while ad load was in flight | Use generation counters and invoke lease release / placement disposal in unmount lifecycles. |
| Cumulative Layout Shift (CLS) | Ad container changes size abruptly upon ad load completion | Maintain fixed/variant placeholder dimensions with matching skeletons; collapse smoothly on failure. |
