import cv2
o=cv2.imread("D://opencv//test//s2.png")
gray=cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
ret,binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

r=cv2.Canny(binary,32,100)
n=len(r)
print(n) 
cv2.imshow("r",r)
retval=cv2.fitEllipse(r[0]) 
print(retval) 
cv2.waitKey()
cv2.destroyAllWindows()  