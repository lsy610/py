from openpyxl import Workbook, load_workbook
import urllib.request as req
url="https://tw.stock.yahoo.com/us-market"
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
#print(data)
import bs4  
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("div",class_="Lh(20px) Fw(600) Fz(16px) Ell")
stocks=root.find_all("span",class_="Fz(14px) C(#979ba7) Ell")
# price=root.find_all("span",class_="Jc(fe) Fw(600) D(f) Ai(c) C($c-trend-down)") 
dictionary = {} 
for i,j in zip(titles,stocks):
    if (j.isupper)!=1:
        key = i.text.strip()
        value = j.text.strip()
        dictionary[key] = value
wb=Workbook()
ws=wb.active
title=['股價名稱','英文代號']
ws.append(title)
for key, value in dictionary.items():
    ws.append([key, value])

wb.save('stock.xlsx')

        
            


