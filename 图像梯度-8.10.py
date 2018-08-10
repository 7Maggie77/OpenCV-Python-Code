#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 09:22:13 2018

@author: zero
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('4.png',0)


'''梯度简单来说就是求导。
OPenCV提供了三种不同的梯度滤波器，或者说高通滤波器：Sobel，Scharr和Laplacian。
前两个是求一阶或二阶导数，Scharr是对Sobel的优化。
Laplacian是求二阶导数。

#cv2.CV_64F 输出图像的深度（数据类型），可以使用-1，与原图像保持一致 np.unit8
laplacian = cv2. Laplacian(img,cv2.CV_64F)
#参数 1，0 为只在x方向求一阶导数， 最大可以求2阶导数。
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
#参数 0,1 为只在y方向求一阶导数，最大可以求2阶导数。
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

plt.subplot(2,2,1),plt.imshow(img,cmap='gray')
plt.title('Original'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap='gray')
plt.title('Laplacian'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap='gray')
plt.title('Sobel X'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap='gray')
plt.title('Sobel Y'),plt.xticks([]),plt.yticks([])
plt.show()

'''

'''我们可以通过参数-1来设定输出图像的深度（数据类型）与原图像保持一致，
但是我们在代码中使用的确是cv2.CV_64F。
因为一个从黑到白的边界的导数是正数，而一个从白到黑的边界点导数却是负数。
如果原图像的深度是np.int8时，所有的负值都会被截断变成0，
换句话说就是会把边界丢失掉。
所以如果这两种边界都想检测到，最好的办法就是将输出的数据类型设置得更高，
比如cv2.CV_16S,cv2.CV_64F等。
取绝对值后再把它转回到cv2.CV_8U。
'''

#Output dtype =cv2.CV_8U
sobelx8u=cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)
#也可以将参数设为-1
#sobelx8u=cv2.Sobel(img,-1,1,0,ksize=5)

#Output dtype=cv2.CV_64F. THen take its absolute and convert to cv2.CV_8U
sobelx64f=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sobel64f=np.absolute(sobelx64f)
sobel_8u=np.uint8(abs_sobel64f)

plt.subplot(1,3,1),plt.imshow(img,cmap='gray')
plt.title('Original'),plt.xticks([]),plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap='gray')
plt.title('Sobel CV_8U'),plt.xticks([]),plt.yticks([])
plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap='gray')
plt.title('Sobel abs(CV_64F)'),plt.xticks([]),plt.yticks([])
plt.show()
























































