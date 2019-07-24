class Player:
    cards = []
    coins = 2
    lives = 2

    def __init__(self, name, uuid):
        self.name = name
        self.uuid = uuid

    def getName(self):
        return self.name

    def getCoins(self):
        return self.coins

    def getUUID(self):
        return self.uuid

    def getCards(self):
        return self.cards

    def setCards(self, cards):
        self.cards = cards

    def alterCoins(self, num):
        self.coins += num
        return self.getCoins()

    def findCardInd(self,card):
        i =0
        for c in self.cards:
            if(card.getName() == c.getName()):
                return i

    def loseCard(self,card):
        ind = self.findCardInd(card)
        self.cards.remove(ind)
        # ADD TO DISCARD DECK



