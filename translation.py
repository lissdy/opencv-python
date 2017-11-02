# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('demo.jpg',0)
rows,cols = img.shape # 默认返回行数，列数，通道数
# 构建平移矩阵
M = np.float32([[1,0,100],[0,1,50]])

# 调用warpAffine进行平移
# img 图像
# M 平移矩阵
# (width,height) 输出图像大小
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)
cv2.waitKey(0)
