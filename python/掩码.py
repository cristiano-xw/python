import cv2
import numpy as np
c7=cv2.imread("D://opencv//c7.jpg",0)
r,c=c7.shape   
key=np.random.randint(0,256,size=[r,c],dtype=np.uint8)
encryption=cv2.bitwise_xor(c7,key)
decryption=cv2.bitwise_xor(encryption,key)
print(key)
cv2.imshow("encryption",encryption)
cv2.imshow("decryption",decryption)
cv2.waitKey()
cv2.destroyAllWindows()
