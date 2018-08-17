#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 09:54:33 2018

@author: zero
"""

import cv2
import numpy as np
img=cv2.imread('1.jpg',0)
'''
直方图的x轴是灰度值（0到255），
y轴是图片中具有同一个灰度值的点的数目。
直方图其实就是对图像的另一种解释。
通过直方图我们可以对图像的对比度、亮度、灰度分布有一个直观的认识。

直方图是根据灰度图像绘制的，而不是彩色图像。

术语：
BINS：如果不需要知道每一个像素值得像素点数目，
而只希望知道两个像素值之间的像素点数目，
只需要把原来的256个值等分成若干小组，取每组的总和。
在OpenCV的文档中用histSize表示BINS

DIMS：表示我们收集数据的参数数目。
在本例中，我们对收集到的数据只考虑一件事：灰度值
所以这里就是1。

RANGE：要统计的灰度值范围，一般来说为[0,256]，也就是所有的灰度值

'''


'''使用OpenCV统计直方图

函数cv2.calcHist可以帮助我们统计一幅图像的直方图。
cv2.calcHist（images，channels，mask，histSize，ranges[，hist[，accumulate]])
images:原图像（图像格式为uint8或float32）。当传入函数时应该用中括号[]括起来，例如[img]
channels:同样需要用中括号括起来，他会告诉函数我们要统计哪幅图像的直方图。
如果输入图像是灰度图，它的值就是[0];
如果是彩色图像的话，传入的参数可以是[0],[1],[2],他们分别对应着通道B，G，R
mask：掩膜图像。要统计整幅图像的直方图就把它设为None。 ----只有mask没有中括号
但是如果你想统计图像某一部分的直方图的话，就需要制作一个掩膜图像并用到它。
histSize：BIN的数目。也应该用中括号括起来，例如：[256]
ranges:像素值范围，通常为[0.256]

hist=cv2.calcHist([img],[0],None,[256],[0,256])
# hist 是一个 256x1 的数组，每一个值代表了与此灰度值对应的像素点数目。

'''


'''使用Numpy统计直方图(OpenCV的函数要比np.histgram（）快40倍)

# img.ravel() 将图像转成一位数组，这里没有中括号
hist,bins=np.histogram(img.ravel(),256,[0,256])

'''


'''绘制是直方图
1、short way（简单方法）：使用Matplotlib中的绘图函数。

from matplotlib import pyplot as plt
plt.hist(img.ravel(),256,[0,256])
plt.show()

2、long way（复杂方法）：使用OpenCV绘图函数

'''

'''只使用matplotlib的绘图功能。
这在同时绘制多通道（BGR）的直方图中很有用。

from matplotlib import pyplot as plt

img3=cv2.imread('apple.jpeg')
color=('b','g','r')

#对一个列表或数组既要遍历索引又要遍历元素时
#使用内置 enumerrate 函数会更加直接，优美的做法
#enumerate 会将数组或列表组成一个索引序列
#使我们再获取索引和索引内容的时候更加方便

for i,col in enumerate(color):
    histr=cv2.calcHist([img3],[i],None,[256],[0,256])
    plt.plot(histr,color=col)
    plt.xlim([0,256])
plt.show()

'''

'''使用掩膜
要统计图像某个局部区域的直方图只需要构建一副掩膜图像。
将要统计的部分设置成白色，其余部分为黑色，就构成了一副掩膜图像。
然后把这个掩膜图像传给函数就可以了。

'''
from matplotlib import pyplot as plt
mask =np.zeros(img.shape[:2],np.uint8)
mask[100:300,100:400]=255
masked_img=cv2.bitwise_and(img,img,mask=mask)

hist_full=cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask=cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221),plt.imshow(img,'gray')
plt.subplot(222),plt.imshow(mask,'gray')
plt.subplot(223),plt.imshow(masked_img,'gray')
plt.subplot(224),plt.plot(hist_full),plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()































