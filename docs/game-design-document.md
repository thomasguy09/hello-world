# Game Design Document (Working Draft)

*Status: Discovery / Concept phase. This document captures the outcome of an initial design discovery session and will evolve as the concept is prototyped.*

## High Concept

An open-world VR PvP sandbox for Meta Quest that fuses real-time strategy commanding (Warcraft III) with embodied first-person play (World of Warcraft). Players swap freely between a god's-eye tabletop view, where they command groups of units, and full possession of a single unit, where they fight in first person using real physical movement. The game is designed to be both mentally and physically demanding.

## Platform & Tech

- **Engine:** Unity
- **Language:** C#
- **Target platform:** Meta Quest (standalone VR)

## Core Concept: Two Modes of Play

### 1. God Mode (Tabletop / Commander View)
- The player stands as a giant over a miniature battlefield, like a tabletop diorama.
- Units and groups are selected and directed using physical motion (reach, point, gesture) rather than menus or a mouse/keyboard-style UI.
- This is the strategic layer: positioning, group orders, resource/army management.

### 2. Possession Mode (First-Person Embodiment)
- The player can fully possess one unit at a time, dropping into first-person control of that character's body.
- While possessed, the rest of the player's forces continue to act on AI.
- Combat, spellcasting, dodging, and movement in this mode are driven by the player's real physical motion (see Physicality below), not abstracted inputs.
- The player can drop out of possession back into God Mode at will.

There is no artificial cost, cooldown, or resource gate on switching between modes — the player can fully possess a unit or pull back to god-mode management freely. The tradeoff is inherent: while possessing one unit, the rest of the army is unattended (AI-driven) until the player returns to God Mode.

## Physicality

Physical exertion is a core mechanic in **both** God Mode and Possession Mode, not just an immersion layer:

- **Movement speed** is driven by real arm-shuffling motion (a run-in-place style input) rather than a thumbstick.
- **Spellcasting / ability use** taps into sustained physical effort (cardio-gated), so casting under real fatigue is part of the challenge.
- **Combat in first person** uses real physical dodging, blocking, and striking rather than button-based combat resolution.
- **God Mode is not purely cerebral** — selecting and directing units also uses physical gesture/motion, so the strategic layer keeps the player physically engaged rather than being a rest period.

The intent is a game that punishes players for being both tactically sloppy and physically unfit, and rewards real cardio conditioning as a competitive advantage.

## Multiplayer Structure: Open-World Sandbox PvP

- **No formal match structure, rounds, or lobbies** — the game world is a persistent open-world sandbox.
- **PvP is unrestricted** ("no rules") — players can engage any other player's forces at any time.
- **Full loot on death:** when a player (or their possessed unit) dies, the victor can take their loot. Death carries real stakes.

This is closer to a survival/looter sandbox (e.g., DayZ-style stakes) layered on top of RTS-style army command and VR embodiment, rather than a traditional round-based RTS or MOBA.

## Setting

- **Fantasy.** Chosen partly for design reasons beyond aesthetics: a fantasy setting was judged to make ability/spell-based mechanics more forgiving and flexible for a choice-driven game, while still supporting physically active combat (melee, casting, dodging).

## Open Questions / Not Yet Decided

These came up during discovery and are worth resolving before/during prototyping:

- How many units can a player command/own at once, and how are they acquired (spawned, built, recruited)?
- What stops a player from just staying in Possession Mode permanently and ignoring the strategic layer, given there's no cost to switching?
- What is the comfort/safety plan for sustained physical exertion in VR (session length limits, warnings, seated fallback)?
- World size/persistence: is progress/loot permanent across sessions? How do players (re)join an open world?
- What happens to a possessed unit's AI behavior in the moments right after the player drops out of it?
- Onboarding: this combines two genres (RTS + embodied VR combat) that are unfamiliar together — how is this taught to a new player?
- Griefing/spawn-camping mitigation given full-loot, no-rules PvP.

## Suggested Next Steps

1. Prototype the two core interaction loops in isolation first:
   - God Mode gesture-based unit selection/command on a tabletop.
   - Possession Mode physical locomotion (arm-shuffle) and one physically-driven combat action.
2. Playtest physical exertion mechanics early — Quest hardware and comfort constraints will shape what's actually viable before investing in broader systems.
3. Answer the open questions above enough to define a minimal vertical slice (e.g., 2 players, 1 small map, a handful of unit types, one loot rule).
