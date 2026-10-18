# Pending Routines

## Operating rules (prepend to every routine)
- Do not spawn sub-agents. Do not use Scryfall MCP tools.
- Read `CLAUDE.md`, `decklist.md`, `interactions.md`, and `oracle-cache.md` first. Use the network (Scryfall direct, then WebSearch) only for cards not in the cache or flagged ⚠️.
- Never reason about card text from memory.
- Append findings to `RESEARCH-LOG.md` with a §9 self-eval block. Never overwrite earlier entries.
- Make at most 2 card changes per batch, each with a named session trigger. After any change, edit `deck.tsv`, run `python3 tools/build.py`, and sync `decklist.md` (counts + version history) in the same commit.
- Commit and push to the working branch.

## Queue
| # | Routine | Question | Status |
|---|---|---|---|
| 0 | Cache Refresh | Is `oracle-cache.md` in sync with `deck.tsv`? Re-run `tools/build.py` and spot-check ⚠️ prices. | queued |
| 1 | Opening Hands | Keep rate over 10+ seeded 7-card hands (3+ lands, both colors, a T1–T2 play) | queued |
| 2 | Engine | Extort triggers and drain per turn from T3 to T6. When does Sorin flip? | queued |
| 3 | Interaction | Post-wipe rebuild; answering a T4 bomb; surviving an alpha strike | queued |
| 4 | Late Game | Which finisher ends games? Is the Exquisite Blood combo needed? Is the Aetherflux 50 reachable? | queued |
