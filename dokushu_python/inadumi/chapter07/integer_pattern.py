import re


def test(pattern, ary, ok=True):
    print("---< {}パターンテスト >---".format("OK" if ok else "NG"))
    ptn = re.compile(pattern)
    count = 0
    match_count = 0
    for n in ary:
        print("{:10} ".format(n), end="")
        results = ptn.findall(n)
        if len(results) == 1:
            print(results[0])
            match_count += 1
        else:
            print()
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


