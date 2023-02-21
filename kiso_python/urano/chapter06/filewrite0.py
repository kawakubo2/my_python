# filewrite0.py
import os

with open(os.path.dirname(__file__) + '/out.txt', 'a', encoding='utf_8') as f:
    while True:
        line = input('文字列(終了時はq): ')
        if line == "q":
            break
        f.write(line + "\n")
