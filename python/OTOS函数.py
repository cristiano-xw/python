import cv2
img=cv2.imread("D://opencv//w.jpg",0)
t1,cmp=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
t2,ct=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("a",cmp)
cv2.imshow("b",ct) 
cv2.waitKey() 
cv2.destroyAllWindows()
