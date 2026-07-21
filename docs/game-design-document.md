# Game Design Document (Working Draft)

*Status: Discovery / Concept phase. This document captures the outcome of an initial design discovery session and will evolve as the concept is prototyped.*

## High Concept

An open-world VR PvP sandbox for Meta Quest that fuses real-time strategy commanding (Warcraft III) with embodied first-person play (World of Warcraft). Players swap freely between a god's-eye tabletop view, where they command groups of units, and full possession of a single unit, where they fight in first person using real physical movement. The game is designed to be both mentally and physically demanding.

## Core Theme: The Individual vs. The Manager

The title *Possessions* is meant to carry a double meaning, and it's the thematic spine the rest of the design should be checked against:

- **To possess** — the player's ability to inhabit and become a character.
- **A possession** — what that character is to whoever currently owns/commands it: an asset, tradeable, disposable, valuable or expendable depending on how it's managed.

This maps directly onto the game's two modes. Playing as **the individual** (Possession Mode) is vulnerable, physical, and real — cardio, real dodging, real risk of permanent loss. Playing as **the manager** (God Mode) is safe, detached, and powerful — bird's-eye, gesture-driven, treating bodies as resources on a board. Choosing to stay possessed isn't just mechanically riskier than retreating to God Mode, it's thematically *staying human* instead of stepping back into the god's-eye view where people become line items. Every system below — permanent death, full loot, trading, lending — should reinforce this: characters are always at risk of being reduced from someone's lived-in identity to someone else's managed asset.

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
- **Fog of war exists wherever your minions don't.** Visibility, in either mode, is limited to where your own characters/minions currently are — there's no omniscient map even in God Mode. While possessed, this collapses further to just what that one unit senses, no minimap or awareness of the rest of the board. Threats to unattended minions, the base, or valuables can only be spotted by having eyes (a minion) near them.
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
- **PvP is unrestricted in the wider world** ("no rules") — players can engage any other player's forces at any time outside friendly zones.
- **Permanent loss on death:** when a player's possessed character dies in PvP, that character (and whatever it has equipped) is gone for good; the victor takes its loot. Death carries real, permanent stakes.
- **Guaranteed fallback:** every player always has one free replacement character available, so permanent loss never fully locks a player out of the game.

This is closer to a survival/looter sandbox (e.g., DayZ-style stakes) layered on top of RTS-style army command and VR embodiment, rather than a traditional round-based RTS or MOBA.

### Friendly Zones vs. The Dangerous World

Every player starts the game in first person (Possession Mode) inside a friendly zone — a systemic, world-provided safe area, not something a player builds. Friendly zones are PvP-free and let players trade, do low-stakes crafting, and simply exist without risking permanent loss.

Everything outside friendly zones is the dangerous world: full-loot PvP, raidable player bases, and sieges. This is a deliberate spectrum, not a forced funnel — a risk-averse or casual player can choose to spend most of their time in friendly zones (consistent with most casual players mainly wanting the first-person experience), while risk-tolerant players venture out to build the deeper base/character economy where the real stakes and rewards live.

## Character Progression & Economy

A key design goal: characters themselves become valuable, tradeable commodities — this is expected to be the primary hook for casual players, who will mostly play in Possession Mode as one character rather than commanding armies.

**What makes a character valuable** (all of the below stack together):
- **Stats/level growth** — time invested playing as a character raises its combat capability, like an RPG avatar.
- **Gear/equipment** — items found, crafted, or looted, including very rare and powerful pieces. A single character may carry many rare items simultaneously.
- **Rarity/traits** — inherent, less-common attributes tied to how a character was generated or recruited.
- **Reputation/history** — kill count, notable wins, and a visible track record attached to the specific character.
- **Spell tree / build** — every character has a spell tree, and the choices made progressing it are as much a per-character investment as gear or stats, not a shared/global skill list.

**The core risk decision: equip vs. stash.** Because character death is permanent and full-loot, owning a rare/powerful item does not mean a player will want to actually equip it. A character walking around in first person is only as valuable (and as risky to lose) as what it currently has equipped. This creates a meaningful pre-fight decision every session: gear up for power at real risk of permanent loss, or stash valuables and go out light. This implies a need for some form of stash/bank storage that is not lost when a character dies (see open questions).

**Ownership is a bundle of rights, not just a binary sale.** A manager can transfer different levels of control over a character they own:
- **Full sale** — ownership and control transfer outright, as with any traded item.
- **Lending** — control is temporarily handed to another player (e.g. arming an ally for a raid), while the original owner retains ultimate ownership and can presumably reclaim it.
- **Shared control** — multiple players can have some form of joint access to controlling the same character.

This turns a manager's power into more than army size or gear — it includes deciding who else gets to *be* an individual, and for how long, reinforcing the individual-vs-manager theme.

**Unpossessed characters are predictable by default.** They follow orders reliably; there's no universal morale/loyalty system fighting the manager. However, personality (e.g. loyal, volatile, independent) can itself be a rarity trait on specific characters, making some assets genuinely harder — or more interesting — to manage than others, without complicating the baseline system.

**Trading:** players can transfer characters and items to each other both directly (in-world, player-to-player) and through a persistent market/auction hub, supporting both opportunistic field trades and broader commerce.

## RTS Economy & Crafting

The commander/base layer and the character item economy are deliberately bridged rather than kept separate, so the two dominant playstyles (macro commanders and first-person adventurers) need each other:

