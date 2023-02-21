print('リストの並び順を元に戻す必要がない場合は、sortメソッド')
sports1 = ['ラグビー', 'テニス', 'バスケ', 'サッカー', 'マラソン']
sports1.sort()
print('sports1=', sports1)

print('リストの並び順は元のままで、戻り値として並べ替えたリストが比すような場合はsort関数')
sports1 = ['ラグビー', 'テニス', 'バスケ', 'サッカー', 'マラソン']
sports2 = sorted(sports1)
print('sports1=', sports1)
print('sports2=', sports2)
