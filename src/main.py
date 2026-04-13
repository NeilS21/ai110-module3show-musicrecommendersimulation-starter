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
    
    # Define diverse test profiles
    profiles = [
        # Standard profiles
        {"name": "High-Energy Pop", "genre": "pop", "mood": "happy", "energy": 0.9, "acoustic": False},
        {"name": "Chill Lofi", "genre": "lofi", "mood": "happy", "energy": 0.1, "acoustic": True},
        {"name": "Deep Intense Rock", "genre": "rock", "mood": "sad", "energy": 0.9, "acoustic": False},
        # Adversarial/Edge Case profiles
        {"name": "[EDGE] Conflicting Energy-Mood", "genre": "pop", "mood": "sad", "energy": 0.95, "acoustic": False},
        {"name": "[EDGE] Acoustic + Electronic Paradox", "genre": "electronic", "mood": "happy", "energy": 0.8, "acoustic": True},
        {"name": "[EDGE] Minimal Energy", "genre": "ambient", "mood": "peaceful", "energy": 0.05, "acoustic": False},
    ]

    # Run recommender for each profile
    for profile in profiles:
        recommendations = recommend_songs(profile, songs, k=5)
        
        profile_info = f"{profile['name']}"
        if "[EDGE]" in profile['name']:
            print("\n" + "⚠️ " * 20)
        
        print("\n" + "="*70)
        print(f"🎵 RECOMMENDATIONS FOR: {profile_info}")
        print(f"   Genre: {profile['genre']:<15} Mood: {profile['mood']:<12} Energy: {profile['energy']}")
        print("="*70 + "\n")
        
        for rank, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            print(f"#{rank} {song['title']:<30} │ Score: {score:>6.1f}/100")
            print(f"    Artist: {song['artist']}")
            print(f"    {explanation}\n")
    
    print("="*70)


if __name__ == "__main__":
    main()
