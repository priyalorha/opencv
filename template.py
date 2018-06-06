import cv2
import numpy as np

image=cv2.imread('2.jpg')
image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
template=cv2.imread('finger.jpeg',0)
w,h=template.shape[::-1]
res=cv2.matchTemplate(image_gray,template,cv2.TM_CCOEFF_NORMED)
threshold=0.8
loc=np.where(res>=threshold)
for pt in zip(*loc[::-1]):
	cv2.rectangle(image,pt,(pt[0]+w,pt[1]+h),(0,255,0),1)
cv2.imshow('detected',image)


#cv2.imshow('resh',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

