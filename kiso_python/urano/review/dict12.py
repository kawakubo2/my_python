flowers = {'チューリップ':'tulip', 'ヒマワリ': 'sunflower', 
            'タンポポ': 'dandelion', 'コスモス': 'cosmos', 'ユリ': 'lily'}
def get_en_flower(ja):
    global flowers
    if ja not in flowers:
        answer = input('追加する(yes/no): ')
        if answer == 'no':
            return None
        en_flower = input('英語の花名: ')
        flowers[ja] = en_flower
    return flowers[ja]

while True:
    ja = input('日本語の花名(終了時はq): ')
    if ja == 'q':
        break
    en = get_en_flower(ja)
    if en:
        print(f"{ja}は英語で「{en}」です。")
    else:
        print("該当する花が見つかりません。")