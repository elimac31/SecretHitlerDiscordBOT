import discord

"""
Not totally sure if its necessary but this is an object for the Policy cards
"""
class policyCard:

    """
    These variables are constants for the 2 types of policies there are
    """
    LIBERAL = "LIBERAL"
    FACIST = "FACIST"

    """
    Constructor takes in the type of policy this card is
    """
    def __init__(self,type:str):
        self.policy = type

    """
    returns the type of policy this card is (LIBERAL or FACIST)
    """
    def getPolicy(self):
        return self.policy
