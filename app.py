from emotion_analysis import detect_emotion
from task_recommender import recommend_task

text = input("How are you feeling today? : ")

emotion = detect_emotion(text)
task = recommend_task(emotion)

print("Detected Emotion:", emotion)
print("Recommended Task:", task)
