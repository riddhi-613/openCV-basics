import cv2 as cv 
import numpy as np

img=cv.imread('D:\openCV-basics\photos\cats.jpg')
cv.imshow('image',img)

## convert to grayscale image 
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY) ## here it means that if the pixel value is more than 150 we need to binarise it to 255
cv.imshow('thresolded image',thresh)

## creat an inverse thresholded image 
threshold,thresh_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV) ## here it means that if the pixel value is more than 150 we need to binarise it to 255
cv.imshow('thresolded image',thresh_inv)

## adaptive thresholding 
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3) ## c value is esentially subtracted from the mean and is the last param
cv.imshow('adaptive thresholding',adaptive_thresh)

cv.waitKey(0)