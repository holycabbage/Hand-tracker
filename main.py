import cv2
import mediapipe as mp

carmera = cv2.VideoCapture(0)
hand_Detector = mp.solutions.hands.Hands()

while True:
    success, img = carmera.read()
    img = cv2.flip(img, 1)
    if success:
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hand_Detector.process(img)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(img, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

        cv2.imshow("Hand Tracking", img)

    quit = cv2.waitKey(1)

    if quit == ord('q'):
        break

carmera.release()
cv2.destroyAllWindows()