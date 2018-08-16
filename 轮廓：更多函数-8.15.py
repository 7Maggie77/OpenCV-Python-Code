#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 17:39:13 2018

@author: zero
"""


import cv2
import numpy as np
img3=cv2.imread('4.png')
img = cv2.imread('4.png',0)
ret,thresh = cv2.threshold(img,127,255,0)
img,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt=contours[30]

'''凸缺陷
前面我们已经学习了轮廓的凸包，对象上任何凹陷都被成为凸缺陷。
OpenCV中有一个函数cv.convexityDefect（）可以帮助我们找到凸缺陷。



注意：如果要查找凸缺陷，在使用函数cv2.convexHull找凸包时，
参数returnPoints一定要是False。

它会返回一个数组，其中每一行包含的值是[起点，终点，最远的点，到最远的点的近似距离]。
我们可以在一张图上显示它。
我们将起点和终点用一条绿线连接，在最远点画一个圆圈，
要记住的是返回结果的前三个值是轮廓点索引。
所以我们还要到轮廓点中去找它们。

hull=cv2.convexHull(cnt,returnPoints=False)
defects=cv2.convexityDefects(cnt,hull)
# print defects[0,0]
for i in range(defects.shape[0]):
    s,e,f,d=defects[i,0]
    start=tuple(cnt[s][0])
    end=tuple(cnt[e][0])
    far=tuple(cnt[f][0])
    cv2.line(img3,start,end,[0,255,0],2)
    cv2.circle(img3,far,5,[0,0,255],-1)

cv2.imshow('img',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''


'''Point Polygon Test
求解图像中的一个点到一个对象轮廓的最短距离。
如果点在轮廓的外部，返回值为负。
如果在轮廓上，返回值为0。
如果在轮廓内部，返回值为正。
下面以点（50,50）为例：

dist=cv2.pointPolygonTest(cnt,(50,50),True)
print dist

此函数的第三个参数measureDist。
如果设置为True，就会计算最短距离，
如果是False，只会判断这个点与轮廓之间的位置关系（返回值为+1，,1,0）。

如果不需要知道具体距离，建议将第三个参数设为False，
这样速度会提高2到3倍。
'''

'''形状匹配
函数cv2.matchShape（）可以帮我们比较两个形状或轮廓的相似度。
如果返回值越小，匹配越好。
它是根据Hu矩来计算的。

img1=cv2.imread('a.png',0)
img2=cv2.imread('b.png',0)

ret,thresh1=cv2.threshold(img1,127,255,0)
ret,thresh2=cv2.threshold(img2,127,255,0)
image,contours,hierarchy=cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt1=contours[0]
image,contours,hierarchy=cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt2=contours[0]

ret =cv2.matchShapes(cnt1,cnt2,1,0.0)
print ret

Hu矩是归一化中心矩的线性组合，之所以这样做是为了
能够获取代表图像的某个特征的矩函数，
这些矩函数对某些变化如缩放，旋转，镜像映射（除了h1）具有不变性

'''

'''练习
创建一个小程序，可以将图片上的点绘制成不同的颜色,
颜色是根据这个点到轮廓的距离来决定的。
要使用的函数：cv2.pointPolygonTest()
'''

rows,cols=img.shape

def draw_circle(x,y):
    dist=cv2.pointPolygonTest(cnt,(x,y),True)
    if dist>0:
        cv2.circle(img3,(x,y),4,(255,0,0),-1)
    elif dist==0:
        cv2.circle(img3,(x,y),4,(0,255,0),-1)
    else:
        cv2.circle(img3,(x,y),4,(0,0,255),-1)

for i in range(0,cols):
    for j in range(0,rows):
        draw_circle(i,j)

cv2.imshow('img3',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()






















