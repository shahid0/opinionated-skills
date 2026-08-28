# Private Opinionated Skills

A curated repository of high-conviction, opinionated AI agent skills for mobile ads monetization and expressive UI design direction.

Compatible with the [`skills`](https://skills.sh) CLI ecosystem across AI coding agents (Antigravity, Claude Code, Cursor, Codex, Windsurf, Gemini, Cline, Roo, OpenCode, and Zed).

---

## 📦 Included Skills

### 1. [`mobile-ads-monetization`](./mobile-ads-monetization)
**Opinionated monetization architecture and full ad orchestration.**
- Centralized presentation concurrency leasing (`AdPresenterMutex`).
- Full-coverage paywall close guards with hardware back-button interception.
- Primed in-memory resume lifecycles (5-minute TTL freshness validation).
- Deterministic interval action triggers and exit screen flows.
- Layout-stable native and banner view leasing with zero cumulative layout shift (CLS).
- Mandatory post-implementation reporting artifacts and verification checklists.

### 2. [`opinionated-mobile-ads`](./opinionated-mobile-ads)
**Opinionated mobile ad architecture for iOS, Android, Flutter, and React Native.**
- Deterministic funnel-tied preloading for AdMob, AppLovin MAX, Unity Ads, and Meta.
- Parallel cold-start initialization with Google UMP consent and iOS ATT.
- Paywall cross-button ad guards with automatic premium ad suppression.
- Counter-based navigation interstitial triggers.

### 3. [`concept-ui-director`](./concept-ui-director)
**Creative & Design Director: 'Show, Don't Tell — But Make It Beautiful'.**
- 13ms visual glanceability and 6 distinct UI Design Classes.
- Machine-auditable `.uispec/` specification contracts.
- High-conviction visual design systems, hero moments, and experience arcs.
- Direct execution handoffs to implementation agents and the `agy` CLI without design dilution.

---

## 🚀 Installation via `skills.sh`

Install individual skills using the `skills` CLI:

```bash
# Install a specific skill from this repository
npx skills add <owner>/<repo>/mobile-ads-monetization
npx skills add <owner>/<repo>/opinionated-mobile-ads
npx skills add <owner>/<repo>/concept-ui-director
```

---

## 🛠 Repository Layout

```
.
├── skills.sh.json              # skills.sh catalog & grouping configuration
├── concept-ui-director/        # UI Creative Direction & .uispec specification engine
│   ├── SKILL.md
│   ├── references/
│   └── scripts/
├── mobile-ads-monetization/    # Advanced Ad Orchestration & View Leasing
│   ├── SKILL.md
│   └── references/
└── opinionated-mobile-ads/     # Mobile Ad Architecture & Preloading Rules
    ├── SKILL.md
    └── references/
```
