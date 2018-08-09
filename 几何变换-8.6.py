#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 17:49:02 2018

@author: zero
"""

import cv2
import numpy as np

"""扩展缩放
在缩放时我们推荐使用cv2.INTER_AREA
在扩展时我们推荐使用cv2.INTER_CUBIC(慢)和cv2.INTER_LINEAR
默认情况下所有改变图像尺寸大小的操作使用的插值方法都是cv2.INTER_LINEAR


img=cv2.imread('4.png')
#下面的None本应该是输出图像的尺寸，但是因为后边我们设置了缩放因子
#因此这里为None
res=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

#OR
#这里我们直接设置输出图像的尺寸，所以不用设置缩放因子

height,width=img.shape[:2]
res=cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)

while(1):
    cv2.imshow('res',res)
    cv2.imshow('img',img)
    
    if cv2.waitKey(1) &0xFF==27:
        break
    cv2.destroyAllWindows()

"""


"""平移
函数cv2.warpAffine()的第三个参数是输出图像的大小，
它的格式应该是图像的（宽，高）。
图像的宽对应的是列数，高对应的是行数。

img=cv2.imread('1.jpg')
rows,cols=img.shape[:2]
#use "rows,cols=img.shape" will result in Traceback (most recent call last):File "1.py", line 4, in <module> rows,cols = img.shape ValueError: too many values to unpack

M=np.float32([[1,0,100],[0,1,50]])
dst=cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""


"""Rotate

img = cv2.imread('4.png')
rows,cols=img.shape[:2]

#the first parameter means center, the seconde means angle, and the last is scaling factor
#prevent over the boundary by this
M = cv2.getRotationMatrix2D((cols/2,rows/2),45,0.6)

# the third parameter means the center of the out image
dst=cv2.warpAffine(img,M,(cols,rows))
while (1):
	cv2.imshow('img',dst)
	if cv2.waitKey(1)&0xFF==27:
		break
cv2.destroyAllWindows()

"""


"""Affine Transformation
在仿射变换中，原图中所有的平行线在结果图像中同样平行。
为了创建这个矩阵我们需要从原图像中找到三个点以及他们在输出图像中的位置。
然后cv2.getAffineTransform会创建一个2*3的矩阵，
最后这个矩阵会被传给函数cv2.warpAffine
All parallel lines in the original image are parallel in the resulting image. 
cv2.getAffineTransform will create a 2*3 matrix and post it to cv2.warpAffine
to get this matrix we need to find 3 points in the original image and where they are in the resulting image

from matplotlib import pyplot as plt
img = cv2.imread('4.png')
rows,cols=img.shape[:2]

pts1=np.float32([[50,50],[200,50],[50,200]])
pts2=np.float32([[10,100],[200,50],[100,250]])

M=cv2.getAffineTransform(pts1,pts2)

dst=cv2.warpAffine(img,M,(cols,rows))
#pyplot.subplot() requires subplot(nrows, ncols, plot_number),
# all three options are integers.
#Matplotlib is trying to cast your f and d lists to integer type and failing.
plt.subplot(121)
plt.imshow(img)
plt.title('Input')
plt.subplot(122)
plt.imshow(dst)
plt.title('Output')
plt.show()

"""


"""透视变换
对于视角变换，我们需要一个3*3变换矩阵。
在变换前后，直线还是直线。
需要在输入图像上找4个点，以及他们在输出图像上对应的位置。这四个点中的任意三个都不能共线。
这个变换矩阵可以由函数cv2.getPerspectiveTransform()构建。
然后把这个矩阵传给函数cv2.warpPerspective。
"""
from matplotlib import pyplot as plt
img = cv2.imread('4.png')
rows,cols=img.shape[:2]

pts1=np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2=np.float32([[0,0],[300,0],[0,300],[300,300]])

M=cv2.getPerspectiveTransform(pts1,pts2)

dst=cv2.warpPerspective(img,M,(300,300))

plt.subplot(121)
plt.imshow(img)
plt.title('Input')
plt.subplot(122)
plt.imshow(dst)
plt.title('Output')
plt.show()



















































