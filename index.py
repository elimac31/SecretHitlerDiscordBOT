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

nameCount = 1
usersInGames = {}
startPromptMessages = {}
gameChannels = {}

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
    startPromptMessages[ctx.channel.id] = await ctx.send('<@' + str(ctx.author.id) + '> has started a game of Secret Hitler! react to this message in the next two minutes to join!', delete_after = 120)
    usersInGames[ctx.channel.id] = []

@client.command()
async def chooseCandidate(ctx, args):
    president = gameChannels[ctx.channel][2].getPresident()

    if(ctx.author == )

@client.event
async def on_reaction_add(reaction, user):
    print("react: " + str(reaction.message))
    if startPromptMessages[reaction.message.channel.id] == reaction.message:
        usersInGames[reaction.message.channel.id].append(user)
    if len(usersInGames) == 10:
        reaction.message.delete()

@client.event
async def on_message_delete(message):
    channel = message.channel
    if startPromptMessages[channel.id] == message:
        if len(usersInGames[channel.id]) >= 5:

            gameMain(usersInGames[channel.id])

            overwrite1 = discord.PermissionOverwrite()
            overwrite1.send_messages = False
            overwrite1.read_messages = False
            overwrite2 = discord.PermissionOverwrite()
            overwrite2.send_messages = True
            overwrite2.read_messages = True

            gameRole = await channel.guild.create_role(name="Secret Hitler " + str(nameCount))

            overwriteDict = {channel.guild.default_role: overwrite1, channel.guild.me: overwrite2, gameRole: overwrite2}
            new_game_channel = await channel.guild.create_text_channel("Secret Hitler " + str(nameCount), overwrites=overwriteDict, category=None,reason=None)
            new_voice_channel = await channel.guild.create_voice_channel("Secret Hitler " + str(nameCount), overwrites=overwriteDict, category=None,reason=None)
            usersInGames[new_game_channel.id] = usersInGames.pop(channel.id)

            gameObject = gameMain(usersInGames[new_game_channel.id])
            gameObject.roleSelection()
            gameChannels[new_game_channel] = [new_voice_channel, gameRole, gameObject]



        else:
            await channel.send("There are not enough players to start, canceling start request")





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

        self.currentPresident= gameObjects.player.player
        self.currentChancellor= gameObjects.player.player
        self.lastPresident = gameObjects.player.player
        self.lastChancellor = gameObjects.player.player

        self.nextPresident: gameObjects.player.player
        self.nextPresidentIndex = 0
        self.playerCount = len(players)

    def roleSelection(self):
        random.shuffle(self.tempPlayerList)
        roleList = []
        playerCount = self.playerCount

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
        random.shuffle(self.playerList)
        self.currentPresident = random.choice(self.playerList)
        self.nextPresidentIndex = self.playerList.index(self.currentPresident) + 1

    def getNextPresident(self):
        self.currentPresident = self.playerList[self.nextPresidentIndex]
        self.nextPresidentIndex += 1
        if self.nextPresidentIndex >= self.playerCount:
            self.nextPresidentIndex = 0

    def startUp(self):
        pass

    def election(self, yes: int, no: int, newChanncellor: gameObjects.player.player):



        if(yes > no):
            self.gameBoard.passElection()
            self.lastPresident = self.currentPresident
            self.currentChanncellor = newChanncellor
            self.lastChancellor = self.newChanncellor
            return 0, self.deck.drawThree()
        else:
            return self.gameBoard.failElection(), None

    def ThreeFailedElections(self):
        self.lastChancellor = None
        self.lastPresident = None
        self.gameBoard.passElection()
        passingPolicy = self.deck.drawOne()
        self.gameBoard.playPolicy(passingPolicy)
        return(passingPolicy)

    def isChanncellorValid(self, candidate: gameObjects.player.player):
        if candidate == self.lastChancellor:
            return False
        elif candidate == self.lastPresident:
            return False
        else:
            return True

    def discard(self, card: gameObjects.policyCard.policyCard):
        self.deck.discard(card)

    def getPresident(self):
        return self.currentPresident

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
