import cv2
o=cv2.imread("D://opencv//cc.jpg",cv2.IMREAD_GRAYSCALE) 
x=cv2.Scharr(o,cv2.CV_64F,1,0)
y=cv2.Scharr(o,cv2.CV_64F,0,1)
x=cv2.convertScaleAbs(x)
y=cv2.convertScaleAbs(y)
xy=cv2.addWeighted(x,0.5,y,0.5,0)
w=xy[450:1200,50:1100] 
cv2.imshow("w",w) 
cv2.imshow("xy",xy)
r=cv2.imwrite("D://opencv//cc2.jpg",w)    
cv2.waitKey()
cv2.destroyAllWindows()



