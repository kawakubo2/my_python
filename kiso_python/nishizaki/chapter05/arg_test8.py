def func(**dic):
    print(dic)
    
func(name="田中一郎", num=1)
# xxx=www ---> 関数内部では辞書として扱われる
func(name="山田太郎", age=59, num=2, point=60)