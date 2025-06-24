import cv2 as cv 
import numpy as np 

## blank image 
blank=np.zeros((500,500,3),dtype='uint8') ## here 3 is the no of color channels
cv.imshow('blank',blank)

# 1. paint the image in certain color
blank[200:300, 300:400]=255,0,0
blank[300:400, 200:300]=0,0,255
blank[200:300, 200:300]=0,255,0
cv.imshow('blue',blank)

# 2. draw a rectangle 
cv.rectangle(blank,(0,0),(250,500),(100,100,100),thickness=cv.FILLED) ## to fill the rectangle we can use following values for thickness a) cv.filled b) -1
# # another option to fill this is fill the end coordindates with (blank.shape[1]//2,blank.shape[0]//2)
cv.imshow('rectangle',blank)

## 3. draw a circle
cv.circle(blank,center=(250,250),radius=40,color=(0,0,255),thickness=-1)
cv.imshow('circle',blank)

## 4. draw a line 
cv.line(blank,(100,0),(350,250),(0,255,0),thickness=4)
cv.imshow('lines',blank)

## 5. writing text on an image
cv.putText(blank,"hello i am riddhi",(10,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('text',blank)

# img=cv.imread('photos/cat.jpg')
# cv.imshow('cat',img)
cv.waitKey(0)