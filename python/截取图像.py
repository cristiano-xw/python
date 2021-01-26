import cv2
import numpy as np
a=cv2.imread("D:/opencv/cr72.jpg")
cv2.imshow("original",a) 
b=np.ones((101,101,3))
b=a[220:400,250:350]
a[0:180,0:100]=b
cv2.imshow("result",a)
cv2.imshow("ok",b) 
cv2.waitKey()
cv2.destroyAllWindows()
