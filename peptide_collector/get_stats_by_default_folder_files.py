"""
Seleniumテスト用プログラム
"""
import os
import sys
import time
import glob
import zipfile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "https://www.metaboanalyst.ca/MetaboAnalyst/upload/StatUploadView.xhtml"

INPUT_BASE_DIR = "c:/temp/kittaka_data/input"
OUTPUT_BASE_DIR = "c:/temp/kittaka_data/output"

driver = None

ANALYSIS_LIST = ["Volcano plot", "Principal Component Analysis (PCA) ", "Heatmaps"]

FOLD_CHANGE_THRESHOLD = None
P_VALUE_THRESHOLD = None

def main():
    """
    アップロード用フォルダからCSVファイルを1つずつ取り出し、
    アップロードから解析結果の圧縮ファイルダウンロード、
    フォルダへの展開までを行う。
    """
    global driver
    set_threshold()
    filepaths = glob.glob(INPUT_BASE_DIR + '/*.csv')
    for filepath in filepaths:
        driver = webdriver.Chrome()
        driver.get(URL)
        time.sleep(5)

        # fold change thresholdとp value thresholdの設定を行う

        goto_data_integrity_check(filepath)
        time.sleep(5)

        # 整合性がない場合、proceedボタンをクリックできない
        # その場合、プログラムをstatus=1で終了する
        if not goto_normalization_overview_page():
            sys.exit(1)

        # auto scalingを選択後、解析ページへ遷移する
        goto_analysis_page()

        # ANALISYS_LISTで指定したページに遷移し解析
        for analysis_text in ANALYSIS_LIST:
            goto_analysis(analysis_text)
            time.sleep(3)

        # 最終的な結果をダウンロード
        goto_download()
        time.sleep(3)

        download(filepath)
        time.sleep(10)

        driver.close()
        driver.quit()

def set_threshold():
    global FOLD_CHANGE_THRESHOLD
    global P_VALUE_THRESHOLD
    
    if input("Fold change thresholdを変更しますか(y/n):") == "y":
        FOLD_CHANGE_THRESHOLD = input_value("Fold change threshold: ", 1.0, 2.0)
    if input("P-value thresholdを変更しますか(y/n):") == "y":
        P_VALUE_THRESHOLD = input_value("P-value threshold: ")

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

def goto_data_integrity_check(filepath):
    """
    整合性チェックに遷移するための関数
    """
    upload_btn = driver.find_element_by_xpath('//input[@id="j_idt11:j_idt25_input"]')
    upload_btn.send_keys(filepath)
    #Submit buttonをクリックして検証ページへ
    submit_btn = driver.find_element_by_xpath('//button[@id="j_idt11:j_idt26"]')
    submit_btn.click()

def goto_normalization_overview_page():
    """
    ○○ページに遷移するための関数
    """
    proceed_btn = driver.find_element_by_xpath('//button[@id="form1:j_idt17"]')
    if proceed_btn:
        proceed_btn.click()
        return True
    else:
        print("データの整合性チェックに失敗しました")
        return False

def goto_analysis_page():
    """
    auto scalingリンクをクリックし
    解析ページに遷移するための関数
    """
    auto_scaling_radio = driver.find_element_by_xpath('//div[@id="form1:j_idt93"]/div[2]')
    driver.execute_script("arguments[0].click();", auto_scaling_radio)

    normalize_btn = driver.find_element_by_xpath('//button[@id="form1:j_idt103"]')
    driver.execute_script("arguments[0].click();", normalize_btn)
    time.sleep(3)
    # normalize_btnを2回クリックすることでproceed_btnに移動できる
    temp = normalize_btn.send_keys(Keys.TAB)
    temp = driver.switch_to.active_element
    temp = temp.send_keys(Keys.TAB)
    proceed_btn = driver.switch_to.active_element
    # 範囲外の要素をクリックする際はJavaScriptを使ってクリックする
    # 参考サイト: https://office54.net/python/scraping/selenium-click-exception
    driver.execute_script("arguments[0].click();", proceed_btn)

    time.sleep(3)

def goto_analysis(text):
    """
    ○○ページに遷移するための関数
    """
    fold_change_analysis_anchor = driver.find_element_by_xpath(f'//a[text()="{text}"]')
    fold_change_analysis_anchor.click()
    time.sleep(3)
    if text == "Volcano plot":
        if FOLD_CHANGE_THRESHOLD is not None:
            # 既に値が入っている場合、そのままテキストを設定すると、最初の値のあとにテキストが追加される
            # そのために、まずはテキストボックスをクリアする
            fold_change_threshold_text = driver.find_element_by_xpath('//input[@id="form3:j_idt39"]')
            fold_change_threshold_text.clear()
            time.sleep(3)
            # クリアした後に閾値を設定する
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

def download(filepath):
    """
    Download.zipリンクをクリックする関数
    """
    download_zip_file = "C:\\Users\\tomok\\Downloads\\Download.zip"
    if os.path.exists(download_zip_file):
        os.remove(download_zip_file)
    download_zip_link = driver.find_element_by_xpath('//a[text()="Download.zip"]')
    download_zip_link.click()
    time.sleep(3)

    filename = filepath.split("\\")[-1:][0].split(".")[:-1][0]
    zipFile = zipfile.ZipFile(download_zip_file)
    zipFile.extractall(os.path.join(OUTPUT_BASE_DIR, filename))

if __name__ == '__main__':
    main()
