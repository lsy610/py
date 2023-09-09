#載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#設定 Chrome Driver 的執行檔路徑
options=Options()
options.chrome_executable_path="C:\\Users\\lsr\\py\\chromedriver.exe"
#建立 Driver 物件實體，用程式操作瀏覽器執行
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://www.google.com/")
driver.save_screenshot("screenshot-google.png")
driver.get("https://www.hnvs.cy.edu.tw/")
driver.save_screenshot("screenshot-hnvs.png")
driver.close()