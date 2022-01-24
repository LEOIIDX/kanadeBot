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
TOKEN = os.getenv('DISCORD_TOKEN')

#intents
intents = discord.Intents.default()
intents.members = True
intents.emojis = True
intents.reactions = True

print('Kanade Bot QOTD module\n')

bot = commands.Bot(command_prefix='ky!',intents=intents)

qotdCh = 792646559601917963

@bot.event
async def on_ready():
	qotd = {}
	qotdCOUNT = 0
	qotdUsed = {}
	qotdUsedCOUNT = 0
	sentQOTD = 0	

	qotdEMBED = discord.Embed(colour = discord.Colour.red())

	with open('qotdResource/'+'qotd.txt') as f:
		for line in f:
			(key, val) = line.split('|')
			newVal = val.rstrip()
			qotd[str(key)] = newVal
			qotdCOUNT = qotdCOUNT + 1
			
	with open('qotdResource/'+'used-qotd.txt') as f:
		for line in f:
			(key, val) = line.split('|')
			newVal = val.rstrip()
			qotdUsed[str(key)] = newVal
			qotdUsedCOUNT = qotdUsedCOUNT + 1

	while sentQOTD != 1:
		print('attempting to send')
		usedCheck = 0
		qotdRan = str(999)

		for key in qotdUsed:
			print(qotdUsed.get(key) + ' and ' + qotdRan)
			if str(qotdUsed.get(key)) == qotdRan:
				print('detected already used question')
				usedCheck = 1
				break

		if qotdUsedCOUNT == qotdCOUNT:
			print('no more questions')

			qotdEMBED = discord.Embed(colour = discord.Colour.red(), title='Question of the Day', description = 'No more questions')	
	
			qotdEMBED.set_footer(text='damn no more questions')

			await bot.get_channel(qotdCh).send(embed=qotdEMBED)	
			break

		if usedCheck == 0:
			qotdEMBED = discord.Embed(colour = discord.Colour.red(), title='Question of the Day', description = 'What is your favorite Christmas Movie?')

			qotdEMBED.set_footer(text='CHRISTMAS EVE QUESTION!!!')

			await bot.get_channel(qotdCh).send(embed = qotdEMBED)
			break
		else:
			pass
			
	print('stopping script')
	exit()
bot.run(TOKEN)
