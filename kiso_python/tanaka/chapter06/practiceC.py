import os, sys

file = os.path.join(os.path.dirname(__file__), "out.txt")

if len(sys.argv) < 2:
    print("引数を指定してください。")
    sys.exit()
    
with open(file, "w", encoding="utf_8") as out_f:
    for i in range(1, len(sys.argv)):
        out_f.write(sys.argv[i] + "\n")