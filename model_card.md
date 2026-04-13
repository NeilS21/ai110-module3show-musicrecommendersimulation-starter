# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

MoodSetter 1.0

---

## 2. Intended Use  

MoodSetter predicts which songs from a small catalog (18 songs) a user will enjoy based on their favorite genre, mood, energy level, and acoustic preference. It's designed for classroom learning about how recommender systems work—not for real users. The system assumes users have a consistent taste profile and want songs matching their stated preferences. It's meant to be transparent and explainable, not powerful.

---

## 3. How the Model Works  

For each song, we calculate a compatibility score (0-100) by looking at four things: Does the genre match? Does the mood match? How close is the energy level? Does the acoustic style match? Each factor is worth points: Genre gets 40, Mood gets 30, Energy proximity gets up to 20 (based on how close the song's energy is to what you want), and Acoustic gets 10. We add up the points and rank songs by score. The top 5 songs are the recommendations. It's simple math, not fancy AI.

---

## 4. Data  

We have 18 songs with 10 audio features each (genre, mood, energy, tempo, valence, etc.). The dataset has 13 genres: pop (5 songs), lofi (3), electronic (3), and 1 each of rock, ambient, jazz, soul, folk, hip-hop, classical, reggae, metal, indie. The dataset is homemade—started with 10 songs and added 8 more to increase variety. Missing from the data: lyrics, popularity, artist history, user listening history. It's a tiny catalog, so you can't really discover variety. Real Spotify has millions of songs; we have 18.

---

## 5. Strengths  

For users who want pop music with happy/energetic vibes, the system works perfectly. Sunrise City gets recommended first and it actually IS the best match for that profile. The algorithm correctly prioritizes genre (the biggest signal), then mood and energy as tie-breakers. It's totally transparent—you can see exactly why each song scored what it did. The scoring formula makes intuitive sense: if you want pop, you get pop. If you want chill, you get low-energy songs. The system is predictable and doesn't surprise you in weird ways.

---

## 6. Limitations and Bias 

The biggest issue is the genre weight. With a 40-point weight out of 100, if you like rock but only one rock song exists in the dataset, you're stuck with that song no matter what. Looking at the data: rock (1 song), ambient (1), jazz (1) vs pop (5 songs). Users who like rare genres can't discover anything else. It also creates an "acoustic divide"—the code checks acousticness > 0.5, which accidentally splits the dataset: all lofi/folk songs are acoustic (0.7+), all pop/rock are electric (0.1-0.2). So an acoustic pop lover would never see recommendations in their preferred combo. The algorithm works correctly but the small dataset + heavy genre weight = users get trapped in filter bubbles.  

---

## 7. Evaluation  

I tested 6 user profiles to see if recommendations made sense:

**Standard Profiles:**
- High-Energy Pop (0.9 energy, happy, pop) → Sunrise City ranked #1 ✓ 
- Chill Lofi (0.1 energy, happy, lofi) → Library Rain ranked #1 ✓
- Deep Intense Rock (0.9 energy, sad, rock) → Storm Runner ranked #1 ✓

**Edge Cases:**
- Conflicting Energy-Mood (0.95 energy + sad mood, pop) → Gym Hero won over mood mismatch
- Acoustic + Electronic Paradox (electronic genre + acoustic preference) → Neon Pulse (electronic) beat Sunrise City
- Minimal Energy (0.05 energy, ambient) → Spacewalk Thoughts won smoothly

**What Surprised Me:** The same songs kept showing up across different profiles—Sunrise City appeared in 4 out of 6 tests. I thought this was a bug, but it turns out it's because there are so few songs in rare genres (only 1 rock, 1 ambient). The algorithm isn't broken; it's just revealing that our dataset is tiny and imbalanced.

---

## 8. Future Work  

**Expand the dataset:** Add 100+ songs so rare genres aren't trapped with 1 option. Right now indie, rock, and ambient fans are stuck. **Reduce genre weight:** Instead of genre being 40 points (40%), make it 25. This would let other features compete more, enabling discovery across genres. **Add diversity mode:** Option to return varied songs instead of always picking the "best" match. Users might want to explore, not just follow their profile. **Use more features:** We have tempo and valence data but don't use it. Adding those could improve recommendations without more songs.

---

## 9. Personal Reflection  

Building this system taught me that recommenders aren't magic—they're just math applied to whatever data you have. The weights (40/30/20/10) seemed reasonable on paper, but when you actually test them against real use cases, you see the cracks. Like, the acoustic divide wasn't a bug; it was just the data being what it was: all acoustic songs happened to be chill, all electric songs happened to be energetic. That's not the algorithm's fault. Also, I learned that diversity in recommendations is basically a data problem, not an algorithm problem. You can't recommend variety when you only have 18 songs. Real Spotify works so well partly because they have millions of songs to pull from. Finally, I realized that when people complain about filter bubbles in real apps, it's not always intentional evil—it's often just how weighted scoring works at scale. You need tons of data AND thoughtful design to break people out of their comfort zones.  
