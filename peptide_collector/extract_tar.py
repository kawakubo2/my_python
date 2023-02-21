import tarfile, os, glob

input_dir = "/temp/peptide/data" 
save_dir = "/temp/peptide/datasets/"
def main():
    tar_files = glob.glob(input_dir + '/*.tar')
    for filename in tar_files:
        print(filename)
        extract_tar(filename)
    
def extract_tar(filename):
    dirname = filename[:-4]
    print(dirname)
    with tarfile.open(os.path.join(dirname, filename)) as tar:
        tar.extractall(path=save_dir)

if __name__ == '__main__':
    main()