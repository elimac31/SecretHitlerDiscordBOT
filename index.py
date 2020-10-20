import discord
from discord.ext import commands

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


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round (client.latency * 1000)}ms')

client.run(getToken())


