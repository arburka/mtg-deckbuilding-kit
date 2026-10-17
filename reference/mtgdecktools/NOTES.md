# mtgdecktools.com — notes

[mtgdecktools.com](https://www.mtgdecktools.com/) is a third-party site (not ours) with three AI-assisted Commander tools: **The Brewer** (build a new deck), **The Tuner** (refine an existing list) and **The Scribe** (write a primer). It doesn't call an AI itself: it generates a prompt, you paste that into an AI, and you paste the AI's JSON answer back into "Process AI Deck Result".

We run its prompts through Claude a few times, capture each run, and use what we learn to write our own commands (`/brew`, `/tune`, `/primer`) that read a deck repo directly.

## How the site works (observed)

- **Card pool input:** one card per line, `Quantity Card Name (SetCode)`, e.g. `1 Rite of Replication (TDC) 165`. Also accepts Moxfield/Archidekt exports and ManaBox / MTG Scanner CSVs. Filters by format legality.
- **Commander:** search and select; supports partners and bracket-based power levels.
- **AI output:** JSON pasted back in, shaped like `{ "deckName": "...", "deckList": [...], ... }`. Full schema: not yet captured.
- **Exports:** "Copy Pool as JSON", "Export CSV".
- **Access:** this cloud session can't reach the site (blocked by the network allowlist), so everything moves by copy-paste.

## Runs

| Date | Tool | Deck | File | Verdict |
|---|---|---|---|---|
| 2026-10-17 | Tuner (Explore New Cards) | Tayam | [run](runs/2026-10-17-tuner-tayam.md) | Prompt is data-rich; import mis-matched 4 card names; filter too broad |

## Patterns across runs

### What their prompts ask for
- Full oracle text + EDHREC inclusion/synergy for every deck and pool card; synergy-first ranking; bracket as a ceiling; strict JSON with HTML tables (run 1)

### What our SOP adds
- Deck house rules (no-search, MV caps, budget) the site prompt has no slot for (run 1)

### What we'd change in our own version
- Verify every imported name before analysis; cap the candidate pool; read house rules from the deck's `CLAUDE.md` (run 1)

## Next step

After 2–3 runs, draft `templates/tune.md` (first, since our decks already exist), then `brew.md` and `primer.md`.
