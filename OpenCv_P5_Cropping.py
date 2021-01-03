from cv2 import cv2
import numpy as np

img = cv2.imread('photo.jpg')
cv2.imshow('original',img)
cv2.waitKey(0)
#cv2.destroyAllWindows()

row,col = img.shape[:2]
print(row,col)
row_s = int(row/4)
col_s = int(col/4)
row_e = int(row/2)
col_e = int(col/2)
cv2.imshow('cropped', img[row_s:row,col_s:col])
cv2.waitKey(0)
cv2.destroyAllWindows()