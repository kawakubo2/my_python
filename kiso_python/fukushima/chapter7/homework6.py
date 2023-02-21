# -*- coding: utf-8 -*-
#宿題１（9/26）リスト、タプル、辞書、集合のいずれかを用いた処理の作成

import random

class CreateCode:

    def __init__(self,dif=1):
        self.__dif = dif
        
    def set_dif(self,dif):
        self.__dif = dif

    def get_dif(self):
        return self.__dif
    dif = property(get_dif,set_dif)


    def question_code(self):
        lst_num = []
        while len(lst_num) < 4 and self.__dif in (1,2):
            rand_value = random.randrange(0,10)
            if self.__dif == 1:
                if rand_value not in lst_num:
                    lst_num.append(rand_value)

            if self.__dif == 2:
                lst_num.append(rand_value)
        return lst_num

class InputCode:
    def __init__(self,num='',hit=0,blow=0):
        self.__num = num
        self.__hit = hit
        self.__blow = blow
    
    def set_num(self,num):
        self.__num = num
    # def get_num(self):
    #     return self.__num
    num = property(None,set_num)
        
    def input_chk(self,dif):
        try:
            int(self.__num)
            if len(self.__num) != 4:
                print(self.__num)
                print('「0~9」の数字をそれぞれ1度ずつ使用した４桁の数字を入力してください。')
                return False
            if dif == 1 and len(set(self.__num)) != 4:
                print(self.__num)
                print('「0~9」の数字をそれぞれ1度ずつ使用した４桁の数字を入力してください。')
                return False
        except ValueError:
            print('「0~9」の数字をそれぞれ1度ずつ使用した４桁の数字を入力してください。')
            return False
        return True            

    def code_chk(self,question):
        self.__hit = 0
        self.__blow = 0
        for i,n in enumerate(self.__num):
            if int(n) == question[i]:
                self.__hit += 1
            else:
                if int(n) in (question):
                    self.__blow += 1
        return self.__hit,self.__blow

if __name__ == '__main__':
    cpu1 = CreateCode()
    question = []
    print('コードブレーカー')
    print('隠された4桁の数字****を当てればあなたの勝ちです。')
    while len(question) == 0:
        cpu1.dif = int(input('難易度選択　１：ふつう　２：難しい　９：終了する：'))
        if cpu1.dif == 1:
            question = cpu1.question_code()
            print('「0~9」の数字をそれぞれ1度ずつ使用した４桁の数字を入力してください。')
            print('挑戦回数は5回です')
        elif cpu1.dif == 2:
            question = cpu1.question_code()
            print('４桁の数字を入力してください。')
            print('挑戦回数は5回です。')
        elif cpu1.dif == 9:
            print('ゲームを終了しました。')
            break
        else:
            print('1 or 2 or 9から選択してください。')
    
    player1 = InputCode()
    
    if cpu1.dif != 9:
        for cnt in range(1,6):
            player1.num = input('{}回目の挑戦：'.format(cnt))
            while player1.input_chk(cpu1.dif) == False:
                player1.num = input('{}回目の挑戦：'.format(cnt))
            result=player1.code_chk(question)
            if result[0] == 4:
                print('コードブレイクに成功しました。あなたの勝ちです。')
                break
            else:
                if cnt == 5:
                    print('コードブレイクに失敗しました。あなたの負けです。\n正解のコードは「{}{}{}{}」です。'.format(question[0],question[1],question[2],question[3]))
                else:
                    print('{}ヒット　{}ブロー'.format(result[0],result[1]))

