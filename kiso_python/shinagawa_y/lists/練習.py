import matplotlib.pyplot as plt

import matplotlib.font_manager as fm
import os
import csv
path = 'C:\Windows\Fonts\msgothic.ttc'
prop = fm.FontProperties(fname=path)
with open(os.path.dirname(__file__) + '/九州大学3.csv',encoding='UTF-8') as cvsfile:
    reader = csv.reader(cvsfile,delimiter=',')
    data = [row for row in reader]
title = '九州大学入試における\nセンター得点と合格・不合格者人数の関係\n({}学部{}学科)'
# 学部名取得
gakubu = []
gakka = []
for i in range(8):
    gakubu.append(data[0][7 * i + 3])
    gakka.append(data[1][7 * i + 1])


# =============================================================================
# p=data[8:48]
# =============================================================================
for i in range(8):
    x = [int(d[7 * i + 0]) for d in data[8:48]]
    goukaku = [d[7 * i + 5] for d in data[8:48]]
    fugoukaku = [d[7 * i + 6] for d in data[8:48]]
    # =============================================================================
    # w=0.35
    # =============================================================================
    
    # =============================================================================
    # x1=[xx-w/2 for xx in x]
    # x2=[xx-w/2 for xx in x]
    # plt.bar(x1,goukaku,w,label=data[7][5])
    # plt.bar(x2,fugoukaku,w,label=data[7][6])
    # =============================================================================
    plt.plot(x,goukaku,label=data[7][5])
    plt.plot(x,fugoukaku,label=data[7][6])
    plt.title(title.format(gakubu[i], gakka[i]),fontproperties=prop,fontsize=15)
    plt.legend(loc='best',prop=prop)
    plt.xlabel(data[7][0],fontproperties=prop)
    plt.ylabel('人数',fontproperties=prop)
    fig = plt.figure()
    fig.savefig("graph",format='png',bbox_inches="tight")

# =============================================================================
# plt.savefig('graph.pdf',format='pdf',bbox_inches="tight")
# =============================================================================
plt.show()
