en_seasons = ["Spring", "Summer", "Autumn", "Winter"]
ja_seasons = ["春", "夏", "秋", "冬"]

seasons = {en: ja for en, ja in zip(en_seasons, ja_seasons)}
print(seasons)

str_seasons = ["Spring,春", "Summer,夏", "Autumn,秋", "Winter,冬"]
seasons2 = {s.split(",")[0]: s.split(",")[1] for s in str_seasons}
print(seasons2)

numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["♥", "♠", "♦", "☘"]

cards = [(number, suit) for number in numbers for suit in suits]
print(cards)

cards2 = []
for number in numbers:
    for suit in suits:
        cards2.append((number, suit))
        
print(cards2)