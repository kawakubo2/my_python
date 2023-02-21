nums1 = [1, 3, 7, 10, 9, 15, 20, 30]
nums2 = [n for n in nums1 if n % 3 == 0]
print(nums2)

langs1 = ["Python", "Java", "C", "Rust", "JavaScript", "C++", "Julia"]
langs2 = [lang for lang in langs1 if len(lang) >= 5]
print(langs2)

files1 = ["aaa.js", "bbb.py", "ccc.java", "ddd.py", "eee.cpp", "fff.rb", "ggg.py"]
python_files = [p for p in files1 if p.endswith(".py")]
print(python_files)