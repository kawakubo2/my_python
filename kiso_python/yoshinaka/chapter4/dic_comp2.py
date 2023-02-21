en_seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
ja_seasons = ['春', '夏', '秋', '冬']

seasons = {en:ja for en, ja in zip(en_seasons, ja_seasons)}
print(seasons)