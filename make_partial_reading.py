"""
Step 1 (Partial Reading): choose 20% of the story, reproducibly.

The cleaned story is divided into three equal parts by sentence count. From each part a
contiguous block equal to 20% of that part is taken:
  Part 1: the FIRST block      Part 2: a RANDOM block (seed 42)      Part 3: the LAST block
Run in the folder that contains corpus.txt. Writes partial_reading_blocks.txt.
"""
import re, random

OCR_FIX = {"111 spite": "in spite", "perltaps": "perhaps", "per/zaps": "perhaps", "wall-p3.per": "wall-paper",
           "wall-pa per": "wall-paper", "evell": "even", "T is very seldom": "It is very seldom",
           'P""ople': "people", "hall s": "halls"}

def clean_story(path="corpus.txt"):
    raw = open(path, encoding="utf-8", errors="ignore").read()
    t = re.sub("\u00ad\\s*\n\\s*", "", raw)
    lines = t.split("\n")[3:]
    keep = [l for l in lines if not re.search(r"WALL.?PA|^[\s*\u2022\u00b7\u00a5.\d]*$|^\s*\d+\.\d+\.\d+", l)]
    text = re.sub(r"\s+", " ", " ".join(keep)).strip()
    for bad, good in OCR_FIX.items():
        text = text.replace(bad, good)
    return text

def choose_blocks(text, share=0.20, seed=42):
    """Return (sentences, blocks). Each block is (part_start, part_end, start, end, text, words); indexes are sentence numbers."""
    sents = re.split(r"(?<=[.!?])\s+(?=[\"'A-Z])", text)
    wc = [len(re.findall(r"[A-Za-z']+", x)) for x in sents]
    n = len(sents); size = n // 3
    blocks = []
    for i, (a, b) in enumerate([(0, size), (size, 2 * size), (2 * size, n)]):
        target = share * sum(wc[a:b])                       # 20% of this part's words
        def end_from(st):                                   # first sentence boundary that reaches the target
            tot = 0
            for j in range(st, b):
                tot += wc[j]
                if tot >= target:
                    return j + 1
            return None
        if i == 0:                                          # Part 1: the FIRST block
            st = a
        elif i == 1:                                        # Part 2: a RANDOM block
            st = random.Random(seed).choice([x for x in range(a, b) if end_from(x)])
        else:                                               # Part 3: the LAST block
            tot, st = 0, b
            while tot < target:
                st -= 1; tot += wc[st]
        en = end_from(st) if i < 2 else b
        blk = " ".join(sents[st:en])
        blocks.append((a, b, st, en, blk, sum(wc[st:en])))
    return sents, blocks

if __name__ == "__main__":
    text = clean_story()
    sents, blocks = choose_blocks(text)
    tot = len(re.findall(r"[A-Za-z']+", text))
    for i, (a, b, st, en, blk, nw) in enumerate(blocks, 1):
        print(f"Part {i}: sentences {a+1}-{b} | block {st+1}-{en} | {nw} words")
    got = sum(b[5] for b in blocks)
    print(f"Story {tot} words; read {got} words = {got/tot*100:.1f}%")
    open("partial_reading_blocks.txt", "w", encoding="utf-8").write("\n\n".join(b[4] for b in blocks))
