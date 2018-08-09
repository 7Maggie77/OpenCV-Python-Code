#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 14:26:42 2018

@author: zero
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('2.jpg')

"""get the value of px

px=img[100,100]     
print px
blue=img[100,100,0]     #0 means B & 1 means G & 2 means R
print blue

"""


"""change the value of px

img[100,100]=[255,255,255]
print img[100,100]

"""


"""Numpy是经过优化了的进行快速矩阵运算的软件包，
所以我们不推荐逐个获取像素值并修改，这样会很慢，
能有矩阵运算就不要用循环。

print img.item(10,10,2)
img.itemset((10,10,2),100)
print img.item(10,10,2)

"""


"""
# img.shape 获取图像的形状，他的返回值是一个包含行数、列数、通道数的元组
print img.shape

# img.size 可以返回图像的像素数目： (行数×列数×3=像素数目)
print img.size

# imh.dtype 返回图像数据类型 (unit8?)
print img.dtype

"""


""" 图像ROI 对一幅图像的特定区域进行操作 (截取并复制)

ball = img[280:320,280:320]
img[140:180,140:180]=ball
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows

"""


"""
# 拆分
b=img[:,:,0]
g=img[:,:,1]
r=img[:,:,2]

# 令所有像素的红色通道值都为0
img[:,:,2]=0
print r

"""
#边界填充
BLUE=[255,0,0]

replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)    # 重复最后一个元素（直接用边界的颜色填充， aaaaaa | abcdefg | gggg）
reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)     # 边界元素的镜像 比如：fedcba | abcdef | fedcba
reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT_101)     # 跟上面一致，但稍作改动 例如：gfedcb|abcdefgh|gfedcba
wrap=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)    # 如：cdefgh|abcdefgh|abcdefg
constant = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)      # 添加有颜色的常数值边界，还需要下一个参数（value）

plt.subplot(231),plt.imshow(img,'gray'),plt.title('Original')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('Replicate')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('Reflect')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('Reflect_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('Wrap')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('Constant')

plt.show()




















