import cv2 as cv
import numpy as np

img=cv.imread('D:\openCV-basics\photos\park.jpg')
cv.imshow('img',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

## laplation - 
lap = cv.Laplacian( gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('laplacian',lap)

## sobel
sobalx=cv.Sobel(gray,cv.CV_64F,1,0)
sobalx=cv.Sobel(gray,cv.CV_64F,1,0)

cv.waitKey(0) 