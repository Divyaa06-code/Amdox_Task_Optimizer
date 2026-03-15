import pandas as pd

def load_data():
    df = pd.read_csv("data/mental_health_journal_dataset.csv")
    return df

def categorize_emotion(mood):
    mood = mood.lower()

    if mood in ["happy", "content", "calm"]:
        return "Happy"
    elif mood in ["tired", "stressed", "anxious"]:
        return "Stressed"
    else:
        return "Neutral"
