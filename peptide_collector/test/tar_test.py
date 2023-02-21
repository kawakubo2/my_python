import tarfile, os

base_dir = os.path.dirname(__file__)
filename = 'DS790_1.tar'
dirname = filename[:-4]
print(dirname)
with tarfile.open(os.path.join(base_dir, 'data', filename)) as tar:
    tar.extractall(path=os.path.join(base_dir, 'datasets'))

