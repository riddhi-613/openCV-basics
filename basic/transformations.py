import cv2 as cv
import numpy as np
img=cv.imread('photos/park.jpg')
cv.imshow('park',img)

## translation - using this we can move the image up down left right 
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

## -x--> left
## -y--> up
## +x-->right
## +y--> bottom

translated_image=translate(img,-100,100)
cv.imshow('translated image',translated_image)

## rotation of an image 
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint==None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(img,-45)
cv.imshow('rotated image',rotated)

rotationOfRotated=rotate(img,-90)
cv.imshow('rotated of rotated image',rotationOfRotated)

## resizing the image 
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized image',resized)

## flipping an image 
flip=cv.flip(img,-1) ## 0 flipping image x axis 1 flipping image along y axis and -1 flipping wrt to both 
cv.imshow('fliiping the image',flip)

### cropping the image 
cropped=img[200:500,300:500]
cv.imshow('cropped image',cropped)


cv.waitKey(0)