from input_utils import input_int_range

def get_char_at(s, index):
    if index < 0 or index >= len(s):
        raise ValueError("範囲外の位置を指定しています")
    return s[index]

s = input("文字列: ")
i = input_int_range(0, len(s), "位置")
try:
    print(get_char_at(s, i))
except ValueError as e:
    
    print(e)