---
description: Start a new MTG Commander deck — follow the deckbuilding SOP from Phase 0
---

You are starting a new MTG Commander deck. Follow the DECKBUILDING-SOP.md lifecycle exactly, in order. Do not skip phases or start building cards before the prior phase is complete.

**Before anything else:**
1. Locate the kit and read its `DECKBUILDING-SOP.md` in full. Use the first that exists:
   - `$MTG_KIT` (an environment variable pointing at a local clone of `mtg-deckbuilding-kit`)
   - a sibling clone: `../mtg-deckbuilding-kit/` (or `./mtg-deckbuilding-kit/` when the working directory holds several repos, as in a cloud session)
   - otherwise clone `https://github.com/arburka/mtg-deckbuilding-kit` into a scratch directory (in a cloud session, read it with the GitHub MCP if `git clone` is blocked).
2. Ask the user for the deck's working name (e.g. `mtg-gruul-stompy`). Create the deck directory as a sibling of the kit clone, `<kit parent>/<deck-name>/`. In a cloud session, create the GitHub repo first and work in the clone instead.
3. Copy `DECKBUILDING-SOP.md` and the templates (`CLAUDE.md`, `CANDIDATES.md`) from the kit into the new directory.
4. Initialize a git repo, create a GitHub repo under the user's account (ask which account if it isn't clear), and push.

**Phase 0 — Tooling (§1, Appendix A). Do not proceed to Phase 1 until complete.**
- Probe card-data access with the one-line `curl` check in SOP Appendix A (Scryfall REST, EDHREC JSON). Access differs per environment, so don't copy another deck's result.
- Run one real lookup through the primary path (direct Scryfall REST if open; otherwise a Scryfall MCP on the user's machine) and through the fallback (WebSearch restricted to site:scryfall.com). Record both results, with today's date, in `CLAUDE.md` under Environment & Tooling.
- Optional: copy a build script from an existing deck (e.g. `mtg-orzhov-extort/tools/build.py` + a `deck.tsv`) so the oracle cache, export, and counts regenerate in one command. It needs direct Scryfall access.
- Add `.claude/settings.json` with pre-approved tool permissions if the user wants it (copy from an existing deck repo).
- Set up `PENDING-ROUTINES.md`: copy the operating rules block from an existing deck, add Test 0 (Cache Refresh) as the first routine.

**Phase 1 — Identity (§2). Do not proceed to Phase 2 until complete.**
- Ask the user: commander, colors, the one-sentence plan, primary engine, bracket, budget cap, house rules (e.g. no tutors, no infinite combos, no Game Changers, Universes Beyond policy), and gift/theme context if relevant.
- Fill in `CLAUDE.md` with all of the above.
- Record any key constraints (search restrictions, budget cap, color priorities) explicitly in Key Rules.
- Confirm: can you state the plan in one sentence? If not, stop and resolve before continuing.

**Phase 2 — Skeleton (§3–§5).**
- Build the 99 using the Command Zone 658 template targets.
- Count overlap-inclusive. Don't conclude a category is short without an honest recount.
- After the 99 is locked:
  - Create `oracle-cache.md` with oracle text + prices for all 99 cards and any CANDIDATES entries. This is required before running any cloud routines.
  - Update prices for ⚠️-flagged expensive cards via WebSearch before noting the estimated total.
  - Create `land-reference.md` with per-color source counts.
  - Create `interactions.md` for any non-obvious rules interactions discovered during building.
  - Generate `moxfield.txt`.
  - Mark Phase 2 complete in `CLAUDE.md`.

**Then:** report back with a summary of what's been set up and ask what the user wants to work on in Phase 3.
