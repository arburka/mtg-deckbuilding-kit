# MTG Deckbuilding Kit

A portable, deck-agnostic method for building and refining Commander/EDH decks with Claude Code.

## What's here

| File | Purpose |
|---|---|
| `DECKBUILDING-SOP.md` | The method — lifecycle, card selection, playtesting, definition of done. Copy into any deck repo. Appendix B accumulates learnings after each build. |
| `templates/CLAUDE.md` | Blank deck-specific context file — fill in commander, plan, engine, key decisions |
| `templates/CANDIDATES.md` | Blank candidate ledger + Watchlist |
| `templates/wrap-up.md` | Generic end-of-session wrap-up command — install globally so `/wrap-up` works in every repo |

## Starting a new deck

1. Create a new repo (e.g. `mtg-gruul-stompy`)
2. Copy `DECKBUILDING-SOP.md` into it unchanged
3. Copy `templates/CLAUDE.md` → `CLAUDE.md`, fill in the deck-specific identity
4. Follow the lifecycle in §0 of the SOP: Setup → Identity → Skeleton → Test → Iterate → Maintain

That's it. The SOP tells Claude exactly what to do at each phase.

## Installing the wrap-up command globally

Copy `templates/wrap-up.md` to `~/.claude/commands/wrap-up.md` once. Then `/wrap-up` works in every project without any per-repo setup. A deck repo can override it by placing its own `.claude/commands/wrap-up.md` for deck-specific steps.

## Updating this kit after each deck build

Open `DECKBUILDING-SOP.md` and add a dated entry to **Appendix B** with anything that surprised you — new rules traps, card-evaluation heuristics, process improvements. If the learning is universal, fold it into §0–§10 directly.

## Worked example

`mtg-simic-etb` — Aesi / Simic Landfall, v1–v20. Full post-mortem in that repo's `RETROSPECTIVE.md`.
