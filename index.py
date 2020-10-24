import discord
from discord.ext import commands
import random
import gameObjects

"""
This file is meant to handle most of the start up for the bot and (possibly) checking for commands
"""



def getToken():
    try:
        TOKEN = open("storedData/token.txt", "r")
        return TOKEN.readline()
    except:
        return("ERROR, TOKEN NOT FOUND")


client = commands.Bot(command_prefix='~')


usersInGames = {}
startPromptMessages = {}

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round (client.latency * 1000)}ms')

@client.command()
async def dmMe(ctx):
    await ctx.author.send("Hello there")


@client.command()
async def atMe(ctx):
    await ctx.send('<@' + str(ctx.author.id) + '>')

@client.command()
async def m(ctx, args):
    await ctx.send(args)

@client.command()
async def start(ctx):
    await ctx.send('<@' + str(ctx.author.id) + '> has started a game of Secret Hitler! react to this message in the next two minutes to join!')

    await startPromptMessages[ctx.channel.id] = ctx.channel.last_message_id
    print("og:" + str(startPromptMessages[ctx.channel.id]))

    """
    print(client.cached_messages[len(client.cached_messages) - 1].channel.id)
    startPromptMessages[client.cached_messages[len(client.cached_messages) - 1].channel.id] = client.cached_messages[len(client.cached_messages) - 1]
    print("og:" + str(client.cached_messages[len(client.cached_messages) - 1]))
    print("oh:" + str(startPromptMessages[client.cached_messages[len(client.cached_messages) - 1].channel.id]))
    """

@client.event
async def on_reaction_add(reaction, user):
    print("react: " + str(reaction.message))
    if startPromptMessages[reaction.message.channel.id] == reaction.message:
        print("DAFDSFSDFSDFFSD")
        print(str(reaction.name))


client.run(getToken())


"""
--------------------------------------------------------------------------------------------------
|Im gonna keep this as a divider in case i decide to move the gameMain back to its own class later|
--------------------------------------------------------------------------------------------------
"""
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
        self.currentPresident: gameObjects.player.player
        self.currentChancellor: gameObjects.player.player
        self.nextPresident: gameObjects.player.player
        self.nextPresidentIndex = 0

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

        for x in range(0, len(self.tempPlayerList)):
            if roleList[x] == "LIBERAL":
                self.playerList.append(gameObjects.player.player(self.tempPlayerList[x], roleList[x], "LIBERAL"))
            else:
                self.playerList.append(gameObjects.player.player(self.tempPlayerList[x], roleList[x], "FASCIST"))
        self.currentPresident = random.choice(self.playerList)
        self.nextPresidentIndex = self.playerList.index(self.currentPresident) + 1

    def startUp(self):
        pass

    def election(self, yes: int, no: int):
        if(yes > no):
            self.gameBoard.passElection()
            return 0, self.deck.drawThree()
        else:
            return self.gameBoard.failElection(), None

    def discard(self, card: gameObjects.policyCard.policyCard):
        self.deck.discard(card)

    def investigateLoyalty(self):
        pass

    def specialElection(self):
        pass

    def policyPeek(self):
        pass

    def execution(self):
        pass


    def legislativeSession(self, card: gameObjects.policyCard.policyCard):
        presidentialPower = self.gameBoard.playPolicy(card)

        if presidentialPower == "POLICY_PEEK":
            self.policyPeek()
        elif presidentialPower == "INVESTIGATE_LOYALTY":
            self.investigateLoyalty()
        elif presidentialPower == "CALL_SPECIAL_ELECTION":
            self.specialElection()
        elif presidentialPower == "EXECUTION":
            self.execution()
        elif presidentialPower == "END":
            pass
        pass


    def gameOver(self):
        pass

    """Should be last function as this will be the primary loop for the game and call most (if not) all others"""
    def mainLoop(self):
        pass
