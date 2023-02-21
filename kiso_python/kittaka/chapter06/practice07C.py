import os, sys

if len(sys.argv) < 2:
    print("引数を指定してください")
    sys.exit()
    
filepath = os.path.join(os.path.dirname(__file__), 'out.txt')
with open(filepath, "w", encoding="utf_8") as out_f:
    #for i in range(1, len(sys.argv)):
    #    out_f.write(sys.argv[i] + "\n")
    for arg in sys.argv[1:]:
        out_f.write(arg + "\n")
    