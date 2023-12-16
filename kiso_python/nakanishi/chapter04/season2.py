season = {"春": "Spring", "夏": "Summer", "秋": "Autumn", "冬": "Winter"}

print("--- キーだけの取得 ---")
for s in season.keys():
    print(s, end=" ")
print()

print("--- 値だけの取得 ---")
for v in season.values():
    print(v, end=" ")
print()

print("--- キーと値の取得 ---")
for k, v in season.items():
    print(f"{k}: {v}", end=" ")
print()

