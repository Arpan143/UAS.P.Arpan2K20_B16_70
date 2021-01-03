from cv2 import cv2
import numpy as np
img = cv2.imread('photo.jpg')
cv2.imshow('preveiw',img)

cv2.waitKey(0)

img_resize = cv2.resize(img,None,fx=2 , fy = 2)
cv2.imshow('resized',img_resize)

cv2.waitKey(0)

img_expand = cv2.resize(img,(800,800))
cv2.imshow('expanded',img_expand)

cv2.waitKey(0)
cv2.destroyAllWindows()