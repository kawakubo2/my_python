def func(arg1, *args):
    print(arg1, args)
    
func(1, 2, 3, 4)
func("Hello", "Python", 2015, 3, 5)
totalsteps = []
def func1(name, totalsteps):
    today_step = int(input("今日の歩数: "))
    totalsteps.append(today_step)
    total = 0
    for step in totalsteps:
        total += step
    print(f"{name}さんの今月の総歩数は{total}歩です。")

while True:
    func1("鈴木", totalsteps)
    print(totalsteps)