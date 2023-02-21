from input_util import input_positive_int

age = input_positive_int('年齢')

if age < 13:
    print('子供料金です。')
else:
    print('大人料金です。')
    
    