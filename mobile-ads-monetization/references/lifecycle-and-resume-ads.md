# Lifecycle & Resume Ad Architecture

## In-Memory Primed Resume Lifecycle

```
[Application Startup]
        │
        └──► Preload Resume Ad (Prime in Memory)
                │
                ▼
[App Transitions to Background]
        │
        └──► Record Background State (Strictly ZERO Network Requests)
                │
                ▼
[App Returns to Foreground]
        │
        ├───► Check Presentation Lease: Is Another Full-Screen Ad Active?
        │       └──► Yes ──► Skip Resume Ad Presentation
        │
        ├───► Check Ad Freshness: Has Cached Ad Expired?
        │       └──► Yes ──► Silently Evict & Trigger Fresh Preload
        │
        ├───► Check Readiness: Is Resume Ad Ready?
        │       │
        │       ├──► YES:
        │       │      ├──► Display Resume Transition Overlay (Resume Splash)
        │       │      ├──► Present Resume Ad
        │       │      ├──► Dismiss Resume Transition Overlay
        │       │      └──► Eagerly Preload Next Instance for Future Resumes
        │       │
        │       └──► NO:
        │              └──► Continue Seamlessly & Trigger Background Preload
```

---

## Technical Contract Rules

### 1. In-Memory Priming Model
- Initiate the resume ad load immediately upon application startup.
- Maintain an active ready instance primed in memory ready for rapid presentation when returning from background.

### 2. Zero Background Network Requests
- Do **not** initiate ad load requests when receiving application backgrounding events.
- Background network calls waste device resources and can be terminated by the operating system before completing.

### 3. Foreground Presentation Safeguards
- **Presentation Lease Check**: Before presenting, verify that no other full-screen interstitial, modal reward flow, or initial splash ad holds the presentation lease. If the lease is occupied, skip the resume ad.
- **Freshness Gate**: Verify that the primed instance has not exceeded the maximum age threshold. If expired, discard the instance immediately and trigger a fresh preload.
- **Transition UI Coordination**: Display a dedicated resume transition overlay immediately before presentation to prevent UI hitching or black screen flashes while the ad takes over the screen. Dismiss the overlay upon ad presentation completion.
- **Immediate Re-Priming**: Immediately upon dismissal of the presented resume ad, trigger a preload operation so that subsequent background/foreground cycles are ready.
