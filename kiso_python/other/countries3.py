country_count = {}

with open("answer.txt", "r", encoding="utf_8") as in_file:
    for line in in_file:
        country = line.rstrip("\n")
        if country in country_count:
            country_count[country] += 1
        else:
            country_count[country] = 1

for country in sorted(country_count.items(), key = lambda v: v[1], reverse = True):
    print("{}: {}".format(country[0], country[1]))
