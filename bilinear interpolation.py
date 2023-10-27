#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import numpy as np
import cv2
 
'''
python implementation of bilinear interpolation
'''


def bilinear_interpolation(img, out_img_size):
    h, w, cc = img.shape
    h_1, w_1 = out_img_size[1], out_img_size[0]
    print("src_h, src_w = ", h, w)
    print("dst_h, dst_w = ", h_1, w_1)
    if h == h_1 and w == w_1:
        return img.copy()
    out_img = np.zeros((h_1, w_1, 3), dtype=np.uint8)
    scale_x, scale_y = float(w) / w_1, float(h) / h_1
    for i in range(3):
        for out_img_y in range(h_1):
            for out_img_x in range(w_1):
 
                # find the origin x and y coordinates of dst image x and y
                # use geometric center symmetry
                # if use direct way, src_x = dst_x * scale_x
                img_x = (out_img_x + 0.5) * scale_x-0.5
                img_y = (out_img_y + 0.5) * scale_y-0.5
 
                # 预防计算出来的像素点坐标超出了图像范围
                img_x0 = int(np.floor(img_x))
                img_x1 = min(img_x0 + 1, w - 1)
                img_y0 = int(np.floor(img_y))
                img_y1 = min(img_y0 + 1, h - 1)
 
                # calculate the interpolation
                temp0 = (img_x1 - img_x) * img[img_y0, img_x0, i] + (img_x - img_x0) * img[img_y0, img_x1, i]
                temp1 = (img_x1 - img_x) * img[img_y1, img_x0, i] + (img_x - img_x0) * img[img_y1, img_x1, i]
                out_img[out_img_y, out_img_x, i] = int((img_y1 - img_y) * temp1 + (img_y - img_y0) * temp0)
 
    return out_img
 
 
if __name__ == '__main__':
    img = cv2.imread('lenna.png')
    dst = bilinear_interpolation(img, (700, 700))
    cv2.imshow('bilinear interp', dst)
    cv2.waitKey(0)
