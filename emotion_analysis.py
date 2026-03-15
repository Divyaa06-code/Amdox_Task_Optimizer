from textblob import TextBlob

def detect_emotion(text):
    analysis = TextBlob(text)
    score = analysis.sentiment.polarity

    if score > 0.2:
        return "Happy"
    elif score < -0.2:
        return "Stressed"
    else:
        return "Neutral"
