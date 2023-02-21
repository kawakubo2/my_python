# -*- coding: utf-8 -*-

import os, sys

in_file = ''
out_file = ''
enc = ''

def arg_num_check(args):
    if (len(args) != 3):
        raise ValueError('3つの引数が必要です')
        
def source_file_exists():
    global in_file
    in_file = sys.argv[1]
    if not os.path.exists(in_file):
        raise FileNotFoundError('ファイルが見つかりません')
        
def confirm_overwrite():
    global out_file
    out_file = sys.argv[2]
    if os.path.exists(out_file):
        if input('上書きしますか?[y/n]: ') == 'y': return True
        else: return False
    return True

def select_encoding():
    global enc
    print('文字エンコーディングを指定してください')
    while True:
        enc_num = input('1:ShiftJIS 2:EUC-JP 3:JIS  : ')
        if enc_num == '1':
            enc = 'shift_jis'
        elif enc_num == '2':
            enc = 'euc_jp'
        elif enc_num == '3':
            enc = 'iso2022_jp'
        else:
            print('1,2,3を指定してください')
        if enc:
            break

def convert_encoding():
    with open(in_file, 'r', encoding='utf_8') as in_f:
        with open(out_file, 'w', encoding=enc) as out_f:
            for line in in_f:
                out_f.write(line)
                
try:
    arg_num_check(sys.argv)
    source_file_exists()
    if (not confirm_overwrite()):
        sys.exit()
    select_encoding()
    convert_encoding()
except ValueError:
    print('引数は3個必要です。')
except FileNotFoundError:
    print('変換元ファイルが存在しません。')
            

