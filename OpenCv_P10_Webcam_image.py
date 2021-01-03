from cv2 import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret , frame = cap.read()
    print(ret)
    print(frame)
else:
    ret = False

img1 = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

cv2.imshow('img',img1)
print(img1.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
#plt.imshow(img1)
