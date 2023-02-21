x = 83.456789

# C言語の書式文字列に近い
print("標準体重: %.1fkg" % (x))

print("標準体重: {:.1f}kg".format(x))

# f文字列
print(f"標準体重: {x:.1f}kg")