from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get('https://uta.pw/sakusibbs/users.php?user_id=2')

a_list = driver.find_elements_by_css_selector('ul#mmlist li a')
for a in a_list:
    print('■', a.text)
    print('└', a.get_attribute('href'))
    
driver.close()