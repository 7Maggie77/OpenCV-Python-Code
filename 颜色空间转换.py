#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 16:10:06 2018

@author: zero
"""
import cv2
import numpy as np

img = cv2.imread("4.png")

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#HSV空间

lower_blue=np.array([110,100,100])#blue
upper_blue=np.array([130,255,255])

lower_green=np.array([60,100,100])#green
upper_green=np.array([70,255,255])

lower_red=np.array([0,100,100])#red
upper_red=np.array([10,255,255])

red_mask=cv2.inRange(hsv,lower_red,upper_red)#取红色
blue_mask=cv2.inRange(hsv,lower_blue,upper_blue)#蓝色
green_mask=cv2.inRange(hsv,lower_green,upper_green)#绿色

red=cv2.bitwise_and(img,img,mask=red_mask)#对原图像处理
green=cv2.bitwise_and(img,img,mask=green_mask)
blue=cv2.bitwise_and(img,img,mask=blue_mask)

res=green+red+blue

cv2.imshow('img',res)
cv2.waitKey(0)

cv2.destroyAllWindows()
