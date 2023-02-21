import os, time, requests, urllib, re
from selenium import webdriver
from selenium.webdriver.support.select import Select

# 正規表現をあらかじめコンパイルしておく
departure_arrival_pattern = re.compile(r'\s*(\d{2}:\d{2})\s*-\s*(\d{2}:\d{2})\s*')
flight_number_pattern = re.compile(r'\s*([a-zA-Z0-9]+)\s*')

driver = None

def main(target_date='20221209', departure='FUK', arrival='HND'):
    global driver
    
    get_price_page(target_date, departure, arrival)
    time.sleep(3)
    
    base_dir = os.path.dirname(__file__)
    file_dir = os.path.join(base_dir, 'files')
    save_file = os.path.join(file_dir, 'price.csv')

    ids = ['availabilityResultMainFare', 'availabilityResultValueFare']

    for id in ids:
        # 発着時刻はMainFareのみ
        if id =='availabilityResultMainFare':
            trs = driver.find_elements_by_css_selector(f"#{id} > table > tbody > tr")
            tr_len = len(trs)
            print(f"行数:{tr_len}")
            for i in range(1, tr_len + 1):
                departure_arrival = driver.find_elements_by_css_selector( \
                    f"#{id} > table > tbody > tr:nth-child({i}) > td.headCell > p.availabilityResultFlightTime")
                departure, arrival = parse_departure_arrival(departure_arrival[0].text)
                print('-----------------')
                print(f"出発時刻: {departure}")
                print(f"到着時刻: {arrival}")
                flight_number = driver.find_elements_by_css_selector( \
                    f"#{id} > table > tbody > tr:nth-child({i}) > td.headCell > p.availabilityResultFlightDetail > span:nth-child(1)")
                print(f"便名: {flight_number_pattern.search(flight_number[0].text).group(1)}")

        tds = driver.find_elements_by_css_selector(
            f"#{id} > table > tbody > tr:nth-child({i}) > td.showResult")
        for i in range(1, tr_len + 1):
            for j in range(1, len(tds) + 1):
                price = driver.find_elements_by_css_selector(
                    f"#{id} > table > tbody > tr:nth-child({i}) > td.showResult:nth-child({j}) > \
                        div:nth-child(1) > span:nth-child(1) > label:nth-child(1) > em")
                if price:
                    print(f"価格: {price[0].text}")

def get_price_page(target_date='20221209', departure='FUK', arrival='HND'):
    """
    出発地、到着地、搭乗日で検索し、表示されたURLを返す
    """
    global driver

    url = 'https://www.ana.co.jp/ja/jp/?type=d'
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    # print(driver.get_attribute('innerHTML'))
    
    # 選択画面の表示
    get_search_form()
    time.sleep(5)
    # 出発地の選択
    select_departure(departure)
    # 到着地の選択
    select_arrival(arrival)
    # 搭乗日の選択
    select_date(target_date)
    time.sleep(5)

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

    search_btn = driver.find_element_by_xpath('//input[@type="submit"][@value="検索する"]')
    search_btn.click()

def parse_departure_arrival(departure_arrival):
    global departure_arrival_pattern
    result = departure_arrival_pattern.search(departure_arrival)
    if result:
        return (result.group(1), result.group(2))
    else:
        return None

if __name__ == '__main__':
    main()
    # https://aswbe-d.ana.co.jp/9Eile48/dms/red12c/dyc/be/pages/res/search/vacantConditionInput.xhtml?aswdcid=1
    # https://aswbe-d.ana.co.jp/9Eile48/dms/red12c/dyc/be/pages/res/search/vacantConditionInput.xhtml?aswdcid=1
