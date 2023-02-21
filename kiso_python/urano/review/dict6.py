def fruits_counter(fruits):
    """
    フルーツの名前が入ったリストを受け取り、それぞれのフルーツが
    何個あるかを辞書として返す関数
    Args:
        fruits: [list] フルーツの名前が入ったリスト
    Returns:
        [dict]: [フルーツをキー、個数を値とする辞書]
    """
    result = {}
    for fruit in fruits:
        if fruit in result:
            result[fruit] += 1
        else:
            result[fruit] = 1
    return result
    
counter = fruits_counter(['バナナ', 'リンゴ', 'バナナ', 'ミカン', 'リンゴ', 'バナナ'])
print(counter)

