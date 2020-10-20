import discord

class player:

    def __init__(self, name, role, party):
        self.name = name
        self.role = role
        self.party = party
        self.isAlive = True

    def isKilled(self):
        self.isAlive = False
        return self.role

    def getParty(self):
        return self.party

    def getRole(self):
        return self.role

    def getName(self):
        return self.name