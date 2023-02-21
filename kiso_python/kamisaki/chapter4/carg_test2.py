import sys
"""
python carg_test2.py 11 2.0 3.5 4.1 1.5 6.7
sys.argv    0         1   2   3   4   5   6
"""

total = 0
for i in range(1, len(sys.argv)):
    total += float(sys.argv[i])

print(f"総和: {total}")

print('こんにちは、世界！')