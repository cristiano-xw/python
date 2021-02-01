import cv2
img=cv2.imread("D://opencv//w.jpg",0)
a=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,3)
b=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,3)
cv2.imshow("a",a) 
cv2.imshow("b",b) 
cv2.waitKey()
cv2.destroyAllWindows()
                        