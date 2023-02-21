"""
辞書・・・Python, C#
ハッシュ・Ruby
連想配列・PHP, JavaScript
マップ・・Java, JavaScript
"""

members = { 'm001': ('山田太郎', 170, 72, '1988-12-30'), 'm002': ('横山花子', 158, 50, '1998-07-25'),
            'm003': ('田中一郎', 172, 63, '2001-03-07'), 'm004': ('星山裕子', 162, 53, '1992-06-11')}

member_id = input('メンバーid: ')

if member_id in members:
    print(f'名前: {members[member_id][0]}')
    print(f'生年月日: {members[member_id][3]}')
else:
    print(f'{member_id}は名簿に見つかりません。')