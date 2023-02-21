import locale
from datetime import datetime, timedelta
locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')

def gessho_youbi(today = datetime.now()):
    num = today.strftime('%w')
    num = int(num)
    return num

def get_gessho(today = datetime.now()):
    """
    指定された日付から曜日を求める関数

    引数
    ------------------------------------
    today
    datetime
    指定がない場合、現在日時(datetime.now())

    戻り値
    ------------------------------------
    曜日の数値を返す
    日:0 月:1 火:2 水:3 木:4 金:5 土:6
    """
    gessho_year = today.year
    gessho_month = today.month
    gessho = datetime(gessho_year, gessho_month, 1)
    return gessho

def print_youbi():
    """
    カレンダーの曜日部分の表示を行う関数

    引数
    ------------------------------------
    なし

    戻り値
    ------------------------------------
    なし


    """
    # w = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    w = ['日', '月', '火', '水', '木', '金', '土']
    for y in w:
        print('{:>4}'.format(y), end='')
    print()


def print_day(gessho):
    """
    1ヶ月文のカレンダーを表示

    引数
    ---------------------------------
    月初の曜日
    0:日 1:月 2:火 3:水 4:木 5:金 6:土

    戻り値
    ---------------------------------
    なし
    """
    init_month = gessho.month
    youbi_num = gessho_youbi(gessho)
    space = ' ' * youbi_num * 5
    print(space, end='')
    while True:
        print('{:5}'.format(gessho.day), end='')
        y = int(gessho.strftime('%w'))
        if y == 6:
            print()
        gessho = gessho + timedelta(days=1)
        if gessho.month != init_month: 
            break

if __name__ == "__main__":
    year = int(input('年:'))
    month = int(input('月:'))
    print('              {}年{}月     '.format(year, month))
    print_youbi()
    print_day(get_gessho(datetime(year, month, 1)))