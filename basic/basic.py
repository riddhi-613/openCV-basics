import cv2 as cv 
img=cv.imread('photos/park.jpg')
cv.imshow('park',img)

## converting an image to grayscale 
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grayscale ',gray)

## blur the image 
## noise of the image is to be removed (lighting issues and camera settings )
blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT) # here (3,3) is the kernel size and this must be an odd number 
cv.imshow('blurred image',blur)

## edge cascade -here the edges are displayed in grayscale but now we dont want all edges to make it messy blur imageto some extent and then pass the image 
canny=cv.Canny(blur,125,175)
cv.imshow('canny image',canny)

## dilating the image 
dilated=cv.dilate(canny,(3,3),iterations=1)
cv.imshow('dilated image',dilated)

## eroding - to get back the same edge cascade 
eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow('eroded image ',eroded)

## resize the image 
resize=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized image',resize)

## cropping the image 
cropped=img[50:200,200:400]
cv.imshow('cropped image',cropped)

cv.waitKey(0)