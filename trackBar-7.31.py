#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 16:03:43 2018

@author: zero
"""

import cv2
import numpy as np

# 当鼠标按下时变为 True
drawing =False
# 如果 mode 为 true 绘制矩形。按下‘m’ 变成绘制曲线
mode=True
ix,iy=-1,-1

# 创建回调函数
def draw_circle(event,x,y,flags,param):
    r=cv2.getTrackbarPos('R','image')
    g=cv2.getTrackbarPos('G','image')
    b=cv2.getTrackbarPos('B','image')
    
    global ix,iy,drawing,mode
# 当按下左键时返回初始位置坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy=x,y
# 当鼠标左键按下并移动时绘制图形。event 可以查看移动， flag 查看是否按下
    elif event==cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(b,g,r),-1)
            else:
                #绘制圆圈，小圆点连在一起就成了线，3代表笔画的粗细
                cv2.circle(img,(x,y),3,(b,g,r),-1)
# 当鼠标松开时停止作画
    elif event == cv2.EVENT_LBUTTONUP:
        drawing == False
        if mode==True:
            cv2.rectangle(img,(ix,iy),(x,y),(b,g,r),-1)
        else:
            cv2.circle(img,(x,y),5,(b,g,r),-1)   
            
def nothing(x):
    pass

#创建一副黑色图像
img =np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
"""
switch ='0:OFF\n1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)
"""
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break
    elif cv2.waitKey(1)&0xFF==ord('m'):
        mode = not mode
    
    
    """s=cv2.getTrackbarPos(switch,'image')
   
    if s==0:
       img[:]=0
    else:
       img[:]=[b,g,r]
    """   
cv2.destroyAllWindows()     
