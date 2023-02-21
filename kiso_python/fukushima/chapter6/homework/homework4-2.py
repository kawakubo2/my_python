# -*- coding: utf-8 -*-

#宿題4（8/29）ジェネレータ関数を用いた処理の作成

filepath='.\data'
infilename='infile.txt'
outfilename='暗号化.txt'
outfilename2='復号.txt'


infile = open(filepath + '\\' + infilename,'r',encoding='utf_8')

textdata=infile.readlines()

def angou(textdata):
    conv_str='' 
    for str1 in textdata:
        conv_str=''
        for s in str1:
            conv_byt=s.encode('utf_8')
            conv_int=int.from_bytes(conv_byt,'little')
            conv_int += 1
            conv_byt2=bytes([conv_int])
            conv_str += conv_byt2.decode('utf_8')
        yield conv_str

outfile = open(filepath + '\\' + outfilename,'w',encoding='utf_8')
for tes1 in angou(textdata):
    outfile.write(tes1)

infile.close()
outfile.close()


infile = open(filepath + '\\' + outfilename,'r',encoding='utf_8')
textdata=infile.read()

def fukugou(textdata):
    conv_str='' 
    for s in textdata:
        if not int.from_bytes(s.encode('utf_8'),'little') == 0:
            conv_byt=s.encode('utf_8')
            conv_int=int.from_bytes(conv_byt,'little')
            conv_int=conv_int - 1
            conv_byt2=bytes([conv_int])
            conv_str=conv_str + conv_byt2.decode('utf_8')
        else:
            pass
    return conv_str

outfile = open(filepath + '\\' + outfilename2,'w',encoding='utf_8')
outfile.write(fukugou(textdata))

infile.close()
outfile.close()

