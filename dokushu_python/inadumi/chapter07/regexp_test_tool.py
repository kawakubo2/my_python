import re


def test(pattern, ary, ok=True):
    print("---< {}パターンテスト >---".format("OK" if ok else "NG"))
    ptn = re.compile(pattern)
    count = 0
    match_count = 0
    for n in ary:
        print("{:10} ".format(n), end="")
        results = ptn.finditer(n)
        count = 0
        for result in results:
            count += 1
            print(result.group())
        print()
        if count == 1:
            match_count += 1
    if ok:
        if len(ary) == match_count:
            s = "合格"
        else:
            s = "不合格"
    else:
        if match_count == 0:
            s = "合格"
        else:
            s = "不合格"
    print("{}({}/{})".format(s, match_count, len(ary)))

ok_aryt = ["+1", "-2", "3", "+12", "-23", "34", "+12345", "-23456", "34567"]
test('^(?:\+|-)?\d+$', ok_aryt, True)
ng_aryt = ["+1+", "-2.0", "2+", "3-", "12a", "12.34.56", "++1", "--3", "abc1245"]
test('^(?:\+|-)?\d+$', ng_aryt, False)
