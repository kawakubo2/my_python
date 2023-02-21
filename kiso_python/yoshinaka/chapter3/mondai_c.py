colors1 = ['yellow', 'red', 'green']
colors2 = ['黄色', '赤', '緑']

for en, ja in zip(colors1, colors2):
    # print(en + ":" + ja)
    print("{:8}:{}".format(en, ja))