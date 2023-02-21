import re



def test(pattern, targets, ok, desc=""):
    print(f"---< {desc } >---")
    regexp = re.compile(pattern)
    ok = 0
    ng = 0
    count = 0
    for target in targets:
        print(f"{target} ", end="")
        count += 1
        result = regexp.findall(target)
        if len(result) == 1:
            ok += 1
        else:
            ng += 1
        print()    
    if ok:
        if ok == len(targets):
            result = "合格"
        else:
            result = "不合格"
    else:
        if ok == 0:
            result = "合格"
        else:
            result = "不合格"
    print(f"【{result}】 {ok}/{len(targets)}")

ok_pattern = ['1', '2', '+2', '-3', '12', '+34', '-56', '12348', '+389387', '-83197', '1.2', \
     '+2.3', '+4.5', '12.34', '+23.45', '-45.678']
    
ng_pattern = ['1+', '++2', '--3', '1.2.3', '12.4a', 'a123', '13b424', '12.a873.32']

float_pattern = r'^[\+-]?\d+(\.\d+)?$'

test(float_pattern, ok_pattern, True, "小数点正常パターン")
test(float_pattern, ng_pattern, False, "小数点異常パターン")