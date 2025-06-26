import cv2 as cv
import numpy as np

img=cv.imread('D:\openCV-basics\photos\cats 2.jpg')
cv.imshow('cats',img)

blank=np.zeros(img.shape[0:2],dtype='uint8') 
cv.imshow('blank image',blank)

# mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
circle=cv.circle(blank.copy(),(img.shape[1]//2+45,img.shape[0]//2),100,255,-1)
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
# cv.imshow('mask',mask)

# masked_image=cv.bitwise_and(img,img,mask=mask)
# cv.imshow('masked image',masked_image)

weird_Shape=cv.bitwise_and(rectangle,circle)
cv.imshow('weird shape',weird_Shape)

weird_mask=cv.bitwise_and(img,img,mask=weird_Shape)
cv.imshow('weird mask',weird_mask)

## size of mask should be equal to size of image 
cv.waitKey(0)