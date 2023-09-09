import cv2
import numpy as np

kernel=np.ones((3,3),np.uint8)
kernel1=np.ones((3,3),np.uint8)
img=cv2.imread('opencv.png')
img=cv2.resize(img,(0,0),fx=2,fy=2)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#色彩轉換
blur=cv2.GaussianBlur(img,(3,3),0)#高斯模糊
canny=cv2.Canny(img,150,200)#讀取像素差,顯示邊緣圖片(邊緣檢測)
dilate=cv2.dilate(canny,kernel,iterations=1)#膨脹效果(加粗)
erode=cv2.erode(dilate,kernel1,iterations=1)#清實效果(加細)

cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.imshow('blur',blur)
cv2.imshow('canny',canny)
cv2.imshow('dilate',dilate)
cv2.imshow('erode',erode)

cv2.waitKey(0)
