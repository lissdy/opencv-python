# -*- coding: utf-8 -*-
import numpy as np
import cv2

# imread 用来读取图像
# 第二个参数表明如何读取：
# 1. v2.IMREAD_COLOR(>0)：读入一副彩色图像。图像的透明度会被忽略(默认参数)
# 2. cv2.IMREAD_GRAYSCALE(0)：以灰度模式读入图像
# 3. cv2.IMREAD_UNCHANGED(<0)：读入一幅图像，并且包括图像的alpha 通道


img = cv2.imread('demo.jpg',0) # 以灰度模式读取图像
# imshow 用来显示图像
# 第一个参数是窗口名字；第二个是图像
cv2.imshow('img',img)
# waitKey 是键盘绑定函数，传入0时无限期的等待键盘输入
cv2.waitKey(0)
# imwrite 用来保存图像，第一个参数是图像名，第二个是图像
cv2.imwrite('result.jpg',img)
