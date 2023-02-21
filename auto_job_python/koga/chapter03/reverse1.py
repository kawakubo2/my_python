w1 = ["日", "月", "火", "水", "木", "金", "土"]

w2 = w1[::-1]

print(w1)
print(w2)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


print(numbers[2::3])

langs = "Python,C,C++,Java,Go,Julia,Rust,TypeScript"
lang_list = langs.split(",")
print(lang_list)
langs2 = "---".join(lang_list)
print(langs2)