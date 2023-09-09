#抓取ptt電影版網頁原始碼(html)
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
#建立request 物件 附加 request headers 的資訊
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
#print(data)
#解析原始碼 取得每篇文章的標題
import bs4
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("div",class_="title")
for title in titles:
    if title.a !=None:
        with open ("ptt電影版爬蟲.txt","w",encoding="utf-8") as file :
            for title in titles:
                file.write(title.a.string+"\n")

