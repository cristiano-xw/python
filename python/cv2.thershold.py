import cv2
img =cv2.imread("D://opencv//bbb.png")
t,rst=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow("b",rst)
cv2.waitKey()
cv2.destroyAllWindows()
