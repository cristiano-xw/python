import cv2
a=cv2.imread("D://opencv//h.jpg")
b=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
cv2.imshow("original",a)
cv2.imshow("result",b)
cv2.waitKey()
cv2.destroyAllWindows() 