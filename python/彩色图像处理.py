import cv2
i=cv2.imread("D:\\opencv\\cr72.jpg",cv2.IMREAD_UNCHANGED)
cv2.imshow("original",i)
i[100:150,100:150]=[66,77,88]
cv2.imshow("result",i)
cv2.waitKey(0)
cv2.destroyAllWindows()