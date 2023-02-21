# -*- coding: utf-8 -*-

#宿題4（8/29）ジェネレータ関数を用いた処理の作成

filepath='./data'
infilename='infile.txt'
outfilename='outfile.txt'

infile = open(filepath + '\\' + infilename,'r',encoding='utf_8')

textdata=infile.readlines()

#改行コード除去
def remove_newline(textdata):
    for str1 in textdata:
        temp = str1.replace('\n','')
        yield temp

outfile = open(filepath + '\\' + outfilename,'w',encoding='utf_8')

for tes1 in remove_newline(textdata):
    print(tes1,'メモリ使用量：{}'.format(tes1.__sizeof__()))
    outfile.write(tes1)

#ジェネレータ関数でない場合の検証
def remove_newline2(textdata):
    temp=''
    for str1 in textdata:
        temp = temp + str1.replace('\n','')
    return temp

outfile2 = open(filepath + '\\outfile2.txt','w',encoding='utf_8')
tes2=remove_newline2(textdata)
print(tes2,'メモリ使用量：{}'.format(tes2.__sizeof__()))
outfile2.write(tes2)
outfile2.close()


infile.close()
outfile.close()
