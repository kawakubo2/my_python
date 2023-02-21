import pickle

with open("./dokushu_python/inadumi/chapter07/rectangles.bin", "rb") as file:
    rectangles = pickle.load(file)
    for rec in rectangles:
        print(rec.get_area())