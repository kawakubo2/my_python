import pickle
import os

with open(os.path.dirname(__file__) + '/book.bin', 'rb') as file:
    b = pickle.load(file)
    print(b)