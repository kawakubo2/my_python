"""
python commandline.py 10 20 30
              ↑        ↑  ↑  ↑
              0        1  2  3
"""

import sys

for i, arg in enumerate(sys.argv):
    print(f'{i}: {arg}')
