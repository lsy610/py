import cv2
import numpy as np
import random
img=cv2.imread('opencv.png')

print(img.shape)#顯示陣列形狀、大小
# print(img)
# print(type(img))

# img=cv2.resize(img,(0,0),fx=0.5,fy=0.5)#fx(寬度)fy(高度) 0.5(倍縮放)

# cv2.imshow('img',img)
# cv2.waitKey(0)

# img=np.empty((300,300,3),np.uint8)
# for row in range(100):
#     for col in range(img.shape[1]):
#         img[row][col]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
newimg=img[:88,100:150]
cv2.imshow('img',img)
cv2.imshow('newimg',newimg)
cv2.waitKey(0)