#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:12:44 2018

@author: zero
"""

import cv2
import numpy as np

"""图像加法
注意：OpenCV中的加法与Numpy的加法是有所不同的。OpenCV的加法是一种饱和操作，而Numpy的加法是一种模操作
这种差别在对两幅图像进行加法时会更加明显。OpenCV的结果会更好一点。所以尽量使用OpenCV函数。

x=np.uint8([250])
y=np.uint8([10])
print cv2.add(x,y)  # 250 + 10 = 260 ---255
print x+y   # 250 + 10 = 260 % 256 = 4 

"""


"""图像混合
其实也是加法，但是两幅图像的权重不同

img1=cv2.imread('060095.jpg')
img2=cv2.imread('076926.jpg')

dst=cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindow()

"""


"""按位运算（AND，OR，NOT，XOR）
当我们提取图像的一部分，选择非矩形ROI时这些操作会很有用：
我想把OpenCV的标志放到另一幅图像上，如果我使用加法，颜色会改变，如果使用混合，会得到透明效果，但我不想要透明。
如果它是矩形我可以像上一章那样使用ROI，但是它不是矩形。但是我们可以通过下面的按位运算实现：

"""

img1=cv2.imread('1.jpg')
img2=cv2.imread('3.png')

#  I want to put logo on top-left corner, So I create a ROI
rows, cols, channels =img2.shape
roi = img1[0:rows, 0:cols]

#  Now create a mask of logo and create its inverse mask also 
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray,175,255,cv2.THRESH_BINARY)
# src：源图像，可以为8位的灰度图，也可以为32位的彩色图像。（两者有区别，如果采用彩色图像进行计算会得到彩色效果，而不是预期的二值化结果） dst：输出图像 thresh：阈值 maxval：dst图像中最大值 type：阈值类型
mask_inv = cv2.bitwise_not(mask)  # 非操作

# Now black-out the area of logo in ROI
# 取 roi 中与 mask 中不为 0 的值对应的像素的值，其他值为 0
# 注意这里必须有 mask = mask 或者 mask = make_inv， 其中的 mask= 不能忽略
img1_bg = cv2.bitwise_and(roi,roi, mask = mask)
# 取 img2 中与 mask_inv 中不为 0 的值对应的像素的值，其他值为 0 
# Take only region of logo from logo image
img2_fg = cv2.bitwise_and(img2,img2,mask=mask_inv)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()



















