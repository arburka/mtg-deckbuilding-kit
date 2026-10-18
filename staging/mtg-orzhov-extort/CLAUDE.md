# Orzhov Extort — Sorin of House Markov

## Identity
**Commander:** Sorin of House Markov // Sorin, Ravenous Neonate {1}{B}
**Colors:** White / Black (Orzhov)
**Plan:** Cast a steady stream of cheap spells with a critical mass of extort permanents out, turning every spell into a table-wide drain, while lifegain-to-drain payoffs multiply each trigger until a finisher closes the game.
**Primary engine:** Extort (Sorin from the command zone + 14 other extort cards), multiplied by "whenever you gain life, opponents lose life" payoffs (Sanguine Bond, Vito, Marauding Blight-Priest, Cliffhaven Vampire).
**Secondary axis:** Lifegain. Every extort payment gains life equal to the total drained (3 in a 4-player pod), which flips Sorin (3+ life in a turn) and feeds Archangel of Thune, Well of Lost Dreams, and the drain payoffs. It free-rides on extort triggers with no separate setup.

## Constraints
- **Bracket:** 3 (Upgraded). Max 3 Game Changers. Current: Demonic Tutor, Smothering Tithe, Teferi's Protection.
- **Budget:** No cap.
- **Two-card combos:** allowed only as late-game finishers (5+ mana). The Exquisite Blood loops (with Sanguine Bond, Vito, Blight-Priest, or Cliffhaven Vampire) are the deck's combos. See `interactions.md`. If the pod objects, cut Exquisite Blood first.

## Key Rules
- Never reason about card text from memory. Check `oracle-cache.md` first, then Scryfall.
- Follow the lifecycle in `DECKBUILDING-SOP.md`.
- `deck.tsv` is the source of truth for the list. After any change, run `python3 tools/build.py` to regenerate `oracle-cache.md` and `moxfield.txt` and print category counts, then sync `decklist.md`.
- Extort costs mana per spell. Ramp and cheap spells are what make the engine go, so protect the 1–3 MV density when making cuts.

## Environment & Tooling
- **Card data (verified 2026-10-18):** direct HTTPS to `api.scryfall.com` works from the cloud sandbox (curl / urllib), so `tools/build.py` hits the Scryfall collection endpoint directly. No Scryfall MCP is needed.
- **Fallback (verified 2026-10-18):** WebSearch works.
- **Blocked:** `json.edhrec.com` returns 403. Use WebSearch for EDHREC and Moxfield research.
- **Cloud routines:** read `oracle-cache.md` first, and use the network only for cards not in the cache.

## Project Stages
1. [x] Phase 0 — Tooling verified (2026-10-18)
2. [x] Phase 1 — Identity fixed (2026-10-18)
3. [x] Phase 2 — Skeleton built (99 cards, v1, 2026-10-18)
4. [ ] Phase 3 — First goldfish + pod test
5. [ ] Phase 4 — Iteration (ongoing)
6. [ ] Phase 5 — Maintain

## Key Decisions
- **2026-10-18 — Commander: Sorin of House Markov** over The Kingpin of Crime, Vito, and Karlov. Sorin is the only 2-mana extort commander, and he flips into a planeswalker whose −1 converts the turn's lifegain into removal or reach (SOP §2: the commander is an engine piece).
- **2026-10-18 — Bolas's Citadel cut** to stay at 3 Game Changers. Kept Demonic Tutor (finds a finisher), Smothering Tithe (ramp), and Teferi's Protection (wipe and combo protection).
- **2026-10-18 — Esper Sentinel cut for a 9th Swamp** (36 → 37 lands). The SOP floor is 38. 37 lands plus 9 mana rocks and a 3.06 average MV justifies being one under.
- **2026-10-18 — Basilica Guards and Syndicate Enforcer left out.** They are the weakest extort bodies (defender, or a 4-mana vanilla 3/2). They sit first on the extort bench in `CANDIDATES.md`.

## Active Routine Registry
| Test | Status | Days Run | Last Finding | Next Action |
|---|---|---|---|---|
| Test 0 — Cache Refresh | queued | 0 | — | Run after any version bump |
| Opening Hands | queued | 0 | — | First goldfish session |
| Engine | queued | 0 | — | Measure extort triggers/turn on T3–T6 |
| Interaction | queued | 0 | — | Post-wipe rebuild; can we answer a T4 threat |
| Late Game | queued | 0 | — | Which finisher actually ends games |
