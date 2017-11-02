# -*- coding: utf-8 -*-
# 改变图像尺寸
import cv2
import numpy as np
img=cv2.imread('demo.jpg')

# src	输入图像
# dsize	输出图像的尺寸，为空时的计算逻辑是 Size(round(fx*src.cols), round(fy*src.rows)), dsize 和 fx,fy不能同时为0
# fx    x轴的缩放因子，为0时的计算逻辑是(double)dsize.width/src.cols
# fy    y轴的缩放因子，为0时的计算逻辑是(double)dsize.height/src.rows
# interpolation	插值方法
#res = cv2.resize(img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)

#或者直接设置输出图像的尺寸，不设置缩放因子，达到的效果是一样的
height,width=img.shape[:2]
res=cv2.resize(img,(width/2,height/2),interpolation=cv2.INTER_AREA)

cv2.imshow('res',res)
cv2.imshow('img',img)
cv2.waitKey(0)
