import numpy as np
import cv2

img=cv2.imread('cherry2.jpg',0)

height,width=img.shape[0:2]

cv2.imshow("Original BW",img)

''''binary=np.zeros([height,width,1],'uint8')
#binary=img[height]
print(binary)

threshold=20
thresh=25

for i in range(0,height):
	for j in range(0,width):
		if binary[i][j]>threshold:
			binary[i][j]=255


cv2.imshow("edited",binary)'''


ret,thresh=cv2.threshold(img,70,255,cv2.THRESH_BINARY)
thresh_adapy=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow("inbuilts",thresh)
cv2.imshow("adaptiveThreshold",thresh_adapy)
cv2.waitKey(0)
cv2.destroyAllWindows()

