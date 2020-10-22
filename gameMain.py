import discord
import random
import gameObjects

class gameMain:

    ROLE_LIST_5 =  ["LIBERAL", "LIBERAL", "LIBERAL", "FASCIST", "HITLER"]
    ROLE_LIST_6 =  ["LIBERAL", "LIBERAL", "LIBERAL", "LIBERAL", "FASCIST", "HITLER"]
    ROLE_LIST_7 =  ["LIBERAL", "LIBERAL", "LIBERAL", "LIBERAL", "FASCIST", "FASCIST", "HITLER"]
    ROLE_LIST_8 =  ["LIBERAL", "LIBERAL", "LIBERAL", "LIBERAL", "LIBERAL", "FASCIST", "FASCIST", "HITLER"]
    ROLE_LIST_9 =  ["LIBERAL", "LIBERAL", "LIBERAL", "LIBERAL", "LIBERAL", "FASCIST", "FASCIST", "FASCIST", "HITLER"]
    ROLE_LIST_10 = ["LIBERAL", "LIBERAL", "LIBERAL", "LIBERAL", "LIBERAL", "LIBERAL", "FASCIST", "FASCIST", "FASCIST", "HITLER"]

    def __init__(self, players: list):
        self.gameBoard = gameObjects.board.board(len(players))
        self.deck = gameObjects.policyDeck.policyDeck()
        self.deck.shuffleDeck()
        self.tempPlayerList = players
        self.playerList = []

    def roleSelection(self):
        random.shuffle(self.tempPlayerList)
        roleList = []
        playerCount = len(self.tempPlayerList)

        if playerCount == 5:
            roleList = self.ROLE_LIST_5
        elif playerCount == 6:
            roleList = self.ROLE_LIST_6
        elif playerCount == 7:
            roleList = self.ROLE_LIST_7
        elif playerCount == 8:
            roleList = self.ROLE_LIST_8
        elif playerCount == 9:
            roleList = self.ROLE_LIST_9
        else:
            roleList = self.ROLE_LIST_10

        for x in range(len(self.tempPlayerList)):
            if roleList[x] == "LIBERAL":
                self.playerList.append(gameObjects.player.player(self.tempPlayerList[x], roleList[x], "LIBERAL"))
            else:
                self.playerList.append(gameObjects.player.player(self.tempPlayerList[x], roleList[x], "FASCIST"))

    def startUp(self):
        pass

    def election(self):
        pass

    def legislativeSession(self):
        pass

    def gameOver(self):
        pass

    """Should be last function as this will be the primary loop for the game and call most (if not) all others"""
    def mainLoop(self):
        pass
