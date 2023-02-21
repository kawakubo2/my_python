taro = 170.0
ichiro = 165.5
makoto = 181.5

average = (taro + ichiro + makoto) / 3
print("平均身長: " + str(average) + "cm")
print("平均身長: %.1fcm" % (average))
print("平均身長: {:.1f}cm".format(average))
print(f"平均身長: {average:.1f}cm")