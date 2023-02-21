# function2.py

s1 = "This is a pen."

def get_length_without_space1(s):
    """
    引数で受け取った文字列から半角空白の除いた文字数を返す関数
    Args:
        s ([str]): [文字列]
    Returns:
        int 空白を除いた文字数
    """
    counter = 0
    for c in s:
        if c != ' ':
            counter += 1
    return counter

str_count1 = get_length_without_space1(s1)
print(f"空白を除いた文字数: {str_count1}")

def get_length_without_space2(s):
    return len(s.replace(' ', ''))

str_count2 = get_length_without_space2(s1)
print(f"空白を除いた文字数: {str_count2}")

def count_alphabet1(s):
    """
    文字列に含まれるアルファベットの数を返す関数
    Args:
        s ([str]): [文字列]
    Returns:
        int 文字数
    """
    counter = 0
    for c in s:
        if "A" <= c <= "Z" or "a" <= c <= "z":
            counter += 1
    return counter
    
str_count3 = count_alphabet1(s1)
print(f"文字列に含まれるアルファベットの数: {str_count3}")    

def count_alphabet2(s):
    counter = 0
    for c in s:
        if c.isalpha():
            counter += 1
    return counter

str_count4 = count_alphabet2(s1)
print(f"文字列に含まれるアルファベットの数: {str_count4}")    

def count_alphabet3(s):
    return len([c for c in s if c.isalpha()])
# ['T', 'h', 'i', 's', 'i', 's', 'a', 'P', 'e', 'n']
str_count5 = count_alphabet3(s1)
print(f"文字列に含まれるアルファベットの数: {str_count5}")    

numbers1 = [5, 4, 2, 1, 6]
numbers2 = [10, 3, 7]
numbers3 = [1, 2, 3, 6]
numbers4 = [10, 5, 15, 20]
def total_arrays(nums1, nums2):
    nums3 = nums1 + nums2
    return sum(nums3)

print(f"合計: {total_arrays(numbers1, numbers2)}")

def total_arrays2(*numbers_array):
    numbers = []
    for nums in numbers_array:
        numbers += nums
    return sum(numbers)

print(f"合計: {total_arrays2(numbers1, numbers2, numbers3, numbers4)}")

def total_num(*num):
    total = 0
    for n in num:
        total += n
    return total
    
total1 = total_num(5, 1, 10, 3, 4, 6)
print(f"合計: {total1}")

def count_item(*items):
    counter = {}
    for item in items:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    return counter
    
dic1 = count_item("りんご", "バナナ", "オレンジ", "いちご", "なし", "いちご", "バナナ", "バナナ")
print(dic1)
# { "りんご": 1, "バナナ": 3, "オレンジ": 1, "いちご": 2, "なし": 1}

dic2 = count_item('Python', 'Java', 'C#', 'Python', 'C++', 'C#', 'Java', 'Python', 'PHP', 'Python', 'PHP')
print(dic2)

dic3 = count_item("鈴木", "加藤", "田中", "佐藤", "佐藤", "山田", "田中", "佐藤")
print(dic3)

rectangles = [(5, 4), (9, 6), (7, 8), (3, 6)]
def calc_total_area(rects):
    """
    幅と高さからなるタプルのリストから、長方形の面積の合計を返す関数
    """