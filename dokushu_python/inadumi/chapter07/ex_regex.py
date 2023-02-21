import os, re

ptn = re.compile(r"\d{2,4}-\d{2,4}-\d{4}")

with open(os.path.dirname(__file__) + "/sample.dat", "r", encoding="UTF-8") as file:
    for line in file:
        results = ptn.findall(line)
        for result in results:
            print(result)