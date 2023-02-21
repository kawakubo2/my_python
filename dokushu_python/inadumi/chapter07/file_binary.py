import os

with open(os.path.dirname(__file__) + '/cat2.jpg', 'rb') as reader,\
    open(os.path.dirname(__file__) + '/output.jpg', 'wb') as writer:
    while d := reader.read(1):
        writer.write(d) 