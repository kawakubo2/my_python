import os

with open(os.path.dirname(__file__) + "/out.txt", "a", encoding="UTF-8") as f:
    while True:
        line = input("文字列(終了するにはq): ")
        if line == "q":
            break
        f.write(line + "\n")
