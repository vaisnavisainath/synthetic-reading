
## Interpretation

**Statements.** S2 is strongly supported: creeping-double vocabulary rises with position in the story (rank correlation 0.87). S1 is suggestive for medical language, which falls from 0.74 to 0.16 hits per 100 words between the first and second half, and weaker for confinement language, which falls from 0.45 to 0.22. S3 is suggestive: liberation vocabulary is 0.56 per 100 words in the last fifth against 0.06 in the first four-fifths. A shuffle test of the ten tenths (analysis_extra.py) gives p of about 0.001 for S2, 0.05 for medical language, 0.09 for S3 and 0.20 for confinement language, so only S2 is firm and the others are tendencies.

**The medical gaze.** Medical language is heaviest in the first tenth (1.93 per 100 words). In Foucault's terms the story opens inside the clinical gaze: diagnosis, tonics and regimen are reported as settled facts. Hartsock's standpoint theory and Spivak's idea of epistemic violence explain why this matters, because the narrator's own account is overruled by a husband who is also her doctor ("You see he does not believe I am sick!"). As her attention moves to the wallpaper, her own looking replaces the clinic's.

**The double.** Creeping-double vocabulary is almost absent until the middle and peaks in tenth 8 (1.93). This fits Gilbert and Gubar's reading of the woman behind the paper as the narrator's double, a figure who becomes clearer as the narrator identifies with her.

**The rupture.** Liberation vocabulary stays near zero until the final tenth (0.96), where the narrator peels the paper, says she has "got out at last" and creeps over her fainted husband. Gilman's own account of the story as an attack on the rest cure makes this the reversal of the opening: the medical gaze is now looked at from outside. Whether the ending is freedom or collapse is what the theme title leaves open. Confinement language also returns in the last tenth (0.80), when she locks the door and throws away the key, so its fall in the first half is not a steady decline.

## Limitations

The scan has errors that the cleaning fixes only in part, so some matches are missed. Each tenth holds only a few hits, so the trends matter more than any single bar. The word lists are mine, and some words (work, woman, free) have other uses. The 1-10 scores come from one run of one model and are estimates.

## References

Foucault, Michel. *The Birth of the Clinic: An Archaeology of Medical Perception*. Translated by A. M. Sheridan Smith. Tavistock, 1973.
Gilbert, Sandra M., and Susan Gubar. *The Madwoman in the Attic*. Yale University Press, 1979.
Gilman, Charlotte Perkins. "Why I Wrote 'The Yellow Wallpaper'?" *The Forerunner*, October 1913.
Gilman, Charlotte Perkins [Stetson]. "The Yellow Wall-Paper." *The New England Magazine*, January 1892.
Hartsock, Nancy. "The Feminist Standpoint." In *Discovering Reality*, edited by Sandra Harding and Merrill Hintikka. Reidel, 1983.
Spivak, Gayatri Chakravorty. "Can the Subaltern Speak?" In *Marxism and the Interpretation of Culture*, edited by Cary Nelson and Lawrence Grossberg. Macmillan, 1988.

## How strongly do the counts support the statements?

The statements above were checked by simple comparison of densities. To see how easily such patterns could arise by chance, the hit counts of the ten tenths were shuffled 10,000 times (`analysis_extra.py`, random seed 42) and the observed pattern was compared with the shuffled ones. The results are in `outputs/robustness.json`.

| Statement | Observed | One-sided p | Reading |
|---|---|---|---|
| S2 creeping double rises with position | rank correlation 0.87 | 0.001 | Strong. Very unlikely to be chance. |
| S1 medical language falls | 0.74 to 0.16 per 100 words | 0.054 | Suggestive, on the edge of the usual 0.05 line. |
| S3 liberation is concentrated at the end | 0.56 against 0.06 per 100 words | 0.091 | Suggestive. Only 10 hits in total, 6 of them in the last tenth. |
| S1 confinement language falls | 0.45 to 0.22 per 100 words | 0.204 | Weak. The last tenth (0.80) is the second-highest tenth, which breaks the trend. |

With only ten tenths and a few hits in each, these tests are a rough guide. The point is that "supported" means different things for the different statements: S2 is firm, S1 (medical) and S3 are suggestive, and S1 (confinement) is only a tendency.

**Robustness to the word lists.** Some words in the lists have many non-thematic uses (`work`, `fancy`, `free`, `shake`, `gate`, `key`, `exercise`). The tests were repeated without them (`outputs/robustness.json`). Every pattern keeps its direction (S2 rho 0.83, S1 medical 0.61 to 0.10, S3 0.48 against 0.06, S1 confinement 0.39 to 0.13), and the p-values stay in the same range. The artistic-expression theme is the most affected, falling from 25 hits to 12, because `fancy` and `fancies` alone give 9 hits (see `outputs/term_breakdown.csv`).

## The model's scores and the counts

The 1 to 10 scores from the language model are 9.5, 9.0, 8.5, 8.0 and 7.5, in exactly the order the themes were listed in the prompt. Even steps of 0.5 in list order suggest the model ranked the themes by the order it was given and did not measure them. They also disagree with the counts: the creeping double has the most hits (37) but only the fourth-highest score, and liberation has the fewest hits (10) and the lowest score, although its concentration in the last tenth is the clearest "event" in the story. The scores are therefore treated as the model's impression, and the counts, which can be checked word by word in `outputs/matches.csv`, carry the argument. The bar chart `graph.png` plots the model's scores, and the notebook's heatmap and trajectory figures (`outputs/theme_heatmap.png`, `outputs/theme_trajectories.png`) plot the counts.
