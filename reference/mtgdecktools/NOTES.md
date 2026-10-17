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
| | | | | |

## Patterns across runs

### What their prompts ask for
-

### What our SOP adds
-

### What we'd change in our own version
-

## Next step

After 2–3 runs, draft `templates/tune.md` (first, since our decks already exist), then `brew.md` and `primer.md`.
