import cv2
import numpy as np

img=np.zeros((600,600,3),np.uint8)#創建二微陣列(圖片)600(高)600(寬)3(B,G,R)np.uint8(8進制)

# cv2.line(img,(0,0),(600,600),(255,0,0),1)#img(圖片),起點,終點,線的顏色,粗度
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,0),1)#同上img(圖片),img.shape[1](寬度)img.shape[0](高度)
cv2.rectangle(img,(0,0),(300,300),(255,255,0),1)#img(圖片),方形左上角座標,右下角座標,顏色,粗度,填滿(cv2.FILLED)
cv2.circle(img,(300,300),100,(0,0,255),1)#img(圖片),圓心,半徑,顏色,粗度,填滿(cv2.FILLED)
cv2.putText(img,'hello',(100,500),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),1)#img(圖片),顯示的字串(英文),字串左下角座標,字體(字型),大小,顏色,粗度

cv2.imshow('img',img)
cv2.waitKey(0)