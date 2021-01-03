from cv2 import cv2
import numpy as np

img = cv2.imread('photo.jpg')

img1 = cv2.pyrUp(img)
img2 = cv2.pyrDown(img)

cv2.imshow("Down", img1)
cv2.waitKey(0)

cv2.imshow("original", img)
cv2.waitKey(0)

cv2.imshow("up", img2)
cv2.waitKey(0)

cv2.destroyAllWindows()