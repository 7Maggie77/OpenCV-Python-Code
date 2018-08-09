import cv2
import numpy as numpy
from matplotlib import pyplot as plt

"""Simple threshold
cv.threshold()的第一个参数是原图像，原图像应该是灰度图。
第二个参数就是用来对像素值进行分类的阈值。
第三个参数就是当像素值高于（有时是小于）阈值时应该被赋予的新的像素值。
OpenCV提供了多种不同的阈值方法，由第四个参数来决定。包括：
cv2.THRESH_BINARY  ----大于阈值的部分像素值变为最大值，其他变为0
cv2.THRESH_BINARY_INV	----大于阈值的部分变为0，其他部分变为最大值
cv2.THRESH_TRUNC	----大于阈值的部分变为阈值，其余部分不变
cv2.THRESH_TOZERO	----大于阈值的部分不变，其余部分变为0
cv2.THRESH_TOZERO_INV	----大于阈值的部分变为0，其余部分不变


img=cv2.imread('4.png',0)
ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles=['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images=[img,thresh1,thresh2,thresh3,thresh4,thresh5]
for i in xrange(6):
	plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])
plt.show()

"""

"""Adaptive threshold
此时的阈值是根据图像上的每一个小区域计算与其对应的阈值。
因此在同一幅图像上的不同区域采用的是不同的阈值
从而使我们能在亮度不同的情况下得到更好的结果。
三个参数：
Adaptive Method
	-cv2.ADPTIVE_THRESH_MEAN_C:阈值取自相邻区域的平均值
	-cv2.ADPTIVE_THRESH_GAUSSIAN_C：阈值取自相邻区域的加权和，权重为一个高斯窗口
Block Size - 邻域大小（用来计算阈值的区域大小）
C - 这就是一个常数，阈值就等于平均值或加权平均值减去这个常数。


img = cv2.imread('8.8.png',0)
#中值滤波
img=cv2.medianBlur(img,5)

ret,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#11 为 Block Size，2为C值
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

titles=['Original Image', 'Global Thresholding(v=127)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images=[img,th1,th2,th3]

for i in xrange(4):
	plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])
plt.show()

"""

"""Otsu's 二值化
对一副双峰图像自动根据其直方图计算出一个阈值（对于非双峰图像，这种方法得到的结果可能会不理想）
这里用到的函数还是cv2.threshold（），但是需要多传入一个参数（flag）：cv2.THRESH_OTSU。
这时若把阈值设为0，算法会找到最优阈值，就是返回值retVal
如果不使用Otsu二值化，返回的retVal值与设定的阈值相等。
	1 设127为全局阈值
	2 直接使用Otsu二值化
	3 首先使用一个5*5的高斯核去除噪声，再使用Otsu二值化
（可看出噪声对结果的影响很大）
"""

img = cv2.imread('8.8-2.png',0)

img=cv2.medianBlur(img,5)

#global thresholding
ret1,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

#Otsu's thresholding
ret2,th2=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#Otsu's thresholding after Gaussian filtering
#(5,5)为高斯核的大小，0为标准差
blur=cv2.GaussianBlur(img,(5,5),0)
#阈值一定要设为0！
ret3,th3=cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#plot all the images and their histograms(柱状图)
images=[img,0,th1,
        img,0,th2,
        blur,0,th3]
titles=['Original Noisy Image','Histogram','Global Thresholding(v=127)',
        'Original Noisy Image','Histogram',"Otsu's Thresholding",
        'Gaussian filtered Image','Histogram',"Otsu's Thresholding"
        ]

这里使用了pyplot中画直方图的方法，plt.hist，要注意的是它的参数是一维数组
所以这里使用了（numpy）ravel方法，将多维数组转换成一维，也可以使用flatten方法
ndarray.flat 1-D iterator over an arry
ndarray.flatten 1-D array copy of the elements of an array in row-major order.


for i in xrange(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]),plt.xticks([]),plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3]),plt.xticks([]),plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]),plt.xticks([]),plt.yticks([])
plt.show()







































































