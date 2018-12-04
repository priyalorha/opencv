import numpy as np
import cv2
canvas=np.ones([500,500,3],'uint8')*255
color=(0,22,255)
line_width=3
radius=10
pressed=False
point=(0,0)


def click(event,x,y,flalgs,param):
	global canvas,pressed
	if event == cv2.EVENT_LBUTTONDOWN:
		pressed=True
		point=(x,y)
		cv2.circle(canvas,point,radius,color,-1)
		
	if event==cv2.EVENT_MOUSEMOVE and pressed==True:
		
		point=(x,y)
		cv2.circle(canvas,point,radius,color,-1)
	if event==cv2.EVENT_LBUTTONUP:
		pressed=False
		#cv2.circle(canvas,point,radius,color,-1)



cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas",click)


while True:

	
	
	cv2.imshow("canvas",canvas)


	ch=cv2.waitKey(1)
	if ch & 0xFF==ord('q'):
		break
	elif ch & 0xFF==ord('r'):
		color=(255,0,0)
	elif ch & 0xFF==ord('b'):
		color=(0,0,255)
 
cv2.destroyAllWindows()