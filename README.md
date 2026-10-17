# MTG Deckbuilding Kit

A portable, deck-agnostic method for building and refining Commander/EDH decks with Claude Code.

## What's here

| File | Purpose |
|---|---|
| `DECKBUILDING-SOP.md` | The method — lifecycle, card selection, playtesting, definition of done. Copy into any deck repo. Appendix B accumulates learnings after each build. |
| `templates/CLAUDE.md` | Blank deck-specific context file — fill in commander, plan, engine, key decisions |
| `templates/CANDIDATES.md` | Blank candidate ledger + Watchlist |
| `templates/wrap-up.md` | Generic end-of-session wrap-up command — install globally so `/wrap-up` works in every repo |
| `reference/command-zone/` | Command Zone episode summaries behind the SOP (template, overlap, curve, removal, card evaluation) plus `card-selection-principles.md`. Index in its `README.md`. |

## Starting a new deck

1. Create a new repo (e.g. `mtg-gruul-stompy`)
2. Copy `DECKBUILDING-SOP.md` into it unchanged
3. Copy `templates/CLAUDE.md` → `CLAUDE.md`, fill in the deck-specific identity
4. Follow the lifecycle in §0 of the SOP: Setup → Identity → Skeleton → Test → Iterate → Maintain

That's it. The SOP tells Claude exactly what to do at each phase.

## Installing commands globally

Copy both command files to `~/.claude/commands/` once:

```bash
cp templates/wrap-up.md ~/.claude/commands/wrap-up.md
cp templates/new-deck.md ~/.claude/commands/new-deck.md
```

Then:
- `/new-deck` — starts a new deck from scratch, follows the SOP lifecycle in order (Phase 0 tooling → Phase 1 identity → Phase 2 skeleton). **Always use this when starting a new deck** — it ensures Phase 0 tooling is verified and the oracle cache is created before any cloud routines run.
- `/wrap-up` — end-of-session wrap-up for any project.

A deck repo can override either command by placing its own `.claude/commands/<command>.md`.

## Updating this kit after each deck build

Open `DECKBUILDING-SOP.md` and add a dated entry to **Appendix B** with anything that surprised you — new rules traps, card-evaluation heuristics, process improvements. If the learning is universal, fold it into §0–§10 directly.

## Worked example

`mtg-simic-etb` — Aesi / Simic Landfall, v1–v20. Full post-mortem in that repo's `RETROSPECTIVE.md`.
