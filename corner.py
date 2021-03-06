import cv2
import numpy as np

filename = "/home/copypasta/CST205/handwriting/testSubjects/test1.JPG"
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image
img[dst>0.03*dst.max()]=[124,252,0]

img = cv2.resize(img, (0,0), fx=0.25, fy=0.25)

cv2.imshow('dst',img)
if (cv2.waitKey(0) & 0xff == 27):
    cv2.destroyAllWindows()
