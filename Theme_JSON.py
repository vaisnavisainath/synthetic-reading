"""
======================================================================
Topic: Synthetic Reading - Thematic Extraction
======================================================================
Author Name(s): Vaisnavi Sainath
Short Description: Thematic extraction and intensity analysis from 
Charlotte Perkins Gilman's 'The Yellow Wallpaper' using AnythingLLM 
and LM Studio.
Semester: Monsoon Semester 2026
Affiliation: Humanities and Social Science, IIT(ISM) Dhanbad
======================================================================
"""

theme_extraction = {
    "text": "The Yellow Wallpaper",
    "themes": {
        "Domestic Confinement & Patriarchal Control": {
            "intensity": 9.5,
            "analysis": "The narrative’s core revolves around the narrator's confinement within the nursery – a space initially intended for rest but ultimately becomes a prison of her husband John’s control. The description of the house itself – ‘three miles from the village,’ ‘separate little houses’ - reinforces the isolation and lack of agency she experiences. John’s constant supervision, meticulous scheduling, and dismissal of her desires highlight the patriarchal structures dictating her life and intellectual pursuits. Phrases like 'he takes all care from me,' and his repeated attempts to silence her creativity underscore this theme.",
            "evidence": [
                "I am sitting by the Window in this Atrocious Nursery",
                "John laughs at me, of course, but one expects that in marriage.",
                "He said there was only one window and not room for two beds, and no near room for him if he took another."
            ]
        },
        "The Medical Gaze & The Rest Cure": {
            "intensity": 9.0,
            "analysis": "Gilman masterfully critiques the ‘rest cure’ – a prevalent medical practice at the time – through the narrator's experience. John embodies the detached and dismissive physician, applying a standardized treatment without considering her individual needs or psychological state. The narrative exposes the inherent power imbalance within this doctor-patient relationship and how it can actively harm rather than heal. The phrase ‘a slight hysterical tendency’ serves as a diagnostic label used to pathologize female emotional expression.",
            "evidence": [
                "If a physician of high standing, and one's own husband, assures friends and relatives that there is really nothing the matter with one but temporary nervous depression - a slight hysterical tendency - what is one to do?",
                "Your exercise depends on your strength, my dear",
                "You see he does not believe I am sick!"
            ]
        },
        "Repression of Female Artistic Expression": {
            "intensity": 8.5,
            "analysis": "The narrator's suppressed desire to write is central to the story’s dramatic tension and thematic resonance. John actively discourages her creative pursuits, viewing them as detrimental to her ‘recovery.’ This represents a broader societal denial of women’s intellectual capabilities and artistic agency during the late 19th century. The act of secretly writing becomes an act of rebellion against this imposed silence.",
            "evidence": [
                "Personally, I disagree with their ideas… Personally, I believe that congenial work, with excitement and change, would do me good.",
                "I did write for a while in spite of them; but it does exhaust me a good deal - having to be so sly about it, or else meet with heavy opposition.",
                "But John says if I feel so, I shall neglect proper self-control; so I take pains to control myself - before him, at least, and that makes me very tired."
            ]
        },
        "The Creeping Double (Subversive Mirror)": {
            "intensity": 8.0,
            "analysis": "The recurring motif of the pattern ‘creeping’ and the narrator's obsession with it can be interpreted as a representation of her own subconscious – a hidden self that is both disturbing and strangely compelling. The 'woman behind the wallpaper’ serves as a mirror reflecting the narrator’s trapped state, embodying her repressed desires and anxieties. This duality reflects the societal pressure for women to conform to idealized roles while simultaneously harboring complex inner lives.",
            "evidence": [
                "It is like a woman stooping down and creeping about behind that pattern.",
                "There is one marked peculiarity about this paper, a thing nobody seems to notice but myself, and that is that it changes as the light changes.",
                "I don't like to look out of the windows even - there are so many of those creeping women, and they creep so fast."
            ]
        },
        "Psychosis as Radical Liberation": {
            "intensity": 7.5,
            "analysis": "As the narrator descends into a state of psychological distress, her perception of reality begins to warp, ultimately leading to a kind of liberation from John’s control and societal expectations. Her fixation on the wallpaper becomes a way of asserting agency within a system designed to suppress female autonomy. The blurring of boundaries between reality and delusion suggests that madness can be a form of rebellion against oppressive norms.",
            "evidence": [
                "'I've got out at last,' said I, 'in spite of you and Jane! And I've pulled off most of the paper, so you can't put me back!'",
                "Now why should that man have fainted? But he did, and right across my path by the wall, so that I had to creep over him every time!",
                "I pulled and she shook, I shook and she pulled, and before morning we had peeled off yards of that paper."
            ]
        }
    },
    "methodology_note": "This analysis draws upon feminist standpoint epistemology, emphasizing the importance of understanding narratives from marginalized perspectives (in this case, a woman’s experience within patriarchal structures). The ‘medical gaze’ is examined through the lens of power imbalances and the potential for medical practices to reinforce social inequalities. Intensity scores are subjective estimations reflecting the cumulative impact of thematic elements across the narrative."
}

if __name__ == "__main__":
    print(f"Extraction summary for: {theme_extraction['text']}\n" + "="*50)
    for theme, details in theme_extraction["themes"].items():
        print(f"Theme: {theme:<42} | Intensity: {details['intensity']}/10")
