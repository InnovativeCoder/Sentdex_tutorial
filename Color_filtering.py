import cv2
import numpy as np

#We will aim to find a specific color like operations performed witht the green screen

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_maroon = np.array([150,50,50]) 
	upper_maroon = np.array([180,255,150])

	#hsv is hue sat value , hue is the mian things that dictate how objects are
	mask = cv2.inRange(hsv, lower_maroon, upper_maroon)
	res = cv2.bitwise_and(frame, frame, mask= mask)

	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()