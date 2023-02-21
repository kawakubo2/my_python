import sys, os

filepath = os.path.join(os.path.dirname(__file__), 'out.txt')

if len(sys.argv) < 2:
    print("引数を指定してください")
    sys.exit()
    
with open(filepath, "w", encoding="utf_8") as out_f:
    for item in sys.argv[1:]:
        out_f.write(item + "\n")