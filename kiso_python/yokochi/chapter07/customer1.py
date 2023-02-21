class Customer:
    # 初期化メソッド(コンストラクタ)
    # 引数=valは、引数を省略した場合、valを使用するという意味
    def __init__(self, number, name, height=0):
        self.number = number
        self.name = name
        self.height = height

# インスタンス化
# クラスからインスタンスを生成(内部では__init__メソッドが動く)
taro = Customer(101, '斉藤太郎')
print(f'{taro.number}: {taro.name} {taro.height}cm')

taro.height = 175
print(f'{taro.number}: {taro.name} {taro.height}cm')