import streamlit as st
import pandas as pd
from datetime import datetime

import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/mental_health_journal_dataset.csv")

from textblob import TextBlob

# Emotion Detection
def detect_emotion(text):
    score = TextBlob(text).sentiment.polarity

    if score > 0.2:
        return "Happy"
    elif score < -0.2:
        return "Stressed"
    else:
        return "Neutral"

# Task Recommendation
def recommend_task(emotion):
    if emotion == "Happy":
        return "Assign analytical or creative tasks."
    elif emotion == "Neutral":
        return "Assign routine and collaborative tasks."
    elif emotion == "Stressed":
        return "Assign lighter tasks or suggest a short break."

st.title("🧠 Amdox AI-Powered Task Optimizer Dashboard")

# ---- REAL-TIME EMOTION ANALYSIS ----
st.subheader("🧠 Real-Time Mood Analysis")

user_text = st.text_area("How are you feeling today?")

if st.button("Analyze Mood"):

    emotion = detect_emotion(user_text)
    task = recommend_task(emotion)

    st.write("### Detected Emotion:", emotion)
    st.write("### Recommended Task:", task)

    # ---- SAVE NEW ENTRY ----
    new_entry = pd.DataFrame({
        "User_ID": [999],  # dummy ID
        "Date": [datetime.now().strftime("%Y-%m-%d")],
        "Mood": [emotion],
        "Mood_Score": [5 if emotion=="Neutral" else 8 if emotion=="Happy" else 2],
        "Anxiety_Level": [2 if emotion=="Happy" else 5 if emotion=="Neutral" else 8],
        "Trigger": ["Realtime Input"],
        "Coping_Activity": ["None"],
        "Journal_Entry": [user_text]
    })

    # Append to dataset
    new_entry.to_csv(
        "data/mental_health_journal_dataset.csv",
        mode='a',
        header=False,
        index=False
    )

    st.success("New mood entry saved to dataset!")


# ---- Mood Distribution ----
st.subheader("Mood Distribution")

mood_counts = df["Mood"].value_counts()

fig, ax = plt.subplots()
mood_counts.plot(kind="bar", ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# ---- Anxiety Level Analysis ----
st.subheader("Average Anxiety Level by Mood")

anxiety_avg = df.groupby("Mood")["Anxiety_Level"].mean()

fig2, ax2 = plt.subplots()
anxiety_avg.plot(kind="bar", ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)

# ---- Mood Trend Over Time ----
st.subheader("Mood Trend Over Time")

df["Date"] = pd.to_datetime(df["Date"])
daily_mood = df.groupby(df["Date"].dt.date)["Mood_Score"].mean()

fig3, ax3 = plt.subplots()
daily_mood.plot(ax=ax3)
st.pyplot(fig3)

# ---- STRESS ALERTS ----
st.subheader("⚠️ Employees Needing Attention")

stress_alerts = df[
    (df["Anxiety_Level"] > 7) |
    (df["Mood_Score"] < 3)
]

if not stress_alerts.empty:
    st.warning("High stress levels detected!")
    st.dataframe(
        stress_alerts[[
            "User_ID",
            "Date",
            "Mood",
            "Anxiety_Level",
            "Mood_Score"
        ]]
    )
else:
    st.success("No high-stress employees detected.")

st.success("Dashboard Loaded Successfully!")
