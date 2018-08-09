#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 10:45:19 2018

@author: zero
"""
import numpy as np
import cv2

# Create a black image
img=np.zeros((512,512,3), np.uint8) #RGB,so 8

""" Draw a blue line  start & end
cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.imshow('line',img)
"""

"""Draw a rectangle  top left corner & lower right corner
cv2.rectangle(img,(50,50),(250,250),(0,255,0),-1)
cv2.imshow('rectangle',img)    
""" 

"""Draw a circle  center & radius
cv2.circle(img,(447,63),63,(0,255,0),1)
cv2.imshow('circle',img)
"""

"""Draw a ellipse   center & (a,b) &  anticlockwise angle & C.W.angle(0,360 means all ellipse)
cv2.ellipse(img,(256,256),(100,50),0,0,180,(0,255,0),-1)
cv2.imshow('ellipse',img)
 """

"""Draw a polygon need to give each point to create a matrix, and transform it into int 32
pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts=pts.reshape((-1,1,2))  # 这里reshape的第一个参数为-1,表明这一维的长度是根据后面的维度计算出来的
img=cv2.polylines(img,[pts],True,(0,255,255))
cv2.imshow('polygon',img)
"""

"""Put text on img    words want to put & position & font-family & font-size & line-type
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),cv2.LINE_AA)
cv2.imshow("putText",img)
"""

cv2.waitKey(0)
cv2.destroyAllWindows()
