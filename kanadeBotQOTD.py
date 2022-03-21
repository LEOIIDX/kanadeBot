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
qotdTest = 867088318466359338

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
		qotdRan = str(random.randint(1,qotdCOUNT))
#		qotdRan = str(71)

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
			with open('qotdResource/'+'used-qotd.txt', 'a') as f:
				f.write(str(qotdUsedCOUNT + 1)  + '|' + str(qotdRan) + '\n')

			qotdEMBED = discord.Embed(colour = discord.Colour.red(), title='Question of the Day', description = qotd.get(qotdRan))

			qotdEMBED.set_footer(text='Question #' + qotdRan)

			await bot.get_channel(qotdCh).send(embed = qotdEMBED)
			break
		else:
			pass
			
	print('stopping script')
	exit()
bot.run(TOKEN)
