from collections import deque

d = deque("")
while True:
    sw = input("1.受付 2.診察 9.終了: ")
    if sw == "9":
        break
    if sw == "1":
        name = input("名前: ")
        d.append(name)
        print(d)
    elif sw == "2":
        if len(d) == 0:
            continue
        name = d.popleft()
        print(f"{name}さん、診察審へどうぞ。")
        print(d)
    else:
        print("1または2を選択してください。")