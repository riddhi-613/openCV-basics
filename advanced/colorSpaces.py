import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('D:\openCV-basics\photos\park.jpg') ## images in BGR format 
## opencv reads the images in BGR format 
cv.imshow('park',img)

# plt.imshow(img) ## matlpotlib.pyplot reads images in the reverse manner i.e. RGB
# plt.show()

## BGR to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

## BGR to HSV - (HSV stands for Hue,Saturation,Value)
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

## BGR to LAB - basically washed down version of an image 
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

## BGR to RGB 
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

## HSV to BGR 
hsv2bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('hsv2bgr',hsv2bgr)

## LAB to BGR
lab2bgr=cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('lab2bgr',lab2bgr)

cv.waitKey(0)   