import cv2
import numpy as np


cap=cv2.VideoCapture(0)#視訊鏡頭

while True:
    ret,frame=cap.read()
    if ret:
        cv2.imshow('videos',frame)
    else:
        break
    if cv2.waitKey(1)==ord('q'):
        break