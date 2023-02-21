import os, time, requests, urllib, sys
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


url = 'https://www.metaboanalyst.ca/MetaboAnalyst/upload/StatUploadView.xhtml'


file_path = 'C:/temp/kittaka_data/Book1.csv'

driver = None

def main(file, url):
    global driver
    
    # options= webdriver.ChromeOptions()

    # chrome_prefs = {}
    # options.experimental_options["prefs"] = chrome_prefs
    # chrome_prefs["profile.default_content_settings"] = {"javascript": 2}
    # chrome_prefs["profile.managed_default_content_settings"] = {"javascript": 2}
    # driver = webdriver.Chrome("/Anaconda3/chromedriver.exe", options=options)
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)

    goto_data_integrity_check_page(file)
    time.sleep(5)
    
    if goto_normalization_overview_page() == False:
        sys.exit(1)

    time.sleep(3)

    goto_analysis_page()
    time.sleep(20)

    driver.close()

def goto_data_integrity_check_page(file):
    global driver
    base_selector = '#j_idt10 > form > table > tbody '
    base_selector += '> tr:nth-child(3) > td:nth-child(1) > table > tbody > tr:nth-child(1) '
    # ファイルを選択
    file_selector = base_selector + '> td:nth-child(1) '
    file_selector += 'table > tbody > tr:nth-child(3)> td:nth-child(2) input[type="file"]'
    upload_btn = driver.find_elements_by_css_selector(file_selector)
    upload_btn[0].send_keys(file)
    # ファイルの妥当性検証ページへのsubmitボタンクリック
    submit_selector = base_selector + '> td:nth-child(2) > button:nth-child(1) > span:nth-child(1)'
    submit_btn = driver.find_elements_by_css_selector(submit_selector)
    submit_btn[0].click()

def goto_normalization_overview_page():
    global driver
    # normalization_overviewページに遷移できるかチェック
    proceed_selector = '#form1 > table > tbody > tr:nth-child(3) > td:nth-child(1) '
    proceed_selector += '> table > tbody > tr:nth-child(1) > td:nth-child(3) > button'
    proceed_btn = driver.find_elements_by_css_selector(proceed_selector)
    if proceed_btn:
        proceed_span = driver.find_elements_by_css_selector(proceed_selector + ' > span:nth-child(1)')
        proceed_span[0].click()    
    else:
        print("データの整合性チェックに失敗しました。")
        return False
    
def goto_analysis_page():
    global driver
    auto_scaling_selector = '#form1 > table > tbody > tr:nth-child(5) > '
    auto_scaling_selector += 'td:nth-child(1) > table > tbody > '
    auto_scaling_selector += 'tr:nth-child(6) > td:nth-child(1) > table > tbody > '
    auto_scaling_selector += 'tr:nth-child(3) > td:nth-child(1) > div > div:nth-child(2)'
    auto_scaling_radio = driver.find_elements_by_css_selector(auto_scaling_selector)
    auto_scaling_radio[0].click()
    
    normalize_btn = driver.find_element_by_xpath('//button[@id="form1:j_idt103"]')
    normalize_btn.click()
    time.sleep(3)
    temp = normalize_btn.send_keys(Keys.TAB)
    temp = driver.switch_to.active_element
    temp = temp.send_keys(Keys.TAB)
    proceed_btn = driver.switch_to.active_element
    proceed_btn.click()

    # proceed_btn = driver.find_element_by_xpath('//button[@id="form1:nextBn"]')
    # proceed_btn.click()
    time.sleep(100) 

if __name__ == '__main__':
    main(file_path, url)