- **Shared resource pool.** Gold/lumber-style base resources fund *both* unit training and gear crafting/refinement from the same pool. A commander choosing to invest in crafting is a commander not spending on army size — a real strategic tradeoff each session, not two parallel currencies.
- **Origin of rarity stays in the world.** Rare items and traits are never conjured purely from base resources — they still only come from combat, exploration, and drops — so scarcity established in Character Progression & Economy holds. Base resources are spent to repair, upgrade, socket, or combine gear that was already found, not to manufacture best-in-slot items from scratch. This is what makes adventurers (bringing in raw finds) and commanders (able to refine them) mutually dependent.
- **Base zoning: safe and unsafe areas.** Outside of the systemic friendly zones (see Multiplayer Structure), nothing is automatically or permanently safe — safety is earned, using the same shared resource pool that also funds units and crafting, making defense a third real tradeoff each session. The one exception is a bare-minimum, un-destroyable core per base (just a respawn/binding point, nothing else) — mirroring the guaranteed free replacement character — so a wiped-out base is a severe setback, never a permanent lockout. Everything beyond that core (stockpiles, crafting stations, outposts) is only as safe as what's actually been built to defend it.
- **Sieges support both styles of play.** An attacker can commit in real time to actively break a base's defenses, or set a siege running and leave it grinding passively, mirroring the active/passive split in crafting below. This lets players self-select their risk appetite: some will stay almost entirely within friendly zones, others will venture into the dangerous world and commit to bases, raids, and sieges.
- **Crafting supports both active and passive play:**
  - **Active/physical crafting** — a hands-on VR minigame or gesture-driven process, keeping the physicality pillar present even in the economic layer, likely rewarded with better speed/quality/yield than passive crafting.
  - **Passive/queued crafting** — classic RTS-style production queues that run automatically once resources are committed, for when the player isn't actively at the base.
  - **Macros** — once a player has manually performed a crafting action, they can record/automate it, converting demonstrated skill/mastery into repeatable automation over time rather than requiring the physical minigame forever.

## Onboarding

- **Sandbox-first.** No explicit guided tutorial content for mechanics, strategy, or systems — players discover the game by playing it. Guided help is limited strictly to movement and interface basics (VR locomotion, how to interact with menus/gestures), never to teaching strategy or systems.
- **God Mode is gated by ownership, not by design walls.** A player's God Mode view only shows and commands the minions (characters) they currently own. A brand-new player with no minions has nothing to command yet, so commanding is never something that needs to be force-taught up front — it's discovered organically as a player's roster grows.
- **Minions and characters are the same roster.** The units a player commands in God Mode are the same ownable, tradeable characters covered in Character Progression & Economy — there is no separate abstract "RTS unit" pool distinct from possessable characters.
- **Total loss recovery is anchored at the friendly zone.** If a player loses every minion they own, their only path forward is to return to their spawn point inside the friendly zone and possess a new one there — this is the guaranteed free replacement character in practice.

## Setting

- **Fantasy.** Chosen partly for design reasons beyond aesthetics: a fantasy setting was judged to make ability/spell-based mechanics more forgiving and flexible for a choice-driven game, while still supporting physically active combat (melee, casting, dodging).

## Open Questions / Not Yet Decided

These came up during discovery and are worth resolving before/during prototyping:

- How many minions can a player command/own at once, and how are they acquired beyond the friendly-zone starting one (spawned, recruited, captured)?
- What is the comfort/safety plan for sustained physical exertion in VR (session length limits, warnings, seated fallback)?
- World size/persistence: is progress/loot permanent across sessions? How do players (re)join an open world?
- What happens to a possessed unit's AI behavior in the moments right after the player drops out of it?
- Should a new player get any temporary protection/grace period the first time they leave the friendly zone into full-stakes PvP, or do full rules apply immediately? (Raised but not yet resolved.)
- Griefing/spawn-camping mitigation given full-loot, no-rules PvP.
- Is there death-safe storage (a bank/stash) for un-equipped valuables, and can it also be raided/stolen, or is it fully safe?
- What does the guaranteed free replacement character start with — bare, or some baseline gear/stats?
- Is a character's reputation/history portable when traded/sold, or does it reset/attach to the new owner?
- How are rarity/traits generated for a new character — procedural generation, drop tables, crafting, or a mix?
- Does macro-automated crafting yield less than manual/active crafting (a real tradeoff), or is it purely a time-convenience with no quality cost?
- How does lending/shared control work mechanically — a revocable-at-will toggle, a timed loan, a rental market with fees?
- If control is shared between multiple players, how is conflict resolved (turns, a designated primary, simultaneous input)?
- Does a character's spell tree get fixed at trade/capture, or can a new owner respec it?
- Are personality traits (loyal/volatile/independent) purely flavor-with-behavior, or do they also factor into a character's rarity/value?
- Is a base defense manned by a possessed player (actively fighting off raiders) meaningfully stronger than the same defense left automated/unmanned, or are turrets/walls equally effective either way? (Raised but not yet resolved — relevant to how strongly the individual-vs-manager theme plays out in base defense.)
- Where are friendly zones located relative to player bases — are bases only buildable in the dangerous world, or can they be sited near friendly zones for partial safety-by-proximity?
- What specifically can be built to defend a base (walls, turrets, traps, terrain) and how does their cost scale against raw siege-breaking power?

## Suggested Next Steps

1. Prototype the two core interaction loops in isolation first:
   - God Mode gesture-based unit selection/command on a tabletop.
   - Possession Mode physical locomotion (arm-shuffle) and one physically-driven combat action.
2. Playtest physical exertion mechanics early — Quest hardware and comfort constraints will shape what's actually viable before investing in broader systems.
3. Answer the open questions above enough to define a minimal vertical slice (e.g., 2 players, 1 small map, a handful of unit types, one loot rule).
