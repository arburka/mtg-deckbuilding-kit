# Interactions — verified card text + rules notes

All text was verified against Scryfall on 2026-10-18 (see `oracle-cache.md`).

## Extort math
> Extort (Whenever you cast a spell, you may pay {W/B}. If you do, each opponent loses 1 life and you gain that much life.)

- In a 4-player pod, one extort payment drains 3 (1 from each opponent) and you gain 3. That is **one** lifegain event of 3, not three events of 1.
- Each instance of extort triggers separately, and each needs its own {W/B} payment. With 4 extort permanents, a 1-mana spell can cost up to 5 mana to fully extort. **Mana is the engine's limit**, which is why ramp runs over target (Crypt Ghast and Cabal Coffers are the big sinks).
- **Pontiff of Blight** gives every other creature you control extort, tokens included (Lingering Souls spirits, Black Market Connections mercenaries, Kaya's Guile spirit).
- Extort triggers on **cast**. Flashback (Lingering Souls) and casting from the graveyard (Lurrus) both count. Lands, MDFC land faces, and activated abilities do not.

## Sorin flip
> At the beginning of each of your postcombat main phases, if you gained 3 or more life this turn, exile Sorin, then return him to the battlefield transformed under his owner's control.

- One paid extort (3 opponents) is enough to flip him. Sorin's own lifelink attack also works.
- The flip happens in the **postcombat** main phase, so he can attack first (lifelink) and then flip.
- **Sorin, Ravenous Neonate:** −1 deals damage equal to the life you gained this turn to any target. A big extort turn makes it removal or face damage.
- The Neonate side also has extort.

## Lifegain → drain multipliers
- **Sanguine Bond** {3}{B}{B}: whenever you gain life, target opponent loses that much life. One extort payment (gain 3) makes one opponent lose 3 more.
- **Vito, Thorn of the Dusk Rose** {2}{B}: the same text on a creature.
- **Marauding Blight-Priest** {2}{B} / **Cliffhaven Vampire** {2}{W}{B}: whenever you gain life, *each* opponent loses 1. This is a per-event trigger, so it does not scale with the amount gained.
- **Archangel of Thune:** a +1/+1 counter on each creature per lifegain event.

## Combos (Bracket 3: late-game two-card combos)
- **Exquisite Blood + Sanguine Bond** (or **+ Vito**): opponent loses life → you gain that much → target opponent loses that much → … The loop is mandatory and unbounded, and it ends when the targeted opponents are dead. Total cost is 10 MV (8 with Vito), so it is not early-game.
- **Exquisite Blood + Marauding Blight-Priest / Cliffhaven Vampire:** opponent loses 1 → gain 1 → each opponent loses 1 → (3 triggers) gain 1 each → … Also unbounded, and it kills the whole table.
- Any extort payment, lifelink hit, or Gray Merchant starts the loop.
- **Demonic Tutor** finds the missing half.

## Finishers
- **Aetherflux Reservoir:** gains life per spell cast this turn (1, 2, 3…). Each gain is a lifegain event for Blight-Priest, Vito, and Sanguine Bond. Paying 50 life deals 50 damage to any target. The deck's life total climbs, so the 50-life payment is reachable.
- **Gray Merchant of Asphodel:** drain equal to devotion to black. Lurrus cannot recast it (MV 5).
- **Debt to the Deathless:** each opponent loses 2X life. Tutorable with Demonic Tutor.
- **Restless Fortress:** attacking drains 2 (defending player only).

## Anti-synergy / self-hit checks (SOP §8)
- **Toxic Deluge / Vanquish the Horde** hit our own extort creatures. Extort enchantments (Blind Obedience, Life Insurance) and payoff enchantments (Sanguine Bond, Exquisite Blood) survive, so the drain engine persists through our own wipe.
- **Austere Command:** pick modes carefully. "All artifacts" hits our rocks, Skullclamp, Aetherflux, and Well. "All enchantments" hits Sanguine Bond, Exquisite Blood, Blind Obedience, Life Insurance, and Arena.
- **Life Insurance:** we lose 1 life and get a Treasure whenever *any* nontoken creature dies, including after our own wipes. The treasures fund extort.
- **Black Market Connections / Phyrexian Arena / Toxic Deluge** cost life. Extort offsets it, but watch the total when holding the Aetherflux 50.
- **Kambal** triggers off *opponents'* noncreature spells only. It is a tax and drain, not part of the extort engine.
- **Lurrus:** casts a permanent with MV 2 or less from the graveyard once per turn. That cast triggers extort. Targets include Thrull Parasite, Basilica Screecher, Syndic, Blind Obedience, Tithe Drinker, Elas il-Kor, Skullclamp, Sol Ring, signets, and Talisman.
