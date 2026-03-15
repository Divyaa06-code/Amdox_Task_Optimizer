import cv2
from fer import FER

# Start webcam
cap = cv2.VideoCapture(0)

detector = FER()

print("Press Q to quit")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Detect emotions
    result = detector.detect_emotions(frame)

    if result:
        emotion, score = detector.top_emotion(frame)

        if emotion:
            cv2.putText(frame,
                        f"Emotion: {emotion}",
                        (20,40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0,255,0),
                        2)

    cv2.imshow("Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()