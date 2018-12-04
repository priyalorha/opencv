import numpy as np
import cv2

img=cv2.imread("butterfly.jpg",1)

#Guassian blur

cv2.imshow("Orignal image",img)

blur=cv2.GaussianBlur(img,(55,5),0)

cv2.imshow("blur imaage",blur)
kernal=np.ones((5,5),'uint8')
dilate=cv2.dilate(img,kernal,iterations=1)
erode=cv2.erode(img,kernal,iterations=1)

cv2.imshow("dilate",dilate)
cv2.imshow("erode",erode)

cv2.waitKey(0)
cv2.destroyAllWindows()