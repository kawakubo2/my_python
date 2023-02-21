colors = {"red", "green", "blue"}
colors.add("orange")
print(colors)
colors.add("red")
print(colors)
colors.discard("red")
print(colors)

my_color = {"yellow", "white", "gray", "orange"}
colors.update(my_color)
print(colors)