# 开发人：张*梅
# 开发时间：2023/10/25 21:57
"""
1.实现灰度化和二值化
2.实现最邻近插值
3.证明双线性插值中心重合
4.实现双线性插值
"""
# 实现图像灰度化和二值化
import cv2
import numpy as np

img = cv2.imread('../image/01.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('img_gray', img_gray)

# 将灰度图gray_logo转换为二值图(binary_logo) 阈值
_, binary = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('binary', binary)
img_binary = np.where(img_gray > 180, 255, 0)
img_binary = img_binary.astype(np.uint8)
cv2.imshow('img_binary', img_binary)
cv2.waitKey(0)

# 3.证明双线性插值中心重合
# 4.实现双线性插值