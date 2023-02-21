with open("rand_gen1.py", "r", encoding="utf_8") as f:
    for i, line in enumerate(f):
        print("{:4d}; {}".format(i + 1, line.rstrip("\n")))
