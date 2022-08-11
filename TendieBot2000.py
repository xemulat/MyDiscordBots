import discord
from os import system
from better_profanity import profanity
import asyncio
from PyProfane import isProfane
system('cls')
client = discord.Client(activity=discord.Game(name="With My Cat"))

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    print("TendieBot Started!")

@client.event
async def on_message(message):
    if profanity.contains_profanity(message.content) or  == True:
        print("Someone said the Bad Word!")
        badword = discord.Embed(title="TendieBot", description="BAD WORD ALERT!", color=0x00ff00)
        badword.set_author(name="TendieBot", icon_url='https://cdn.discordapp.com/attachments/999996335170256896/1001180037812322314/th.jpg')
        badword.add_field(name="Host:", value="Why did you say a bad word?\n"
                                              "Have some Tendies instead!", inline=False)
        badword.set_thumbnail(url="https://cdn.discordapp.com/attachments/999996335170256896/1001180037812322314/th.jpg")
        badword.set_footer(text="Made By Xemulated")
        await message.channel.send(embed=badword)
    
    if message.content.startswith('$help'):
        print("HELP COMMAND ACTIVE")
        about = discord.Embed(title="TendieBot", description="Help Gui:", color=0x00ff00)
        about.set_author(name="TendieBot", icon_url='https://cdn.discordapp.com/attachments/999996335170256896/1001180037812322314/th.jpg')
        about.add_field(name="Wut?", value="For short, if you say a bad word god will smite you all.", inline=False)
        about.set_thumbnail(url="https://cdn.discordapp.com/attachments/999996335170256896/1001180037812322314/th.jpg")
        about.set_footer(text="Made By Xemulated")
        await message.channel.send(embed=about)

client.run('PASTE YOUR BOT TOKEN HERE')
