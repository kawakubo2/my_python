countries = ["US", "China", "Germany", "Japan", "India"]

def gdp_ranking(countries):
    for i, country in enumerate(countries):
        print(f"{i+1}.{country}")

gdp_ranking(countries)