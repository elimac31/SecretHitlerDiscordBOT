import discord
"""
This class is for creating player objects
it keeps track of who the player is, their role, thier party, and if they have been killed
"""
class player:

    def __init__(self, name, role, party):
        self.name = name
        self.role = role
        self.party = party
        self.isAlive = True

    """
    is called when this player is killed
    returns their role to determine if they were hitler
    """
    def isKilled(self):
        self.isAlive = False
        return self.role

    """
    returns this player's party
    """
    def getParty(self):
        return self.party

    """
    returns this player's role
    """
    def getRole(self):
        return self.role

    """
    Returns this player's name
    """
    def getName(self):
        return self.name