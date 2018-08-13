#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 11:12:07 2018

@author: zero
"""

'''轮廓可以简单认为成将连续的点（连着边界）连在一起的曲线，具有相同的颜色或灰度。
---为了更加准确，要使用二值化图像。在寻找轮廓之前，要进行阈值化处理或者Canny边界检测。
---查找轮廓的函数会修改原始图像。如果再找到轮廓之后还想使用原始图像的话，
    应该将原始图像存储到其他变量中。
---在OpenCV中，查找轮廓就像在黑色背景中找白色物体。要找的物体应该是白色而背景应该是黑色。

函数cv2.findContours（）有三个参数，第一个是输入图像，第二个是轮廓检索模式，
第三个是（轮廓的）层析结构。轮廓（第二个返回值）是一个Python列表，其中存储这图像中的所有轮廓。
每一个轮廓都是一个Numpy数组，包含对象边界点（x，y）的坐标。
当第三个参数被设置为cv2.CHAIN_APPROX_NONE，所有的边界点都会被存储。
但是我们有时不需要这么多点。例如，当我们找的边界是一条直线时，
我们不需要用直线上所有的点来表示直线，而只需要这条直线的两个端点而已，
这就是cv2.CHAIN_APPROX_SIMPLE要做的，它会将轮廓上的冗余点都去掉，压缩轮廓，从而节省内存开支。



函数cv2.drawContours（）可以被用来绘制轮廓。它可以根据你提供的边界点绘制任何形状。
它的第一个参数是原始图像，第二个参数是轮廓（一个Python列表），
第三个参数是轮廓的索引（在绘制独立轮廓时很有用，当设置为-1时绘制所有轮廓）
接下来的参数是轮廓的颜色和厚度等。

'''


import cv2
import numpy as np

'''在一幅图像上绘制所有的轮廓：

im=cv2.imread('4.png')
imgray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgray,127,255,0)
image,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#img=cv2.drawContours(image,contours,-1,(0,255,0),3)
img=cv2.drawContours(image,contours,3,(0,255,0),3)
cv2.imshow('lower_reso',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''

im=cv2.imread('rectangle.png')
imgray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgray,127,255,0)
image,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#img=cv2.drawContours(image,contours,-1,(0,255,0),3)
img=cv2.drawContours(image,contours,3,(0,255,0),3)
for i in range(0,len(contours)):
    cv2.circle(img,contours[i],1,(0,255,0),1)
    
cv2.imshow('circle',img)
cv2.imshow('lower_reso',img)
cv2.waitKey(0)
cv2.destroyAllWindows()




















