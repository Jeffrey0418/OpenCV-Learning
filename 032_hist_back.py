import cv2
import numpy as np

roi = cv2.imread('rose_red.png')
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
target = cv2.imread('rose.png')
hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)

# ---------------------------------------------
# Numpy方法
# ---------------------------------------------
#
# M = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
# I = cv2.calcHist([hsvt], [0, 1], None, [180, 256], [0, 180, 0, 256])
#
# R = M / I
# h, s, v = cv2.split(hsvt)
# B = R[h.ravel(), s.ravel()]
# B = np.minimum(B, 1)
# B = B.reshape(hsvt.shape[:2])
#
# disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
# B = cv2.filter2D(B, -1, disc)
# B = np.uint8(B)
# cv2.normalize(B, B, 0, 255, cv2.NORM_MINMAX)
# ret, thresh = cv2.threshold(B, 50, 255, 0)
#
# cv2.imshow('res', thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ---------------------------------------------
# OpenCV方法
# ---------------------------------------------
roihist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

cv2.normalize(roihist, roihist, 0, 255, cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt], [0, 1], roihist, [0, 180, 0, 256], 1)

disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
dst = cv2.filter2D(dst, -1, disc)

ret, thresh = cv2.threshold(dst, 50, 255, 0)
thresh = cv2.merge((thresh, thresh, thresh))
res = cv2.bitwise_and(target, thresh)

res = np.hstack((target, thresh, res))
cv2.imwrite('rose_res.jpg', res)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
