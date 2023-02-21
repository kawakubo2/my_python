# -*- coding: utf-8 -*-

import glob

files = glob.glob('./*')

for file in files:
    print(file)