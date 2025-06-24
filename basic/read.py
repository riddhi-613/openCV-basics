import cv2 as cv

## reading an image

#img=cv.imread('photos/cat.jpg')
#cv.imshow('cat',img)
#cv.waitKey(0)

## reading a video

capture=cv.VideoCapture('video/dog.mp4')
while True:
    isTrue,frame=capture.read()
    cv.imshow('dog',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
