import numpy as np
import cv2

img=cv2.imread('butterfly.jpg')
cv2.imshow("Image",img)
cv2.moveWindow("Image",10,10)
b,g,r=cv2.split(img)
print(b)
height,width,channels=img.shape

rgb_split=np.empty([height,width*3,3],'uint8')
rgb_split[:,0:width]=cv2.merge([b,b,b])
rgb_split[:,width:width*2]=cv2.merge([g,g,g])
rgb_split[:,width*2:width*3]=cv2.merge([r,r,r])

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
hsv_split=np.concatenate((h,s,v),axis=1)
cv2.imshow("Split hsv",hsv_split)









#cv2.imshow("channels",rgb_split)






cv2.waitKey(0)
cv2.destroyAllWindows()