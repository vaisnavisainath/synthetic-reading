import matplotlib.pyplot as plt

themes = [
    "Domestic Confinement\n& Patriarchal Control",
    "The Medical Gaze\n& The Rest Cure",
    "Repression of Female\nArtistic Expression",
    "The Creeping Double\n(Subversive Mirror)",
    "Psychosis as\nRadical Liberation"
]
scores = [9.5, 9.0, 8.5, 8.0, 7.5]
colors = ["#2b5c8f", "#1f78b4", "#33a02c", "#e31a1c", "#ff7f00"]

plt.figure(figsize=(10, 5.5))
bars = plt.barh(themes, scores, color=colors, edgecolor="black", height=0.55)

plt.xlabel("Thematic Intensity Score (Out of 10)", fontsize=11, fontweight="bold")
plt.title("Synthetic Reading: Thematic Salience in 'The Yellow Wallpaper'", fontsize=13, weight="bold", pad=15)
plt.xlim(0, 10.5)

for bar in bars:
    w = bar.get_width()
    plt.text(w + 0.15, bar.get_y() + bar.get_height() / 2, f"{w:.1f}", va="center", weight="bold", fontsize=10)

plt.gca().invert_yaxis()
plt.grid(axis="x", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("thematic_visualisation.png", dpi=300)
plt.show()
