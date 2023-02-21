import os, sys

base_dir = os.path.dirname(__file__)

if len(sys.argv) != 3:
    print("使い方: python conv_enc1.py ファイルパス1 ファイルパス2")
    sys.exit()
    
if sys.argv[1] == sys.argv[2]:
    print("入力ファイルと出力ファイルが同じです。入力ファイルが消去されるので処理を中断します")
    sys.exit()
    
in_file = os.path.join(base_dir, sys.argv[1])
if not os.path.exists(in_file):
    print("ファイルが存在しません。")
    sys.exit()

out_file = os.path.join(base_dir, sys.argv[2])
if os.path.exists(out_file):
    if input("上書きしますか?(y/n): ") != "y":
        sys.exit()
        
print("文字エンコーディングを指定してください")
enc_num = input("1.ShiftJIS 2.EUC-JP 3.JIS: ")
if enc_num == "1":
    enc = "shift_jis"
elif enc_num == "2":
    enc = "euc_jp"
elif enc_num == "3":
    enc = "iso2022_jp"
else:
    print("エンコーディングが正しくありません")
    sys.exit()
    
with open(in_file, "r", encoding="utf_8") as in_f:
    with open(out_file, "w", encoding=enc) as out_f:
        for s in in_f:
            out_f.write(s)