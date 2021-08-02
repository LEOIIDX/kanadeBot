'''
kanadeBotQOTD.py

Condensed version of Kanade Bot programmed for the purpose of QOTD.

Meant to be executed via crontab
'''
import os
import discord
import random
import re
import datetime
import asyncio
import pendulum
import string
import math

from discord.ext import commands
from dotenv import load_dotenv
from leoDictionary import dictionaryMessages, dictionaryStatuses
from leoEmbed import iidxSPClassEmbeds, iidxDPClassEmbeds, sdvxDanEmbeds, infoEmbeds

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#intents
intents = discord.Intents.default()
intents.members = True
intents.emojis = True
intents.reactions = True

print('Kanade Bot QOTD module\n')

stDict = dictionaryStatuses()

for key in stDict.multiStatus:
	print(key + ' ' + stDict.multiStatus.get(key))

'''
command section
command prefix ky!
'''
bot = commands.Bot(command_prefix='ky!',intents=intents)

bot.remove_command('help')

qotdCh = 867088318466359338

@bot.event
async def on_ready():
	sDict = dictionaryStatuses()
	qDict = dictionaryMessages()
	uQotd = {}
	uQotdCount = 0

	readyVer = 1
	sPick = str(input('Input Desired Status. \n (0) for random \n'))

	await bot.change_presence(status=discord.Status.online, activity=discord.Game(sDict.multiStatus.get(sPick)))

	if debugValue == 0:
		print('Bot is ready!!\n')

bot.run(TOKEN)
