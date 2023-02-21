list39 = ['abc@yahoo.co.jp', 'xyz@gmail.com', 'fff.gggg@example.com', 'zzz@abc.ne.jp']

for address in list39:
    pos = address.find('@')
    print(f"{address}の@の位置:{pos}")
    print(address[pos+1:])