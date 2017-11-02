# -*- coding: utf-8 -*-
# numpy 是非常有名的python科学计算工具包
import numpy as np
import cv2
# 创建一张黑色图像
img = np.zeros((512,512,3),np.uint8)
# 以5px绘制一条蓝色直线
# 参数
# img	图像
# pt1	起始坐标
# pt2	终止坐标
# 线条颜色 这里使用蓝色(BRG:255,0,0)
# 笔画宽度
cv2.line(img,(0,0),(512,512),(255,0,0),5)
cv2.imshow('img',img)
cv2.waitKey(0)
