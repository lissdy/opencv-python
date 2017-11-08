# -*- coding: utf-8 -*-
# 放射变换
import cv2
import numpy as np
from matplotlib import pyplot as plt


img_bgr = cv2.imread('demo.jpg')
img_rgb = np.zeros(img_bgr.shape, img_bgr.dtype)
img_rgb[:,:,0] = img_bgr[:,:,2]
img_rgb[:,:,1] = img_bgr[:,:,1]
img_rgb[:,:,2] = img_bgr[:,:,0]


rows,cols,ch = img_rgb.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img_rgb,M,(cols,rows))
plt.subplot(121),plt.imshow(img_rgb),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
