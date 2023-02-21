import sys, time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://www.metaboanalyst.ca/MetaboAnalyst/upload/StatUploadView.xhtml"

file_path = "c:/temp/kittaka_data/Book1.csv"

analysis_list = ["Fold Change Analysis", "T-tests", "Volcano plot", 
                 "Principal Component Analysis (PCA) ", "Heatmaps"]

driver = None

def main(file, url):
    global driver
    global analysys_list
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    
    goto_data_integrity_check(file)
    time.sleep(5)

    if goto_normalization_overview_page() == False:
        sys.exit(1)

    goto_analysis_page()

    for analysis_text in analysis_list:
        goto_fold_change_analysis(analysis_text)
        time.sleep(3)

    goto_download()
    time.sleep(3)
    
    download()

def goto_data_integrity_check(file):
    global driver
    base_selector = '#j_idt10 > form > table > tbody > tr:nth-child(3) > td:nth-child(1) > table > tbody > tr:nth-child(1) '
    #ファイルの選択
    file_selector = base_selector + '> td:nth-child(1) >table > tbody > tr:nth-child(3) > td:nth-child(2) input[type="file"]'
    upload_btn = driver.find_elements_by_css_selector(file_selector)
    upload_btn[0].send_keys(file)
    #Submit buttonをクリックして検証ページへ
    submit_selector = base_selector +'> td:nth-child(2) > button:nth-child(1) > span:nth-child(1)'
    submit_btn = driver.find_elements_by_css_selector(submit_selector)
    submit_btn[0].click()
    
def goto_normalization_overview_page():
    global driver
    proceed_selector = '#form1 > table > tbody > tr:nth-child(3) > td:nth-child(1) '
    proceed_selector += '> table > tbody > tr:nth-child(1) > td:nth-child(3) > button'
    proceed_btn = driver.find_elements_by_css_selector(proceed_selector)
    if proceed_btn:
        proceed_span = driver.find_elements_by_css_selector(proceed_selector + ' > span:nth-child(1)')
        proceed_btn[0].click()
    else:    
        print("データの整合性チェックに失敗しました")
        return False
    
    
def goto_analysis_page():
    global driver
    auto_scaling_selector = '#form1 > table > tbody > tr:nth-child(5) > '
    auto_scaling_selector += 'td:nth-child(1) > table > tbody > '
    auto_scaling_selector += 'tr:nth-child(6) > td:nth-child(1) > table > tbody > '
    auto_scaling_selector += 'tr:nth-child(3) > td:nth-child(1) > div > div:nth-child(2)'
    auto_scaling_radio = driver.find_elements_by_css_selector(auto_scaling_selector)
    driver.execute_script("arguments[0].click();", auto_scaling_radio[0])
    # auto_scaling_radio[0].click()
    
    normalize_btn = driver.find_element_by_xpath('//button[@id="form1:j_idt103"]')
    driver.execute_script("arguments[0].click();", normalize_btn)
    # normalize_btn.click()
    time.sleep(3)
    temp = normalize_btn.send_keys(Keys.TAB)
    temp = driver.switch_to.active_element
    temp = temp.send_keys(Keys.TAB)
    proceed_btn = driver.switch_to.active_element
    # 範囲外の要素をクリックする際はJavaScriptを使ってクリックする
    # 参考サイト: https://office54.net/python/scraping/selenium-click-exception
    driver.execute_script("arguments[0].click();", proceed_btn)

    time.sleep(3)

def goto_fold_change_analysis(text):
    global driver
    fold_change_analysis_anchor = driver.find_element_by_xpath(f'//a[text()="{text}"]')
    fold_change_analysis_anchor.click()
    time.sleep(3)
    statistics_link = driver.find_element_by_xpath('//span[text()="Statistics"]')
    statistics_link.click()

def goto_download():
    global driver
    download_btn = driver.find_element_by_xpath('//span[text()="Download"]')
    download_btn.click()

def download():
    global driver
    download_zip_link = driver.find_element_by_xpath('//a[text()="Download.zip"]')
    download_zip_link.click()

if __name__ == '__main__':
    main(file_path, url)

