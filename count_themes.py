"""
Step 3 (pre-processing) and Step 6 (computation) for the synthetic reading of
'The Yellow Wallpaper'.

STATEMENT TO PROVE (written before counting):
  H1. Confinement and medical-gaze language is denser in the first half of the
      story than in the second half.
  H2. Creeping-double language becomes denser as the story moves towards its end.
  H3. Liberation language is concentrated in the last 20% of the story.
"""
import re, json
from math import sqrt

# ---- Step 3: clean the OCR text -------------------------------------------
raw = open("corpus.txt", encoding="utf-8", errors="ignore").read()
t = re.sub("\u00ad\\s*\n\\s*", "", raw)                 # join words split by soft hyphens
lines = t.split("\n")[3:]                               # drop epigraph, title, byline
keep = [l for l in lines
        if not re.search(r"WALL.?PA|^[\s*•·¥.\d]*$|^\s*\d+\.\d+\.\d+", l)]  # running heads, page numbers, ornaments
t = " ".join(keep)
for bad, good in {"111 spite": "in spite", "perltaps": "perhaps", "per/zaps": "perhaps",
                  "wall-p3.per": "wall-paper", "wall-pa per": "wall-paper", "evell": "even",
                  "T is very seldom": "It is very seldom", 'P""ople': "people", "hall s": "halls"}.items():
    t = t.replace(bad, good)
words = re.findall(r"[A-Za-z']+", t)
N = len(words)

# ---- Step 6: theme vocabularies (from the verified evidence plus key terms) ----
themes = {
 "Domestic Confinement & Patriarchal Control": r"nursery|barred|\bbars\b|\bgate|locked|\bkey\b|forbidden|not hear of|hardly lets|laughs at me",
 "The Medical Gaze & The Rest Cure": r"physician|doctor|phosphates|phosphites|tonics|nervous|hysterical|rest cure|treatment|medicine|\bsick\b|get well|exercise",
 "Repression of Female Artistic Expression": r"\bwrit(?:e|ing|ten)\b|\bwrote\b|\bwork\b|\bpen\b|dead paper|\bsly\b|imagination|fancies|fancy",
 "The Creeping Double (Subversive Mirror)": r"creep\w*|crawl\w*|\bwomen?\b|\bshapes?\b|\bshake|smooch\w*|stooping",
 "Psychosis as Radical Liberation": r"got out|out at last|in spite of|peel\w*|pull(?:ed|ing) off|\btore\b|fainted|astonish|\bfree\b",
}
SEG = 10
size = N // SEG
segs = [" ".join(words[i*size:(i+1)*size if i < SEG-1 else N]).lower() for i in range(SEG)]
seglen = [len(s.split()) for s in segs]
res = {}
for name, pat in themes.items():
    hits = [len(re.findall(pat, s)) for s in segs]
    res[name] = {"hits": hits, "per100": [round(h/l*100, 2) for h, l in zip(hits, seglen)]}

def spearman(y):
    x = list(range(len(y)))
    def rank(v): return [sorted(v).index(a) + (v.count(a)-1)/2 for a in v]
    rx, ry = rank(x), rank(y)
    mx, my = sum(rx)/len(rx), sum(ry)/len(ry)
    num = sum((a-mx)*(b-my) for a, b in zip(rx, ry))
    return num / sqrt(sum((a-mx)**2 for a in rx) * sum((b-my)**2 for b in ry))
def dens(hits, a, b): return sum(hits[a:b]) / sum(seglen[a:b]) * 100

out = {"words": N, "segment_words": seglen, "themes": res, "tests": {}}
for n in list(themes)[:2]:
    h = res[n]["hits"]; out["tests"]["H1 "+n] = {"first_half": round(dens(h,0,5),2), "second_half": round(dens(h,5,10),2)}
n = list(themes)[3]; out["tests"]["H2 "+n] = {"spearman_with_position": round(spearman(res[n]["per100"]),2)}
n = list(themes)[4]; h = res[n]["hits"]; out["tests"]["H3 "+n] = {"last_20pct": round(dens(h,8,10),2), "first_80pct": round(dens(h,0,8),2)}
json.dump(out, open("theme_counts.json", "w"), indent=1)
print(json.dumps(out, indent=1))
