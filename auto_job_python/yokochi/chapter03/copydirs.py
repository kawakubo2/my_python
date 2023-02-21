# copydirs.py
import shutil, os

base_dir = os.path.dirname(__file__)

source = os.path.join(base_dir, 'dir1')
dest = os.path.join(base_dir, 'dir2')

shutil.copytree(source, dest)

shutil.rmtree(source)