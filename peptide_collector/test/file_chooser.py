from tkinter import filedialog

base_dir = "c:/temp/kittaka_data"
file = filedialog.askopenfilename(initialdir = base_dir)

print(file)