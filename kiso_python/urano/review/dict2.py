def day_of_week(ja):
    """
    日本語の曜日から英語の曜日を返す関数
    Args:
        ja ([str]): [日本語の曜日]
    Returns:
        英語の曜日
    """
    w = { '日': 'Sunday', '月': 'Monday', '火': 'Tuesday', '水': 'Wednesday',
          '木': 'Thursday', '金': 'Friday', '土': 'Saturday'}
    if ja not in w:
        return None
    return w[ja]

ja = input('日本語の曜日: ')
print(f"{ja}曜日は英語で{day_of_week(ja)}です。")
        