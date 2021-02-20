import cv2
import numpy as np
o=cv2.imread("D://opencv//test//s2.png")
cv2.imshow("original",o)

gray=cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
ret,binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,hierarchy=cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

n=len(contours)
cntlen=[]
for i in range(n):
    
    print("contours["+str(i)+"]长度=",cv2.arcLength(contours[i],True))
    temp=np.zeros(o.shape,np.uint8)
    cntlen.append(temp)
    cntlen[i]=cv2.drawContours(cntlen[i],contours,i,(255,255,255),1)
    #cntlen[i]=cv2.drawContours(cntlen[i],contours,i,(255,255,255),3)
    cv2.imshow("contours["+str(i)+"]",cntlen[i])  
    
    
cv2.waitKey()
cv2.destroyAllWindows() 
    