from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
# 設定執行檔路徑
options = Options()
options.chrome_executable_path = "C:\\Users\\lsr\\py\\chromedriver.exe"
# 建立 driver 物件實體
driver = webdriver.Chrome(options=options)
# 連結到 leetcode 登入頁面
driver.get("https://leetcode.com/accounts/login/")
# 等待 5 秒，確保頁面載入完成
time.sleep(5)
# 輸入帳號密碼
usernameInput = driver.find_element(By.ID, "id_login")
passwordInput = driver.find_element(By.ID, "id_password")
usernameInput.send_keys("myhmdo314@gmail.com") 
passwordInput.send_keys("Aa0984286692")  
# 找到登入按鈕並按下 Enter 鍵
signinBtn = driver.find_element(By.ID, "signin_btn")
signinBtn.send_keys(Keys.ENTER)
# 這裡可以等待一段時間，確保網頁處理完成
time.sleep(5)
#連線到要抓取資料的網址
driver.get("https://leetcode.com/problemset/all/")
time.sleep(3)
statElemet=driver.find_element(By.CSS_SELECTOR,"[data-difficulty=TOTAL]")
# print(statElemet.text)
columns=statElemet.text.split("\n")
print("以刷題數量",columns[1])
# 關閉瀏覽器視窗
driver.quit()
