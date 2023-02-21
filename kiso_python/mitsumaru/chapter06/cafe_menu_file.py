import random, os

question = []
with open(os.path.dirname(__file__) + "/cafe_menu.txt", "r", encoding="utf_8") as f:
    for line in f:
        row = line.rstrip("\n").split(",")
        question.append({'name': row[0], 'ryaku': row[1], 'kigou': row[2]})

pattern = {"1": ('name', 'ryaku'), "2": ('name', 'kigou'), "3": ('ryaku', 'kigou'),
           "4": ('ryaku', 'name'), "5": ('kigou', 'name'), "6": ('kigou', 'ryaku')}

# print(question)

def training(arg1, arg2):
    random.shuffle(question)
    cnt = 1
    for q in question:
        print("途中でやめたいときはquitを入力")
        print(q[arg1] + ": ", end="")
        answer = input('')
        if answer == "quit":
            break
        if answer == q[arg2]:
            print('正解！')
        else:
            print('残念・・・')

while True:
    print("1.正式名から略名 2.正式名から記号 3.略名から記号")
    print("4.略名から正式名 5.記号から正式名 6.記号から略名 quit:終了")
    s = input("番号: ")
    if s == "quit":
        break
    if s in ("1", "2", "3", "4", "5", "6"):
        training(pattern[s][0], pattern[s][1])
    else:
        print("1～6を入力してください")

