# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 11:08:39 2018

@author: murali.nsr
"""

import cv2
import numpy as np
import os

def transform(pos) :
    pts=[]
    n=len(pos)
    for i in range(n):
        pts.append(list(pos[i][0]))
        
    sums={}
    diffs={}
    tl=tr=bl=br=0
    for i in pts:
        x=i[0]
        y=i[1]
        sum=x+y
        diff=y-x
        sums[sum]=i
        diffs[diff]=i
    sums=sorted(sums.items())
    diffs=sorted(diffs.items())
    n=len(sums)
    rect=[sums[0][1],diffs[0][1],diffs[n-1][1],sums[n-1][1]]
    
    h1=np.sqrt((rect[0][0]-rect[2][0])**2 + (rect[0][1]-rect[2][1])**2)     
    h2=np.sqrt((rect[1][0]-rect[3][0])**2 + (rect[1][1]-rect[3][1])**2)     
    h=max(h1,h2)
   
    w1=np.sqrt((rect[0][0]-rect[1][0])**2 + (rect[0][1]-rect[1][1])**2)     
    w2=np.sqrt((rect[2][0]-rect[3][0])**2 + (rect[2][1]-rect[3][1])**2)   
    w=max(w1,w2)
   
    return int(w),int(h),rect

img=cv2.imread('C:/Users/murali.nsr/Downloads/IMG_3084.JPG')
print (img)
r=500.0 / img.shape[1]
dim=(500, int(img.shape[0] * r))
img=cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

cv2.imshow('INPUT',img)
cv2.waitKey(10000)
cv2.destroyAllWindows()

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.GaussianBlur(gray,(11,11),0)
edge=cv2.Canny(gray,100,200)
_,contours,_=cv2.findContours(edge.copy(),1,1)
cv2.drawContours(img,contours,-1,[0,255,0],2)
cv2.imshow('Contours',img)
cv2.waitKey(10000)
cv2.destroyAllWindows()


n=len(contours)
max_area=0
pos=0
for i in contours:
    area=cv2.contourArea(i)
    if area>max_area:
        max_area=area
        pos=i
peri=cv2.arcLength(pos,True)
approx=cv2.approxPolyDP(i,0.02*peri,True)
 
size=img.shape
w,h,arr=transform(approx)
 
pts2=np.float32([[0,0],[w,0],[0,h],[w,h]])
pts1=np.float32(arr)
M=cv2.getPerspectiveTransform(pts1,pts2)
dst=cv2.warpPerspective(img,M,(w,h))
image=cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)
#image=cv2.adaptiveThreshold(image,255,1,0,11,2)
image = cv2.resize(image,(w,h),fx=1, fy=1,interpolation = cv2.INTER_AREA)
cv2.imshow('OUTPUT',image)
cv2.waitKey(10000)
cv2.destroyAllWindows()
