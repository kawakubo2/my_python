taro = 170.0
ichiro = 165.5
makoto = 181.5

average = (taro + ichiro + makoto) / 3
print("平均身長: " + str(average) + "cm")

member = [taro, ichiro, makoto]
average = sum(member) / len(member)
print("平均身長: " + str(average) + "cm")
print("最大:" + str(max(member)) + "cm")
print("最小:" + str(min(member)) + "cm")