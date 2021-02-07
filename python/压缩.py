import cv2
import numpy as np
o=cv2.imread("D://opencv//ci.jfif")
k=np.ones((8,8),np.uint8) 
e=cv2.erode(o,k)
cv2.imshow("original",o)
cv2.imshow("e",e)
cv2.waitKey()
cv2.destroyAllWindows() 