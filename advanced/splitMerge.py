import cv2 as cv
import numpy as np

img=cv.imread('D:\openCV-basics\photos\park.jpg')
cv.imshow('img',img)

blank=np.zeros(img.shape[:2],dtype='uint8')

b,g,r=cv.split(img)

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

print(img.shape) ## --> has a shape of (427,640,3) here 3 denotes the channels (BGR -3 channels)
## these images are shown as grayscale because there shapes are 1 
print(b.shape) ## (427,640) - when there is nothing for the third place it has 1 
print(g.shape) ## (427,640) - when there is nothing for the third place it has 1
print(r.shape) ## (427,640) - when there is nothing for the third place it has 1
print(blue.shape) ## this one now again has 3 color channels though 2 of them are blank 

merged=cv.merge([b,g,r])

cv.imshow('merged image',merged)

cv.waitKey(0)