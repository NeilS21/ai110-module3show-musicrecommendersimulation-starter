from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv
import os

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Score all songs and return top k recommendations."""
        # Score all songs
        scored_songs = []
        for song in self.songs:
            score, reasons = score_song(user, song)
            scored_songs.append((song, score, reasons))
        
        # Sort by score (highest first)
        scored_songs.sort(key=lambda x: x[1], reverse=True)
        
        # Return top k songs
        return [song for song, score, reasons in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Generate a human-readable explanation for why a song was recommended."""
        # Get score and reasons
        score, reasons = score_song(user, song)
        
        # Format explanation
        if reasons:
            return f"{score:.1f}/100 - Because: {', '.join(reasons)}"
        else:
            return f"{score:.1f}/100 - Limited match"

def score_song(user: UserProfile, song: Song) -> Tuple[float, List[str]]:
    """Score a song (0-100) based on genre, mood, energy, and acoustic preferences."""
    reasons = []
    score = 0.0
    
    # Genre match (40 points)
    if song.genre == user.favorite_genre:
        score += 40
        reasons.append(f"genre match (+40)")
    
    # Mood match (30 points)
    if song.mood == user.favorite_mood:
        score += 30
        reasons.append(f"mood match (+30)")
    
    # Energy proximity (0-20 points)
    energy_distance = abs(song.energy - user.target_energy)
    energy_score = max(0, 20 * (1 - energy_distance))
    score += energy_score
    if energy_score > 0:
        reasons.append(f"energy proximity (+{energy_score:.1f})")
    
    # Acoustic preference (10 points)
    song_is_acoustic = song.acousticness > 0.5
    if song_is_acoustic == user.likes_acoustic:
        score += 10
        reasons.append(f"acoustic preference (+10)")
    
    return score, reasons


def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from CSV, converting numeric fields to float/int for calculations."""
    songs = []
    
    try:
        with open(csv_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields from strings to numbers
                row['id'] = int(row['id'])
                row['energy'] = float(row['energy'])
                row['tempo_bpm'] = float(row['tempo_bpm'])
                row['valence'] = float(row['valence'])
                row['danceability'] = float(row['danceability'])
                row['acousticness'] = float(row['acousticness'])
                
                songs.append(row)
        
        print(f"✓ Loaded {len(songs)} songs from {csv_path}")
        return songs
    
    except FileNotFoundError:
        print(f"Error: File not found at {csv_path}")
        return []
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return []


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score and rank songs, returning top k with scores and explanations."""
    # Convert dict preferences to UserProfile object for score_song function
    user = UserProfile(
        favorite_genre=user_prefs.get('genre', 'pop'),
        favorite_mood=user_prefs.get('mood', 'happy'),
        target_energy=float(user_prefs.get('energy', 0.5)),
        likes_acoustic=user_prefs.get('acoustic', False)
    )
    
    # Score all songs using list comprehension (Pythonic approach)
    scored_songs = []
    for song in songs:
        song_obj = Song(**song)  # Convert dict to Song object
        score, reasons = score_song(user, song_obj)
        explanation = ", ".join(reasons) if reasons else "Limited match"
        scored_songs.append((song, score, explanation))
    
    # Sort by score (highest first) using sorted() - doesn't modify original
    ranked_songs = sorted(scored_songs, key=lambda x: x[1], reverse=True)
    
    # Return top k results with formatted explanation
    return [(song, score, f"{score:.1f}/100 - {explanation}") 
            for song, score, explanation in ranked_songs[:k]]

