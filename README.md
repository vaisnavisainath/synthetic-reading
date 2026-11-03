# Synthetic Reading of "The Yellow Wallpaper"

Author: Vaisnavi Sainath, Humanities and Social Sciences, IIT (ISM) Dhanbad. Monsoon Semester 2026.

A synthetic reading of Charlotte Perkins Gilman's story through feminist standpoint epistemology and the medical gaze.

| File | Step | Contents |
|---|---|---|
| `partial_reading.txt` | 1 and 2 | Sample lines, initial impression, research problem, frameworks |
| `corpus.txt` | 3 | Full text of the story (OCR scan, 1892) |
| `prompt.txt` | 4 | Prompt given to the LLM |
| `Theme_JSON.py` | 5 | Extracted themes, scores and evidence (quotes checked against the story) |
| `count_themes.py`, `theme_counts.json` | 6 | Cleans the text and counts theme vocabulary per tenth of the story |
| `visualisation.py`, `graph.png` | 6 | Bar chart of the model's theme scores |
| `index.html` | 7 | The website, with the interpretation |

Run `python count_themes.py` in the same folder as `corpus.txt` to reproduce the counts.
