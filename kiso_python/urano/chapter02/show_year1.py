"""
このプログラムは
西暦から令和に変換するプログラムです。
"""
year = 2021
print("西暦" + str(year) + "年は", end="") # end=""と書くと改行されないようになる
print("令和" + str(year - 2018) + "年です")