import cv2
import numpy as np 

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')
#botht the images are of identical size
add_sign = img1 + img2 #will impose one over the other

#add = img1 + img2
add = cv2.add(img1,img2)

cv2.imshow('add_sign',add_sign)
cv2.imshow('add',add)

weighted = cv2.addWeighted(img1,0.6,img2,0.4, 0)
cv2.imshow('weighted',weighted)

img3 = cv2.imread('mainlogo.png')
#So first remove the background to make it transparent

rows,cols,channels = img3.shape
roi = img1[0:rows, 0:cols]

img3gray = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img3gray,220,255,cv2.THRESH_BINARY_INV)
#So if pixel value is above 220 , it would be converted to 255 i.e. white
#and if it is below 220 then it is converted to 0 i.e. black

mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
img3_fg = cv2.bitwise_and(img3, img3, mask=mask)

dst = cv2.add(img1_bg,img3_fg)
img1[0:rows, 0:cols] = dst

#Visualizing : 
cv2.imshow('res',img1)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img3_fg',img3_fg)
cv2.imshow('dst',dst)
cv2.imshow('mask',mask)

cv2.waitKey(0)
cv2.destroyAllWindows()