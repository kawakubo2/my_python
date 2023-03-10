DIAL_CODES = [
    (86, 'China'), (91, 'India'), (1, 'United States'), (62, 'Indonesia'), (55, 'Brazil'), (92, 'Pakistan'),
    (880, 'Bangladesh'), (234, 'Nigeria'), (7, 'Rusia'), (81, 'Japan')
]

country_code = {country: code for country, code in DIAL_CODES}
print(country_code)

print({code: country.upper() for code, country in country_code.items() if code < 66})