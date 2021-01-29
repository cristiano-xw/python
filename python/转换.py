import cv2
import numpy as np
img=np.random.randint(0,256,size=[100,200],dtype=np.uint8)
rst=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#cv2.imshow("img",img)
#cv2.imshow("rst",rst)
#print(img)
#print(rst)
print("img=\n",img)
print("rst=\n",rst)
