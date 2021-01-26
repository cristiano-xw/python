# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 21:10:03 2021

@author: cristiano
"""

import cv2
import numpy as np
a=cv2.imread("D://opencv//cr72.jpg")
b=a
add1=a+b
add2=cv2.add(a,b)
cv2.imshow("add1",add1)
cv2.imshow("add2",add2) 
cv2.waitKey()  
cv2.destroyAllWindows()