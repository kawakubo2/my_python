# -*- coding: utf-8 -*-

class Okashi:
    def __init__(self, name, maker, seibun_list):
        self.__name = name
        self.__maker = maker
        self.__seibun_list = seibun_list
        
    def get_name(self):
        return self.__name
    
    def get_maker(self):
        return self.__maker
    
    def add_seibun(self, seibun):
        if seibun not in self.__seibun_list:
            self.__seibun_list.append(seibun)
    
    def del_seibun(self, seibun):
        if seibun in self.__seibun_list:
            self.__seibun_list.remove(seibun)
            
    def check_seibun(self, seibun):
        return seibun in self.__seibun_list
            
    def print_seihin(self):
        print('【製品名: {}】'.format(self.__name))
        print('【メーカー: {}】'.format(self.__maker))
        print('---< 成分 >---')
        for seibun in self.__seibun_list:
            print("・{} : ".format(seibun))
            
            
okashi = Okashi('おにぎり', 'マスヤ', ['うるち米(アメリカ産、国産)', '植物油', '醤油', '砂糖', 'デキストリン'])

okashi.print_seihin()

okashi.add_seibun('デキストリン')

if (okashi.check_seibun('醤油')):
    print('醤油は苦手だからパス')
        
        
    