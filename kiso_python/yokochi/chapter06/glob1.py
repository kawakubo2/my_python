import glob

files = glob.glob('./**/**')

def printfile(file):
    print(f"---< file path: {file} >---")
    # with open(file, 'r', encoding='utf_8') as f:
    #     for line in f:
    #         print(line)

for file in files:
    printfile(file)