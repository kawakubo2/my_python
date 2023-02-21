# -*- coding: utf-8 -*-

src_images = [
        "E.png",
        "D.png",
        "C.png",
        "H1.png",
        "H2.png"
]

dest = []

while True:
    line = input('>')
    if line == '_':
        break
    dest.append(line.split(','))
    
for row in dest:
    for num in row:
        print('<img src="' + src_images[int(num)] + '" alt="" />')
    print('<br>')
