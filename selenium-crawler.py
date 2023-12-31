#載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#設定 Chrome Driver 的執行檔路徑
options=Options()
options.chrome_executable_path="C:\\Users\\lsr\\py\\chromedriver.exe"
#建立 Driver 物件實體，用程式操作瀏覽器執行
driver=webdriver.Chrome(options=options)
# driver.maximize_window() #視窗最大化
#連線ptt 股票版
#取得股票版中的文章標題
driver.get("https://www.ptt.cc/bbs/Stock/index.html")
# print(driver.page_source) #取得網頁原始碼
tags=driver.find_elements(By.CLASS_NAME,"title")# 搜尋class屬性是title的所有成員
for tag in tags:
    print(tag.text)
#取得上一頁文章標題
while(True):
    link=driver.find_element(By.LINK_TEXT,"‹ 上頁")
    link.click()#模擬使用者點擊
    tags=driver.find_elements(By.CLASS_NAME,"title")# 搜尋class屬性是title的所有成員
    for tag in tags:
        print(tag.text)
        
driver.close()