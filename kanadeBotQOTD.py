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
	qotd = {}
	qotdCOUNT = 0
	qotdUsed = {}
	qotdUsedCOUNT = 0
	sentQOTD = 0

    
	with open('qotdResource/'+'qotd.txt') as f:
		for line in f:
			(key, val) = line.split('|')
			newVal = val.rstrip()
			qotd[str(key)] = val
			qotdCOUNT = qotdCOUNT + 1
			
	with open('qotdResource/'+'used-qotd.txt') as f:
		for line in f:
			(key, val) = line.split('|')
			newVal = val.rstrip()
			qotdUsed[str(key)] = val
			qotdUsedCOUNT = qotdUsedCOUNT + 1

	while sentQOTD != 1:
		print('attempting to send')
		qotdRan = str(random.randint(1,qotdCOUNT))
		usedCheck = 0
		for key in qotdUsed:
			if qotdUsed.get(key) == qotdRan:
				usedCheck = usedCheck + 1
		if usedCheck >= 1:
			pass
		else:
			with open('qotdResource/'+'used-qotd.txt', 'a') as f:
				f.write(str(qotdUsedCOUNT + 1)  + '|' + str(qotdRan) + '\n')
			await bot.get_channel(qotdCh).send(qotd.get(qotdRan))
			sentQOTD = sentQOTD + 1
			
	print('stopping script')
	exit()

bot.run(TOKEN)
