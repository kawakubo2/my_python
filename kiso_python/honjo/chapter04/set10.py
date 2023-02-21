# -*- coding: utf-8 -*-

members = [1001, 1001, 1002, 1001, 1004, 1005, 1001, 1002]

members2 = set(members)

for member in members2:
    print(member)

print("------------")
  
members3 = set()

for member in members:
    members3.add(member)
    
for member in members3:
    print(member)