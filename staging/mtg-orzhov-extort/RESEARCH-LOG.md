# Research Log

## 2026-10-18 — Phase 0–2: tooling, identity, v1 skeleton

**Tooling.** Direct HTTPS to `api.scryfall.com` works from the sandbox (search, named, and collection endpoints). `json.edhrec.com` returns 403. WebSearch works as the fallback; a query for Sorin extort lists returned Commander's Herald, Archidekt, and EDHREC average-deck pages.

**Commander pool.** Scryfall query `is:commander (keyword:extort OR o:extort)` returns only Sorin of House Markov and The Kingpin of Crime. Vito and Karlov were also considered as lifegain/drain leads. The user chose Sorin.

**Extort pool.** `(keyword:extort OR o:extort) id<=wb legal:commander` returns 18 cards. All 14 real extort cards except Basilica Guards and Syndicate Enforcer are in the deck. Temporal Extortion only matched on its name.

**Build.** The 99 was filled to the SOP §3 targets, and `tools/build.py` verified legality, color identity, and Game Changer flags. The first draft had 4 Game Changers, so Bolas's Citadel was cut. Lands came in at 36, so Esper Sentinel was cut for a Swamp.

### Self-eval — Phase 2 skeleton, 2026-10-18
- Question:       Build a legal, on-plan Bracket 3 Sorin extort 99.
- Answer/Decision: v1 locked. 100 cards, 0 legality problems, 3 Game Changers. Every category is at or over target except lands (37, one under; reason in CLAUDE.md).
- Verification:   Scryfall `/cards/collection` for all 88 unique cards (oracle-cache.md); WebSearch fallback proven.
- Checklist:      §1 ✅  §2 ✅  §3 ✅. Unplaytested; Phase 3 is next.
