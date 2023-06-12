a = [['AAA-ON', 'BBB-ON'],['AAA-ON', 'BBB'],['AAA-ON', None],['AAA', 'BBB-ON'],['AAA', None],['AAA','BBB'],['AAA', None],[None, 'BBB'],[None, None]]
for b in a:
    print(f"処理前: {b}")
    cnt = len([e for e in b if e is not None and e.endswith('-ON')])
    if cnt == 2:
        product = 'AAA'
    elif cnt == 1:
        product = 'BBB'
    else:
        product = 'CCC'
        
    d = {'poductName': product, 'value1': b[0], 'value2': b[1]}
    print(f"処理後: {d}")