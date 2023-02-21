from selenium import webdriver
import os

driver = webdriver.Chrome()
driver.get('https://python.org')
driver.save_screenshot(os.path.join(os.path.dirname(__file__), 'screenshot.png'))
driver.quit()