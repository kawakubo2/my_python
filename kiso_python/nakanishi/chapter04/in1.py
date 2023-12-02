files = ["aaa.py", "bbbb.java", "cc.c", "dddd.js"]
search = ".php"
print(search in [file[-3:] for file in files])
