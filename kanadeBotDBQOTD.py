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
from PIL import Image

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#intents
intents = discord.Intents.default()
intents.members = True
intents.emojis = True
intents.reactions = True

print('Kanade Bot DEATH BATTLE QOTD module\n')

bot = commands.Bot(command_prefix='kyt!',intents=intents)

qotdTestCh = 867088318466359338

async def dataPrep():
	global charaList, imgList, imgList_COUNT

	imgList_COUNT = 0

	with open ('DB.json', 'r', encoding='utf8') as f:
		charaList = json.load(f)

	imgList = os.listdir("dbResource/dbIMG/")

	for item in imgList:
		imgList_COUNT = imgList_COUNT + 1

async def imgGen(imgA, imgB):
	im2 = Image.open("dbResource/dbIMG/" + str(imgB) + ".png")
	im1 = Image.open("dbResource/dbIMG/" + str(imgA) + ".png") 
	im3 = Image.open("img/orig.png")

	finIM = im3.copy()
	finIM.paste(im1)
	finIM.paste(im2, (303, 0))
	finIM.save('dbIMG/final.png')

async def embedCreator():
	ranOne = (random.randint(1, imgList_COUNT) - 1)
	ranTwo = (random.randint(1, imgList_COUNT) - 1)

	await imgGen(ranOne, ranTwo)

	charaEmbed = discord.Embed()

	file = discord.File('dbResource/dbIMG/final.png', filename= 'final.png')

	charaEmbed.set_image(url='attachment://'+ 'final.png')
	charaEmbed.add_field(name="Who would win in a fight?",value='‏', inline=False)
	charaEmbed.add_field(name=charaList[ranOne]['name'], value=charaList[ranOne]['source'], inline=True)
	charaEmbed.add_field(name='OR', value='‏',inline=True)
	charaEmbed.add_field(name=charaList[ranTwo]['name'], value=charaList[ranTwo]['source'], inline=True)
	charaEmbed.set_footer(text='Nanahira Monke Vs.')

	await bot.get_channel(qotdTestCh).send(file=file, embed=charaEmbed)

@bot.event
async def on_ready():
	await dataPrep()
	await embedCreator()

	os.system('rm dbResource/dbIMG/final.png')
	exit()
bot.run(TOKEN)
