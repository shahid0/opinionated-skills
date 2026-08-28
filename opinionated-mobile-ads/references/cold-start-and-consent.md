# Cold Start & Consent (UMP / ATT) Workflow

## Cold Start Architecture

```
[App Cold Launch]
       │
       ├──► Start SDK Init in Parallel (Ads SDK, Firebase, Analytics)
       ├──► Request UMP Consent Info (GDPR / Privacy)
       ├──► Request ATT Authorization (iOS Only)
       └──► Start Preloading Cold Start Ad (App Open or Interstitial)
               │
               ▼
   [Wait for Init + Consent/ATT Resolution]
               │
               ├───► Consent Granted / Refused (Personalized vs Non-Personalized)
               │     *Note: Consent status does NOT block showing ads!*
               │
               ▼
   [Check Preloaded Ad Status]
       ├──► Ad Ready   ──► Show Cold Start Ad Immediately ──► Route to Onboarding/Main
       └──► Ad Failed  ───────────────────────────────────► Route to Onboarding/Main
```

---

## Key Rules

### 1. Parallel SDK & Consent Execution
- Never block SDK initialization behind consent fetch or ATT prompts sequentially. Run UMP consent checks, ATT authorization prompts (on iOS), and SDK initialization tasks in parallel.
- UMP consent determines whether ads served will be **personalized** or **non-personalized** (limited ads). It does **not** stop ads from displaying.

### 2. Cold Start Ad Fast Path
- On initial launch (first-time user), initiate the App Open or Interstitial ad preloading request immediately alongside SDK init.
- Once UMP and ATT dialogs are dismissed by the user, if the cold start ad is ready, display it immediately to complete the cold start funnel.
- On subsequent app launches (returning user), consent status is already cached in local storage. Omit dialog display and present the preloaded cold start ad instantly upon load.

### 3. Premium Bypass
- If the user has an active Premium subscription or local entitilement, bypass all cold start ad loading and presentation instantly.
