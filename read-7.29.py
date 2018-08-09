#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 09:56:02 2018

@author: zero
"""

#matplotlib显示彩色图像
import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('1.jpg')
#b,g,r=cv2.split(img)
img2=img[:,:,::-1]
plt.subplot(121);plt.imshow(img)
plt.subplot(122);plt.imshow(img2)
plt.show()

cv2.imshow('bgr image',img)
cv2.imshow('rgb image',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()




#读取视频
import numpy as np
import cv2

cap = cv2.VideoCapture('tree.avi')

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        cv2.imshow('frame',gray)
    else:
        break  
    
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
