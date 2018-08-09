#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 09:14:20 2018

@author: zero
"""

"""Python 提供了一个叫time的模块，可以用它来测量程序的运行时间。
另外一个叫做profile的模块会帮我们得到一份关于我的程序的详细报告
其中包含了代码中每个函数运行需要的时间，以及每个函数被调用的次数
"""

"""cv2.getTickCount函数返回从参考点到这个函数被执行的时钟数。
所以当你在一个函数执行前后都调用它的话，你就会得到这个函数的执行时间
cv2.getTickFrequency返回时钟频率，或者说每秒钟的时钟数。
所以可以按照下面的方式得到一个函数运行了多少秒。
"""

import cv2
import numpy as np
import time
img1=cv2.imread('1.jpg')

"""Shell
#查看优化是否开启
cv2.useOptimized()

#优化关闭
cv2.setUseOptimized(False)
cv2.useOptimized()


"""

#e1=cv2.getTickCount()
e1=time.time()
# your code execution
for i in xrange(5,49,2):
    img1=cv2.medianBlur(img1,i)

#e2=cv2.getTickCount()
e2=time.time()
time = (e2-e1)/cv2.getTickFrequency()
print time

"""
IPython
shell
%timeit
"""

"""
Python 的标量计算比Numpy的标量计算要快。对于仅包含一两个元素的操作Python标量比Numpy的数组要快
但是当数组稍微大一点时Numpy就会胜出了。
%timeit z= cv2.countNonZero(img)
%timeit z= np.count_nonzero(img)
"""









































