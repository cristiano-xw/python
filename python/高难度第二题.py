# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 21:34:56 2021

@author: cristiano
"""

import cv2
import numpy as np 
opencv=cv2.imread("D://opencv//test//c2.png")
#cv2.imshow("origianl",o) 
#gray=cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
#ret,binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
#contours,hierarchy=cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

hsv=cv2.cvtColor(opencv,cv2.COLOR_BGR2HSV)
minBlue=np.array([5,50,50])
maxBlue=np.array([18,255,255]) 
mask=cv2.inRange(hsv,minBlue,maxBlue)
blue=cv2.bitwise_and(opencv,opencv,mask=mask)
cv2.imshow("o",blue)
img=cv2.cvtColor(blue,cv2.COLOR_HSV2RGB)
img=cv2.cvtColor(img,cv2.COLOR_RGBA2GRAY)
img=cv2.Canny(img,128,200) 
#cv2.imshow("img",img)   

ret,thresh = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
#cv2.imshow("o",thresh) 
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#contours为轮廓集，可以计算轮廓的长度、面积等


for cnt in contours:  
    #if  len(cnt)>100 :
        (x,y),radius=cv2.minEnclosingCircle(cnt)
        center=(int(x),int(y))
        radius=int(radius)
        print("圆心： ",center)
        print("半径: ",radius)   
       # if radius < 50：
        if radius>10:
            cv2.circle(opencv,center,radius,(0,0,0),2)
            cv2.imshow("result",opencv)
        
cv2.waitKey()
cv2.destroyAllWindows() 