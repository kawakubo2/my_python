import os

with open(os.path.dirname(__file__) + "/out.txt", "w", encoding="utf_8") as f:
    while True:
        s = input("文字列(終了時はxxxxx): ")
        if s == "xxxxx":
            break
        f.write(s + "\n")
