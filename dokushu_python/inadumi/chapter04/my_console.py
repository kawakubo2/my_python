class MyConsole:

    @classmethod
    def input_int_range(cls, min, max, prompt):
        if not(type(min) == int and type(max) == int):
            raise Exception('minまたはmaxが整数値ではありません')
        if max < min:
            raise Exception('下限と上限が逆転しています')
        while True:
            try:
                n = int(input(prompt + ': '))
                if min <= n <= max:
                    result = n
                    break
                else:
                    print('{}～{}の範囲で入力してください'.format(min, max))
            except:
                print('数値の形式に誤りがあります')
        return result

if __name__ == '__main__':
    try:
        score = MyConsole.input_int_range(0, 10, 'ポイント')
        print('点数 =', score)
    except Exception as e:
        print(e)