list35 = [ 'abc.py', 'bcd.php', 'cde.py', 'def.java', 'efg.cs', 'fgh.py']

#
# Pythonのファイル(拡張子が.py)だけ表示する
#

for filename in list35:
    if filename.endswith('.py'):
        print(filename)