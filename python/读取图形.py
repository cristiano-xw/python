import cv2
i=cv2.imread("D:\\opencv\\cr7.jpg")
cv2.imshow("cr7",i)  #前一个是窗口名称 后一个是图像名称
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("D:\\opencv\\c7.jpg",i)


