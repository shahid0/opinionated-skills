# Funnel-Tied Preloading & Ad Freshness Rules

## High-Probability Intent Preloading

```
                    [User Enters High-Intent Step]
                    (e.g., Popup Mounted or Feature Screen Mounted)
                                  │
                                  ▼
                    Start Preloading 1 Ad Instance
                                  │
                  ┌───────────────┴───────────────┐
                  ▼                               ▼
       [User Taps Action (Ready)]       [User Taps Action (Loading)]
                  │                               │
                  ▼                               ▼
            Show Ad Instantly            Show Button Loading State
                                                  │
                                                  ▼
                                      Show Ad as Soon as Loaded
```

---

## Key Placement & Lifecycle Rules

### 1. Opt-in Post-Dismissal Preloading
- **Default Rule**: Do **NOT** automatically call `load()` for a new ad inside `onAdDismissed()` or `onAdClosed()` callbacks.
- **Opt-in Exception**: Developer/agent must justify post-dismissal preloading explicitly (e.g., if user is guaranteed to repeat the exact ad-triggering step within the same session).
- **Reasoning**: Preloading ads after a funnel completes wastes system bandwidth, memory, and eCPM freshness if the user navigates away or closes the app.

### 2. High-Probability Popup Intent (e.g., "Watch Ad vs Buy Premium")
- Preload the rewarded / interstitial ad as soon as the choice popup mounts.
- User decision time (reading options) provides natural buffering for ad load completion.
- If user clicks "Watch Ad" while ad is still loading, display a button loading spinner until ad load completes, then call `show()`.
- Do NOT preload a replacement ad upon dismissal; the popup lifecycle is over once acted upon.

### 3. Feature Screen Intent
- Preload ad upon mounting a feature screen where the primary action triggers an ad.
- If the feature supports repeated executions on the same screen, developer may explicitly opt-in to auto-preload the next ad upon dismissal.

### 4. Ad Freshness & Expiration Verification
- SDK preloaded ads expire after a platform/network-specific duration (typically 1 to 4 hours).
- **Mandatory Check**: Prior to calling `show()`, check `ad.isExpired` or verify cached timestamp age.
- **Action on Expiration**: Discard expired ad objects silently without showing them to the user. Showing an expired ad generates zero eCPM revenue while degrading user experience.
