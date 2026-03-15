def recommend_task(emotion):
    if emotion == "Happy":
        return "Assign analytical or creative tasks."
    
    elif emotion == "Neutral":
        return "Assign routine and collaborative tasks."
    
    elif emotion == "Stressed":
        return "Assign lighter tasks or suggest a short break."
    
    else:
        return "No recommendation available."

from data_processing import load_data, categorize_emotion
from task_recommender import recommend_task

df = load_data()

# Example: first 5 records
for i in range(5):
    mood = df.loc[i, "Mood"]
    
    emotion = categorize_emotion(mood)
    task = recommend_task(emotion)

    print("Mood:", mood)
    print("Emotion:", emotion)
    print("Task:", task)
    print("------")
