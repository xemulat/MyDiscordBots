from time import sleep
import discord
from os import system
from sys import exit
from ping3 import ping
import asyncio
from discord.ext import commands
from animals import Animals
from random import randint
from urllib.request import urlopen
import interactions
animal = Animals('cat')
system('cls')
bot = interactions.Client(token='PASTE YOUR BOT TOKEN HERE', presence="With My Cat")

@bot.event
async def on_ready():
    print('Logged in')
    print("CatBot Started!")

@bot.command(name="about", description="A simple About command!")
async def about(ctx: interactions.CommandContext):
    await ctx.send("Information about this Project / Bot:"
                   "\n"
                   "Host:\n"
                   "CPU - INFO\n"
                   "RAM - INFO\n"
                   "GPU - INFO"
                   "\n"
                   "Project:\n"
                   "Python 3.10.5\n"
                   "163 Lines of Code\n"
                   "10 Libraries\n"
                   "8 Mental Breakdowns Coded by Xemulated")

@bot.command(name="catimage", description="Sends an image of a cat, what else did you expect?")
async def catimage(ctx: interactions.CommandContext):
    await ctx.send("Cat Image: " + str(animal.image()))

@bot.command(name="catfact", description="Sends a random fact about cats.")
async def catfact(ctx: interactions.CommandContext):
        await ctx.send("Cat Fact: " + str(animal.fact()))
    
@bot.command(name="coinflip", description="Flips a coin for you.")
async def coinflip(ctx: interactions.CommandContext):
        coinflipped = randint(1, 2)
        if coinflipped == 1:
            await ctx.send("CoinFlip - Tails")
        if coinflipped == 2:
            await ctx.send("CoinFlip - Heads")
        
@bot.command(name="online", description="Checks if the bot is online.")
async def online(ctx: interactions.CommandContext):
        await ctx.send("Yes")

@bot.command(name="stackof", description="Checks if StackOverflow is online, useful for programmers.")
async def stackof(ctx: interactions.CommandContext):
        if ping('stackoverflow.com') == False:
            await ctx.send("StackOverflow is Offline. F for all programmers at work.")
        else:
            await ctx.send("StackOverflow is Online. Let's steal some code!")

@bot.command(name="isonline", description="Pings selected url.", options = [ interactions.Option( name="text",description="What Url to ping.", type=interactions.OptionType.STRING, required=True,)])
async def isonline(ctx: interactions.CommandContext, text: str):
        if ping(text) == False:
            online = 'Offline'
        else:
            online = 'Online'
        print(text + " Responded With " + online)
        await ctx.send("Site: " + text + " is " + online)

@bot.command(name="help", description="Help Command")
async def Help(ctx: interactions.CommandContext):
    await ctx.send("Cat-Related:\n"
                   "/catimage - Sends a random image of a cat.\n"
                   "/catfact - Sends a random fact about cats.\n")
    await ctx.send("Other:\n"
                   "/help - This Menu.\n"
                   "/about - About Menu.\n"
                   "/coinflip - Flips a coin for You.\n"
                   "/online - Checks if The Bot is online.\n"
                   "/stackof - Checks if StackOverflow is online.\n"
                   "/isonline - Checks if Selected site is Online.\n")

bot.start()
