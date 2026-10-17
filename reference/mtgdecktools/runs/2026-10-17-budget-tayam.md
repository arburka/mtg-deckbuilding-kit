# Run — 2026-10-17 — Tuner (Budget Optimization) — Tayam

**Deck repo:** `arburka/mtg-tayam` at decklist v2
**Site settings:** Tuner → Budget Optimization; target budget $107; bracket detected 1; no Game Changers detected

## Card pool given to the site
None. Budget mode works from the decklist only. The decklist was `moxfield.txt` v2, names only.

## Site prompt (structure, not pasted verbatim)
- Same opening as run 1: role line, Prepare/Prepared note, commander card data
- Tuning goal `budget-optimization`, detected bracket
- Decklist as JSON with oracle text, EDHREC data and `priceUsd` per card (18 of 84 entries had no price)
- EDHREC commander data, plus "Popular cards NOT in the deck" as the preferred source for additions
- Changes to the decklist **are** allowed here (run 1's Explore mode forbade them)
- Optional tool-use block: Scryfall `cards/named` and `cards/search` URLs, the EDHREC JSON URL, and a request to run a verification script and put it in `verification.verificationScript`
- `strategyPrimer`: summary of changes, reasoning, how they meet the goal, expected improvement; no filler

## Claude's answer
`2026-10-17-budget-tayam.answer.json` (valid JSON, 100 cards, verification script passes).
- Cut Kutzil, Malamet Exemplar ($15.39), add Inspiring Call (about $0.30; text verified on Scryfall, price not)
- Restored the four card names the site mis-imported again: Life from the Loam, Commune with the Gods, Golgari Rot Farm, Ransack the Lab

## Result on the site
Not yet pasted back.

## Assessment
- **Useful:** per-card `priceUsd` makes the expensive cards obvious at once; the estimated deck total (about $105) was already under the $107 target.
- **Wrong or missing:**
  - The name mis-import from run 1 recurred: the prices quoted for those four cards were for the wrong cards.
  - Missing prices meant the total could only be estimated.
  - The prompt sets a target but no floor. When the deck is already under target it doesn't say whether to cut further or hold.
- **Ideas to keep for our own prompt:**
  - Read prices into the deck repo once (a cache) rather than per run.
  - State whether the goal is "get under X" or "cut as much as possible without losing synergy".
  - List the expensive cards being kept, with the reason for each.

## Applied to the deck?
Applied as `mtg-tayam` v3 (Kutzil, Malamet Exemplar → Inspiring Call).
