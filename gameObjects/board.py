import discord
from policyCard import policyCard

"""
This class is for board objects
this will keep track of how many policies are in play
this also tracks how many elections have been failed
"""
class board:

    """
    Constants of what actions are taken based on how many policies are in play
    """
    FASCIST_BOARD_1 = ["BLANK", "BLANK", "POLICY_PEEK", "EXECUTION", "EXECUTION", "END"]
    FASCIST_BOARD_2 = ["BLANK", "INVESTIGATE_LOYALTY", "CALL_SPECIAL_ELECTION", "EXECUTION", "EXECUTION", "END"]
    FASCIST_BOARD_3 = ["INVESTIGATE_LOYALTY", "INVESTIGATE_LOYALTY", "CALL_SPECIAL_ELECTION", "EXECUTION", "EXECUTION", "END"]
    LIBERAL_BOARD = ["BLANK", "BLANK", "BLANK", "BLANK", "END"]


    """
    constructor for board objects, takes the number of players in the game(playerCount) as input
    based on playerCount a fascistBoard will be chosen for this game
    creates and sets all counters to zero
    """
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
        self.LiberalPolicyCount = 0
        self.failedElectionCounter = 0

    """
    adds one to either LiberalPolicyCount or FascistPolicyCount (Depending on what policy the policy variable has)
    returns the presidential power (if there is one) that happens now
    """
    def playPolicy(self, policy:policyCard):
        if policy.isLiberal:
            self.LiberalPolicyCount += 1
            return self.LiberalBoard[self.LiberalPolicyCount - 1]
        else:
            self.FascistPolicyCount += 1
            return self.FascistBoard[self.FascistPolicyCount - 1]

    """
    adds 1 to the failedElectionCounter
    returns the failedElectionCounter
    """
    def failElection(self):
        self.failedElectionCounter += 1
        return self.failedElectionCounter

    """
    resets the failedElectionCounter to zero
    """
    def passElection(self):
        self.failedElectionCounter = 0

    """
    Returns how many FASCIST policies have been passed
    """
    def getFascistPolicies(self):
        return self.FascistPolicyCount

    """
    Returns how many LIBERAL policies have been passed
    """
    def getLiberalPolicies(self):
        return self.LiberalPolicyCount

    """
    TODO: add this so that the current boards can be seen by the players
    """
    def printBoard(self):
        pass
