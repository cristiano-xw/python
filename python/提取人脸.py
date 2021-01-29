import cv2
img=cv2.imread("D://opencv//w.jpg")
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv) 
minhue=5
maxhue=170
huemask=cv2.inRange(h,minhue,maxhue)
minset=25
maxset=166
satmask=cv2.inRange(s,minset,maxset)
mask=huemask & satmask
roi=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("img",img)
cv2.imshow("roi",roi)
cv2.waitKey()
cv2.destroyAllWindows()
