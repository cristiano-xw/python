import cv2
img=cv2.imread("D://opencv//w.jpg")
t,rst=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
r,cp=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
cv2.imshow("img",img)
cv2.imshow("w1",cp) 
cv2.imshow("w",rst)
cv2.waitKey()
cv2.destroyAllWindows()