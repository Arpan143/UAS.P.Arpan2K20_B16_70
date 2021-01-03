from cv2 import cv2
import numpy as np

img = cv2.imread('photo.jpg')
cv2.imshow('original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

   # Sobel approach
height,width = img.shape[0:2]
print(height,width)
img1 = cv2.imread('photo.jpg',0)
sobel_x = cv2.Sobel(img1,cv2.CV_64F, 1 , 0 ,ksize=5)
sobel_y = cv2.Sobel(img1,cv2.CV_64F, 0 , 1 ,ksize=5)
cv2.imshow('sobel_x',sobel_x)
cv2.imshow('sobel_y',sobel_y)

Added = cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow('added',Added)
cv2.waitKey(0)
cv2.destroyAllWindows()
   # Laplacian approach
lapla = cv2.Laplacian(img1, cv2.CV_64F)
cv2.imshow('lapla',lapla)
cv2.waitKey(0)
cv2.destroyAllWindows()

   # Kenny approach
Kenny = cv2.Canny(img1,10,170)
cv2.imshow('canny', Kenny)
cv2.waitKey()
