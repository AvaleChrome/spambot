#ENTER THIS IN CMD BEFORE U RUN CODE - py -m pip install discord
 
##IMPORTS##
import discord                      
from discord.ext.commands import bot
from discord.ext import commands
import random
import asyncio
import time
 
##PREFIX##
bot = commands.Bot(command_prefix='!')
 
##BOT IS READY##
@bot.event
async def on_ready():
    print("Bot Is Online! And Ready To Spam")
 
##SPAM COMMAND##
@bot.command(pass_context=True)
async def spam(ctx): #run "!spam" to run the command
    while True:
        await bot.say("put what u want it to say in here") #NOTE - you need the \n (new lines)
        await bot.say("")
        await bot.say("")
        await bot.say("")
        await bot.say("")
 
##BOT TOKEN##
bot.run ("BOT_TOKEN")
