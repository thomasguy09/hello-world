# Handoff notes (cloud session → local session)

Context for whichever session picks this up next on a machine with real access to a Meta Quest.

## Where things stand

- `docs/game-design-document.md` — the full game design from a discovery session: core theme (individual vs. manager), God Mode / Possession Mode, character economy, RTS/item economy, base zoning, onboarding.
- `prototypes/possessions-demo.html` — a self-contained WebGL2 + WebXR tech demo of the core hook (tabletop god-view ↔ possessing a minion at full scale). Written and syntax/render-tested in a headless browser (no runtime errors, shaders compile, both render paths produce correct output), but never tested on real XR hardware.

## The open problem

The demo was published as a Claude.ai Artifact and opened in the Meta Quest Browser, but `navigator.xr.isSessionSupported()` failed immediately. The most likely cause: Claude.ai renders artifact pages inside a sandboxed iframe, and iframes need an explicit `allow="xr-spatial-tracking"` from the parent frame to use WebXR — which a generic content host is unlikely to grant. This was never confirmed with a real console/error message, just inferred from the failure happening before any session was even requested.

**Recommended next step:** stop relying on Claude.ai hosting. Serve `possessions-demo.html` directly from the local machine (e.g. a plain local HTTP server) and open it as a top-level page in the Quest Browser — no iframe, no sandboxing, should behave like any normal WebXR page. If that also fails, the actual browser console output (via `chrome://inspect` USB debugging from a PC with the headset connected) will finally show the real error instead of guessing.

## Also worth considering

Given the friction getting a browser demo onto the headset at all, a native Unity build (per the design doc's intended tech stack: Unity + C#) may be the more direct path going forward — it sidesteps browser/iframe permission issues entirely. The design doc has enough detail (God Mode tabletop view, possession swap, minion roster, physical input needs) to scaffold a first Unity scene and grip/possession script from scratch.
