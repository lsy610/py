import cv2

img=cv2.imread('qq.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#轉灰階圖片
faceCascade=cv2.CascadeClassifier('face_detect.xml')#載入人臉辨識模組
faceRect=faceCascade.detectMultiScale(gray,1.1,6)#圖片變數、圖片縮小倍數小,大(執行時間長,短)、最少框幾次越大(精準)越小(框到非人臉)
print(len(faceRect))
for(x,y,w,h) in faceRect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)#圖片變數、左上角座標、右下角座標、顏色、粗度

cv2.imshow('img',img)
cv2.waitKey(0)