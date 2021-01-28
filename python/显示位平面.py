# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 20:41:57 2021

@author: cristiano
"""
  
import cv2
import numpy as np
c7=cv2.imread("D://opencv//c7.jpg",0)
cv2.imshow("c7",c7)
r,c=c7.shape
x=np.zeros((r,c,8),dtype=np.uint8) 
for i in range(8):
    x[:,:,i]=2**i 
r=np.zeros((r,c,8),dtype=np.uint8)  
for i in range(8):
    r[:,:,i]=cv2.bitwise_and(c7,x[:,:,i])
    mask=r[:,:,i]>0
    r[mask]=255 
    cv2.imshow(str(i),r[:,:,i])
cv2.waitKey()  
cv2.destroyAllWindows()