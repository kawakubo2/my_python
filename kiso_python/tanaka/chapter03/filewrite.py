import os

f = open(os.path.dirname(__file__) + '/sample.txt', 'w', encoding='utf_8')

line = input('文字列(終了時はq): ')
while line != 'q':
    f.write(line + "\n")    
    line = input('文字列(終了時はq): ')

f.close()
    