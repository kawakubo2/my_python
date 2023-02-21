fruits = ['banana', 'orange', 'apple', 'banana', 'pear', 'apple',
          'banana', 'orange', 'apple', 'grape', 'banana', 'grape',
          'orange', 'banana', 'apple', 'banana', 'pineapple', 'banana']

results = {}

for f in fruits:
    if f in results:
        results[f] += 1
    else:
        results[f] = 1
        
for fruit, num in results.items():
    print(f"{fruit}: {num}") 