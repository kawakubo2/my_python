list15 = [ 'strawberry', 'banana', 'watermelon', 'grape', 'pineapple', 
          'apple', 'kiwi', 'plum', 'raspberry']

a_counter = []
for fruit in list15:
    count = 0
    for c in fruit:
        if c ==  'a':
            count += 1
    a_counter.append(count)

print(a_counter)

word_len_list = []
for fruit in list15:
    word_len_list.append(len(fruit))
    
print(word_len_list)
    
sorted_list = sorted(list15, key = lambda fruit : len(fruit))
print(sorted_list)
