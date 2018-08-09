#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 10:56:25 2018

@author: zero
"""

import numpy as np
import cv2

def nothing(x):
    pass

img = np.zeros((600,500),np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('weight','image',0,100,nothing)


img0 = cv2.imread('1.jpg')
img1 = cv2.imread('2.jpg')
res=cv2.resize(img0,(600,500),interpolation=cv2.INTER_CUBIC)
res1=cv2.resize(img1,(600,500),interpolation=cv2.INTER_CUBIC)
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) &0xFF
    if k == ord('q'):
        break
    r=cv2.getTrackbarPos('weight','image')
    r=float(r)/100.0
    img=cv2.addWeighted(res,r,res1,1-r,0)

cv2.imwrite('8.4.jpg',img)
cv2.destroyAllWindows()