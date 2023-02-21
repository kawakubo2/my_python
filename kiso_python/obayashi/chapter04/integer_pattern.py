import re

def test(pattern, targets, desc, ok):
    print(f"------< {desc} >------")
    ptn = re.compile(pattern)
    match_counter = 0
    for target in targets:
        print(target, end='')
        results = ptn.finditer(target)
        count = 0
        for result in results:
            print(f"\t{result.group()}")
            count += 1
        if count == 1:
            match_counter += 1
        elif count == 0:
            print()
    print(f"{match_counter} / {len(targets)}\t", end="")
    if ok:
        result = "合格" if match_counter == len(targets) else "不合格"
    else:
        result = "合格" if match_counter == 0 else "不合格"
    print(result)

integer_pattern = "^(\+|-)?\d+$"

ok_list = [ "+1", "-2", "3", "+45", "-67", "89", "+831983", "-37198", "699137"]
ng_list = [ "++1", "--2", "1+", "2-", "1+2", "1.2", "12.34.56", "abc", "12a", "a234"]
test(integer_pattern, ok_list, "整数値OKテスト", True)
test(integer_pattern, ng_list, "整数値NGテスト", False)