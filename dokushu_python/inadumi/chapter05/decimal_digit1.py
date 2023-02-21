import unicodedata

print('123'.isdecimal())
print('123'.isdigit())
print('123'.isnumeric())
print('123.45'.isdecimal())
print('123.45'.isdigit())
print('123.45'.isnumeric())

print(unicodedata.digit('５'))
print(unicodedata.numeric('参'))
print(unicodedata.numeric('Ⅷ'))

str1 = '壱弐参'

result = 0
for c in str1:
    result = result * 10 + unicodedata.numeric(c)
print(result)
