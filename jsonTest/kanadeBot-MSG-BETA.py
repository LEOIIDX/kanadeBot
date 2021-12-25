'''
kanadeBot.py
By: Nanahira Monke Kanade Dev

Priority TODO

General TODO
React Roles Backup (eventually)
multiple cum images
rework of message handler
more messages
Known Bugs

Import List
os: for filesystem interactions
discord: for use of discord objects
random: For randomized elements
re: for text formatting
string: for im message formatting

discord.ext-commands: for command creation
dotenv-load_dotenv: environment variables for Discord Token
leoDictionary: container for classes relating to dictionaries
leoEmbed: container of Discord Embeds
'''
import os
import discord
import random
import re
import datetime
import asyncio
import string
import math
import json

from discord.ext import commands
from dotenv import load_dotenv
from leoDictionary import dictionaryMessages, dictionaryStatuses

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#intents
intents = discord.Intents.default()
intents.members = True
intents.emojis = True
intents.reactions = True

print('Kanade Bot Message Beta \n')

'''
Debug Mode details
sets various bot behaviors that make it easier to prod for bugs.

debugValue = 0: no debug functionality
debugValue = 1: prints message debug info to console and sets all chances to 100%
debugValue = 2: only prints message debug info

-Changes command prefix to kyt!
'''
masterQuery = 0
debugValue = int(input('Input desired debug value. \n (1) for debug display plus randoms to 100%. \n (2) for debug display only. \n (0) for standard operation.\n'))
if debugValue >= 1:
	masterQuery = int(input('Is a Master .env in use? \n (1) for yes. \n (0) for no. \n'))
	if masterQuery == 1:
		testTOKEN = os.getenv('DEBUG_TOKEN')

'''
command section
command prefix ky!
'''
if debugValue >= 1:
	bot = commands.Bot(command_prefix='kyt!',intents=intents)
else:
	bot = commands.Bot(command_prefix='ky!',intents=intents)

bot.remove_command('help')
'''
Changes the status randomly on startup
Statuses come from dictionary generated from a txt file
'''

memberCounterChannel = 837031791994208258
memberCounterChannelTest = 846244059768029265
qotdCh = 867088318466359338
global responseCheck
responseCheck = 1

@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.online, activity=discord.Game('MESSAGE BETA'))

	if debugValue == 0:
		print('Bot is ready!!\n')
			
'''
kanadeBot Message Handler

The base of the code comes from lolzepBot with some modifcation from original leoBot.

Bot ignores

Channels:
bot-commands
hobbies-chat
suggestions
admin/mod channels
server-resources
birthdays

Users:
Itself
Kanade Bot [ky!] when in debug mode

Bot will also ignore all messages if ky!noresponse is set on
'''
@bot.event
async def on_message(message):
	if message.author == bot.user or str(message.channel.id) == '751618333912072219' or str(message.channel.id) == '749844960194330714' or str(message.channel.id) == '755183591603961959' or str(message.channel.id) == '792599858572820480' or str(message.channel.id) == '750098737854021655' or str(message.channel.id) == '752960043275780224' or str(message.channel.id) == '812903612551397386' or str(message.author) == '840869717727248444':
		return

	miku = message.guild.get_member(693294060143640586)
	michael = message.guild.get_member(195748601639600128)
	lolzep = message.guild.get_member(924060600491991082)

	if debugValue >= 1:
		print('MESSAGE DEBUG VIEW\n')
		print('Message Guild: ' + str(message.guild))
		print('Message Channel: ' + str(message.channel))
		print('Message Author: ' + str(message.author) + '\n')

	dumb = str(message.content).strip().lower() #message with punctuation
#	print(dumb)
	dumbLetters = re.sub(r'([^\s\w]|_)+', '', dumb) #message with no punctuation

	if debugValue >= 1:
		print('raw message: ' + str(message.content))
		print('message all lowercase: ' + dumb)
		print('message no punctuation: ' + dumbLetters + '\n')

	if 'https' in dumbLetters: #ignores links
		return

	if debugValue >= 1:
		if dumb[0:4] == 'kyt!': #ignores kyt! commands
			await bot.process_commands(message)
			return
	else:
		if dumb[0:3] == 'ky!': #ignores ky! commands
			await bot.process_commands(message)
			return

	if responseCheck != 1:
		return

	mDict = dictionaryMessages()

	for key in mDict.otherResponses:
		if key in dumbLetters:
			if debugValue >= 1:
				print('Triggered Keyword: ' + key + '\n')
			dumbLetters = mDict.otherResponses.get(key)

	with open ('input.json', 'r') as f:
		bResp = json.load(f)

	for data in bResp:
		respStep = 0
		for item in data['keywords']:
			if dumbLetters in data['keywords'][0]:
				if data['type'] == 0:
					ran = random.randint(data['rarity'][0], data['rarity'][1])
					if ran == 1:
						for item in data['responses']:
							respStep = respStep + 1
						respStep = respStep - 1
						respRan = random.randint(0, respStep)
						await message.channel.send(data['responses'][respRan])
						return
					else:
						pass
				elif data['type'] == 1:
					ran = random.randint(data['rarity'][0], data['rarity'][1])
					if ran == 1:
						for item in data['responses']:
							await message.channel.send(data['responses'][respStep])
							await message.channel.send('‏')
							respStep = respStep + 1
						return
				elif data['type'] == 2:
					ran = random.randint(data['rarity'][0], data['rarity'][1])
					if ran == 1:
						for item in data['responses']:
							respStep = respStep + 1
						respStep = respStep - 1
						respRan = random.randint(0, respStep)
						await message.channel.send(file=discord.File("img/" + data['responses'][respRan]))
				else:
					pass

if masterQuery == 1:
	bot.run(testTOKEN)
else:
	bot.run(TOKEN)