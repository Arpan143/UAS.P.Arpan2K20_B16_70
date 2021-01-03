from cv2 import cv2 
import numpy as np

img = cv2.imread('photo.jpg')

cv2.imshow("original",img)
cv2.waitKey(0)

B,G,R = cv2.split(img)

zeros = np.zeros(img.shape[:2] , dtype="uint8")
cv2.imshow("empty", zeros)

cv2.imshow("red", cv2.merge([zeros,zeros,R]))
cv2.waitKey(0)

cv2.imshow("green", cv2.merge([zeros,G,zeros]))
cv2.waitKey(0)

cv2.imshow("blue", cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)

height,width = img.shape[:2]
q_height,q_width = height/4 , width/4
T = np.float32([[1,0,q_height],[0,1,q_width]])
img_r = cv2.warpAffine(img,T,(height,width))
cv2.imshow("Translated", img_r)
cv2.waitKey(0)
cv2.destroyAllWindows()