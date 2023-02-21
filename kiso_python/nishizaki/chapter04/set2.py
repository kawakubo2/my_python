words1 = { "空", "海", "川", "地球" }
words2 = { "山", "海", "空", "空気" }

words3 = words1 | words2
print(words3)

words4 = words1 & words2
print(words4)

words5 = words1 ^ words2
print(words5)

words6 = words1 - words2
print(words6)

words7 = words2 - words1
print(words7)

refreg = { "たまご", "じゃがいも", "にんじん", "たまねぎ", "にく"}
recipes = [
    { "じゃがいも", "きのこ", "さんま", "あおじそ" },
    { "しいたけ", "たまねぎ", "にんじん", "にく" },
    { "たまねぎ", "にんじん", "じゃがいも"},
    { "にく", "たまご", "たまねぎ"}
]

for r in recipes:
    if r < refreg:
        print(r)