words = [{'福岡', '人口', '2000年'}, {'ロシア', '人口'}, {'人口', '日本'}, {'東日本', '人口'},
         {'日本', '現在', '人口'}]

w = {'日本', '人口'}
result = []
for word in words:
    if w <= word:
        result.append(word)

print(result)