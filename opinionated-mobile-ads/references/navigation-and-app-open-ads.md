# Navigation & App Open Ad Lifecycles

## Counter-Based Navigation Ads

```
[Tab / Screen Navigation Click]
              │
              ├───► Destination is Paywall / IAP Screen ──► Suppress Counter & Ad Display
              │
              └───► Normal App Navigation
                        │
                        ├───► Increment Click Counter (e.g., count++)
                        │
                        └───► Is First Click?
                                │
                                ├───► Yes ──► Start Preloading Navigation Interstitial Ad
                                │
                                └───► Check Counter (e.g., count >= 3 or 4)
                                        │
                                        └───► Threshold Met ──► Show Preloaded Interstitial Ad
                                                                      │
                                                                 Reset Counter & Preload Next Ad
```

---

## App Open Ads (Background <-> Foreground)

```
[App Enters Background]
       │
       └──► Trigger Lifecycle Observer `onBackground()`
               │
               └───► Start Preloading App Open Ad in Background
                       │
                       ▼
[App Returns to Foreground]
       │
       └──► Trigger Lifecycle Observer `onForeground()`
               │
               ├───► Verify Ad Freshness (Not Expired) & User Not Premium
               │
               └───► Show App Open Ad
```

---

## Key Implementation Rules

### 1. Navigation Counter Rules
- **Initial Load Call**: Start preloading the navigation ad on the user's **first click** in navigation.
- **Paywall Protection**: Navigation counter logic must explicitly check the destination route. If navigating *into* a Paywall/IAP view, **do not increment counter and do not show an ad**.
- **Auto-Reload Contract**: Immediately after a navigation interstitial ad is dismissed (`onAdDismissed`), preload the next navigation ad.

### 2. App Open Foreground Lifecycle Rules
- Preload App Open ad during app backgrounding (`onBackground`).
- Present App Open ad during app foregrounding (`onForeground`).
- Skip ad display if user converted to Premium or if the cached ad has expired.
