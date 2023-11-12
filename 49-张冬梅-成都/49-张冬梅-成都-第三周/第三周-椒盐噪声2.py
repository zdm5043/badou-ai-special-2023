import cv2
import numpy as np

# 加载图像
image = cv2.imread('2.jpg', cv2.IMREAD_COLOR)

# 获取图像的高度和宽度
h, w = image.shape[:2]

# 设置噪声密度，通常在0到1之间
density = 0.5

# 获取随机的噪声像素
row = np.random.randint(0, h, int(h * density))
col = np.random.randint(0, w, int(w * density))

# 将噪声像素设置为0（黑色）或255（白色）
salt = np.random.randint(0, 2, int(len(row)))

# 添加噪声
for i in range(len(row)):
    if salt[i] == 0:
        image[row[i], col[i]]
    else:
        image[row[i], col[i]] = 255

    # image[row[i], col[i]] = [0 if s == 0 else 255 for s in salt]

# 显示噪声图像
cv2.imshow('Salt and Pepper Noise', image)
cv2.waitKey(0)
cv2.destroyAllWindows()