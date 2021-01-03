from cv2 import cv2
import numpy as np

def sketch(image):
    img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    img_gray_blur = cv2.medianBlur(img_gray,5)
    
    canny_edge = cv2.Canny(img_gray_blur,10,60)
    
    ret, mask = cv2.threshold(canny_edge,70,255,cv2.THRESH_BINARY)
    
    return mask


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame1 = cv2.flip(frame , 1)
    cv2.imshow('frame',sketch(frame1))
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.DestroyAllWindows()
