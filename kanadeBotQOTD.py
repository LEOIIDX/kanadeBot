'''
kanadeBotQOTD.py
By: Nanahira Monke Kanade Dev

Condensed version of Kanade Bot programmed for the purpose of QOTD.

Meant to be executed via crontab
'''
import os
import discord
import random
import re
import asyncio
import string
import math

from discord.ext import commands
from dotenv import load_dotenv
from leoDictionary import dictionaryMessages, dictionaryStatuses
from leoEmbed import iidxSPClassEmbeds, iidxDPClassEmbeds, sdvxDanEmbeds, infoEmbeds

load_dotenv()
TOKEN = os.getenv('DEBUG_TOKEN')

#intents
intents = discord.Intents.default()
intents.members = True
intents.emojis = True
intents.reactions = True

print('Kanade Bot QOTD module\n')

bot = commands.Bot(command_prefix='ky!',intents=intents)

qotdCh = 867088318466359338

@bot.event
async def on_ready():
	sentQOTD = 0

	while sentQOTD != 1:
		print('Sending QOTD')
		await bot.get_channel(qotdCh).send('QOTD Bot Hijack test')
	exit()

bot.run(TOKEN)
