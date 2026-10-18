# Deckbuilding SOP — Portable Standard Operating Procedure

> **Purpose.** One deck-agnostic, repeatable kit for building and refining a Commander/EDH
> deck. Copy this file into any deck repo and follow it. The deck-specific *what* (commander,
> engine, card list) lives in that repo's `CLAUDE.md`; this file is the *how*.
>
> **Provenance.** Consolidates the prior `DECKBUILDING-PLAYBOOK`, `ROUTINE-CHECKLIST`, and
> `PLAYTEST-PROCESS` into a single kit, plus lessons from a full 19-version build (see that
> repo's `RETROSPECTIVE.md`). §0–§10 are the timeless method; **Appendix A** is the
> environment-specific runbook (skip it if you aren't on Claude Code on the web).
>
> **How to update this file.** After each deck build, add a dated entry to **Appendix B** with
> any high-level learnings not already captured in §0–§10. If a learning is universal, fold it
> in directly and note the source deck in a parenthetical.

---

## §0 — Lifecycle map

A deck moves through six phases. Each has an entry condition, an exit condition, and the
artifact it writes. Don't skip forward — a phase's exit is the next phase's entry.

| Phase | Enter when… | Do | Exit when… | Writes |
|---|---|---|---|---|
| **0 Setup** | new repo | Stand up + **verify** the card-data pipeline and its fallback (§1) | a card lookup succeeds *and* the fallback is proven | `CLAUDE.md`, tooling |
| **1 Identity** | tooling works | Name commander, colors, the one-sentence plan, the primary engine (§2) | you can state the plan in one sentence | `CLAUDE.md` |
| **2 Skeleton** | identity fixed | Fill the template targets; count overlap-inclusive (§3); select cards (§4–§5) | ~100 cards, every category at/over target after honest counting | `decklist.md` |
| **3 Test** | a 99 exists | Goldfish + pod; ask specific questions (§7) | each test type reaches a verdict | `RESEARCH-LOG.md`, findings |
| **4 Iterate** | tests expose a flaw | ≤2 changes/batch, isolate + compute, then re-test (§6) | no category under target; finishers redundant; floor acceptable | decklist version bumps |
| **5 Maintain** | deck is "done" | Triage the candidate/watchlist bench; keep exports + docs in sync (§6, §10) | — (ongoing) | `CANDIDATES.md`, `moxfield.txt` |

Iteration is a loop: **Test → decide → ≤2 changes → re-test.** You will revisit §3–§7 many times.

---

## §1 — Phase 0: Tooling & verification *(do this first)*

The single biggest time-sink in a build is a card-data pipeline you *assumed* worked.

- **Stand up a primary card-data source and a fallback, and prove both before researching.**
  Run one real lookup through each path. (On Claude Code on the web, that's direct Scryfall REST
  where the environment allows it, plus WebSearch. Access differs per environment — see Appendix A.)
- **Verify before you reason.** Never assert card text from memory. Confirm every card via a
  primary source (Scryfall) before it informs a decision. **No card is added, cut, or
  reclassified before its text is confirmed.**
- **Fall back, don't stall.** If one channel is blocked (e.g. HTTP 403), switch sources rather
  than logging an open question. *A blocked tool is a fallback trigger, not a dead end.* The
  classic failure mode is leaning on a blocked tool and recording "research gaps" that a second
  source would have closed in one query.

---

## §2 — Phase 1: Identity

- **Name the identity in one sentence.** Commander, color identity, and the *one* primary engine
  the deck is about. Every other card serves that engine or keeps you alive to use it. If you
  can't say the plan in a sentence, stop and fix that before adding cards.
- **Favor a commander that is itself an engine piece.** An enabler/payoff you always have from
  the command zone beats one you must draw — it's the consistency backbone for every hand that
  doesn't open the primary combo. *(Validated: the command-zone engine carried every off-engine
  goldfish hand.)*

---

## §3 — Phase 2: Template skeleton + overlap-inclusive counting

**Build on a skeleton, not a blank page.** Category targets are scaffolding, not a cage. A
workable 100-card EDH baseline (Command Zone "658" template):

| Category | Target | Definition |
|---|---|---|
| Lands | ~38 | MDFCs count; resist cutting below this |
| Card Advantage | ~12 | Net **+1 card or more**. Cantrips (draw 1, replace 1) don't count. |
| Ramp | ~10–12 | **Repeatable** mana acceleration. One-shot rituals are not ramp. |
| Targeted Disruption | ~12 | One card disrupts **one** thing (counterspells count). |
| Mass Disruption | ~6 | One card disrupts **many** — wipes, taxes, graveyard hate, fogs, protection. |
| Plan Cards | ~30 | Enablers (~40%) / Payoffs (~35%) / Enhancers (~25%) |

Targets sum to **>100 on purpose** — because:

**Count overlap-inclusive.** Credit each card to **every** role it fills, not one bucket. A
land-fetch creature is Ramp *and* a Plan card; a typed dual that channels removal is Land *and*
Targeted Disruption; a draw-on-landfall creature is Payoff *and* Card Advantage. Totals will run
well over 100 — that overlap is where good deckbuilding lives. **This single step dissolves most
imagined "gaps."** Always recount honestly *before* concluding a category is short.

---

## §4 — Card selection

**Find the ONE real gap.** After honest overlap counting, usually only a single category is
genuinely under-target. Fix *that* one; don't manufacture problems in categories that are fine.
To source candidates, triangulate aggregate community data (EDHREC inclusion / synergy %) with
real built lists (Moxfield) — aggregates show *what's* played, real lists show *how it fits* —
then verify card text before trusting either.

**Selection filters** (apply when choosing what fills a slot):
- **Prefer double-duty cards.** The best fix for a gap *also advances the plan* (removal *and* a
  body; a land *and* an answer) — it earns its slot twice.
- **Put answers on cards you'd run anyway.** Disruption stapled to a land or creature costs no
  dedicated slot — and with a tutor becomes an on-demand silver bullet.
- **Reject feel-bad cards.** Non-interactive locks, repeatable fogs, grindy stax — cut them even
  if they technically fill a category. Play experience is a real constraint.
- **Redundancy beats raw power for engine pieces.** If the deck dies without piece X, run several
  cards that do X's job, not one better X.
- **Asymmetric-through-deckbuilding.** Symmetric effects (everyone draws/ramps) are fine when
  *your* deck abuses them far harder than the table.

**Dependency check** *(before locking any add).* Confirm the rest of the deck **supports what the
card needs.** A payoff that needs a full graveyard is dead if you don't fill the yard; a card that
needs to die needs a sac outlet; a "untap" loop needs the untapper. *Evaluate the card in the
context of this deck, not in isolation.* *(Lesson: a graveyard-recursion spell was nearly added to
a deck with no self-mill to feed it.)*

**Audit the finishers.** Ask explicitly:
- Can our closers actually end the game from a winning board?
- Are they **redundant across different mana costs** (a cheap one and a haymaker)?
- Is at least one **tutorable**?
A board-building deck with a single overrun/combo is one removal spell away from not converting.

**Design a complementary secondary axis.** The best secondary synergy (a) **free-rides** on
triggers the primary engine already makes, (b) **feeds the finisher** (e.g. makes the bodies an
overrun needs), and (c) is a **resilient Plan B** if the primary combo is answered. If a "synergy"
needs its own separate setup, it's a second deck, not a complement.

---

## §5 — Mana-base rigor

Count **reliable** sources per color against a target (commonly ~20 of each color a two-color deck
wants). Track, per land, three *separate* properties:
- **Color production** — untapped & unconditional vs. conditional.
- **Fetchability** — does it carry a basic land *type*? Fetchlands/land-tutors search by printed
  subtype, so a fetchable typed dual beats a non-fetchable fixer.
- **Entry tempo** — tapped / conditional-entry cost.

Utility lands that make no colored mana must justify their slot with an effect. **When swapping
lands, measure the change in sources *per color*, not the upgrade in any one land's quality** —
cutting two duals for one "better" dual is a *net loss* of color access. Keep a
`land-reference.md` with exact production + fetch targets per land.

---

## §6 — Changing safely (the iteration loop)

1. **Isolate and compute every change.** One structural change at a time so the result is
   attributable. Compute **before→after** counts (color sources, category totals) rather than
   trusting "X is better than Y." **Never bundle a mana-base change into a card swap** — that's
   the change that quietly wrecks color access and forces a revert.
2. **Critique adversarially before locking.** Read each card against your *own* board: does your
   wipe/removal hit your own permanents? Is a claimed "infinite" actually resource-limited? Could
   a replacement effect skip a payoff? (See §8.) Self-critique catches what playtesting won't.
3. **≤2 changes per batch, then test.** Flag changes as **unplaytested** and stress-test the batch
   as a unit before layering more on top. *(Lesson: a long pile of unplaytested changes had to be
   retro-tested all at once.)*
4. **Decide, log, sync.** Every pass ends with a concrete keep/add/cut + a self-eval (§9), a
   decklist version bump, **and** a sync of every doc the change touches (counts, version history,
   interactions, exports). Stale counts and mis-ordered version history are the recurring drift —
   close them in the same commit.

**The candidate ledger + Watchlist loop** (how Maintain-phase triage stays one-in/one-out):
- **`CANDIDATES.md` = the add-bench.** Cards evaluated (and verified) but not in the deck, ranked,
  each with a suggested cut. Triage to ≤2 before adding.
- **A Watchlist section = the cut-bench.** In-deck cards on the bubble, in cut-priority order.
- When you want an add, pair the top of the add-bench with the top of the cut-bench. One in, one
  out, counts recomputed, then test.

**Default lightweight.** Not every observation needs a file edit + commit + long write-up. Reserve
the full docs-and-commit treatment for durable changes (card swaps, version bumps); a quick note or
a one-line memory is enough for the rest.

---

## §7 — Playtesting (turn results into decisions)

**Two modes, different jobs:**
- **Goldfish (solitaire, no opponents)** measures **engine speed, consistency, ceiling and floor** —
  how fast the combo comes online, whether the hand stays full, where the dead turns are. It
  **under-tests interaction and resilience** (no one is disrupting you).
- **Pod (adversarial scenarios)** measures **interaction and resilience** — does your disruption
  suite actually answer a table; do you survive a wipe / an alpha strike; can you protect and
  rebuild. Use scenario snapshots ("after a board wipe", "racing three opponents") rather than a
  full turn-by-turn.

**Four standard test questions** (use all for a new deck; retire as findings converge):

| Test | Question | Retire when |
|---|---|---|
| **Opening Hands** | Is the deck consistent? What causes mulligans? | Keep-rate ≥ 40% across 2+ sessions |
| **Engine** | How does the core combo perform across scenarios? | All scenarios resolved, no new edge cases |
| **Interaction/Combo** | Is the key interaction worth its assembly cost? | Verdict confirmed across 2+ sessions |
| **Late Game** | What actually wins? What's dead at high resource counts? | All win-cons evaluated, card-text gaps closed |

**Discipline:**
- **Variance vs. signal.** Small samples can't tell bad luck from a real flaw. **Require a repeated
  pattern — a problem in 4+ hands or across 2+ sessions — before changing anything.** ~40% keep
  rate is healthy; one bad session is probably variance.
- **Keep/mulligan rubric (starting point):** 3+ lands, both colors available, ≥1 ramp/engine piece,
  fewer than two dead cards; refine with "can I cast something turn 1–2?"
- **Reproducible.** Record the method (and seed, if simulated) so a later session can re-run.
- **Decide and prune.** Each test ends with one of **keep / compress / retire / redesign**, and any
  *applied* change names the session that triggered it and re-runs the tests that referenced that
  card.

---

## §8 — Rules & legality traps

Facts about *how Magic works* — getting them wrong silently invalidates decisions. (Each bit a real
build at least once.)

**Legality (check first, non-negotiable):**
- **Color identity includes mana symbols in rules text, not just the cost.** A card that *produces*
  off-color mana (e.g. a land with "{T}: Add {B}") has that color in its identity and is **illegal**
  in a deck whose commander doesn't share it. Production, fetchability, and legality are three
  separate checks.
- Singleton: exactly one of each card except basic lands.

**Mana-base traps:**
- **Color production ≠ fetchability.** Fetchlands search by **printed land subtype**. A land can tap
  for a color yet lack the type (not a fetch target); another can carry the type but enter tapped.
- **Battlefield-only type-changers don't touch your library.** Turning your lands into a basic type
  applies only on the battlefield — library cards keep printed types, so fetch targets don't change.

**Engine / combo traps:**
- **"Infinite" that needs a resource each loop isn't infinite.** If a loop consumes a card / land /
  life per iteration, state how many iterations it actually gets.
- **Replacement effects can switch off your own payoffs.** A draw-replacement or dredge can skip the
  very "draw a card" triggers your engine wants.
- **Sacrifice-as-a-cost happens before the trigger.** A creature you sac for value can't carry an
  aura/effect that needs it to remain — it's gone when the ability resolves.
- **A death payoff needs a death you can cause.** "When this dies" does nothing if you can't kill it
  (no sac outlet; blink/bounce aren't deaths).
- **Watch self-anti-synergy.** Your own "destroy all artifacts/enchantments," edicts, and symmetric
  taxes hit *your* pieces too. Read every wipe/removal card against your own board.
- **A multiplier engine turns incremental effects into combos.** If the engine repeats a step
  (extra upkeeps, extra combats, copied triggers), evaluate each payoff at the multiplied rate. A
  "mill 10 per upkeep" card is a fast alternate win once upkeeps repeat. *(Obeka: Court of
  Cunning rejected.)*
- **An unbounded loop needs both directions.** "Gain life → opponents lose life" is bounded until a
  card adds "opponent loses life → you gain life." To audit a no-infinites rule, search the oracle
  cache for the reverse trigger, not just the forward one. *(Orzhov: Exquisite Blood cut.)*

---

## §9 — Definition of Done (run at the end of every routine)

Every research / build / playtest routine **ends by grading itself** and recording the result (a
short block in `RESEARCH-LOG.md` or the session log). It exists because sessions quietly degrade
into "logged a gap" instead of "answered the question." Grade honestly — a ‼️ is more useful than a
false ✅.

1. **Verified, not remembered** — every card-text claim backed by a primary source (≥2 sources for
   exact wording); blocks worked around, not surrendered to; no change made before its text was
   confirmed.
2. **Scope discipline** — before→after counts computed for any land/ramp/color/category change;
   structural changes isolated (≤2/batch).
3. **Output quality** — the routine ends with a concrete decision (keep / cut / add / no-change +
   why); any open question is genuinely un-answerable here, with the unblock path named.
4. **Reproducible** — playtests record method/seed so a later session can re-run them.

**Self-eval block** (paste into the log at the end of each routine):

```
### Self-eval — <routine name>, <date>
- Question:       <what it set out to answer>
- Answer/Decision: <conclusion, OR the specific blocker + the unblock path>
- Verification:   <source per claim — MCP / WebSearch URL(s)>
- Checklist:      §1 ✅/‼️  §2 ✅/‼️  §3 ✅/‼️   (one line on any ‼️)
```

**Stop rule:** if two or more sections are ‼️, the routine is **not done** — fix it or hand off with
the blocker named. Don't ship a "gap."

---

## §10 — The artifact set (keep it minimal)

A deck repo's canonical docs. Resist sprawl — each file earns its place, and each is **synced at the
end of every change that touches it** (stale counts/headers are the recurring drift).

| File | Holds | Updated |
|---|---|---|
| `CLAUDE.md` | deck-specific *what* + house rules; points at this SOP | identity / rule changes |
| `DECKBUILDING-SOP.md` | this kit (portable) | rarely; copy forward |
| `decklist.md` | the 99 + commander, category counts, **version history** | every version bump |
| `RESEARCH-LOG.md` | dated findings, each with a self-eval (append; never overwrite) | every routine |
| session log (`PROJECT-STEPS.md`) | per-session what/decisions/next-steps | every session wrap-up |
| `interactions.md` | **verified** card text + rules notes for key interactions | when an interaction changes |
| `CANDIDATES.md` | add-bench (ranked, with cuts) **+ Watchlist** cut-bench | when triaging |
| `land-reference.md` | exact production + fetch targets per land | mana-base changes |
| `oracle-cache.md` | verified oracle text + approximate prices for every deck card and CANDIDATES entry | every version bump; price spot-check monthly |
| an export (`moxfield.txt`) | importable list; regenerate from `decklist.md` | every version bump |
| *optional:* a build script (`tools/build.py`) + machine-readable list (`deck.tsv`) | regenerates the cache, the export, and category counts; checks legality, color identity, Game Changers | every version bump |

**Optional / create-when-needed:** a pending-routines queue (e.g. `PENDING-ROUTINES.md`) when a
backlog of routines accrues; per-deck playtest findings (`PLAYTEST-FINDINGS.md`); a `RETROSPECTIVE.md`
at the end of a build. Make these on demand — don't carry empty scaffolding between decks.

**The repo is the source of truth, not the deckbuilding site.** Pasted Moxfield/Archidekt exports
mangle names (split and MDFC cards, Universes Beyond reprint names) and silently drop cards. When the
owner pastes an export, diff it against the repo list, sync the real changes in, and build from the
repo file. *(Orzhov v4: a pasted 98-card list had four mangled names and two dropped cards.)*

**`oracle-cache.md` — why it exists and how to maintain it.**
Cloud routines (remote agents) cannot use the Scryfall MCP without interactive approval, and using
WebSearch for every card lookup burns token usage fast (one search per card × 99 cards = ~100 searches
per routine). The oracle cache pre-populates oracle text and prices locally so routines read a file
instead of hitting the network.

Structure:
- A price table with one row per card, approximate price, and a ⚠️ flag for cards to spot-check
- Oracle text blocks organized by decklist section
- CANDIDATES/Watchlist entries at the bottom

Maintenance rules:
1. **After any version bump:** add new cards to the cache (oracle text + price) before running the next routine. Remove or move cut cards to a "Graduated/Cut" section.
2. **Before a budget pass:** WebSearch the ⚠️-flagged high-cost cards to verify current prices. Update the price table and the estimated total.
3. **Routine operating rule:** every `PENDING-ROUTINES.md` should say "read `oracle-cache.md` first; only use WebSearch for cards not in the cache or flagged ⚠️."
4. Oracle text almost never changes (errata are rare) — re-verify only if a ruling or errata is announced.

---

## Appendix A — Running it in Claude Code on the web *(environment-specific)*

The §0–§10 method is timeless; this runbook is the operational layer for one runtime. Skip it if
you're building elsewhere.

**The environment.** An ephemeral sandbox behind an **egress allowlist**, cloned fresh per session.
Anything worth keeping must be committed and pushed.

**Card-data access depends on the environment, not the runtime.** Each cloud environment has
its own network policy, and the same host can be open in one deck's environment and blocked
(HTTP 403 on CONNECT) in another's. Never copy another deck's "works" note; probe at the start of
every session that needs the network.

Observed so far (re-verify; these are snapshots, not guarantees):

| Date | Environment | Scryfall REST | EDHREC JSON | Other | Source |
|---|---|---|---|---|---|
| 2026-06-02 | `mtg-simic-etb` | ⛔ 403 | ⛔ 403 | `mtgjson.com`, `api.github.com` ⛔ | Simic `CLAUDE.md` |
| 2026-10-17 | `mtg-obeka-upkeeps` | ✅ | ✅ | — | Obeka `CLAUDE.md` |
| 2026-10-18 | `mtg-orzhov-extort` | ✅ | ⛔ 403 | — | Orzhov `CLAUDE.md` |
| 2026-10-18 | MTG project (built-in env) | ⛔ 403 | ⛔ 403 | `data.scryfall.io`, `edhrec.com`, `mtgjson.com`, Moxfield and Archidekt APIs ⛔; `api.github.com`, `raw.githubusercontent.com`, `pypi.org` ✅ | kit re-verify |

What has held in every environment so far:
- ✅ **WebSearch** and **managed MCP servers** (e.g. GitHub MCP) work, because they run *outside*
  the sandbox. WebSearch restricted to `scryfall.com` / `gatherer.wizards.com` is the universal
  fallback.
- ⛔ **Local stdio MCP servers** make their calls from inside the sandbox, so they are only as open
  as direct `curl`. A local Scryfall MCP gains nothing over a direct REST script.

**Probe (one line per host, ~5 seconds):**

```bash
for u in "https://api.scryfall.com/cards/named?exact=Sol%20Ring" \
         "https://json.edhrec.com/pages/commanders/atraxa-praetors-voice.json"; do
  printf '%s  %s\n' "$(curl -s -o /dev/null -w '%{http_code}' -A 'mtg-deck/1.0' --max-time 15 "$u")" "$u"
done   # 200 = open; 000 = blocked by policy (curl -sS shows "CONNECT tunnel failed, response 403")
```

Record the result with its date in the deck's `CLAUDE.md` → Environment & Tooling.

**When Scryfall is blocked:**
- Read `oracle-cache.md` first; it is the reason the cache exists (§10).
- Verify new cards by WebSearch on `scryfall.com` (≥2 sources for exact wording), then add them to
  the cache by hand.
- A build script that needs direct Scryfall (e.g. Orzhov's `tools/build.py`) can't regenerate the
  cache; edit the deck file, recount by hand, and re-run the script in a session where it is open.
- To open the host, add `api.scryfall.com` (and `json.edhrec.com` if wanted) under the
  environment's allowed domains (Claude Code on the web → environment settings → Network access).
  Sessions started afterwards pick it up.
- **Fallback is always WebSearch** — never stall on a 403.

**Session-start hook (optional).** If the deck uses a local MCP or Python dependencies, provision
them each session via `.claude/hooks/session-start.sh` (registered for SessionStart). It re-creates
anything the ephemeral container loses. Stdlib-only scripts (`urllib`, `json`) need no hook.

**Scheduled playtest routines (optional automation).** Playtests can run as scheduled remote agents
that read the repo, append findings to `RESEARCH-LOG.md`, apply supported changes, and commit:
- **Prepend a constraints block** to each routine prompt, e.g.:
  `CONSTRAINTS: Do not spawn sub-agents. Do not call ToolSearch. Network/Scryfall may be blocked (403). Use only verified text from interactions.md and decklist.md.`
- **Tools:** `Bash`, `Read`, `Write`, `Edit`, `Grep`. **Model:** Haiku for mechanical Opening-Hand
  sims, Sonnet for analysis.
- **Stagger** same-day runs (~45 min apart) to avoid git conflicts on `RESEARCH-LOG.md`; run order
  Opening Hands → Engine → Interaction → Late Game.
- Track active tests in a small registry table in `CLAUDE.md` (Status / Days Run / Last Finding /
  Next Action); after each batch decide **keep / compress / retire / redesign** and record a
  synthesis entry in `RESEARCH-LOG.md`.

**Session wrap-up.** End each session by appending a session entry (what / decisions / next steps),
verifying every routine has a self-eval (§9), sanity-checking the decklist (total, overlap counts,
version-history vs. headers), then commit and push the working branch; fast-forward `master` only if
it's a clean fast-forward.

---

## How to start a new deck repo

1. Copy **this file** (`DECKBUILDING-SOP.md`) in unchanged.
2. Write a deck-specific `CLAUDE.md`: commander, colors, the one-sentence plan, the primary engine,
   house rules — then point it at this SOP.
3. Phase 0 (§1): stand up + verify the card-data pipeline and fallback.
4. Scaffold the artifact set (§10) as you go — `decklist.md` with a version history, `RESEARCH-LOG.md`
   with self-evals, a session log; add the rest when the phase needs them.
5. Run the lifecycle (§0): Setup → Identity → Skeleton → Test → Iterate → Maintain. Wrap up every
   session by logging it.

---

## Appendix B — Per-deck learnings *(update after each build)*

### Deck 1: Aesi / Simic Landfall (2026-05-31 → 2026-06-21, v1–v20)
*Source repo: `mtg-simic-etb`. Full post-mortem: `RETROSPECTIVE.md` in that repo.*

**The Mulldrifter pattern — prefer creature-based interaction.**
In a deck with a copy engine (Springheart), a blink engine (Thassa), and ETB draw (Guardian Project), every piece of interaction that's a creature is strictly better than the spell equivalent: it gets copied, blinked for repeated value, and triggers your draw. When evaluating a disruption slot, always ask "does a creature exist that does this?" before reaching for a spell. (e.g. Venser, Shaper Savant over Mystic Snake; Caustic Caterpillar over Reality Shift; Reclamation Sage over artifact-only removal spells.)

**Thematic coherence compounds.**
Generic goodstuff (Rhystic Study, Fierce Guardianship) works fine in isolation, but a deck with strong identity plays better and is more fun when every card feels like it belongs. The thematic re-skin (v13) replaced five generic blue spells with nature-flavored equivalents at the same mana cost with no loss in power — and opened up synergies (Garruk's Uprising giving the whole board trample; Mystic Snake being blinkable). When adding a slot, ask "does a thematic version of this exist?" before defaulting to the best generic.

**Read the actual current decklist before proposing cuts.**
After many versions and cloud agent sessions, the deck diverged significantly from what earlier context held. Recommending a cut for a card that was already removed several versions ago wastes time and erodes trust. At the start of any cut/add discussion, read `decklist.md` — the version history and current card list, not memory.

**LIFO stack behavior makes trigger-copiers anti-synergistic with compounding chains.**
Strionic Resonator looks powerful alongside Springheart but is actually worse than baseline: copying a chain trigger via Resonator sends the copied trigger's sub-chain to full exhaustion (LIFO) before the original trigger resolves — when the original finally fires, mana is gone. The {2},{T} activation competes directly with {1}{G} chain iterations. Any card that costs mana to copy a trigger inside a compounding mana-limited loop faces this same issue. Verify with explicit mana accounting before adding.

**Dependency check is non-negotiable.**
A card's value depends entirely on what else is in the deck. World Shaper (dies → return all graveyard lands) looks strong but requires (a) a sac outlet and (b) repeatable self-mill — neither of which this deck had. It was added, found dead in testing, and replaced. Before locking any add, confirm the deck supports what the card needs: a death trigger needs a way to die; a graveyard payoff needs a way to fill the yard; a loop needs the enabler chain intact.

---

### Deck 2: Terra, Magical Adept (2026-07-04 → ongoing)
*Source repo: `arburka/mtg-terra`. 5-color enchantress/Saga + enchantment reanimator. Phase 3 in progress.*

**The oracle cache pattern — eliminate network calls in cloud routines.**
Cloud routines (remote scheduled agents) cannot use the Scryfall MCP without interactive user approval, and using WebSearch for every card lookup burns significant token usage (~100 searches per routine for a 99-card deck). Solution: create `oracle-cache.md` at the end of Phase 2 with verified oracle text and approximate prices for every deck card and CANDIDATES entry. Routines read the file instead of hitting the network. Only WebSearch the small set of high-cost cards (⚠️-flagged) when running a budget audit.

Maintenance: add new cards to the cache after each version bump; spot-check ⚠️-flagged prices before each budget pass. Oracle text almost never needs re-verification (errata are rare).

Add `oracle-cache.md` creation to the Phase 2 → Phase 3 transition checklist. Add a Cache Refresh routine to `PENDING-ROUTINES.md` so it stays current automatically. See §10 for the full maintenance rules.

**Cloud routine MCP approval blocks unattended runs.**
Even with MCP tool calls pre-approved in `settings.json`, the MCP *server connection* requires interactive approval and will block a scheduled remote agent. Hard-ban MCP tools in `PENDING-ROUTINES.md` operating rules: "Do NOT use Scryfall MCP tools. Read `oracle-cache.md` first; only use WebSearch for cards not in the cache." This makes routines fully unattended.

**Finality counter loop requires a counter-removal piece.**
Yuna, Hope of Spira and Rydia, Summoner of Mist both return cards with finality counters — the card is exiled on next death instead of going to the graveyard, making reanimation one-shot per card. To enable a loop, include a cheap counter-removal piece (e.g. O'aka, Traveling Merchant: tap + remove counter → draw a card). Without this, the recursion engine is a sequence, not a loop.

**Saga copy tokens are sacrificed before combat via SBA — not after.**
When Esper Terra copies a Saga, the token enters with 1 lore counter, Terra immediately adds up to 3 more, all chapter triggers fire, and the Saga SBA sacrifices the token before the main phase ends — well before combat. Any "win condition" that requires the copy to deal combat damage (e.g. Summon: Primal Odin's Zantetsuken) will never trigger on a Terra-made copy. Verify copy-dependent win conditions explicitly against SBA timing before including them.

---

### Deck 3: Obeka, Splitter of Seconds (2026-10-17 → ongoing, v1–v11)
*Source repo: `arburka/mtg-obeka-upkeeps`. Grixis extra-upkeep engine. Phase 4, unplaytested at the table.*

**A seeded goldfish sim turns "it feels slow" into a structural answer.**
`sim/goldfish.py` (stdlib Python, ~250 lines) plays 20,000 seeded games on the play, ignores colors and draw spells, spends mana greedily, and reports "online by T6 / T8 / never," plus a wipe-recovery scenario. It showed the owner's complaint ("struggles to set up before getting disrupted") was structural: each extra payoff the kill waits for roughly halves online-by-T6 (61% at 1 payoff, 29% at 2, 7% at 3), and no single swap moved it more than 4 points. The fix was fewer pieces per kill plus a play pattern ("attack with evasion and one payoff"), not more power. How to reuse it:
- Test each candidate as a **single swap against the baseline**, then as a package (§6).
- Record the seed and the exact command in the self-eval (`python3 sim/goldfish.py moxfield.txt --need 2 --seed 17`), so every version is compared on the same games.
- Write the model's blind spots into the script header and the log. This sim undervalues magnitude (Paradox Haze doubling payoffs) and doesn't model protection at all; weigh those by hand.

**Owner overrides of the SOP are identity decisions; record them so they aren't "fixed."**
The owner cut every mana rock (ramp far under target) and applied batches of 5–8 swaps. Both go in `CLAUDE.md` → Key Decisions with "owner's call, don't fix without asking," and the self-eval marks the batch-size item ‼️ with the reason instead of pretending it passed. Later sessions then measure the cost (the sim logged the goldfish speed lost) instead of re-proposing rocks.

**Verification reverses memory-based tune-ups.**
A tune-up written from memory before Phase 0 got three calls wrong (cut two instant-speed pumps that are finishers here, cut a card that extra upkeeps turn into a draw burst, and mislabeled a Game Changer). Re-checking against Scryfall reversed all three. Treat any pre-verification analysis as a draft to re-audit, not a starting list.

**Declare a flavor direction as the tiebreaker.**
`CLAUDE.md` names the theme (time manipulation) and says: when two cards do the same job, prefer the on-theme one. It settled many slot decisions quickly and kept the "fun over optimal" brief concrete.

---

### Deck 4: Sorin of House Markov / Orzhov Extort (2026-10-18 → ongoing, v1–v4.7)
*Source repo: `arburka/mtg-orzhov-extort`. Extort drain with lifegain → drain payoffs. Phase 4, unplaytested.*

**Make the oracle cache a build artifact.**
`tools/build.py` (stdlib Python) reads `deck.tsv` (qty, name, section, comma-separated roles), fetches every card from Scryfall's `/cards/collection` endpoint (75 per request), and in one run: regenerates `oracle-cache.md` and `moxfield.txt`, prints overlap-inclusive category counts against the template targets, and flags color-identity violations, non-legal cards, and Game Changers. The cache never drifts from the list, and the recount after each swap is free. It needs direct Scryfall access, so probe first (Appendix A); when blocked, edit `deck.tsv` and the cache by hand and re-run later.

**The repo is the source of truth (now in §10).**
A pasted 98-card Moxfield list had four import-mangled names and two missing cards. v4 was built from `deck.tsv`, and the owner's later land update was diffed and synced in rather than taken wholesale.

**Record a Universes Beyond policy per owner, and check printings, not names.**
The owner's rule: Final Fantasy and LotR are usually fine; Marvel, TMNT and similar are case by case (ask before adding, don't cut just for being UB); other UB sets, ask. A card is UB-only if every printing matches Scryfall `is:ub`. Reprint names resolve to one Oracle name (Heaven-Sent Marvel, MAR 41 = Archangel of Thune), so keep the Oracle name in the list and prefer the non-UB printing.

**Category definitions belong to the owner.**
The owner doesn't count conditional mana (Crypt Ghast, Cabal Coffers, Treasure makers) as ramp. The cards were retagged as enhancers and the build script's ramp target set to 0, instead of arguing the template. The same goes for "no tutors," "no Game Changers," and "no infinite combos": write each into `CLAUDE.md` Constraints with the date.
