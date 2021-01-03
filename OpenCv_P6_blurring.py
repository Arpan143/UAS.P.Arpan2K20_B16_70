from cv2 import cv2
import numpy as np

img = cv2.imread('photo.jpg')
cv2.imshow('original', img)
cv2.waitKey(0)

filter_3x3 = np.ones((3,3) , np.float32)/9
filtered_3x3 = cv2.filter2D(img,-1,filter_3x3)
cv2.imshow('filtered', filtered_3x3)
cv2.waitKey(0)

filter_9x9 = np.ones((9,9) , np.float32)/80
filtered_9x9 = cv2.filter2D(img,-1,filter_9x9)
cv2.imshow('filtered_9', filtered_9x9)
cv2.waitKey(0)

cv2.destroyAllWindows()