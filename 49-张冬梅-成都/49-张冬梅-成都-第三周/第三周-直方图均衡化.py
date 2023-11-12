import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读取图像
image = cv2.imread('2.jpg', cv2.IMREAD_GRAYSCALE)  # 使用灰度模式读取图像，因为直方图均衡化通常在灰度图像上执行

# 执行直方图均衡化
equ = cv2.equalizeHist(image)  # OpenCV 3.x
# equ = cv2.equalizeHist(image, mask=None)  # OpenCV 4.x

# 显示原始图像和均衡化后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equ)

# 直方图
hist = cv2.calcHist([equ],[0],None,[256],[0,256])

plt.figure()
plt.hist(equ.ravel(), 256)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()