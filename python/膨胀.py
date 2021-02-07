import cv2
import numpy as np
o=cv2.imread("D://opencv//c.png")
k=np.ones((9,9),np.uint8)
d=cv2.dilate(o,k)
cv2.imshow("o",o)
cv2.imshow("k",d)
cv2.waitKey()
cv2.destroyAllWindows() 