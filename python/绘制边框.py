import cv2
import numpy as np
o=cv2.imread("D://opencv//test//s2.png")
gray=cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
ret,binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours,hierarchy=cv2.findContours(binary,cv2.RETR_LIST, 
                                          cv2.CHAIN_APPROX_SIMPLE)
x,y,w,h=cv2.boundingRect(contours[0])
brcnt=np.array([[[x,y]],[[x+w,y]],[[x+w,y+h]],[[x,y+h]]])
cv2.drawContours(o,[brcnt],-1,(0,22,225),2)

cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows()              