# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:45:31 2021

@author: cristiano
"""

import cv2
import numpy as np
a=cv2.imread("D://opencv//cr72.jpg")
b,g,r=cv2.split(a)
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)
m=cv2.merge([r,b,g])
cv2.imshow("wrong",m)

wrong=cv2.imwrite("D://opencv//w.jpg",m)   
print(wrong)    
cv2.waitKey()
cv2.destroyAllWindows() 