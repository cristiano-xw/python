import cv2
o=cv2.imread("D://opencv//test//s2.png")
gray=cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
ret,binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,hierarchy=cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("original",o)
ellipse=cv2.fitEllipse(contours[0])
#print(ellipse)

(x,y)=ellipse[0] 
(s,l)=ellipse[1]
w=ellipse[2]  
print("中心点：",(x,y)) 
print("短轴和长轴:",(s,l))
print("旋转角度",w)    

cv2.ellipse(o,ellipse,(0,255,0),3)
cv2.imshow("result",o)
cv2.waitKey()
cv2.destroyAllWindows() 
