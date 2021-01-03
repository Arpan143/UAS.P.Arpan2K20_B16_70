from cv2 import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame1 = cv2.flip(frame , 1)
    cv2.imshow('video',frame1)
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()