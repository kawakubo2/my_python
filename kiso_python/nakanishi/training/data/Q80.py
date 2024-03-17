print("--- listコンストラクタを使用する方法 ---")
c = ["red", "green", "yellow"]
c_copy = list(c)
c[0] = "white";
print(c)
print(c_copy)

print("--- copyメソッドを使用する方法 ---")
c = ["red", "green", "yellow"]
c_copy = c.copy() 
c[0] = "white";
print(c)
print(c_copy)

print("--- スライスを使用する方法 ---")
c = ["red", "green", "yellow"]
c_copy = c[:] 
c[0] = "white";
print(c)
print(c_copy)
