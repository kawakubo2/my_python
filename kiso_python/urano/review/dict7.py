def fruit_price(fruit):
    """
    引数で受け取ったフルーツの単価を返す関数
    Args:
        fruit ([str]): [フルーツの日本語名]
    Returns:
        int: フルーツの単価
    """
    prices = {'バナナ': 100, 'リンゴ': 120, 'イチゴ': 300, 'オレンジ': 150, 'ブドウ': 350}
    if fruit not in prices:
        return None
    return prices[fruit]
    
fruit = input("フルーツ: ")
price = fruit_price(fruit)
if price:
    print(f"{fruit}は{price}円です。")
    
    