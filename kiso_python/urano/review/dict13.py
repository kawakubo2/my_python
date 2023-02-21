import os

flowers_dict = {}
with open(os.path.dirname(__file__) + '/flowers.txt', 'r', encoding='utf_8') as f:
    for line in f:
        item = line.split(',')
        flowers_dict[item[0]] = item[1].rstrip('\n')
        
def get_english_flower(ja):
    global flowers_dict
    if ja not in flowers_dict:
        answer = input('追加する(yes/no): ')
        if answer == 'yes':
            en = input('英語の花名: ')
            flowers_dict[ja] = en
        else:
            return None
    return flowers_dict[ja]

while True:
    ja = input('日本語の花名(終了時はq): ')
    if ja == 'q':
        saved = input('保存しますか?(yes/no): ')
        if saved:
            with open(os.path.dirname(__file__) + '/flowers.txt', 'w', encoding='utf_8') as f:
                for ja_flower, en_flower in flowers_dict.items():
                    f.write(f"{ja_flower},{en_flower}\n")
        break
    en_flower = get_english_flower(ja)
    if en_flower:
        print(f"{ja}は英語で「{en_flower}」です。")
    