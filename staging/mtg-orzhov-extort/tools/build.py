"""Regenerate oracle-cache.md and moxfield.txt from deck.tsv, and print category counts.

Usage: python3 tools/build.py
Requires direct access to api.scryfall.com (works in this cloud env as of 2026-10-18).
"""
import collections
import datetime
import json
import pathlib
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
TARGETS = {"land": 38, "ca": 12, "ramp": 10, "targeted": 12, "mass": 6, "plan": 30}
PLAN_ROLES = {"enabler", "payoff", "enhancer"}


def load_deck():
    rows = []
    for line in (ROOT / "deck.tsv").read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        qty, name, section, roles = line.split("\t")
        rows.append((int(qty), name, section, roles.split(",")))
    return rows


def fetch(names):
    cards = {}
    for i in range(0, len(names), 75):
        body = json.dumps({"identifiers": [{"name": n} for n in names[i:i + 75]]}).encode()
        req = urllib.request.Request(
            "https://api.scryfall.com/cards/collection", data=body,
            headers={"Content-Type": "application/json", "User-Agent": "mtg-orzhov-extort/1.0",
                     "Accept": "application/json"})
        data = json.load(urllib.request.urlopen(req))
        for nf in data.get("not_found", []):
            raise SystemExit(f"Scryfall could not find: {nf}")
        for c in data["data"]:
            cards[c["name"]] = c
            cards[c["name"].split(" // ")[0]] = c
        time.sleep(0.2)
    return cards


def main():
    rows = load_deck()
    cards = fetch(sorted({r[1] for r in rows}))

    total = sum(r[0] for r in rows)
    counts = collections.Counter()
    for qty, name, _, roles in rows:
        for role in roles:
            counts[role] += qty
        if PLAN_ROLES & set(roles) and "land" not in roles:
            counts["plan"] += qty
    problems = []
    for _, name, _, _ in rows:
        c = cards[name]
        if not set(c["color_identity"]) <= {"W", "B"}:
            problems.append(f"{name}: color identity {c['color_identity']}")
        if c["legalities"]["commander"] != "legal":
            problems.append(f"{name}: {c['legalities']['commander']}")
    game_changers = [n for _, n, _, _ in rows if cards[n].get("game_changer")]

    print(f"Total cards: {total}")
    for role, target in TARGETS.items():
        print(f"  {role:9} {counts[role]:3}  (target ~{target})")
    for role in ("enabler", "payoff", "enhancer", "finisher"):
        print(f"  {role:9} {counts[role]:3}")
    print(f"Game Changers ({len(game_changers)}): {', '.join(game_changers)}")
    print("Legality problems:", problems or "none")

    # moxfield.txt
    lines = []
    for qty, name, section, _ in rows:
        full = cards[name]["name"]
        lines.append(f"{qty} {full}")
    (ROOT / "moxfield.txt").write_text("\n".join(lines) + "\n")

    # oracle-cache.md
    today = datetime.date.today().isoformat()
    out = [f"# Oracle Cache — Sorin of House Markov Extort",
           "",
           f"> Verified via Scryfall `/cards/collection` on {today}. Regenerate with `python3 tools/build.py`.",
           "> Routines: read this file first; only hit the network for cards not listed here or flagged ⚠️.",
           "",
           "## Prices (USD, Scryfall nonfoil market)",
           "",
           "| Card | Qty | Price | Flag |",
           "|---|---|---|---|"]
    est = 0.0
    for qty, name, _, _ in rows:
        p = cards[name]["prices"].get("usd")
        price = float(p) if p else 0.0
        est += price * qty
        flag = "⚠️" if price >= 20 else ""
        out.append(f"| {cards[name]['name']} | {qty} | {p or 'n/a'} | {flag} |")
    out += ["", f"**Estimated total:** ${est:,.2f} (cheapest printing prices vary; ⚠️ = spot-check before a budget pass)", ""]
    section = None
    for _, name, sec, roles in rows:
        if sec != section:
            section = sec
            out += ["", f"## {sec}", ""]
        c = cards[name]
        out.append(f"### {c['name']}")
        out.append(f"*{c.get('mana_cost') or ''} — {c['type_line']}* — roles: {', '.join(roles)}")
        out.append("")
        for face in c.get("card_faces") or [c]:
            if c.get("card_faces"):
                out.append(f"**{face['name']}** {face.get('mana_cost', '')} — {face['type_line']}")
            text = face.get("oracle_text", "")
            out += [f"> {t}" for t in text.split("\n")] if text else ["> (no rules text)"]
            out.append("")
    (ROOT / "oracle-cache.md").write_text("\n".join(out))
    print(f"Wrote oracle-cache.md (est ${est:,.2f}) and moxfield.txt")


if __name__ == "__main__":
    main()
