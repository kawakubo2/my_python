import os, sys

if len(sys.argv) < 2:
    print("引数を指定してください")
    sys.exit()

with open("out.txt", "w", encoding="utf_8") as out_f:
    for i in range(1, len(sys.argv)):
        out_f.write(sys.argv[i] + "\n")