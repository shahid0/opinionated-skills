# Native & Banner View Ad Specifications

## View Leasing & Layout Stabilization Lifecycle

```
[View Ad Widget Mounted]
           │
           ├──► Increment Generation Token (generation++)
           │
           ├──► Check User Entitlement: Is User Entitled / Ad-Free?
           │       └──► Yes ──► Collapse Container to Zero Height
           │
           ├──► Display Dimension-Accurate Skeleton Shimmer Placeholder
           │
           ├──► Request View Ad for Specific Placement Identifier
           │       │
           │       ▼
           │  [Load Completes]
           │       │
           │       ├──► Has Generation Changed or Widget Unmounted?
           │       │       └──► Yes ──► Release Acquired Lease & Discard
           │       │
           │       ├──► Did Load Fail or Return Ineligible?
           │       │       └──► Collapse Container to Zero Height (No Empty Frames)
           │       │
           │       └──► Did Load Succeed?
           │               │
           │               ├──► Acquire Exclusive View Lease
           │               ├──► Render Ad View Inside Fixed Bounds
           │               └──► Remove Skeleton Placeholder Seamlessly
           │
[View Ad Widget Unmounts / Reconfigures]
           │
           ├──► Increment Generation Token
           └──► Release View Lease & Dispose Placement Slot
```

---

## Technical & Layout Contract Rules

### 1. View Lease Ownership Model
- Every mounted banner or native view component must acquire an exclusive view lease tied to a distinct placement identifier.
- Simultaneously mounted views must never share placement identifiers; independent leases ensure clear ownership and prevent memory leaks or handle collisions.

### 2. Generation Counter Concurrency Guard
- Maintain an internal monotonically increasing generation token.
- Increment the token on view initialization, reconfiguration, and unmount.
- When an asynchronous load resolves:
  - If the active token no longer matches the local generation, immediately release the acquired lease and discard the rendering pipeline.
  - This guarantees that rapid screen re-renders or prop changes never attach obsolete ad view handles to the user interface.

### 3. Zero Cumulative Layout Shift (CLS) Skeletons
- Before the view ad loads, the container must reserve the exact target dimensions:
  - **Banner Views**: Fixed standard dimensions or container-matched aspect ratios.
  - **Native Views**: Standard variant dimensions (small, medium, large) matching the exact skeleton layout (icon box, headline line, body lines, and call-to-action button).
- Render an animated shimmer skeleton inside the reserved bounds while loading is in flight to eliminate layout shifting when the content resolves.

### 4. Graceful Collapse Protocol
- If the ad loading operation fails, times out, or reports user ineligibility (such as acquiring a subscription):
  - Transition the container state to cleanly collapse to zero dimensions.
  - Never leave empty blank boxes, gray frames, or broken layout placeholders on the screen.

### 5. Lease Release on Disposal
- In view unmount/disposal lifecycles, immediately release the active view lease and notify the central coordinator to clean up resources.
