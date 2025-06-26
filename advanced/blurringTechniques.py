import cv2 as cv
import numpy as np

img=cv.imread('D:\openCV-basics\photos\cats.jpg')
cv.imshow('img',img)

## method 1 averaging - uses the concept of sliding window where in the avg of the kernel is placed at the center pixel
average=cv.blur(img,(3,3))
cv.imshow('average blur',average)

## gaussian blur -
blur1=cv.GaussianBlur(img,(3,3),0) ## --> here 0 is the std deviation w.r.t x
cv.imshow('blurred image 1 ',blur1)

## median blurring - same as averaging but instead of finding the avg it finds the median -- more effective in removing noises (for advanced OpenCV projects)
median=cv.medianBlur(img,3)
cv.imshow('median blur',median)

## bilateral blurring -- most effective
bilateral=cv.bilateralFilter(img,10,35,55) ## third param - sigmaColor (higher the value means more colors in the surrounding are will be considered)
cv.imshow('bilateral blur',bilateral)

cv.waitKey(0)