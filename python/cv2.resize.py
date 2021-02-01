import cv2
b=cv2.imread("D://opencv//bb.jpg")
b1=cv2.resize(b,None,fx=0.9,fy=1)
cv2.imshow("bb",b1)
cv2.waitKey()
cv2.destroyAllWindows()