def random_item_list(item_dic):
    import random
    result = []
    for item, num in item_dic.items():
        result += [item] * num
    random.shuffle(result)
    return result

if __name__ == '__main__':
    answer = random_item_list({'イギリス': 6, 'スペイン': 8, 'イタリア': 14,
                            'ドイツ': 3, 'フランス': 9})
    print(answer)