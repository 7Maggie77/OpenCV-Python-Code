#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 15:10:47 2018

@author: zero
"""

import cv2
import numpy as np

img=cv2.imread('4.png',0)
kernel=np.ones((5,5),np.uint8)


'''腐蚀

erosion=cv2.erode(img,kernel,iterations=1)
cv2.imshow('erosion',erosion)


'''


'''膨胀
与腐蚀相反，与卷积核对应的原图像的像素值中只要有一个是1,
中心元素的像素值就是1。

dilation=cv2.dilate(img,kernel,iterations=1)
cv2.imshow('dilation',dilation)

'''


'''开运算（去除噪声）
先腐蚀后膨胀

opening =cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel) #morphology 形态学
cv2.imshow('opening',opening)

'''


'''闭运算（填补前景中的小洞，或者前景物体上的小黑点）
先膨胀再腐蚀

closing =cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
cv2.imshow('closing',closing)

'''


'''形态学梯度
其实就是一幅图像膨胀与腐蚀的差别。
结果看上去就像前景物体的轮廓。

gradient =cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
cv2.imshow('gradient',gradient)

'''


'''礼帽
原始图像与进行开运算之后得到的图像的差。
'''
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
cv2.imshow('tophat',tophat)

'''黑帽
进行闭运算之后得到的图像与原始图像的差。

blackhat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
cv2.imshow('blackhat',blackhat)

'''

cv2.waitKey(0)
cv2.destroyAllWindows()


'''结构化元素
在前面的例子中我们使用Numpy构建了结构化元素，它是正方形的。
但有时我们需要构建一个椭圆形/圆形的核。为了实现这种要求，提供了OpenCV函数cv2.getStructuringElement（）。
你只需要告诉他你需要的核的形状和大小。

cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

'''

































