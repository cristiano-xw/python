import cv2
o=cv2.imread("D://opencv//bb.jpg")
cv2.imshow("original",o)
t=o.copy()
g=cv2.cvtColor(t,cv2.COLOR_BGR2GRAY)
ret,binary=cv2.threshold(g,127,255,cv2.THRESH_BINARY)
contours,hierarchy=cv2.findContours(binary,
                                          cv2.RETR_EXTERNAL,
                                          cv2.CHAIN_APPROX_SIMPLE)
p=cv2.drawContours(g,contours,-1,(255,0,0),5) 
cv2.imshow("t",p)  
cv2.waitKey()
cv2.destroyAllWindows()   

