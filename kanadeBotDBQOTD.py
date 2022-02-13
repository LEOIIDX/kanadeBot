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
import json

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#intents
intents = discord.Intents.default()
intents.members = True
intents.emojis = True
intents.reactions = True

print('Kanade Bot DEATH BATTLE COTD module\n')

bot = commands.Bot(command_prefix='kyt!',intents=intents)

qotdTestCh = 867088318466359338

async def dataPrep():
	global charaList, imgList, imgList_COUNT

	imgList_COUNT = 0

	with open ('DB.json', 'r', encoding='utf8') as f:
		charaList = json.load(f)

	imgList = os.listdir("dbIMG/")

	for item in imgList:
		imgList_COUNT = imgList_COUNT + 1

async def embedCreator():
	ran = (random.randint(1, imgList_COUNT) - 1)

	charaEmbed = discord.Embed()

	file = discord.File('dbIMG/'+ str(ran)  +'.png', filename= str(ran) + '.png')

	charaEmbed.set_image(url='attachment://'+ str(ran) +'.png')
	charaEmbed.add_field(name=charaList[ran]['name'], value=charaList[ran]['source'])
	charaEmbed.set_footer(text='Nanahira Monke Vs.')

	await bot.get_channel(qotdTestCh).send(file=file, embed=charaEmbed)

@bot.event
async def on_ready():
	await dataPrep()

	file = discord.File('dbIMG/' + str(charaList[0]['id']) + '.png')

	await embedCreator()
	await bot.get_channel(qotdTestCh).send('\nVs.\n')
	await embedCreator()
	exit()
bot.run(TOKEN)
