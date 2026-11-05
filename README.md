# Synthetic Reading of "The Yellow Wallpaper"

A reader-oriented, language-model-assisted reading of Charlotte Perkins Gilman's "The Yellow Wall-Paper" (1892) through feminist standpoint epistemology and the medical gaze. A short partial reading gives the researcher's position and three statements to prove. A language model extracts themes and evidence from the full text, the evidence is verified against the story, theme vocabulary is counted across ten equal parts of the story, and the results are interpreted.

**Author:** Vaisnavi Sainath
**Semester:** Monsoon Semester 2026
**Affiliation:** Department of Humanities and Social Sciences, Indian Institute of Technology (Indian School of Mines), Dhanbad
**Source text:** Gilman, Charlotte Perkins [Stetson]. "The Yellow Wall-Paper." *The New England Magazine*, January 1892 (OCR scan, `corpus.txt`).

## Research problem

How does institutional paternalism pathologize female creative autonomy as illness, and how does the domestic interior become a site of epistemic violence and counter-hegemonic madness?

## Statements to prove (written before counting)

| | Statement | Result | Strength |
|---|---|---|---|
| S1 | Confinement and medical language is denser in the first half | confinement 0.45 to 0.22, medical 0.74 to 0.16 hits per 100 words | medical: suggestive (p = 0.05); confinement: weak (p = 0.20) |
| S2 | Creeping-double language grows towards the end | rank correlation with position 0.87 | strong (p = 0.001) |
| S3 | Liberation language is concentrated in the last 20% | 0.56 against 0.06 per 100 words | suggestive (p = 0.09) |

The p-values come from shuffling the hit counts of the ten tenths 10,000 times (`analysis_extra.py`). They are a rough guide only, because each tenth holds just 0 to 12 hits. Full discussion in `docs/interpretation.md`.

## Main findings

- **The story opens inside the medical gaze.** Medical vocabulary is densest in the first tenth (1.93 per 100 words) and almost gone from the seventh tenth onwards.
- **The double takes over.** Creeping-double vocabulary is nearly absent until the middle, then peaks in the eighth tenth (1.93).
- **The rupture comes at the very end.** 6 of the 10 liberation hits fall in the last tenth ("got out at last", the peeled paper, the fainted husband).
- **Confinement returns at the end.** Its density rises again in the last tenth (0.80) when she locks the door and throws the key away, so its fall is not steady.
- **The model's scores do not follow the counts.** The five scores fall in even steps of 0.5 in the order of the prompt's list (9.5 to 7.5), and the theme with the most hits (creeping double, 37) is scored fourth. The counts carry the argument.

## Method (the seven steps)

1. **Partial reading.** Three blocks of about 20% of each third of the story: the first block of Part 1, a random block of Part 2 (seed 42) and the last block of Part 3. Together 1,265 of 6,225 words (20.3%). Code: `make_partial_reading.py`.
2. **Initial impression.** Impression, positionality, research problem, frameworks and three statements to prove: `initial_impression.md`.
3. **Text upload.** `corpus.txt` is cleaned of running heads, page numbers, ornaments and some scan errors (6,225 words).
4. **Query generation.** `prompt.txt` is the prompt used. The notebook builds a stricter `outputs/prompt_v2.txt` for any re-run.
5. **Targeted extraction and formatting.** AnythingLLM on LM Studio, running google/gemma-3-4b, returned a Python dictionary (`Theme_JSON.py`). All 15 quotations were checked against the story word for word and all match (`outputs/extraction_check.csv`). Record: `docs/extraction_record.md`.
6. **Computation and visualisation.** Word lists per theme are counted in ten equal tenths and reported per 100 words (`count_themes.py`, `theme_counts.json`). Every matched word is listed in `outputs/matches.csv`. Figures: `outputs/theme_trajectories.png`, `outputs/theme_heatmap.png`, and `graph.png` (the model's scores).
7. **Interpretation.** `docs/interpretation.md` and the website `index.html`, read through Foucault, Hartsock, Spivak, and Gilbert and Gubar.

## Repository structure

The notebook expects the first group of files in the same folder, so they stay at the top level.

```
synthetic-reading-main/
├── README.md                                    this file
├── index.html                                   project webpage
├── synthetic_reading_yellow_wallpaper.ipynb     notebook, Steps 1 to 7 (open in Google Colab)
├── corpus.txt                                   full text of the story (OCR scan)
├── partial_reading.txt                          Steps 1 and 2: three blocks and the initial impression
├── prompt.txt                                   Step 4: prompt given to the model
├── Theme_JSON.py                                Step 5: themes, scores and evidence from the model
├── make_partial_reading.py                      Step 1: chooses the three blocks (seed 42)
├── count_themes.py                              Steps 3 and 6: cleaning and counting
├── theme_counts.json                            Step 6: hits and hits per 100 words per tenth
├── analysis_extra.py                            Step 6: match list, term breakdown, permutation tests
├── visualisation.py, graph.png                  bar chart of the model's scores
├── initial_impression.md                        Step 2 as a stand-alone document
├── docs/
│   ├── interpretation.md                        Step 7: written interpretation and strength of evidence
│   └── extraction_record.md                     Step 5: tool, prompt, verification record
└── outputs/
    ├── cleaned_corpus.txt                       cleaned text used for counting
    ├── extraction_check.csv                     15 of 15 quotations verified
    ├── matches.csv                              all 121 matched words with tenth and context
    ├── term_breakdown.csv                       which words give each theme's hits
    ├── robustness.json                          permutation tests, with and without ambiguous words
    ├── prompt_v2.txt                            stricter prompt for a re-run
    ├── theme_trajectories.png, theme_heatmap.png
    └── interpretation.md                        as generated by the notebook
```

## Usage

Open the notebook in Google Colab and upload `corpus.txt`, `partial_reading.txt`, `prompt.txt` and `Theme_JSON.py` next to it, then run all cells. From the command line:

```
python count_themes.py      # writes theme_counts.json
python analysis_extra.py    # writes outputs/matches.csv, term_breakdown.csv, robustness.json
python visualisation.py     # writes thematic_visualisation.png (the model's scores; shipped here as graph.png)
```

Python 3 with `pandas` and `matplotlib` is enough.

## Limitations

- The scan has errors that the cleaning fixes only in part, so some matches are missed.
- The word lists are the researcher's. Some words have other uses (`work`, `fancy`, `free`, `shake`). Without them the patterns keep their direction, but the artistic-expression theme loses half its hits.
- Each tenth holds only 0 to 12 hits, so trends matter more than single bars, and the shuffle tests are a rough guide.
- The themes come from one run of one model with one prompt. The scores are estimates and do not follow the counts.
- Counts show vocabulary, not tone, irony or unreliable narration. The researcher's position (a sociological reading focused on institutions and power) may lead to overlooking literary form and the details of nineteenth-century medicine.

## Citation

Sainath, V. (2026). *Synthetic Reading of "The Yellow Wallpaper": Feminist Standpoint Epistemology and the Medical Gaze*. Department of Humanities and Social Sciences, IIT (ISM) Dhanbad.
