word = "基礎Python第2版"

def is_valid_index(string, index):
    if not (0 <= index < len(string)):
        raise ValueError(f"インデックスが範囲外: {index}")

def substring(string, begin, end):
    is_valid_index(string, begin)
    is_valid_index(string, end - 1)
    return string[begin: end]

print(substring(word, 2, 8))
