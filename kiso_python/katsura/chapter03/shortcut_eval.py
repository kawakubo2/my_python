# short_cut.py

# ショートカット評価
msg = "名前は必須です。"
msg = msg or "エラーなし"
print(msg)

if msg:
    print(msg)
else:
    print("特になし")