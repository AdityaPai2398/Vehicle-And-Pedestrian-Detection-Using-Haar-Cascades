# -*- coding: utf-8 -*-

import cv2
print('Project Topic : Vehicle Classification')
print('Research Internship on Machine learning using Images')
print('By Aditya Yogish Pai and Aditya Baliga B')

video_src = 'pedestrians.avi'

cap = cv2.VideoCapture(video_src)

bike_cascade = cv2.CascadeClassifier('pedestrian.xml')

while True:
    ret, img = cap.read()
	
    
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bike = bike_cascade.detectMultiScale(gray,1.3,2)

    for(a,b,c,d) in bike:
        cv2.rectangle(img,(a,b),(a+c,b+d),(0,255,210),4)
    
    cv2.imshow('video', img)
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
