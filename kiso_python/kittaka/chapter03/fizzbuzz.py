for n in range(1, 101):
    """
    3の倍数     ・・・Fizz
    5の倍数     ・・・Buzz
    3かつ5の倍数・・・FizzBuzz
    """
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
    