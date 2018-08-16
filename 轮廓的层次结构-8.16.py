#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 14:46:52 2018

@author: zero
"""

import cv2 
import numpy as np
img=cv2.imread('4.png',0)
ret,thresh=cv2.threshold(img,127,255,0)

'''层次结构
通常我们使用函数cv2.findContours在图片中查找一个对象。
有时对象可能位于不同的位置。
还有些情况，一个形状在另外一个形状的内部。
这种情况下我们称外部的形状为父，内部的形状为子。
按照这种方式分类，一幅图像中的所有轮廓之间就建立父子关系。
这样我们就可以确定一个轮廓与其他轮廓是怎样连接的，
比如它是不是某个轮廓的子轮廓，或者是父轮廓。
这种关系就称为组织结构。

-----OpenCV中的层次结构
[Next,Previous,First_Child,Parent]
NEXT 表示同一级组织结构中的下一个轮廓（没有为-1）
Previous 表示同一级结构中的前一个轮廓（没有为-1）
First_Child 表示它的第一个子轮廓（按从上往下，从左往右的顺序排序）
Parent 表示它的父轮廓 （如果没有父与子，就为-1）

'''

'''轮廓检索模式
RETR_LIST 从解释的角度来看，这种应是最简单的。
它只是提取所有的轮廓，而不去创建任何父子关系。
换句话说就是“人人平等”，它们属于同一级组织轮廓
image,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

RETR_EXTERNAL 选择这种模式，只会返回最外边的轮廓，
所有的子轮廓都会被忽略掉
image,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

RETR_CCOMP 在这种模式下会返回所有的轮廓并将轮廓分为两级组织结构
例如，一个对象的外轮廓为第1级组织结构。
而对象内部中空洞的轮廓为第2级组织结构，
空洞中的任何对象的轮廓又是第1级组织结构。
空洞的组织结构为第2级。
image,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

RETR_TREE 这种模式下会返回所有轮廓，并创建一个完整的组织结构列表
它甚至会告诉你谁是爷爷，爸爸，儿子，孙子等。
image,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

'''

print hierarchy