import os, time, requests, urllib
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = None

def get_price_page(target_date='20221109', departure='FUK', arrival='HND'):
    """
    出発地、到着地、搭乗日で検索し、表示されたURLを返す
    """
    global driver

    url = 'https://www.ana.co.jp/ja/jp/?type=d'
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    
    # 選択画面の表示
    get_search_form()
    time.sleep(5)
    # 出発地の選択
    select_departure(departure)
    # 到着地の選択
    select_arrival(arrival)
    # 搭乗日の選択
    select_date(target_date)
    time.sleep(60)
    url = driver.current_url
    
    driver.quit()
    
    return url

def get_search_form():
    """
    検索画面の表示
    """
    global driver
    ticket_submit_button = driver.find_elements_by_css_selector('.be-domestic-reserve-ticket-submit__button')
    ticket_submit_button[0].click()

def select_departure(departure):
    """
    出発地の選択
    """
    global driver
    departure_elem = driver.find_element_by_id('departureAirport')
    select_departure = Select(departure_elem)
    select_departure.select_by_value(departure)

def select_arrival(arrival):
    """
    到着地の選択
    """
    global driver
    arrival_elem = driver.find_element_by_id('arrivalAirport')
    select_arrival = Select(arrival_elem)
    select_arrival.select_by_value(arrival)

def select_date(target_date):
    """
    搭乗日をクリックすると日付を選択できるカレンダーが表示される
    クリックしないと日付が選択できない(日付はreadonlyになっている)
    """
    global driver
    outwardEmbarkationDate_elem = driver.find_element_by_id('outwardEmbarkationDate')
    outwardEmbarkationDate_elem.click()
    time.sleep(3)
    # カレンダーから日付を選択
    calendar_elem = driver.find_elements_by_css_selector(f"#modal_scroller_calendar_outwardEmbarkationDate td[data-date = '{target_date}'] > a")
    calendar_elem[0].click()

    search_btn = driver.find_element_by_name('j_idt502')
    search_btn.click()

if __name__ == '__main__':
    url = get_price_page()
    print(f"url: {url}")
    # https://aswbe-d.ana.co.jp/9Eile48/dms/red12c/dyc/be/pages/res/search/vacantConditionInput.xhtml?aswdcid=1
    # https://aswbe-d.ana.co.jp/9Eile48/dms/red12c/dyc/be/pages/res/search/vacantConditionInput.xhtml?aswdcid=1


