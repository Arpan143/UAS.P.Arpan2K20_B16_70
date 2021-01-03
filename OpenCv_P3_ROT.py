from cv2 import cv2
import numpy as np
img = cv2.imread('photo.jpg')
height , width = img.shape[:2]
print(height,width)
r_matrix = cv2.getRotationMatrix2D((height/2,width/2) , 90 ,.5)
r_image = cv2.warpAffine(img , r_matrix , (height, width))
cv2.imshow('orig', img)
cv2.waitKey(0)
cv2.imshow('rotated', r_image)
cv2.waitKey(0)
# cv2.destroyAllWindows()

#    #Method 2 Using transpose(It doesn't rotate image , it just mirrors the image along x=y) 
from cv2 import cv2 
t_img = cv2.transpose(img)
cv2.imshow('transposed',t_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

