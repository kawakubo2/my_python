str1 = "私の実家の郵便番号は〒123-4567です。"

index = str1.index("〒")

if index != -1: # 検索に成功
    print("郵便番号は", str1[index+1:index+9])
else:
    print("文字列に郵便番号は含まれていません。")