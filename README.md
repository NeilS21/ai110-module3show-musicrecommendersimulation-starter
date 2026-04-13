# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

The system will use a hybrid approach for content and collaborative filtering

Real world music recommenders (like Spotify) use two main strategies: content based filtering (matchtes audio features) and collaborative filtering (matches from what similar users enjoyed). This system combines both in a simplified way. 

**Song Features:** Each song has categorical attributes (genre, mood) and audio characteristics (energy level, acousticness, etc.) that describe its sound and vibe.

**User Profile:** We want to capture a user's taste preferences as: favorite genre, favorite mood, target energy level, and whether they prefer acoustic vs. electronic instruments.

**Scoring Algorithm:** For each song, we calculate a compatibility score (0-100 points) by weighing:
- **Genre match** (40 pts): Prioritizes songs in their favorite genre
- **Mood alignment** (30 pts): Ensures emotional fit (happy, chill, etc)
- **Energy proximity** (20 pts): Tracks songs close to their preferred intensity level
- **Acoustic preference** (10 pts): Matches instrumentation style

**Collaborative Boost:** If a user has liked songs before, we add a secondary signal that boosts songs similar to those previous favorites—encouraging discovery of related music.

**Recommendations:** We score all songs, sort them by score (highest first), and return the top 5. This prioritizes accuracy and explainability over complex matrix math.

### Algorithm Recipe

```
For each song:
  Genre match:     +40 if exact match, else 0
  Mood match:      +30 if exact match, else 0
  Energy:          20 × (1 - |song.energy - user.energy|)
  Acoustic match:  +10 if match, else 0
  
  Content Score = sum above (0-100)
  Boost Score = similarity to liked_songs × 20 (0-20)
  Final Score = 0.8 × Content + 0.2 × Boost
```

### Known Biases

- **Genre dominance**: System strongly prefers favorite genre, may miss good songs in other genres
- **Binary moods**: No partial credit (happy ≠ relaxed, even though similar)
- **Cold start**: New users get generic recommendations until they like songs
- **Small catalog**: Only 10 songs limits diversity

### CLI Output Example

Running `python src/main.py` produces:

```
✓ Loaded 18 songs from data/songs.csv

======================================================================
🎵 RECOMMENDATIONS FOR: Pop & Happy User (Energy: 0.8)
======================================================================

#1 Sunrise City                   │ Score:   99.6/100
    Artist: Neon Echo
    99.6/100 - genre match (+40), mood match (+30), energy proximity (+19.6), acoustic preference (+10)

#2 Gym Hero                       │ Score:   67.4/100
    Artist: Max Pulse
    67.4/100 - genre match (+40), energy proximity (+17.4), acoustic preference (+10)

#3 Rooftop Lights                 │ Score:   59.2/100
    Artist: Indigo Parade
    59.2/100 - mood match (+30), energy proximity (+19.2), acoustic preference (+10)

#4 Night Drive Loop               │ Score:   29.0/100
    Artist: Neon Echo
    29.0/100 - energy proximity (+19.0), acoustic preference (+10)

#5 Neon Pulse                     │ Score:   28.4/100
    Artist: SynthWave Masters
    28.4/100 - energy proximity (+18.4), acoustic preference (+10)

======================================================================
```

**Verification**: Top result (Sunrise City) is correct! It's the only song with both pop genre AND happy mood that matches the user's energy and acoustic preferences.

---


## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

