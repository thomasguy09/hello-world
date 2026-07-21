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

There is no artificial cost, cooldown, or resource gate on switching between modes — the player can fully possess a unit or pull back to god-mode management freely. Instead, three organic pressures create a "dive and recover" rhythm and keep God Mode meaningful even for players who mostly want to stay possessed:

- **Physical fatigue.** Possession Mode already demands sustained real exertion (arm-shuffle movement, cardio-gated casting, real dodging). As in-game stamina depletes from that exertion, the possessed unit's dodge speed and cast power degrade, eventually forcing a retreat to God Mode to recover.
- **Tunnel vision.** While possessed, the player only sees/hears what that unit senses — no minimap, no awareness of the rest of the board. Threats to other units, the base, or valuables can only be spotted from God Mode.
- **Passive AI.** Unpossessed units defend themselves and hold formation but never proactively expand, reposition, or seize opportunities — a steady tax on staying possessed too long against an actively-directed opponent.

This is deliberately soft — casual players who mostly want to stay in first person as one character are expected and supported (see Character Progression & Economy below); the pressures above matter most for players trying to run a broader strategic game.

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
- **Permanent loss on death:** when a player's possessed character dies in PvP, that character (and whatever it has equipped) is gone for good; the victor takes its loot. Death carries real, permanent stakes.
- **Guaranteed fallback:** every player always has one free replacement character available, so permanent loss never fully locks a player out of the game.

This is closer to a survival/looter sandbox (e.g., DayZ-style stakes) layered on top of RTS-style army command and VR embodiment, rather than a traditional round-based RTS or MOBA.

## Character Progression & Economy

A key design goal: characters themselves become valuable, tradeable commodities — this is expected to be the primary hook for casual players, who will mostly play in Possession Mode as one character rather than commanding armies.

**What makes a character valuable** (all of the below stack together):
- **Stats/level growth** — time invested playing as a character raises its combat capability, like an RPG avatar.
- **Gear/equipment** — items found, crafted, or looted, including very rare and powerful pieces. A single character may carry many rare items simultaneously.
- **Rarity/traits** — inherent, less-common attributes tied to how a character was generated or recruited.
- **Reputation/history** — kill count, notable wins, and a visible track record attached to the specific character.

**The core risk decision: equip vs. stash.** Because character death is permanent and full-loot, owning a rare/powerful item does not mean a player will want to actually equip it. A character walking around in first person is only as valuable (and as risky to lose) as what it currently has equipped. This creates a meaningful pre-fight decision every session: gear up for power at real risk of permanent loss, or stash valuables and go out light. This implies a need for some form of stash/bank storage that is not lost when a character dies (see open questions).

**Trading:** players can transfer characters and items to each other both directly (in-world, player-to-player) and through a persistent market/auction hub, supporting both opportunistic field trades and broader commerce.

## RTS Economy & Crafting

The commander/base layer and the character item economy are deliberately bridged rather than kept separate, so the two dominant playstyles (macro commanders and first-person adventurers) need each other:

- **Shared resource pool.** Gold/lumber-style base resources fund *both* unit training and gear crafting/refinement from the same pool. A commander choosing to invest in crafting is a commander not spending on army size — a real strategic tradeoff each session, not two parallel currencies.
- **Origin of rarity stays in the world.** Rare items and traits are never conjured purely from base resources — they still only come from combat, exploration, and drops — so scarcity established in Character Progression & Economy holds. Base resources are spent to repair, upgrade, socket, or combine gear that was already found, not to manufacture best-in-slot items from scratch. This is what makes adventurers (bringing in raw finds) and commanders (able to refine them) mutually dependent.
- **Base zoning: safe and unsafe areas.** A base is not uniformly safe or uniformly raidable — some core area is protected, while outposts, expansions, and exposed stockpiles are fully raidable and lootable. This extends full-loot PvP stakes into the strategic layer without exposing commanders to total, instant wipeout.
- **Crafting supports both active and passive play:**
  - **Active/physical crafting** — a hands-on VR minigame or gesture-driven process, keeping the physicality pillar present even in the economic layer, likely rewarded with better speed/quality/yield than passive crafting.
  - **Passive/queued crafting** — classic RTS-style production queues that run automatically once resources are committed, for when the player isn't actively at the base.
  - **Macros** — once a player has manually performed a crafting action, they can record/automate it, converting demonstrated skill/mastery into repeatable automation over time rather than requiring the physical minigame forever.

## Setting

- **Fantasy.** Chosen partly for design reasons beyond aesthetics: a fantasy setting was judged to make ability/spell-based mechanics more forgiving and flexible for a choice-driven game, while still supporting physically active combat (melee, casting, dodging).

## Open Questions / Not Yet Decided

These came up during discovery and are worth resolving before/during prototyping:

- How many units can a player command/own at once, and how are they acquired (spawned, built, recruited)?
- What is the comfort/safety plan for sustained physical exertion in VR (session length limits, warnings, seated fallback)?
- World size/persistence: is progress/loot permanent across sessions? How do players (re)join an open world?
- What happens to a possessed unit's AI behavior in the moments right after the player drops out of it?
- Onboarding: this combines two genres (RTS + embodied VR combat) that are unfamiliar together — how is this taught to a new player?
- Griefing/spawn-camping mitigation given full-loot, no-rules PvP.
- Is there death-safe storage (a bank/stash) for un-equipped valuables, and can it also be raided/stolen, or is it fully safe?
- What does the guaranteed free replacement character start with — bare, or some baseline gear/stats?
- Is a character's reputation/history portable when traded/sold, or does it reset/attach to the new owner?
- How are rarity/traits generated for a new character — procedural generation, drop tables, crafting, or a mix?
- What exactly defines a base's safe vs. unsafe zones — fixed geography, an upgrade path players invest in, defenses/guards, or some combination?
- Can safe zones ever be worn down over time (e.g., a siege mechanic), or are they permanently protected regardless of assault?
- Does macro-automated crafting yield less than manual/active crafting (a real tradeoff), or is it purely a time-convenience with no quality cost?

## Suggested Next Steps

1. Prototype the two core interaction loops in isolation first:
   - God Mode gesture-based unit selection/command on a tabletop.
   - Possession Mode physical locomotion (arm-shuffle) and one physically-driven combat action.
2. Playtest physical exertion mechanics early — Quest hardware and comfort constraints will shape what's actually viable before investing in broader systems.
3. Answer the open questions above enough to define a minimal vertical slice (e.g., 2 players, 1 small map, a handful of unit types, one loot rule).
