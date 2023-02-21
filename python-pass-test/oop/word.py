# -*- coding: utf-8 -*-

class Word:
    def __init__(self, english, japanese, pos, filename='explist.txt'):
        self.english = english
        self.japanese = japanese
        if pos == '1':
            tmp = '名詞'
        elif pos == '2':
            tmp = '動詞'
        elif pos == '3':
            tmp = '形容詞'
        elif pos == '4':
            tmp = '助動詞'
        elif pos == '5':
            tmp = '副詞'
        self.pos = tmp
        self.explist = []
        #self.read_exp_list()
    def add_exp(self, exp):
        self.explist.append(exp)
                
    def __str__(self):
        print('english={}, japanese={}, pos={}'.format(self.english, self.japanese, self.pos))
        for i, exp in enumerate(self.explist):
            return str(i + 1) + ':' + exp
                

class WordList:
    wordlist = {}
    def add(word):
        if word.english not in WordList.wordlist:
            WordList.wordlist[word.english] = {}
            WordList.wordlist[word.english][word.pos] = word
        else:
            if word.pos not in WordList.wordlist[word.english].keys():
                WordList.wordlist[word.english][word.pos] = word
            else:
                WordList.wordlist[word.english][word.pos].explist += word.explist
    
    def search(search_word):
        if search_word in WordList.wordlist:
            return WordList.wordlist[search_word]
                               
while(True):
    print('単語を登録します。終了するには「💤」を入力してください')
    english = input('英単語 > ')
    if english == 'zzz':
        break
    japanese = input('日本語 > ')
    pos = input('品詞 1:名詞 2:動詞 3:形容詞 4:助動詞 5:副詞 > ')
    word = Word(english, japanese, pos)
    exp = input('例文 > ')
    word.add_exp(exp)
    WordList.add(word)
    
while(True):
    print('単語を検索します。終了するには「zzz」を入力してください')
    english = input('英単語 > ')
    if english == 'zzz':
        break
    target_word = WordList.search(english)
    if target_word is not None:
        for word_pos in target_word.items():
            print('品詞:{}'.format(word_pos[0]))
            print('日本語:{}'.format(word_pos[1].japanese))
            for i, exp in enumerate(word_pos[1].explist):
                print('{}:{}'.format(i+1, exp))
         