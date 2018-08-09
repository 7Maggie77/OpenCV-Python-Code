#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 14:15:47 2018

@author: zero
"""

import cv2
import numpy as np
""" print mouse events
----------------------------------------------
events=[i for i in dir(cv2) if 'EVENT' in i]
print events
CV_EVENT_MOUSEMOVE 0             滑动  
CV_EVENT_LBUTTONDOWN 1           左键点击  
CV_EVENT_RBUTTONDOWN 2           右键点击  
CV_EVENT_MBUTTONDOWN 3           中间点击  
CV_EVENT_LBUTTONUP 4             左键释放  
CV_EVENT_RBUTTONUP 5             右键释放  
CV_EVENT_MBUTTONUP 6             中间释放  
CV_EVENT_LBUTTONDBLCLK 7         左键双击  
CV_EVENT_RBUTTONDBLCLK 8         右键双击  
CV_EVENT_MBUTTONDBLCLK 9         中间释放
----------------------------------------------
"""

"""Double click left button to draw a circle
----------------------------------------------
#mouse callback function

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)

#创建图像与窗口并将窗口与回调函数绑定
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27:
        break
cv2.destroyAllWindows()
----------------------------------------------
"""

"""Drag mouse to draw
----------------------------------------------"""
# 当鼠标按下时变为 True
drawing =False
# 如果 mode 为 true 绘制矩形。按下‘m’ 变成绘制曲线
mode=True
ix,iy=-1,-1

# 创建回调函数
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
# 当按下左键时返回初始位置坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy=x,y
# 当鼠标左键按下并移动时绘制图形。event 可以查看移动， flag 查看是否按下
    elif event==cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                #绘制圆圈，小圆点连在一起就成了线，3代表笔画的粗细
                cv2.circle(img,(x,y),3,(0,0,255),-1)
# 当鼠标松开时停止作画
    elif event == cv2.EVENT_LBUTTONUP:
        drawing == False
        if mode==True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)   

#创建图像与窗口并将窗口与回调函数绑定
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(1)&0xFF==27:
        break
    elif cv2.waitKey(1)&0xFF==ord('m'):
        mode = not mode
cv2.destroyAllWindows()




















