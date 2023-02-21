def log_func(func):
    def inner(*args, **keywds):
        print('-------------------')
        print(f'Name: {func.__name__}')
        print(f'Args: {args}')
        print(f'keywds: {keywds}')
        print('-------------------')
        return func(*args, **keywds)
    return inner

@log_func
def hoge(x, y, m='bar', n='piyo'):
    print(f'hoge: {x}-{y}/{m}-{n}')

hoge(15, 37, m="ほげ", n="ぴよ")

@log_func
def foo(a, b, c, d, x=1, y= 2, z=3):
    print(f'foo: {a} {b} {c} {d} / x={x} y={y} z={z}')

foo('a', 'bb', 'ccc', 'dddd', x=-100, y=200, z=-300)
