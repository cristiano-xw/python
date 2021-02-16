import cv2
o=cv2.imread("D://opencv//w.jpg")
x=cv2.Canny(o,128,200)
y=cv2.Canny(o,32,108)
cv2.imshow("origianl",o)
cv2.imshow("x",x)
cv2.imshow("y",y)
cv2.waitKey()
cv2.destroyAllWindows()
