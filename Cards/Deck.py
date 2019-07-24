import Cards.Card
import random


class Deck:
    cardNames = ["Ambassador", "Assassin", "Captain", "Contessa", "Duke"]
    cards = []

    def __init__(self, num):
        self.numOfEach = num
        for i in range(self.numOfEach):
            for j in range(len(self.cardNames)):
                self.cards.append(Cards.Card(self.cardNames[j]))


    def popCards(self, num):
        temp = []
        for i in range(num):
            temp.append(self.cards[i])
        for j in range(num):
            self.cards.remove(0)
        return temp

    def shuffle(self):
        temp = []
        while len(self.cards) > 0:
            ind = random.randint(0, len(self.cards))
            temp.append(self.cards[ind])
            self.cards.remove(ind)
        self.cards = temp
