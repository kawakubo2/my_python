import sys
"""
python review_b.py 1.1 2.2 3.3
xxxxxx sys.argv ---> ["review_b.py", 1.1, 2.2, 3.3]

range(1, 4) ---> 1, 2, 3
for i in range(1, len(sys.argv)):
    print(i)
"""
total = 0
for i in range(1, len(sys.argv)):
    total += float(sys.argv[i])
    
average = total / (len(sys.argv) -  1)
print(f"平均: {average:.3f}")