"""
Extra analysis for the synthetic reading of 'The Yellow Wallpaper'.

Uses the same cleaning, the same ten equal segments and the same word lists as
count_themes.py (it is imported, so the numbers cannot drift), and adds:

  1. outputs/matches.csv        every single matched word, with its tenth and context
  2. outputs/term_breakdown.csv which words produce the hits for each theme
  3. outputs/robustness.json    permutation tests and a re-run without ambiguous words

Run:  python analysis_extra.py        (needs corpus.txt in the same folder)
"""
import re, json, random, csv, os, io, contextlib
from math import sqrt

with contextlib.redirect_stdout(io.StringIO()):      # count_themes prints its results; keep this quiet
    import count_themes as ct

os.makedirs("outputs", exist_ok=True)
themes, segs, seglen, N = ct.themes, ct.segs, ct.seglen, ct.N
names = list(themes)

# ---- 1. every matched occurrence ---------------------------------------------
rows = []
for name, pat in themes.items():
    for i, s in enumerate(segs):
        for m in re.finditer(pat, s):
            ctx = s[max(0, m.start() - 40): m.end() + 40]
            rows.append({"theme": name, "tenth": i + 1, "matched": m.group(0).strip(),
                         "context": "..." + ctx + "..."})
with open("outputs/matches.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["theme", "tenth", "matched", "context"])
    w.writeheader(); w.writerows(rows)

# the CSV must agree with theme_counts.json
for name in names:
    for i in range(10):
        n = sum(1 for r in rows if r["theme"] == name and r["tenth"] == i + 1)
        assert n == ct.res[name]["hits"][i], (name, i)
print(f"matches.csv: {len(rows)} occurrences, identical to the counts in theme_counts.json")

# ---- 2. which words carry each theme -----------------------------------------
breakdown = {}
for r in rows:
    breakdown.setdefault(r["theme"], {}).setdefault(r["matched"].lower(), 0)
    breakdown[r["theme"]][r["matched"].lower()] += 1
with open("outputs/term_breakdown.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["theme", "matched_word", "count"])
    for t in names:
        for k, v in sorted(breakdown.get(t, {}).items(), key=lambda kv: -kv[1]):
            w.writerow([t, k, v])

# ---- 3. permutation tests ------------------------------------------------------
# Question: if the hits were scattered over the ten tenths at random, how often would the
# pattern be as strong as observed?  The tenths are almost equal in length (622 or 631 words),
# so the hit counts of the tenths are shuffled directly.
def spearman(y):
    x = list(range(len(y)))
    rank = lambda v: [sorted(v).index(a) + (v.count(a) - 1) / 2 for a in v]
    rx, ry = rank(x), rank(y)
    mx, my = sum(rx) / len(rx), sum(ry) / len(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))
    return num / den if den else 0.0

def dens(h, a, b): return sum(h[a:b]) / sum(seglen[a:b]) * 100

def perm_p(hits, stat, n=10000, seed=42):
    rnd = random.Random(seed)
    obs, h, c = stat(hits), list(hits), 0
    for _ in range(n):
        rnd.shuffle(h)
        if stat(h) >= obs - 1e-12: c += 1
    return obs, (c + 1) / (n + 1)

def run_tests(hits_by_theme):
    out = {}
    for n in names[:2]:
        h = hits_by_theme[n]
        obs, p = perm_p(h, lambda x: dens(x, 0, 5) - dens(x, 5, 10))
        out[f"H1 {n}"] = {"first_half": round(dens(h, 0, 5), 2), "second_half": round(dens(h, 5, 10), 2),
                          "difference": round(obs, 2), "p_one_sided": round(p, 4)}
    h = hits_by_theme[names[3]]
    obs, p = perm_p(h, lambda x: spearman([a / l * 100 for a, l in zip(x, seglen)]))
    out[f"H2 {names[3]}"] = {"spearman_with_position": round(obs, 2), "p_one_sided": round(p, 4)}
    h = hits_by_theme[names[4]]
    obs, p = perm_p(h, lambda x: dens(x, 8, 10) - dens(x, 0, 8))
    out[f"H3 {names[4]}"] = {"last_20pct": round(dens(h, 8, 10), 2), "first_80pct": round(dens(h, 0, 8), 2),
                             "difference": round(obs, 2), "p_one_sided": round(p, 4)}
    return out

main_hits = {n: ct.res[n]["hits"] for n in names}

# ---- 4. robustness: drop words that have many non-thematic uses ----------------
ambiguous = {
    names[0]: r"\bgate|\bkey\b",
    names[1]: r"exercise|medicine|treatment|\bsick\b",
    names[2]: r"\bwork\b|\bpen\b|imagination|fancies|fancy",
    names[3]: r"\bshake|\bshapes?\b",
    names[4]: r"\bfree\b|astonish",
}
strict_hits = {}
for n in names:
    strict = "|".join(p for p in themes[n].split("|") if p not in ambiguous[n].split("|"))
    strict_hits[n] = [len(re.findall(strict, s)) for s in segs]

report = {
    "note": "Permutation tests shuffle the hit counts of the ten tenths 10,000 times (seed 42). "
            "With only ten tenths and a few hits each, they are a rough guide, not proof.",
    "main_word_lists": run_tests(main_hits),
    "without_ambiguous_words": run_tests(strict_hits),
    "ambiguous_words_removed": {n: ambiguous[n] for n in names},
    "hits_total": {"main": {n: sum(main_hits[n]) for n in names},
                   "without_ambiguous_words": {n: sum(strict_hits[n]) for n in names}},
}
json.dump(report, open("outputs/robustness.json", "w"), indent=1)

for label in ("main_word_lists", "without_ambiguous_words"):
    print(f"\n{label}")
    for k, v in report[label].items():
        print(" ", k[:55].ljust(56), v)
print("\nTotal hits:", report["hits_total"])
