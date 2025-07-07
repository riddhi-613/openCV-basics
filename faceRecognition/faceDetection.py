import cv2 as cv
face_cascade=cv.CascadeClassifier('haarcascade_frontalface_default.xml')

cap=cv.VideoCapture(0)

##img=cv.imread('D:\openCV-basics\photos\group 2.jpg')

while True:
    success, img=cap.read()

    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.1,4)

    for(x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv.imshow('img',img)

    if cv.waitKey(30) & 0xff==27 :
        break

cap.release()