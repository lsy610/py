import cv2
img=cv2.imread('find.jpg')#讀取讀片
img=cv2.resize(img,(0,0),fx=0.5,fy=0.5)#設定長寬比
imgContour=img.copy()
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#將圖片從BGR轉至灰階
canny=cv2.Canny(img,150,200)#過濾像素150~200的邊緣
contours,hierarchy=cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)#邊緣圖片,偵測方式(內輪廓、外輪廓、內外輪廓,壓縮方式)
#contours(輪廓)
#hierarchy(階層)

for cnt in contours:
    cv2.drawContours(imgContour,cnt,-1,(255,0,0),4)#描繪圖檔,輪廓名稱,-1(全部輪廓),顏色,線的粗度
    area=cv2.contourArea(cnt)
    if area >500:
        # print(cv2.contourArea(cnt))#輪廓面積(輪廓名稱)
        # print(cv2.arcLength(cnt,True))#輪廓邊長(輪廓名稱,是否閉合)
        peri=cv2.arcLength(cnt,True)#設定近似值
        vertices=cv2.approxPolyDP(cnt,peri*0.02,True)#近似多邊形頂點(輪廓名稱,近似值,是否閉合)
        corners=(len(vertices))#頂點數目
        # print(len(vertices))
        x,y,w,h=cv2.boundingRect(vertices)#回傳左上角x座標,右上角座標,寬度,高度
        cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),4)#圖片名稱,左上角座標,右下角座標,顏色,粗度
        if corners==3:
            cv2.putText(imgContour, 'triangle', (x,y-5), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
        elif corners==4:
            cv2.putText(imgContour, 'rectangle', (x,y-5), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
        elif corners==5:
            cv2.putText(imgContour, 'pentagon', (x,y-5), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
        elif corners>=6:
            cv2.putText(imgContour, 'circle', (x,y-5), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
cv2.imshow('img',img)
cv2.imshow('canny',canny)
cv2.imshow('imgContour',imgContour)

cv2.waitKey(0)