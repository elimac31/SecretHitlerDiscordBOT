import discord

"""
Not totally sure if its necessary but this is an object for the Policy cards
"""


class policyCard:
    """
    These variables are constants for the 2 types of policies there are
    """
    LIBERAL = "LIBERAL"
    FASCIST = "FASCIST"

    """
    Constructor takes in the type of policy this card is
    """

    def __init__(self, policy: str):
        self.policy = policy

    """
    returns the type of policy this card is (LIBERAL or FASCIST)
    """

    def getPolicy(self):
        return self.policy

    """
    returns true if this card is LIBERAL, false otherwise
    """

    def isLiberal(self):
        return self.policy == self.LIBERAL

    """
    returns true if this card is FASCIST, false otherwise
    """

    def isFascist(self):
        return self.policy == self.FASCIST
