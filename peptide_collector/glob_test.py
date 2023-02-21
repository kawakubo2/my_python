import os, glob

input_dir = '/temp/peptide/datasets'
dirnames = glob.glob(input_dir + '/DS*')
for dirname in dirnames:
    print(dirname)
    filenames = glob.glob(dirname + '/*tsv')
    for filename in filenames:
        print(filename)