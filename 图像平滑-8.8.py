#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 15:12:40 2018

@author: zero
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('4.png')

"""2D卷积
OpenCV提供的函数cv.filter2D()可以让我们对一幅图像进行卷积操作。
低通滤波（LPF）
高通滤波（HPF）


kernel=np.ones((5,5),np.float32)/25

dst=cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]),plt.yticks([])
plt.show()

"""

'''平均
由一个归一化卷积框完成。
用卷积框覆盖区域所有像素的平均值来代替中心元素。
可以使用函数cv2.blur（）和cv2.boxFilter（）来完成。
'''

blur=cv2.bilateralFilter(img,9,75,75)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]),plt.yticks([])
plt.show()




'''高斯模糊
把卷积核换成高斯核。
(方框不变，原来每个方框的值是相等的，现在里面的值是符合高斯分布的
方框中心的值最大，其余方框根据距离中心元素的距离递减，构成一个高斯小山包。
原来的求平均数现在变成求加权平均数，权就是方框里的值)
实现的函数是cv2.GaussianBlur（）。
我们需要指定高斯核的宽和高（必须是奇数）。
以及高斯函数沿X，Y方向的标准差。
如果我们只指定了X方向的标准差，Y方向也会取相同值。
如果两个标准差都是0，那么函数会根据核函数的大小自己计算。
高斯滤波可以有效的从图像中去除高斯噪声。

blur=cv2.GaussianBlur(img,(5,5),0)

'''


'''中值模糊

median=cv2.medianBlur(img,5)

'''

'''双边滤波
函数cv2.bilateralFilter()能在保持边界清晰的情况下有效地去除噪声
但是这种操作与其他滤波器相比会比较慢。

blur=cv2.bilateralFilter(img,9,75,75)

'''





















