def get_season_by_month(month):
    if month in (12, 1, 2):
        return '冬'
    elif month in (3, 4, 5):
        return '春'
    elif month in (6, 7, 8):
        return '夏'
    elif month in (9, 10, 11):
        return '秋'
    else:
        return None

test = {12: '冬', 1: '冬', 2: '冬', 3: '春', 4: '春', 5: '春', 6: '夏', 7: '夏', 
        8: '夏', 9: '秋', 10: '秋', 0: None, 13: None}

success = 0
for month, expect_season in test.items():
    actual_season = get_season_by_month(month)
    print(f"期待値: {expect_season}, 検出値: {actual_season}, {'○' if expect_season == actual_season else '×'}")
    if expect_season == actual_season:
        success += 1

print('---------< 判定 >---------')
if len(test) == success:
    print('合格')
else:
    print('不合格')