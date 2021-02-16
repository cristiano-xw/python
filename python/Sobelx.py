import cv2
o=cv2.imread("D://opencv//hei.png") 
x=cv2.Sobel(o,-1,1,0)
cv2.imshow("original",o)
cv2.imshow("x",x)
cv2.waitKey()
cv2.destroyAllWindows() 
