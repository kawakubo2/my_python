height = [180, 165, 159, 171, 155]
print(height)
print(height[0])
print(height[1])
print(height[2])
print(height[3])
print(height[4])

for h in height:
    print(h)

height[1] = 182

for h in height:
    print(h)

print("最後の要素は: ")
print(height[len(height) - 1])
print("後ろの方から取り出す: ")
print(height[-1])
print(height[-2])
print(height[-3])
print(height[-4])
print(height[-5])