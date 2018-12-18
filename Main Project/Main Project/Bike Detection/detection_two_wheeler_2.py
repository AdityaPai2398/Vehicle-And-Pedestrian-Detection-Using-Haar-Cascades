# -*- coding: utf-8 -*-

import cv2
print('Project Topic : Vehicle Classification')
print('Research Internship on Machine learning using Images')
print('By Aditya Yogish Pai and Aditya Baliga B')

cascade_src = 'two_wheeler.xml'

video_src = 'two_wheeler1.mp4'

cap = cv2.VideoCapture(video_src)

car_cascade = cv2.CascadeClassifier(cascade_src)


while True:
    ret, img = cap.read()
    
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray,1.19, 1)


    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,215),2)
    
    cv2.imshow('video', img)
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
