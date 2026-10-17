# Run — 2026-10-17 — Tuner (Explore New Cards) — Tayam

**Deck repo:** `arburka/mtg-tayam` at decklist v0 (reconstruction)
**Site settings:** Tuner → Explore New Cards; bracket detected 1, prompt says Bracket 2; no Game Changers detected

## Card pool given to the site
`moxfield.txt` pasted as-is (no set codes). Scryfall filter:
`id<=wbg f:commander mv<=3 -t:land -o:"search your library" (o:counter OR o:sacrifice) usd<=2`
— returned roughly 1,000 cards. **Too broad**: the prompt asks for a row per pool card.

## Site prompt (structure, not pasted verbatim — ~1,000-card pool)
- Role line + "new set mechanics" note (Prepare / Prepared)
- Commander card data (JSON: cost, type, oracle text, EDHREC rank, price)
- Tuning goal, detected bracket, Game Changer list, bracket guidelines (bracket is a ceiling, synergy first)
- Full decklist as JSON with oracle text, EDHREC inclusion % and synergy per card
- EDHREC commander data: average deck shape, themes, popular combos (with a bracket warning)
- Explore pool as JSON with oracle text and EDHREC data
- Rules: synergy is the primary ranking driver; value redundancy; only reference cards confirmed in the decklist; don't modify the decklist
- Output: strict JSON; `strategyPrimer` = exactly two HTML tables (cuts/adds, then full pool ranking sorted high→low), card names in `<code>`

## Claude's answer
`2026-10-17-tuner-tayam.answer.json` (valid JSON, 100 cards). Table 2 lists the 40 most relevant cards plus a summary row for the rest, rather than ~1,000 rows.

## Result on the site
Not yet pasted back.

## Assessment
- **Useful:** the prompt carries oracle text + EDHREC inclusion/synergy for every card, so card text didn't have to be recalled from memory. The combo list with a bracket warning is a good guardrail.
- **Wrong or missing:**
  - **Name matching:** four cards were resolved to the wrong card on import: Ransack the Lab → Ransack (blue, off-identity), Commune with the Gods → Commune with Evil, Life from the Loam → Afterlife from the Loam, Golgari Rot Farm → Golgari Brownscale (a land became a creature). Moxfield-format lines without set codes are not safe input.
  - **Pool size:** no cap or warning; a broad filter produced a pool the output format can't cover.
  - **House rules:** the prompt has no place for deck-specific constraints (no library search, MV ≤ 3 for Tayam recursion, budget).
  - Detected bracket 1 but the guidelines say Bracket 2.
- **Ideas to keep for our own prompt:** include oracle text and EDHREC synergy for deck and pool; "only reference cards confirmed in the decklist"; combo flags with bracket check; a fixed output table. Add: house rules from `CLAUDE.md`, a pool-size cap (~50–100), and a name-match check step.

## Applied to the deck?
None yet.
