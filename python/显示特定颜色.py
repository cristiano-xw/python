import cv2
import numpy as np
d=cv2.imread("D://opencv//d.jpg")
hsv=cv2.cvtColor(d,cv2.COLOR_BGR2HSV)
cv2.imshow("d",d)
cv2.imshow("hsv",hsv)     
minBule=np.array([50,100,100])    
maxBule=np.array([70,255,255])
mask = cv2.inRange(hsv,minBule,maxBule)
blue=cv2.bitwise_and(d,d,mask=mask)
cv2.imshow("blue",blue)
cv2.waitKey()
cv2.destroyAllWindows()  
