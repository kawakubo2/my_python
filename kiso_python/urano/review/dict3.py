def get_en_color(ja):
    """
    日本語の色名を引数で受け取り、英語の色名を返す関数
    Args:
        ja ([str]): [日本語の色名]
    Returns:
        英語の色名
    """
    c = {'赤': 'Red', '青': 'Blue', '黒': 'Black', '白': 'White', '緑': 'Green'}
    
    if ja not in c:
        return None
    return c[ja]

ja = input('日本語の色名: ')
en_color = get_en_color(ja)
if en_color:
    print(f"{ja}は英語で「{en_color}」です。")