from cv2 import cv2
import numpy as np

img = cv2.imread('photo.jpg')
cv2.imshow('original', img)
cv2.waitKey(0)

blur = cv2.blur(img, (9,9))
cv2.imshow('blur',blur)
cv2.waitKey(0)

gaussianblur = cv2.GaussianBlur(img, (9,9) , 0)
cv2.imshow('gblur',gaussianblur)
cv2.waitKey(0)

median = cv2.medianBlur(img,5)
cv2.imshow('mblur', median)
cv2.waitKey(0)

bilateral = cv2.bilateralFilter(img, 9 , 75 , 75)
cv2.imshow('Bblur', bilateral)
cv2.waitKey()