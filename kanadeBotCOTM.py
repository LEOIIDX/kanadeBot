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

print('Kanade Bot COTM module\n')

bot = commands.Bot(command_prefix='ky!',intents=intents)

cotwCh = 922405898662600755

@bot.event
async def on_ready():
	Guild = bot.get_guild(744622412267782234)
	memberIdDict = {}
	memberIdCounter = 0
	memberNameDict = {}
	memberNameCount = 0

	for member in Guild.members:
		if 'Gold' in str(member.roles) or 'Platinum' in str(member.roles) or 'Diamond' in str(member.roles) or 'Master' in str(member.roles) or 'Grandmaster' in str(member.roles) or 'Exalted' in str(member.roles) or 'Galaxy' in str(member.roles) or 'Konmai' in str(member.roles):
			memberIdCounter = memberIdCounter + 1
			memberIdDict [str(memberIdCounter)] = str(member.id)
			memberNameCount = memberNameCount + 1
			memberNameDict [str(memberNameCount)] = str(member.display_name)

	memberRan = random.randint(1, memberNameCount)

	for key in memberIdDict:
		ranStr = str(memberRan)
		if key == ranStr:
			coomMention = Guild.get_member(int(memberIdDict.get(key)))

			coomEMBED = discord.Embed(colour = discord.Colour.red(), title=('Coomer of the Month'), description=('Congratulations to ' + memberNameDict.get(key) + ' for being Coomer of the Month'))

			coomEMBED.set_thumbnail(url= 'https://i.ibb.co/4RNtzYH/coomIcon.png')

			await bot.get_channel(cotwCh).send(embed = coomEMBED)
			await bot.get_channel(cotwCh).send(f"{coomMention.mention}")
			break
	print('stopping script')
	exit()
bot.run(TOKEN)
