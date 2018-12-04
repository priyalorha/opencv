import numpy as np

import cv2

img=cv2.imread("butterfly.jpg",1)
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

cv2.imwrite("gray.jpg",gray)

b,g,r=img[:,:,0],img[:,:,1],img[:,:,2]
rgba=cv2.merge((b,g,r,g))
#png can hodl transparent image
cv2.imwrite("rgba.png",rgba)


cv2.waitKey(0)
cv2.destroyAllWindows()