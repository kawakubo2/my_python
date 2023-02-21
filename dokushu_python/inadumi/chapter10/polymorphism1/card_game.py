class CardGame:
    def init(self):
        print('CardGame#init')

    def play(self):
        print('CardGame#play')

    def gameover(self):
        print('CardGame#gameover')

class Blackjack(CardGame):
    def init(self):
        print('Blackjack#init')

    def play(self):
        print('Blackjack#play')

    def gameover(self):
        print('Blackjack#gameover')

class Porker(CardGame):
    def init(self):
        print('Porker#init')

    def play(self):
        print('Porker#play')

    def gameover(self):
        print('Porker#gameover')

class Controller:
    def play_game(self, cardgame):
        cardgame.init()
        cardgame.play()
        cardgame.gameover()

if __name__ == '__main__':
    cardgame = None
    controller = Controller()
    while True:
        sw = int(input("1.Blackjack 2.Porker ... 0.終了: "))
        if sw == 0:
            break
        if sw == 1:
            cardgame = Blackjack()
        elif sw == 2:
            cardgame = Porker()
        else:
            print("1または2を選択してください")
            
        controller.play_game(cardgame)

