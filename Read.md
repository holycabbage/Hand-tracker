# Hand Tracker
## Auther: Haosong Zhang
## Date: 21 Sep 2022

This is a hand tracker project for the course of Computer Vision. The project is based on the paper [Real-time Hand Tracking with MediaPipe](https://google.github.io/mediapipe/solutions/hands.html).

Using the MediaPipe package, we can easily get the hand landmarks and the hand gesture. The hand landmarks are 21 points on the hand, and the hand gesture is the classification of the hand. The hand gesture can be used to control the computer.

Using the cv2 package, we can get the video from the camera. Then we can use the MediaPipe to get the hand landmarks and the hand gesture. Finally, we can use the hand landmarks to draw the hand on the video.

