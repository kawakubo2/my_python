colors1 = ["yellow", "red", "green", "lemon chiffon"]
colors2 = ["黄色", "赤", "緑", "レモンシフォン"]

max_len = max([len(color) for color in colors1])

for en, ja in zip(colors1, colors2):
    print(f"{en:{max_len}} : {ja}")