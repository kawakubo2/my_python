import os, sys

if len(sys.argv) != 3:
    print("使い方: python conv_enc1.py file1 file2")
    sys.exit()
    
in_file = sys.argv[1]
if not os.path.exists(in_file):
    print("ファイルが存在しません")
    sys.exit()
    
out_file = sys.argv[2]

if in_file == out_file:
    print('変換元と変換先が同じです')
    sys.exit()
    
if os.path.exists(out_file):
    if input('上書きしますか?(y/n): ') != 'y':
        sys.exit()
        
print('文字エンコーディングを指定してください')
enc_num = input('1.ShiftJIS 2.EUC-JP 3.JIS: ')
if enc_num == '1':
    enc = 'shift_jis'
elif enc_num == '2':
    enc = 'euc_jp'
elif enc_num == '3':
    enc = 'iso2022_jp'
else:
    print('エンコーディングが正しくありません')
    sys.exit()
    
base_url = os.path.dirname(__file__)
with open(os.path.join(base_url, in_file), 'r', encoding='utf_8') as in_f:
    with open(os.path.join(base_url, out_file), 'w', encoding=enc) as out_f:
        for str in in_f:
            out_f.write(str)