import datetime
from time import gmtime, strftime

def greet(hour):
    result = ""
    if 0 <= hour <= 11:
        result = "おはようございます。"
    elif hour == 12:
        result = "お昼です。"
    elif 13 <= hour <= 18:
        result = "こんにちは。"
    elif 19 <= hour <= 23:
        result = "こんばんは。"
    else:
        result = "時刻の範囲を超えています。"
    return result
        
hour = int(strftime("%H", gmtime()))
print(greet(hour))

hours_ok = [0, 7, 11, 12, 13, 16, 18, 19, 21, 23]
hours_ng = [-1, 24]

print("---< 正しい時刻 >---")
for hour in hours_ok:
    print(f"{hour}時: {greet(hour)}")
    
print("---< 正しくない時刻 >---")
for hour in hours_ng:
    print(f"{hour}時: {greet(hour)}")
    
def greet2(name, time):
    return f"{name}さん、{greet(time)}"

print(greet2("田中", 15))