import cv2
import numpy as np
a=cv2.imread("D://opencv//cr7.jpg",1)
w,h,d=a.shape
mask=np.zeros((w,h),dtype=np.uint8)
mask[100:200,200:400]=255
mask[100:300,100:200]=255
c=cv2.bitwise_and(a,a,mask)  
print("a.shape=",a.shape)
print("mask.shape=",mask.shape)
cv2.imshow("a",a)
cv2.imshow("mask",mask) 
cv2.imshow("c",c)
cv2.waitKey()
cv2.destroyAllWindows()