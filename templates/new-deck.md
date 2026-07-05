---
description: Start a new MTG Commander deck — follow the deckbuilding SOP from Phase 0
---

You are starting a new MTG Commander deck. Follow the DECKBUILDING-SOP.md lifecycle exactly, in order. Do not skip phases or start building cards before the prior phase is complete.

**Before anything else:**
1. Read `/Users/andrewburka/Projects/mtg/mtg-deckbuilding-kit/DECKBUILDING-SOP.md` in full.
2. Ask the user for the deck's working name, then create the project directory at `/Users/andrewburka/Projects/mtg/<deck-name>/`.
3. Copy `DECKBUILDING-SOP.md` and the templates (`CLAUDE.md`, `CANDIDATES.md`) from the kit into the new directory.
4. Initialize a git repo, create a GitHub repo (`arburka/<deck-name>`), and push.

**Phase 0 — Tooling (§1). Do not proceed to Phase 1 until complete.**
- Ask the user which card data sources are available (Scryfall MCP? WebSearch?).
- Run one real lookup through each path to confirm it works. Record the result in `CLAUDE.md` under Environment & Tooling.
- Confirm the fallback (WebSearch restricted to site:scryfall.com) works.
- Wire the Scryfall MCP via `.mcp.json` + session-start hook if not already present (copy from `mtg-simic-etb/scryfall-mcp/` or `mtg-terra/scryfall-mcp/`).
- Add `.claude/settings.json` with pre-approved tool permissions (copy from an existing deck repo).
- Set up `PENDING-ROUTINES.md`: copy the operating rules block from an existing deck, add Test 0 (Cache Refresh) as the first routine.

**Phase 1 — Identity (§2). Do not proceed to Phase 2 until complete.**
- Ask the user: commander, colors, the one-sentence plan, primary engine, budget cap, house rules (e.g. no-search constraint), and gift/theme context if relevant.
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
