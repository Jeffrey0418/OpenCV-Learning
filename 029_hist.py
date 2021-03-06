import cv2
import matplotlib.pyplot as plt
import numpy as np

# 单通道直方图
# img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
# plt.hist(img.ravel(), 256, [0, 256])
# plt.show()

# 三通道直方图
# img = cv2.imread('lena.jpg')
# color = ('b', 'g', 'r')
#
# for i, col in enumerate(color):
#     histr = cv2.calcHist([img], [i], None, [256], [0, 256])
#     plt.plot(histr, color=col)
#     plt.xlim([0, 256])
# plt.show()

# 使用掩膜
img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

mask = np.zeros(img.shape[:2], np.uint8)
mask[100: 400, 100: 400] = 255
masked_img = cv2.bitwise_and(img, img, mask=mask)

hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_mask = cv2.calcHist([img], [0], mask, [256], [0, 256])

plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0, 256])

plt.show()
