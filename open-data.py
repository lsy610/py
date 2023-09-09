#網路連線
#import urllib.request as request
#src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
#with request.urlopen(src) as response:
#    data=response.read().decode("UTF-8")
#print(data)
#串接、擷取資料
import urllib.request as request
import json
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data=json.load(response) #利用json 模組處理json 資料格式
#取得公司名稱
clist=data["result"]["results"]
with open ("date.txt","w",encoding="utf-8") as file :
    for i in clist:
        file.write(i["公司名稱"]+"\n")
