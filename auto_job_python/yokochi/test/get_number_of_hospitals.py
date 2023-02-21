import re, os, time, requests, urllib, math
from bs4 import BeautifulSoup
import openpyxl as exel

pref_code = 40
page = 1
base_dir = os.path.dirname(__file__)

book = exel.Workbook()
sheet = book.active

# 特定の都道府県の1ページに相当するURL
# target_url = 'https://caremap.jp/facility_medicals/map/prefIds:40/key1:0/list_type:list/'
target_url = f'https://caremap.jp/facility_medicals/map/page:{page}/prefIds:{pref_code}/key1:0/list_type:list'
base_url = target_url.split('/map/')[0]
row = 1
def extract_int(s):
    if "," in s:
        pattern = "^(([0-9]{1,3}),)+([0-9]{1,3})件$"
        ptn = re.compile(pattern)
        num = int(ptn.sub(r"\g<2>" + r"\g<3>", s))
    else:
        pattern = "^([0-9]{1,3})件$"
        ptn = re.compile(pattern)
        num = int(ptn.sub(r"\g<1>", s))
    return num

def find_number_of_hospitals(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')
    # soup.selectした結果は「1,234件」のような文字列なので、extract_intで整数値に変換する
    return extract_int(soup.select('table[id!="dataList"] tr:nth-child(5) > td')[0].text)

nb_hospitals = find_number_of_hospitals(target_url)
print(f"福岡県の病院数: {nb_hospitals}")