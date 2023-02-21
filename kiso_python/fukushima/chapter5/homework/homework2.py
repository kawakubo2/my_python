# -*- coding: utf-8 -*-
#宿題２（8/15）可変長変数または辞書変数を利用した関数の作成


colors=['黒','赤','緑','青','白']
colors_code=['\x1b[30m','\x1b[31m','\x1b[32m','\x1b[34m','\x1b[37m']
font_colors={color:code for (color,code) in zip(colors,colors_code)}

# =============================================================================
# inp_msg=input('メッセージを入力してください。：')
# inp_color=input('フォントカラーを{}から指定してください。（省略の場合はそのまま実行）\n'
#                 '省略時は白になります。複数選択する場合は,で区切ってください。例）赤,青\n：'.format(colors))
# 
# =============================================================================
#入力されたメッセージとフォントカラーをもとにメッセージを指定の色で表示する
#フォントカラー指定が複数の場合は指定の数分メッセージを表示する
def set_font_color(msg='',*set_color,**color_dic):
    try:
        if msg == '':
            print('メッセージがありません。メッセージを入力してください。')
            return False
        else:           
            for i,j in enumerate(set_color):
                #'\x1b[0m'は効果をリセットする
                if set_color[i] == '':
                    print('\x1b[0m' + msg)
                else:
                    print(color_dic[set_color[i]] + msg + '\x1b[0m')
            return True
    
    except KeyError:
        print('色の指定が誤っています。'.format(list(color_dic.keys())))
        print('省力するか{}のいずれかを入力して下さい。'.format(list(color_dic.keys())))
        
        return False

#set_font_color(inp_msg,'赤','白','青','緑','黒',**font_colors)
result1 = False
while result1 == False:
    inp_msg=input('メッセージを入力してください。：')
    inp_color=input('フォントカラーを{}から指定してください。（省略の場合はそのまま実行）\n'
                    '省略時は白になります。複数選択する場合は,で区切ってください。例）赤,青\n：'.format(colors))
    result1 = set_font_color(inp_msg,*inp_color.split(','),**font_colors)

