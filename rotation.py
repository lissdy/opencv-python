# -*- coding: utf-8 -*-
# 旋转
import cv2
import numpy as np
img=cv2.imread('demo.jpg',0)

rows,cols = img.shape
# cv2.getRotationMatrix2D()用于构建旋转矩阵
# 参数一：旋转中心
# 参数二：旋转角度
# 参数三：缩放因子
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
# 参数三是输出图像的尺寸
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('dst',dst)
cv2.waitKey(0)
