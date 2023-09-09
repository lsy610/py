#載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
#設定chrome driver 的執行檔路徑
options=Options()
options.chrome_executable_path="C:\\Users\\lsr\\py\\chromedriver.exe"
#建立 driver 物件實體,用程式操作瀏覽器執行
driver=webdriver.Chrome(options=options)
#連線到linkedIn工作搜尋網址
driver.get("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0")
# driver.maximize_window()
#捲動視窗並等待瀏覽器載入更多內容
n=0
while n<5:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")#捲動視窗到底部
    time.sleep(3)#等待3秒鐘
    n+=1
tags=driver.find_elements(By.CLASS_NAME,"base-search-card__title")
for tag in tags:
    print(tag.text)
driver.close