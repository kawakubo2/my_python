s = "A001Yamada     28" # 0:5 会員番号 5:15 名前 15:18 年齢
id_slice = slice(0, 4)
name_slice = slice(4, 14)
age_slice = slice(14, 17)

print(f"会員番号: {s[id_slice]} 名前: {s[name_slice]} 年齢: {s[age_slice]}")