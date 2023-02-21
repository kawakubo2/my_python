def greeting(ja, lang):
    """
    引数の日本語の挨拶から第2引数で指定した言語の挨拶を返す関数
    例) greeting("おはよう", "en") ---> "Good Morning"
        greeting("おはよう", "de") ---> "Guten Morgen"
    Args:
        ja ([str]): [日本語の挨拶文]
        lang (str): [変換したい言語]
    Returns:
        str: 挨拶文
    """
    greetings = {
        "おはよう": {"en": "Good morning.", "de": "Guten morgen.", "it": "Buon giorno."},
        "こんにちは": {"en": "Good afternoon.", "de": "Hallo.", "it": "Ciao."},
        "こんばんは": {"en": "Good evening.", "de": "Guten abend.", "it": "Buona serata."}
    }
    if ja not in greetings:
        return None
    if lang not in ('en', 'de', 'it'):
        return None
    
    return greetings[ja][lang]

print(greeting("おはよう", "it"))
print(greeting("こんにちは", "en"))
print(greeting("こんばんは", "de"))