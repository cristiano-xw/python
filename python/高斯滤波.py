import cv2
o=cv2.imread("D://opencv//yan.png")
r=cv2.GaussianBlur(o,(11,11),0,0) 

cv2.imshow("1",o)
cv2.imshow("2",r)

cv2.waitKey()
cv2.destroyAllWindows()