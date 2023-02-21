import calendar

cal = calendar.TextCalendar()
cal.prmonth(2021, 1)

help(cal)

def add(x, y):
    """
    
    引数:
        x: 数値型(float)
        y: 数値型(float)
    戻り値:
        xとyの合計(float)
    """
    return x + y

help(add)