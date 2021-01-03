from cv2 import cv2
import numpy as np

device = cv2.VideoCapture(0)
while True:
    ret , frame = device.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    range_l = np.array([110,50,50])
    range_u = np.array([130,255,255])
    mask = cv2.inRange(hsv, range_l, range_u)
    cv2.imshow('show', mask)
    cv2.imshow('show1', frame)

    if cv2.waitKey(1) == 13:
        break