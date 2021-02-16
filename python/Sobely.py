import cv2
o=cv2.imread("D://opencv//hei.png")
x=cv2.Sobel(o,cv2.CV_64F,0,1)
x=cv2.convertScaleAbs(x)
cv2.imshow("origianl",o)
cv2.imshow("x",x)
cv2.waitKey()
cv2.destroyAllWindows() 