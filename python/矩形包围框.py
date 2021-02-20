import cv2
o=cv2.imread("D://opencv//test//s2.png")
gray=cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
ret,binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours,hierarchy=cv2.findContours(binary,cv2.RETR_LIST,
                                          cv2.CHAIN_APPROX_SIMPLE)

x,y,w,h=cv2.boundingRect(contours[0])
print("顶点及其长宽的点的形式")
print("x=",x)
print("y=",y)
print("w=",w)      
print("h=",h)   
              
rect=cv2.boundingRect(contours[0])
print("rect=",rect)           