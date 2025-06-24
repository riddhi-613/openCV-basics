import cv2 as cv 

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img=cv.imread('photos/cat.jpg')
cv.imshow('cat',img)
resized_img=rescaleFrame(img)
cv.imshow('resized cat',resized_img)
cv.waitKey(0)

# capture=cv.VideoCapture('video/dog.mp4')
# while True:
#     isTrue,frame=capture.read()
#     frame_resized=rescaleFrame(frame,0.2)
#     cv.imshow('video',frame)
#     cv.imshow('video resized',frame_resized)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()