import Cards


class GameInfo:
    players = []
    numOfEachCard = 3
    numPlayers = 0
    activeDeck = []
    discardDeeck = []
    def __init__(self, gameCode):
        self.gameCode = gameCode

    def update(self):
        if self.numPlayers >= 3 or self.numPlayers <= 6:
            self.numOfEachCard = 3
        elif self.numPlayers == 7 or self.numPlayers == 8:
            self.numOfEachCard = 4
        else:
            self.numOfEachCard = 5

    def insertPlayer(self, player):
        self.players.append(player)
        self.numPlayers += 1
        self.update()

    def startGame(self):
        self.activeDeck = Cards.Deck()

    def getNumOfEachCard(self):
        return self.numOfEachCard

    def searchPlayersByUUID(self, uuid):
        for player in self.players:
            if player.getUUID() == uuid:
                return player

    def searchPlayersByName(self, name):
        for player in self.players:
            if player.getName() == name:
                return player

    def getPlayer(self, identifierType, identifier):
        if identifierType == "uuid":
            return self.searchPlayersByUUID(identifier)
        else:
            return self.searchPlayersByName(identifier)

    def getPlayerCoins(self, idType, id):
        self.getPlayer(idType, id).getCoins()

    def getPlayerCards(self, idType, id):
        self.getPlayer(idType, id).getCards()

    def alterPlayerCoins(self, idType, id, num):
        self.getPlayer(idType, id).alterCoins(num)

    def playerLoseCard(self, idType, id, card):
        self.getPlayer(idType, id).loseCard(card)