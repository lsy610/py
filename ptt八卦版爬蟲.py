# 抓取ptt八卦版的網頁原始碼(html)
import urllib.request as req
def getData(url):
    #建立一個 Request 物件,附加request headers 的資訊
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    #解析網頁原始碼
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")#讓 beautifulsoup 協助我們解析 html 格式文件
    titles=root.find_all("div",class_="title")#尋找所有 class="title"的div標籤
    for title in titles:
        if title.a !=None:#如果標題包含a標籤(沒有被刪除).印出來
            print(title.a.string)  
    #抓取上一頁網址
    nextLink=root.find("a",string="‹ 上頁")#找到內文是‹ 上頁 的a標籤印出來
    return nextLink["href"]
# 主程序 抓取多個頁面標籤
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<5:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1
