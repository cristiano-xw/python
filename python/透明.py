import cv2
img=cv2.imread("D://opencv//bbb.png") 
bgra=cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
b,g,r,a=cv2.split(bgra)
a[:,:]=0.0
bgra1=cv2.merge([b,g,r,a]) 
print(bgra1) 
cv2.imshow("1",bgra)
cv2.imshow("2",bgra1)        
cv2.waitKey()
cv2.destroyAllWindows()                          