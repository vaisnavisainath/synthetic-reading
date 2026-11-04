# Synthetic Reading of "The Yellow Wallpaper"

Author: Vaisnavi Sainath, Humanities and Social Sciences, IIT (ISM) Dhanbad. Monsoon Semester 2026.

A synthetic reading of Charlotte Perkins Gilman's story through feminist standpoint epistemology and the medical gaze.

| File | Step | Contents |
|---|---|---|
| `synthetic_reading_yellow_wallpaper.ipynb` | 1 to 7 | Notebook that runs the whole reading (open in Google Colab) |
| `partial_reading.txt` | 1 and 2 | Three 20% blocks of the story (first, random, last), then the initial impression, research problem and frameworks |
| `make_partial_reading.py` | 1 | Code that chooses the three blocks (random seed 42) |
| `partial_reading_earlier_selection.txt` | 1 | The ten hand-picked lines used for the first impression, kept for reference |
| `corpus.txt` | 3 | Full text of the story (OCR scan, 1892) |
| `prompt.txt` | 4 | Prompt given to the LLM |
| `Theme_JSON.py` | 5 | Extracted themes, scores and evidence (quotes checked against the story) |
| `count_themes.py`, `theme_counts.json` | 6 | Cleans the text and counts theme vocabulary per tenth of the story |
| `visualisation.py`, `graph.png` | 6 | Bar chart of the model's theme scores |
| `index.html` | 7 | The website, with the interpretation |

Run the notebook with `corpus.txt`, `partial_reading.txt`, `prompt.txt` and `Theme_JSON.py` in the same folder.
