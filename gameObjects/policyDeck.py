import discord
import random
from policyCard import policyCard


"""
This class uses the policyCard class to create and maintain a deck of Policy cards
"""
class policyDeck:

    """
    initializes a deck of policyCards
    starts with 11 FASCIST policies and 6 LIBERAL policies
    all cards are initially added to the discard so they can be shuffled to the drawpile
    """
    def __init__(self):
        self.policiesDrawpile = []
        self.policiesDiscard = []
        self.fascistCount = 11
        self.liberalCount = 6
        for x in range(11):
            self.policiesDiscard.append(policyCard(policyCard.FACIST))
        for x in range(6):
            self.policiesDiscard.append(policyCard(policyCard.LIBERAL))

    """
    adds a card to the discard pile
    """
    def discard(self, card:policyCard):
        self.policiesDiscard.append(card)
        if card.isFacist():
            self.fascistCount += 1
        else:
            self.liberalCount += 1

    """
    remove the next card in the draw pile
    returns the removed card
    """
    def drawOne(self):
        card = self.policiesDrawpile.pop()
        if card.isFacist():
            self.fascistCount -= 1
        else:
            self.liberalCount -= 1
        return card

    """
    removes the next three cards in the drawpile
    returns a list of the removed cards
    """
    def drawThree(self):
        draw = []
        for x in range(3):
            draw.append(self.drawOne())
        return draw

    """
    returns the next three cards in the drawpile
    """
    def viewNextThree(self):
        return(self.policiesDrawpile[0:3])

    """
    Shuffles all of the cards in the discard pile back into the draw pile,
    should be called when there is either zero cards in the drawpile or not enough for a coming function call
    """
    def shuffleDeck(self):
        random.shuffle(self.policiesDiscard)
        self.policiesDrawpile.extend(self.policiesDiscard)
        self.policiesDiscard = []

    """
    Returns the total number of policy cards remaining in the drawpile
    """
    def drawpileSize(self):
        return(len(self.policiesDrawpile))

    """
    Returns the total number of policy cards remaining in the discard pile
    """
    def discardSize(self):
        return(len(self.policiesDiscard))

    """
    Returns the total number of policy cards remaining in the deck
    """
    def totalCards(self):
        return(self.drawpileSize() + self.discardSize())

    """
    Returns the total number of FACIST cards remaining in the deck
    """
    def totalFacist(self):
        return(self.facistCount)

    """
    Returns the total number of LIBERAL cards remaining in the deck
    """
    def totalLiberal(self):
        return(self.liberalCount)

    """
    ***THIS FUNCTION IS STRICTLY FOR DEBUGGING AND SHOULD NEVER BE OTHERWISE CALLED***
    prints the policy of every card that is currently in the deck
    """
    def printDeck(self):
        for x in self.policies:
            print(x.getPolicy())


