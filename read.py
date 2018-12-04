import cv2
import numpy as np
img=cv2.imread("cherry.jpeg")
#cv2.namedWindow("Image",cv2.WINDOW_NORMAL)


''' file information'''
print(type(img))
print(len(img))
print(img.shape)
print(img.dtype)
print(img[:,:,0])
print(img.size)
cv2.imshow("MyImage",img)
black=np.zeros([150,200,1],'uint8')
cv2.imshow("dark ",black)
print(black[0,0,:])

cv2.waitKey(0)
cv2.destroyAllWindows()