---
name: opinionated-mobile-ads
description: >-
  Opinionated mobile ad architecture and monetization strategy for iOS, Android, Flutter, and React Native.
  Use when designing, auditing, or implementing mobile ad placements, cold start parallel init, UMP/ATT consent handling,
  paywall cross button ad guards, counter-based navigation interstitials, high-probability intent preloading,
  background/foreground App Open ads, premium ad suppression, or ad freshness validation.
---

# Opinionated Mobile Ads Architecture & Funnel Strategy

## Overview

This skill provides an opinionated blueprint for integrating, preloading, and displaying mobile advertisements (AdMob, AppLovin MAX, Unity Ads, Meta) across iOS (Swift), Android (Kotlin), Flutter, and React Native. It eliminates ad management anti-patterns by enforcing deterministic funnel-tied preloading, strict paywall cross-button guards, parallel cold-start consent flows, and automatic premium ad suppression.

---

## Prerequisites & Trigger Conditions

Activate this skill when:
- Designing or implementing ad monetization strategies in mobile applications.
- Configuring cold-start initialization, Google UMP consent, or iOS AppTrackingTransparency (ATT) prompts.
- Building paywall screens with close/cross-button ad requirements.
- Setting up navigation/tab-bar counter-based interstitial ads.
- Preloading ads based on high-probability user intent or app lifecycle state (background/foreground).
- Auditing existing code to prevent serving ads to Premium users or presenting expired ads.

---

## Step-by-Step Operational Workflow

### Phase 1: Context & Discovery
1. Identify the target platform (iOS native, Android native, Flutter, or React Native) and ad network SDKs (AdMob, AppLovin MAX, Unity).
2. Check existing user state and entitlements to verify whether Premium status is active (`isPremium == true`).
3. Locate the current screen lifecycle context (Cold Start, Onboarding, Paywall, Tab Navigation, Action Popup, or Feature Screen).

### Phase 2: Core Execution & Implementation

#### 1. Cold Start & Parallel Init Strategy
- Initialize Ads SDK, UMP Consent SDK, and Firebase in parallel at launch.
- Trigger ATT authorization prompt on iOS in parallel without blocking SDK init.
- Preload the Cold Start ad (App Open or Interstitial) immediately.
- Once init/consent finishes, display the preloaded ad if ready, then route to onboarding/main.
- On returning launches, use cached UMP consent to present the cold start ad immediately upon load.
- *Detailed Reference*: [Cold Start & Consent Workflow](./references/cold-start-and-consent.md)

#### 2. Paywall Cross-Button Guard Protocol
- Upon paywall view mounting:
  - If user is Premium, show cross button instantly without ad loading.
  - If user is Free, hide and disable the cross button, then start preloading 1 interstitial cross-ad scoped to the paywall instance.
- When ad load resolves (success OR failure), reveal and enable the cross button.
- If user purchases subscription while on paywall, reveal cross button instantly and suppress ad display.
- *Detailed Reference*: [Paywall Cross Guard Specifications](./references/paywall-cross-guard.md)

#### 3. Navigation Counter-Based Ads
- Increment navigation click counter on tab/screen switches.
- **Exclusion**: Never increment counter or trigger ads when navigating *into* a Paywall/IAP screen.
- Initiate first ad preload on the user's first navigation click.
- Display interstitial when counter reaches threshold (e.g., 3 or 4 clicks), reset counter, and immediately preload the next navigation ad upon dismissal.
- *Detailed Reference*: [Navigation & App Open Ads](./references/navigation-and-app-open-ads.md)

#### 4. High-Probability Intent Preloading & Freshness
- Do **not** automatically preload ads post-dismissal for standard feature/rewarded ads.
- Preload ads upon view mount for high-probability intent steps (e.g., "Watch Ad vs Buy" popups or ad-gated feature screens).
- Prior to calling `show()`, validate ad freshness/expiration (`!ad.isExpired`). Discard expired ads without presenting them.
- *Detailed Reference*: [Funnel Preloading & Intent Rules](./references/funnel-preloading-rules.md)

#### 5. App Lifecycle (Background <-> Foreground) App Open Ads
- Preload App Open ad during app backgrounding (`onBackground`).
- Present App Open ad during app foregrounding (`onForeground`) after verifying ad freshness and non-premium status.

### Phase 3: Verification & Quality Assurance

1. **Premium Enforcement Gate**: Verify that `isPremium` checks precede both `load()` and `show()` calls.
2. **Paywall State Gate**: Confirm cross button visibility is bound to ad promise completion (success or failure) and purchase events.
3. **Paywall Navigation Shield**: Ensure tab navigation counter ignores route transitions targeting Paywall/IAP views.
4. **Ad Freshness Gate**: Verify that expiration timestamps are validated before `show()` invocations.

---

## Failure Modes & Recovery

| Failure Scenario | Root Cause | Recovery Operational Action |
| :--- | :--- | :--- |
| Cross button stuck in hidden state | Ad load callback timed out or errored without updating UI | Force reveal cross button on load failure/timeout fallback handler. Never trap user on paywall. |
| Navigation ad shown on Paywall screen | Route listener failed to filter destination route | Inject explicit route guard (`destination != Route.Paywall`) before counter evaluation. |
| Zero revenue on ad presentation | Expired ad displayed from long-cached instance | Validate `!ad.isExpired` timestamp before `show()`. If expired, discard silently. |
| Premium user seeing ads | Missing entitlement check before `show()` | Wrap all ad invocation entrypoints with central `AdManager.shouldShowAds()` guard. |
