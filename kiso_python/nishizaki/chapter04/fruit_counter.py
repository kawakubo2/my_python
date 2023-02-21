fruits = ['banana', 'orange', 'apple', 'banana', 'pear', 'apple',
          'banana', 'orange', 'apple', 'grape', 'banana', 'grape',
          'orange', 'banana', 'apple', 'banana', 'pineapple', 'banana']

banana_counter = 0
orange_counter = 0
apple_counter = 0
pear_counter = 0
grape_counter = 0
pineapple_counter = 0

for fruit in fruits:
    if fruit == 'banana':
        banana_counter += 1
    elif fruit == 'orange':
        orange_counter += 1
    elif fruit == 'apple':
        apple_counter += 1
    elif fruit == 'pear':
        pear_counter += 1
    elif fruit == 'grape':
        grape_counter += 1
    elif fruit == 'pineapple':
        pineapple_counter += 1
        
print(f"banana: {banana_counter}")
print(f"orange: {orange_counter}")
print(f"apple: {apple_counter}")
print(f"pear: {pear_counter}")
print(f"grape: {grape_counter}")
print(f"pineapple: {pineapple_counter}")