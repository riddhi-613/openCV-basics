import cv2 as cv 

## rescale function 
def rescaleFrame(frame,scale=0.75):
    ## this function used for the images videos and live videos (works on everything)
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
    # works only on live videos (caputred using camera in realtime)
    capture.set(3,width) ## 3 references the width 
    capture.set(4,height) ## 4 references the height 


## image resizing 
img=cv.imread('photos/cat.jpg')
cv.imshow('cat',img)
resized_img=rescaleFrame(img)
cv.imshow('resized cat',resized_img)
cv.waitKey(0)

## video resizing 
capture=cv.VideoCapture('video/dog.mp4')
while True:
    isTrue,frame=capture.read()
    frame_resized=rescaleFrame(frame,0.2)
    cv.imshow('video',frame)
    cv.imshow('video resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()