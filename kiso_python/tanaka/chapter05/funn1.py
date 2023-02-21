def calc_weight(init, month):
    result = init
    for i in range(month):
        result *= 1.1
    return result

w = 10
m = 36
print(f"{w}kgの豚は{m}か月後には{calc_weight(w, m)}kgになっています。")