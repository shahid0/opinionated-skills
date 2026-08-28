# Implementer Handoff & Orchestration

The Director specifies the vision; implementers build it. This file governs the execution boundary across subagents, CLIs, and prompt platforms.

---

## 1. What the Implementer Receives

Exactly two files per surface:
1. `.uispec/specs/<name>.spec.md` (The Spec Sheet)
2. `.uispec/content/<name>.slots.md` (The Keyed Verbatim Content)

*(Optionally `.uispec/foundations.md` if existing design tokens are referenced).*

The implementer never receives raw source materials, interviews, or `concept.md`. Bounded context guarantees zero hallucinated copy or decorative bloat.

---

## 2. The Implementer Contract (State Verbatim)

```
You are implementing a finished specification produced by Concept UI Director.
Build strictly what the spec sheet prescribes. Do not design, invent, or add decoration.

ABSOLUTE RULES:
1. Verbatim Content: Every string rendered in UI must match .slots.md character-for-character. If a string is missing, report MISSING_SLOT. Never use lorem ipsum or fake mock data.
2. Element Budget: Build only elements listed in Section 5 (Element inventory). Never add unprescribed cards, hero sections, sparkles, or dividers.
3. Visual Telemetry: Build the exact visual telemetry controls (rings, sparklines, gauges) specified in Section 3.
4. Composited Motion Only: Animate ONLY transform, opacity, and clip-path. NEVER animate height, width, margin, padding, or font-size.
5. Settled Geometry Invariant: Settled animated geometry must equal static layout geometry (motion disabled).
6. Single Growth Region: Only the declared growth region may expand across states.
7. Known Gaps: Never fabricate mock data or fake counters for items listed under Known Gaps.

If the spec is ambiguous, halt and report it to the Director.
```

---

## 3. The 3 Execution Channels

### Channel 1: Subagent Invocation (`concept-ui-implementer`)
Invoke the specialized `concept-ui-implementer` subagent:

```json
{
  "Subagents": [{
    "TypeName": "concept-ui-implementer",
    "Role": "UI Implementation Specialist",
    "Prompt": "Implement the UI surface for .uispec/specs/<name>.spec.md using .uispec/content/<name>.slots.md.\nTarget component file: <path/to/component>.\nScope: Presentation layer only. Verify all 15 Pass-1 mechanical assertions."
  }]
}
```

### Channel 2: External CLI Engines (`agy`, Codex, Cursor CLI, Kilocode)
Scope the target path strictly:

```bash
# Example agy CLI execution:
agy -p "Read .uispec/specs/dashboard.spec.md and .uispec/content/dashboard.slots.md. Implement the dashboard component in src/components/Dashboard.tsx. <Insert Implementer Contract>. Scope: only modify src/components/Dashboard.tsx."
```

### Channel 3: Prompt-Only Platforms (Lovable, Bolt, v0, Figma Make)
Emit a **Portable Spec**: inline the slot file directly into a single self-contained prompt block with the prohibitions at the very top.

---

## 4. Pre-Handoff Script Verification

Before passing files to an implementer or committing, run the deterministic validator:

```bash
python3 /Users/macbookpro/.agents/skills/concept-ui-director/scripts/verify_uispec.py \
  --spec .uispec/specs/<name>.spec.md \
  --slots .uispec/content/<name>.slots.md
```

If the validator returns errors, resolve missing slots or token discrepancies before handoff.

---

## 5. Failure Routing Matrix

| Failure Observed | Route To | Action |
|---|---|---|
| **Pass 1 Failure** (Slot mismatch, extra elements, animated height) | **Implementer** | Send assertion number and observed value. Rejection converges quickly. |
| **Pass 2 Failure** (Generic look, 13ms glanceability failure) | **Director** | Refine the concept, visual telemetry, and composition in `.spec.md`. |
| **Missing Slot Reported** | **Director** | Add the missing verbatim key to `.slots.md`. |
| **Spec Ambiguity Reported** | **Director** | Update the spec sheet with resolved values. |
