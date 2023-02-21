import os, re

ptn = re.compile(r"(\w+),(\w+),(\w+),(\w+)")

with open(os.path.dirname(__file__) + "/members.csv","r", encoding="utf_8") as in_file:
    with open(os.path.dirname(__file__) + "/members2.csv", "w", encoding="utf_8") as out_file:
        for line in in_file:
            line = line.rstrip("\n")
            line = ptn.sub(r"\2,\1,\4,\3", line)
            out_file.write(line + "\n")