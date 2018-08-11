#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 10:12:44 2018

@author: zero
"""

'''原理：
1、噪声去除：由于边缘检测很容易受到噪声影响，所以第一步是使用5x5的高斯滤波器去除噪声
2、计算图像梯度：对平滑后的图像使用Sobel算子计算水平方向和竖直方向的一阶导数（图像梯度）
根据得到的这两幅梯度图（Gx和Gy）找到边界的梯度和方向。
梯度的方向一般总是与边界垂直。梯度方向被归为四类：垂直、水平和两个对角线。
3、非极大值抑制：在获得梯度的方向和大小之后，应该对整幅图像做一个扫描，去除那些非边界上的点。
对每一个像素进行检查，看这个点的梯度是不是周围具有相同梯度方向的点中最大的。
4、滞后阈值：现在要确定哪些边界才是真正的边界。这是我们需要设置两个阈值：
minVal和maxVal。当图像的灰度梯度高于maxVal时被认为是真的边界，那些低于minVal的边界会被抛弃。
如果介于两者之间的话，就要看这个点是否与某个被确定为真正的边界点（高于maxVal）相连，
如果是就认为它也是边界点，如果不是就抛弃。

在OpenCV中只需要一个函数：cv2.Canny（），就可以完成以上几步。
'''


import cv2
import numpy as np
from matplotlib import pyplot as plt

img =cv2.imread('4,png')

'''
edge = cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient ]]])
第一个参数是输入图像，第二和第三个分别是minVal和maxVal。
第三个参数设置用来计算图像梯度的Sobel卷积核的大小，默认值为3。
最后一个参数是L2gradient，它可以用来设定求梯度大小的方程。
如果设为True，就会使用我们上面提到过的方程。默认值为False。
'''

cv2.Canny
edges=cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('Original Image'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap='gray')
plt.title('Edge Image'),plt.xticks([]),plt.yticks([])

plt.show()



