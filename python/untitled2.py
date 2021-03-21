import cv2
import math
img=cv2.imread("D://opencv//test//m4.png",3)  

imgray=cv2.Canny(img,200,250,5) #拟合出了边缘 
#imgray=imgray[200:400,0:250] 
cv2.imshow("p",imgray)  
ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#contours为轮廓集，可以计算轮廓的长度、面积等

for cnt in contours: 
    if len(cnt)>200:
        S1=cv2.contourArea(cnt)
        ell=cv2.fitEllipse(cnt) 
        S2 =math.pi*ell[1][0]*ell[1][1]
        if (S1/S2)>0 :   
            img = cv2.ellipse(img, ell, (0, 0, 0), 2) 
            cv2.imshow("0",img)
            print("中心点:",ell[0])
            print("短轴长度:",ell[1][0])
            print("长轴长度:",ell[1][1])
            print("旋转角度:",ell[2]) 
            
            
cv2.waitKey(0)
cv2.destroyAllWindows()