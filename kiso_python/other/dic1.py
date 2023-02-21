week_dict = {'日': 'Sunday', '月': 'Monday', '火': 'Tuesday', '水': 'Wednesday', '木': 'Thursday', \
    '金': 'Friday', '土': 'Saturday'}

weekofday_ja = input('日本語の曜日を入力してください: ')
if weekofday_ja in week_dict:
    print(week_dict[weekofday_ja])
else:
    print('キー"{}"が見つかりませんでした'.format(weekofday_ja))
