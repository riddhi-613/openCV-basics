import cv2 as cv 
import numpy as np 

img=cv.imread('D:\openCV-basics\photos\cats.jpg')
cv.imshow('cats',img)

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('blank',blank)

## conversion to grayscale 
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grayscale',gray)

blur=cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

cann=cv.Canny(blur,125,175)
cv.imshow('canny',cann)

# ret, thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY) ## threshold binarises the image 
# cv.imshow('thresh image',thresh)
## simple thresholding has some disadvantages 


## countours and heirarchies 
contours,heirarchies=cv.findContours(cann,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
## # counoutrs is the list of all the contours that were found in the image (they are basically edge in the image)
## # heirarchy is heiracrchial rep of the contours 
## # RETR_LIST gives all the contours present in the image 
## # RETR_EXTERNAL gives all the extrnal contours of the image
## # RETR_TREE countours in the herarchical system are returned by this 
## # counter approx method -chain approx none returns all the contours 
## # CHAIN_APPROX_SIMPLE essentially takes all the pts of the line and takes the final 2 endpts 

print(f'{len(contours)} contours were found')

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('countours drawn',blank)

cv.waitKey(0) 