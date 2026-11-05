# Extraction record (Step 5)

| Item | Record |
|---|---|
| Tool | AnythingLLM running on LM Studio (local) |
| Model | google/gemma-3-4b |
| Prompt given | `prompt.txt` |
| Stricter prompt for a re-run | `outputs/prompt_v2.txt` (made by Step 4 of the notebook: exact quotations, one theme per quotation, scoring rubric, JSON only) |
| Output as kept | `Theme_JSON.py` (a Python dictionary: 5 themes, intensity, analysis, 3 quotations each) |
| Verification | Every quotation is checked against the story ignoring line breaks, hyphens and quote marks (Step 5 of the notebook). Result in `outputs/extraction_check.csv`: **15 of 15 quotations match the story word for word.** |
| Researcher rejections | None. No quotation failed the check. |
| What is not verified | The intensity scores and the analyses are the model's own judgement. They are not checked against the text and, as `docs/interpretation.md` explains, they do not follow the counts. |

## How the counts relate to the extraction

The model's quotations were used to build the word lists in `count_themes.py` (the lists are "from the verified evidence plus key terms"). The counts in `theme_counts.json` and `outputs/matches.csv` therefore come from the researcher's word lists, and not from the model's scores.
