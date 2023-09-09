import cv2

cap=cv2.VideoCapture('淒美地.mp4') #視訊鏡頭(0)

while(True):
    ret,frame=cap.read()#ret=取得下一幀數是否成功(布林值) frame=如果成功回傳下一張圖片
    frame=cv2.resize(frame,(0,0),fx=0.4,fy=0.4)
    if ret:
        cv2.imshow('videos',frame)
    else:
        break
    if cv2.waitKey(10) ==ord('q'):
        break