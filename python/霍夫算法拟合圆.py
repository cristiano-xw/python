import cv2
import numpy as np
import matplotlib.pyplot as plt  
img=cv2.imread("D://opencv//q.jpg",0) #调为灰度图像
imgo=cv2.imread("D://opencv//q.jpg",-1) #格式不变
o=cv2.cvtColor(imgo,cv2.COLOR_BGR2RGB)
oshow=o.copy()
img=cv2.medianBlur(img,5) #进行中值滤波
circles=cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,300,param1=50,param2=30,
                         minRadius=100,maxRadius=200)   
x=circles[0][0][0]
y=circles[0][0][1]  
print("圆心坐标:(",x,y,")") 
print("半径:(",circles[0][0][2],")") 
 
circles=np.uint16(np.ceil(circles))   
        
for i in circles[0,:]:
    cv2.circle(o,(i[0],i[1]),i[2],(0,0,0),5)#绘制圆周   
    cv2.circle(o,(i[0],i[1]),2,(0,0,0),5)#绘制圆心

plt.subplot(121)
plt.imshow(oshow)
plt.axis('off')
cv2.imshow("o1",oshow)  
plt.subplot(122)
plt.imshow(o)            
plt.axis('off') 
cv2.imshow("o2",o) 
cv2.waitKey()
cv2.destroyAllWindows()
 