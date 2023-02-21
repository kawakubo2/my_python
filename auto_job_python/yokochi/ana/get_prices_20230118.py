import os, sys, time, requests, urllib, math, re
from bs4 import BeautifulSoup
import openpyxl as exel
from select_test import get_price_page

save_dir = os.path.dirname(os.path.abspath(__file__))
save_file = os.path.join(save_dir, 'price.csv')

url = get_price_page('20221101')
time.sleep(3)
print(f"url = {url}")

ids = ['#availabilityResultMainFare', '#availabilityResultValueFare']

for id in ids:
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')
    table = soup.select(id + " .availabilityResultTable")
    print('--- table start ---')
    print(table)
    print('--- table end   ---')

    departure_arrival = table.select('tbody > tr > td[class="headCell"] p[class="availabilityResultFlightTime"]').text()
    print('--- departure_arrival start ---')
    print(departure_arrival)
    print('--- departure_arrival end ---')
