"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from recommender import load_songs, recommend_songs


def main() -> None:
    # Construct path relative to this file's location
    csv_path = Path(__file__).parent.parent / "data" / "songs.csv"
    
    songs = load_songs(str(csv_path)) 

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    # Format output with clean layout
    print("\n" + "="*70)
    print(f"🎵 RECOMMENDATIONS FOR: Pop & Happy User (Energy: 0.8)")
    print("="*70 + "\n")
    
    for rank, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        print(f"#{rank} {song['title']:<30} │ Score: {score:>6.1f}/100")
        print(f"    Artist: {song['artist']}")
        print(f"    {explanation}\n")
    
    print("="*70)


if __name__ == "__main__":
    main()
