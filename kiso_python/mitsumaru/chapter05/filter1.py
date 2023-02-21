def larger_5(inch):
    return inch > 5

inches = [9, 5.5, 6, 4, 6.5, 10]
cms = []
for inch in filter(larger_5, inches):
    cms.append(inch * 2.54)
print(cms)

flowers = ["Sun Flower", "Tulip", "Rose", "Morning Glory"]

for f in flowers:
    print(len(f.replace(' ', '')))

for flower in filter(lambda s: len(s.replace(' ', '')) > 5, flowers):
    print(flower)

names = ['Yamada', 'Tanaka', 'Suzuki', 'Yamamoto', 'Takeda', 'Yamaguchi']

for name in filter(lambda name: name.startswith("Y"), names):
    print(name)

for name in filter(lambda name: name[0] == "Y", names):
    print(name)

cms = [inch * 2.54 for inch in inches if inch > 5]
print(cms)

cms = list(map(lambda inch: inch * 2.54, filter(lambda inch: inch > 5, inches)))
print(cms)

lst1 = ["fly", "good", "ABC", "Bad", "Woo", "Foo", "and"]
lst2 = sorted(lst1, key=str.upper)
print(lst2)