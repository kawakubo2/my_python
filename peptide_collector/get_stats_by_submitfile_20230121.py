"""
Seleniumテスト用プログラム
"""
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import filedialog

URL = "https://www.metaboanalyst.ca/MetaboAnalyst/upload/StatUploadView.xhtml"

BASE_DIR = "c:/temp/kittaka_data"
FILE_PATH = filedialog.askopenfilename(initialdir = BASE_DIR)

ANALYSIS_LIST = ["Volcano plot", "Principal Component Analysis (PCA) ", "Heatmaps"]

driver = webdriver.Chrome()

FOLD_CHANGE_THRESHOLD = None
P_VALUE_THRESHOLD = None

def main():
    """
    ファイルのアップロードから解析結果の取得まで
    """
    global FOLD_CHANGE_THRESHOLD
    global P_VALUE_THRESHOLD
    driver.get(URL)
    time.sleep(5)
    
    if input("Fold change thresholdを変更しますか(y/n):") == "y":
        FOLD_CHANGE_THRESHOLD = input_value("Fold change threshold: ", 1.0, 2.0)
    if input("P-value thresholdを変更しますか(y/n):") == "y":
        P_VALUE_THRESHOLD = input_value("P-value threshold: ")

    goto_data_integrity_check()
    time.sleep(5)

    if not goto_normalization_overview_page():
        sys.exit(1)

    goto_analysis_page()

    for analysis_text in ANALYSIS_LIST:
        goto_fold_change_analysis(analysis_text)
        time.sleep(3)

    goto_download()
    time.sleep(3)

    download()
    time.sleep(10)
    driver.quit()

def input_value(text, lower=0.0, upper=1.0):
    while True:
        try:
            val = float(input(text + ": "))
            if lower <= val <= upper:
                return val
            else:
                print(f"{lower}～{upper}までの値を入力してください")
        except ValueError:
            print("数値を入力してください")

def goto_data_integrity_check():
    """
    整合性チェックに遷移するための関数
    """
    base_selector = '''#j_idt10 > form > table > tbody > tr:nth-child(3)
        > td:nth-child(1) > table > tbody > tr:nth-child(1) '''
    #ファイルの選択
    file_selector = base_selector + '''> td:nth-child(1) >table > tbody > tr:nth-child(3) >
    td:nth-child(2) input[type="file"]'''
    upload_btn = driver.find_elements_by_css_selector(file_selector)
    upload_btn[0].send_keys(FILE_PATH)
    #Submit buttonをクリックして検証ページへ
    submit_selector = base_selector +'> td:nth-child(2) > button:nth-child(1) > span:nth-child(1)'
    submit_btn = driver.find_elements_by_css_selector(submit_selector)
    submit_btn[0].click()

def goto_normalization_overview_page():
    """
    ○○ページに遷移するための関数
    """
    proceed_selector = '#form1 > table > tbody > tr:nth-child(3) > td:nth-child(1) '
    proceed_selector += '> table > tbody > tr:nth-child(1) > td:nth-child(3) > button'
    proceed_btn = driver.find_elements_by_css_selector(proceed_selector)
    if proceed_btn:
        proceed_span = \
            driver.find_elements_by_css_selector(proceed_selector + ' > span:nth-child(1)')
        proceed_span[0].click()
        return True
    else:
        print("データの整合性チェックに失敗しました")
        return False

def goto_analysis_page():
    """
    解析ページに遷移するための関数
    """
    auto_scaling_radio = driver.find_element_by_xpath('//div[@id="form1:j_idt93"]/div[2]')
    driver.execute_script("arguments[0].click();", auto_scaling_radio)

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
    """
    ○○ページに遷移するための関数
    """
    global FOLD_CHANGE_THRESHOLD
    global P_VALUE_THRESHOLD
    fold_change_analysis_anchor = driver.find_element_by_xpath(f'//a[text()="{text}"]')
    fold_change_analysis_anchor.click()
    time.sleep(3)
    if text == "Volcano plot":
        if FOLD_CHANGE_THRESHOLD is not None:
            fold_change_threshold_text = driver.find_element_by_xpath('//input[@id="form3:j_idt39"]')
            fold_change_threshold_text.clear()
            time.sleep(3)
            fold_change_threshold_text.send_keys(str(FOLD_CHANGE_THRESHOLD))
            time.sleep(3)
            
        if P_VALUE_THRESHOLD is not None:
            p_value_threshold_text = driver.find_element_by_xpath('//input[@id="form3:j_idt50"]')
            p_value_threshold_text.clear()
            time.sleep(3)
            p_value_threshold_text.send_keys(str(P_VALUE_THRESHOLD))
            time.sleep(3)

        submit_btn = driver.find_element_by_xpath('//button[@id="form3:j_idt58"]')
        submit_btn.click()
    
    time.sleep(3)    
    statistics_link = driver.find_element_by_xpath('//span[text()="Statistics"]')
    statistics_link.click()

def goto_download():
    """
    ダウンロードページに遷移するための関数
    """
    download_btn = driver.find_element_by_xpath('//span[text()="Download"]')
    download_btn.click()

def download():
    """
    Download.zipリンクをクリックする関数
    """
    download_zip_link = driver.find_element_by_xpath('//a[text()="Download.zip"]')
    download_zip_link.click()

if __name__ == '__main__':
    main()
