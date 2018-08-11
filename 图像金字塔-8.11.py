#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 10:52:45 2018

@author: zero
"""

'''原理
一般情况下，我们要处理的是一副具有固定分辨率的图像。
但是有些情况下，我们需要对同一图像的不同分辨率的子图像进行处理。
比如：我们要在一幅图像中查找某个目标，比如脸，我们不知道目标在图像中的尺寸大小。
这种情况下，我们需要创建一组图像，这些图像是具有不同分辨率的原始图像。
我们把这组图像叫做图像金字塔（简单来说就是同一图像的不同分辨率的子图集合）。
如果我们把最大的图像放在底部，最小的放在顶部，看起来像一座金字塔，故而得名图像金字塔。
有两类图像金字塔：高斯金字塔和拉普拉斯金字塔。

高斯金字塔(Gaussian pyramid): 用来向下采样
拉普拉斯金字塔(Laplacian pyramid): 用来从金字塔低层图像重建上层未采样图像

高斯金字塔的顶部是通过将底部图像中的连续的行和列去除得到的。
顶部图像中的每个像素值等于下一层图像中5个像素的高斯加权平均值。
这样操作一次一个MxN的图像就变成了一个M/2xN/2的图像。
所以这幅图像的面积就变为原来图像面积的四分之一。这被称为Octave。
连续进行这样的操作我们就会得到一个分辨率不断下降的图像金字塔。
我们可以使用函数cv2.pyrDown()和cv2.pyrUp()构建图像金字塔。
函数cv2.pyrDown（）从一个高分辨率大尺寸的图像向上构建一个金字塔。（尺寸变小，分辨率降低）
'''

import cv2
import numpy as np

'''高斯金字塔

img = cv2.imread('4.png')
lower_reso=cv2.pyrDown(img)
cv2.imshow('lower_reso',lower_reso)

#higher_reso=cv2.pyrUp(img)
#cv2.imshow('higher_reso',higher_reso)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''


'''
拉普拉斯金字塔可以由高斯金字塔计算得来
拉普拉斯金字塔的图像看起来就像边界图，其中很多像素都是0。
他们经常被用在图像压缩中。

'''


'''使用金字塔进行图像融合
无缝连接。
步骤：
1、读入两幅图像，苹果和橘子
2、构建苹果和橘子的高斯金字塔（6层） ----由于程序采用六层金字塔，一次其图片像素的行数和列数要能够被（2X2X2X2X2X2）整除，否则计算过程中像素矩阵对不上就麻烦了
3、根据高斯金字塔计算拉普拉斯金字塔
4、在拉普拉斯的每一层进行图像融合（苹果的左边与橘子的右边融合）
5、根据融合后的图像金字塔重建原始图像。
'''

A=cv2.imread('apple1.jpeg')
B=cv2.imread('orange2.jpeg')

A=cv2.resize(A, (256, 256), interpolation=cv2.INTER_CUBIC)
B=cv2.resize(B, (256, 256), interpolation=cv2.INTER_CUBIC)
#genrate Gaussian pyramid for A 
G= A.copy()
gpA=[G]
for i in xrange(6):
    G=cv2.pyrDown(G)
    gpA.append(G)

#genrate Gaussian pyramid for B
G=B.copy()
gpB=[G]
for i in xrange(6):
    G=cv2.pyrDown(G)
    gpB.append(G)

#genrate Laplacian pyramid for A 
lpA=[gpA[5]]
for i in xrange(5,0,-1):
    GE=cv2.pyrUp(gpA[i])
    L=cv2.subtract(gpA[i-1],GE)
    lpA.append(L)
    
#genrate Laplacian pyramid for B 
lpB=[gpB[5]]
for i in xrange(5,0,-1):
    GE=cv2.pyrUp(gpB[i])
    L=cv2.subtract(gpB[i-1],GE)
    lpB.append(L)

''' Now add left and right halves of images in each level
numpy.hstack(tup)
Take a sequence of arrays and stack them horizontally
to make a single array    
'''
LS=[]
for la,lb in zip(lpA,lpB):
    rows,cols,dpt=la.shape
    ls=np.hstack((la[:,0:cols/2],lb[:,cols/2:]))     #将两个图像的矩阵的左半部分和右半部分拼接到一起
    LS.append(ls)

# now reconstuct    
ls_=LS[0]       #这里LS[0]为高斯金字塔的最小图片
for i in xrange(1,6):       #第一次循环的图像为高斯金字塔的最小图片，依次通过拉普拉斯金字塔恢复到大图像
    ls_=cv2.pyrUp(ls_)
    ls_=cv2.add(ls_,LS[i])      #采用金字塔拼接方法的图像

# image with direct connecting each half
    
real=np.hstack((A[:,:cols/2],B[:,cols/2:]))     #直接的拼接

cv2.imwrite('Pyramid_blending2.jpg',ls_)
cv2.imwrite('Direct_blending.jpg',real )


























