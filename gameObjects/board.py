import discord
from policyCard import policyCard
from policyDeck import policyDeck


class board:

    FASCIST_BOARD_1 = ["BLANK", "BLANK", "POLICY_PEEK", "EXECUTION", "EXECUTION", "END"]
    FASCIST_BOARD_2 = ["BLANK", "INVESTIGATE_LOYALTY", "CALL_SPECIAL_ELECTION", "EXECUTION", "EXECUTION", "END"]
    FASCIST_BOARD_3 = ["INVESTIGATE_LOYALTY", "INVESTIGATE_LOYALTY", "CALL_SPECIAL_ELECTION", "EXECUTION", "EXECUTION", "END"]
    LIBERAL_BOARD = ["BLANK", "BLANK", "BLANK", "BLANK", "END"]

    def __init__(self, playerCount):
        if playerCount <= 6:
            self.FascistBoard = self.FASCIST_BOARD_1
        elif playerCount <= 8:
            self.FascistBoard = self.FASCIST_BOARD_2
        else:
            self.FascistBoard = self.FASCIST_BOARD_3
        self.LiberalBoard = self.LIBERAL_BOARD
        self.playerCount = playerCount
        self.FascistPolicyCount = 0
        self.LiberalPolicyCount

    def playPolicy(self):
        pass

    def failElection(self):
        pass

    def passElection(self):
        pass

    def checkFailedElections(self):
        pass

    def getFacistPolicies(self):
        pass

    def getLiberalPolicies(self):
        pass

    def printBoard(self):
        pass

    def isGameOver(self):
        pass
