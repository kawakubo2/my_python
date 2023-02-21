import os

filepath = os.path.join(os.path.dirname(__file__), "out.txt")
with open(filepath, "w", encoding="utf_8") as f:
    f.write("こんにちは")
    f.write("Pythonの世界へようこそ\n")
    f.write(str(2021))
    f.write("年\n")