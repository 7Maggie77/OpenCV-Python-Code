#!/usr/bin/python
#-*-coding:utf-8-*-

"""
Created on Tue Aug 14 11:35:54 2018

@author: zero
"""

import cv2

import numpy as np

img = cv2.imread('4.png',0)
ret,thresh=cv2.threshold(img,127,255,0)
#findContours函数传入的是一个二值图
image,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
'''矩
图像的矩可以帮助我们计算图像的质心，面积等
函数cv2.moments（）会将计算得到的矩以一个字典的形式返回。

cnt=contours[30]
M=cv2.moments(cnt)
print M

cx=int(M['m10']/M['m00'])
cy=int(M['m01']/M['m00'])

print cx
print cy

'''


'''轮廓面积
可以使用函数cv2.contourArea（）计算得到，也可以使用矩（0阶矩），M['m00']

cnt=contours[30]
area=cv2.contourArea(cnt)
print area
area2= cv2.moments(cnt)['m00']
print area2

'''


'''轮廓周长
也被成为弧长。可以使用函数cv2.arcLength计算得到。
这个函数的第二参数可以用来指定对象的形状是闭合的（True），还是打开的（一条曲线）。

cnt=contours[0]
perimeter=cv2.arcLength(cnt,True)
perimeter2=cv2.arcLength(cnt,False)
print perimeter
print perimeter2

'''


'''轮廓近似(使用Douglas-Peaucker算法：
1、在曲线首尾两点A，B之间连接一条直线AB，该直线为曲线的弦；
2、得到曲线上离该直线段距离最大的点C，计算其与AB的距离d；
3、比较该距离与预先给定的阈值threshold的大小，如果小于threshold，则该直线段作为曲线的近似，该段曲线处理完毕。
4、如果距离大于阈值，则用C将曲线分为两段AC和BC，并分别对两段取信进行1~3的处理。
5、当所有曲线都处理完毕时，依次连接各个分割点形成的折线，即可以作为曲线的近似。
)

将轮廓形状近似到另外一种由更少点组成的轮廓形状，
新轮廓的点的数目由我们设定的准确度来决定。
cv2.approxPolyDP
第二个参数叫epsilon，它是从原始轮廓到近似轮廓的最大距离。
它是一个准确度参数。
选择一个好的epsilon对于得到满意结果非常重要。

length=len(contours)
print length
for i in range(length):
        cnt=contours[i]
        epsilon=0.001*cv2.arcLength(cnt,True)
        approx=cv2.approxPolyDP(cnt,epsilon,True)
       # cv2.drawContours(img,approx,-1,(0,0,255),3) 
       # 代码里使用drawContours只能画出轮廓点，不能连成线.
       
        cv2.polylines(img,[approx],True,(0,0,255),2)
cv2.imshow("approx",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''


'''凸包
凸包与轮廓近似相似，但不同，虽然有些情况下它们给出的结果是一样的
函数cv2.convexHull（）可以用来检测一个曲线是否具有凸性缺陷，并能纠正缺陷。
一般来说，凸性曲线总是凸出来的，至少是平的。
如果有地方凹进去了就被叫做图形缺陷。

hull=cv2.convexHull(points[,hull[,clockwise[,returnPoints]]])
参数：
points:我们要传入的轮廓
hull：输出，通常不需要
clockwise：方向标志。如果设置为True，输出的凸包是顺时针方向的，否则为逆时针方向。
returnPoints默认值为True。它会返回凸包上点的坐标。
如果设置为False，就会返回与凸包点对应的轮廓上的点。

cnt=contours[0]
hull=cv2.convexHull(cnt)
print hull

'''


'''凸性检测
函数cv2.isContourConvex（）可以用来检测一个曲线是不是凸的
它只能返回True或False

cnt=contours[0]
k=cv2.isContourConvex(cnt)
print k

'''


'''边界矩形（两类）
1、直边界矩形  一个直矩形（就是没有旋转的矩形）。它不会考虑对象是否旋转。
所以边界矩形的面积不是最小的。可以使用函数cv2.boundingRect（）查找得到。
（x,y）为矩形左上角的坐标，（w,h）是矩形的宽和高
2、旋转的边界矩形  这个边界矩形是面积最小的，因为它考虑了对象的旋转。
用到的函数为cv2.minAreaRect（）。返回的是一个Box2D结构，
其中包含矩形左上角角点的坐标（x,y），矩形的宽和高（w,h），以及旋转角度。
但是要绘制这个矩形需要矩形的4个角点，可以通过函数cv2.boxPoints()获得。

cnt=contours[0]
# 用绿色(0, 255, 0)来画出最小的矩形框架
x, y, w, h = cv2.boundingRect(cnt)
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
 
# 用红色表示有旋转角度的矩形框架
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
cv2.imwrite('contours.png', img)

'''


'''最小外接圆
函数cv2.minEnclosingCircle（）可以帮我们找到一个对象的外切圆。
它是所有能够包括对象的圆中面积最小的一个。

cnt=contours[10]
(x,y),radius=cv2.minEnclosingCircle(cnt)
center=(int(x),int(y))
radius=int(radius)
print(center,radius)
cv2.circle(img,center,radius,(0,0,0),2)

cv2.imshow('circle',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''


'''椭圆拟合
使用的函数为cv2.fitEllipse（）
返回值其实就是旋转边界矩形的内切圆。

cnt=contours[30]
ellipse=cv2.fitEllipse(cnt)
img=cv2.ellipse(img,ellipse,(0,255,0),2)
cv2.imshow('ellipse',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''

'''直线拟合
我们可以根据一组点拟合出一条直线，同样我们也可以为图像中的点拟合出一条直线


'''
rows,cols=img.shape[:2]
cnt=contours[10]
[vx,vy,x,y]=cv2.fitLine(cnt,cv2.DIST_L2,0,0.01,0.01)
lefty=int((-x*vy/vx)+y)
righty=int(((cols-x)*vy/vx)+y)
img=cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)
cv2.imshow('line',img)
cv2.waitKey(0)
cv2.destroyAllWindows()














