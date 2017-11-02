# -*- coding: utf-8 -*-
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('demo.jpg',0) # 以灰度模式读取图像
plt.imshow(img, cmap='gray',interpolation='bicubic')
plt.show()
