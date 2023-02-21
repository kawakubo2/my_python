from collections import deque

dq1 = deque(range(10))
print(dq1)
# 右に追加1個追加
dq1.append(10)
dq1.append(11)
print(dq1)
# 左に追加1個追加
dq1.appendleft(-1)
dq1.appendleft(-2)
print(dq1)
# 右にリストで指定した分追加
dq1.extend([12, 13, 14])
print(dq1)
# タプルを使って追加することも可能
dq1.extend((15, 16))
print(dq1)
# 左にリストで指定した分追加
# ただし、指定したリストの左から追加されるため
# 右に追加するのに比べ直感的ではない
dq1.extendleft([-3, -4])
print(dq1)
# タプルを使っても追加できる
dq1.extendleft((-5, -6, -6))
print(dq1)
# 右からから削除
e1 = dq1.pop()
print('削除した要素:', e1)
print('削除後:', dq1)
# 左から削除
e2 = dq1.popleft()
print('削除した要素:', e2)
print('削除後:', dq1)
# 右に3個回転
dq1.rotate(3)
print(dq1)
# 左に回転するメソッドはないが、引数に負の値を指定すると左に回転
# 左に9個回転
dq1.rotate(-9)
print(dq1)
