import os

PATH = "/Users/tomok/OneDrive/ドキュメント/my_python/dokushu_python"

def indent(indent_num):
    print(' ' * indent_num, end='')

def recursive_file_list(dir, indent_num = 0):
    if not os.path.isdir(dir):
        raise ValueError('ディレクトリではない')

    for f in os.listdir(dir):
        if f == '.' or f == '..':
            continue
        indent(indent_num)
        child_path = os.path.join(dir, f)
        if os.path.isdir(child_path):
            print('■' + f)
            recursive_file_list(child_path, indent_num + 4)
        elif os.path.isfile(child_path):
            print('□' + f)
        else:
            print('？')

recursive_file_list(PATH)