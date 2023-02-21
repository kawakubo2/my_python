planets = ["水星", "金星", "地球", "火星", "木星", "土星", "天王星", "海王星","冥王星", ]

with open("planets.txt", "w", encoding="utf-8") as f:
    for planet in planets:
        f.write(planet + "\n")

