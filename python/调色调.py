import cv2
img=cv2.imread("D://opencv//w.jpg")
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
s[:,:]=255.0
h[:,:]=255.0
newhsv=cv2.merge([h,s,v])
art = cv2.cvtColor(newhsv,cv2.COLOR_HSV2BGR)
cv2.imshow("img",img)
cv2.imshow("art",art)
cv2.waitKey()
cv2.destroyAllWindows()  