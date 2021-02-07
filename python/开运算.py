import cv2
import numpy as np
o=cv2.imread("D://opencv//j.png")
k=np.ones((10,10),np.uint8)
r=cv2.morphologyEx(o,cv2.MORPH_OPEN,k)
cv2.imshow("o",o)
cv2.imshow("r",r)
cv2.waitKey()
cv2.destroyAllWindows() 