from book import Book
from bookshelf import Bookshelf

shelf = Bookshelf()

# ファイルから本の情報を取り出し、本棚に詰め込む
with open('books.txt', 'r', encoding='utf_8') as f:
    for line in f:
        line = line.rstrip('\n')
        lst = line.split(',')
        shelf.add(Book(lst[0], lst[1], int(lst[2])))

shelf.printBooks()

while True:
    sw = int(input("1.追加 2.削除 3.検索 9.終了: "))
    if sw == 9:
        break

    if sw == 1:
        subject = input('題名: ')
        author = input('作者: ')
        price = int(input('価格: '))
        book = Book(subject, author, price)
        shelf.add(book)
        shelf.printBooks()
    elif sw == 2:
        subject = input('題名: ')
        book = shelf.remove(subject)
        if book is None:
            print('該当する本はありません')
        else:
            print('{}を取り出しました'.format(book.subject))
        shelf.printBooks()
    elif sw == 3:
        keywd = input('検索語: ')
        booklist = shelf.search(keywd)
        print('---< 検索結果 >---')
        if len(booklist) > 0:
            for book in booklist:
                print(book)
        else:
            print('該当なし')

    else:
        print('1～3を指定してください')