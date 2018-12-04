import numpy as np

import cv2

img=cv2.imread('cherry2.jpg',1)

#scale

img_half=cv2.resize(img,(0,0),fx=0.5,fy=0.5)
img_stretch=cv2.resize(img,(600,600))
img_stretch_near=cv2.resize(img,(600,600),interpolation=cv2.INTER_NEAREST)

cv2.imshow("half",img_half)
cv2.imshow("expand",img_stretch)
cv2.imshow("expand2",img_stretch_near)


#rotation

M=cv2.getRotationMatrix2D((0,0),-80,1)
rotate=cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))

cv2.imshow("rotate",rotate)



cv2.waitKey(0)
cv2.destroyAllWindows()