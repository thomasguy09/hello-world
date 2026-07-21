# Prototypes

## possessions-demo.html

First playable tech demo for *Possessions* — a single-file, dependency-free WebGL2 + WebXR page. No Unity, no build step; open it directly in the Meta Quest Browser.

**What it demonstrates:** the core hook from the design doc — stand over a shrunk-down tabletop battlefield (God Mode), point at a minion and pull the trigger to possess it (camera snaps to that minion's position at true scale), squeeze the grip to release and pop back to the tabletop. Left thumbstick walks around while possessed.

**How to run it on a Quest:**
- Easiest: open the demo's published Artifact link directly in the Meta Quest Browser and tap "Enter VR."
- Locally: serve this file over HTTPS (WebXR requires a secure context) and open that URL in the Quest Browser, e.g. `npx http-server -S -C cert.pem -K key.pem .` or tunnel a local dev server with a tool like `ngrok`.

**Status:** the WebGL rendering (diorama transform, full-scale mode, lighting, geometry) has been verified in a headless browser — it compiles, links, and renders correctly. The WebXR-specific parts (headset session, controller ray-picking, locomotion) could not be tested without real hardware, so the first run on-device is the real test. If something misbehaves, the on-page log panel (bottom of screen) will show what happened even inside the headset.

**Known limits, deliberately kept out of this first pass:** no physical exertion mechanics (arm-shuffle movement, cardio-gated casting), no fatigue/tunnel-vision pressure, no base zoning, no items/economy — this is purely a proof of the God Mode ↔ Possession Mode switch feeling right in VR before investing further.
