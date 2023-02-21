from selenium import webdriver
import time

# Chromeを起動する
driver = webdriver.Chrome()
# Pythonのページを開く
driver.get('https://python.org')
# 30秒後に終了する
time.sleep(30)
driver.quit()