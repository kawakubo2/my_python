import os

for path, dirs, files in os.walk('/Users/tomok/OneDrive/ドキュメント/my_python/dokushu_python'):
    print(path)
    print(dirs)
    print(files)
    print('-----------------')
