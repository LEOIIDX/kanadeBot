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
from leoEmbed import iidxSPClassEmbeds, iidxDPClassEmbeds, sdvxDanEmbeds, infoEmbeds

load_dotenv()
TOKEN = os.getenv('APRIL_TOKEN')

#intents
intents = discord.Intents.default()
intents.members = True
intents.emojis = True
intents.reactions = True

print('Shizuku Bot\n')

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

stDict = dictionaryStatuses()

for key in stDict.multiStatus:
	print(key + ' ' + stDict.multiStatus.get(key))

'''
command section
command prefix ky!
'''
if debugValue >= 1:
	bot = commands.Bot(command_prefix='syt!',intents=intents)
else:
	bot = commands.Bot(command_prefix='sy!',intents=intents)

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
	sDict = dictionaryStatuses()
	qDict = dictionaryMessages()
	uQotd = {}
	uQotdCount = 0

	readyVer = 1
	sPick = str(input('Input Desired Status. \n (0) for random \n'))

	await bot.change_presence(status=discord.Status.online, activity=discord.Game(sDict.multiStatus.get(sPick)))

	if debugValue == 0:
		print('Bot is ready!!\n')
			
#command error handler
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Command missing arguments')

@bot.command(name='gacha')
async def gacha(ctx):
	gachaCount = 0

	with open ('input.json', 'r', encoding="utf8") as f:
		bResp = json.load(f)

		for data in bResp:
			gachaCount = gachaCount + 1

		gachaCount = gachaCount - 1
		gachaRan = random.randint(0, gachaCount)
		respStep = 0

		if bResp[gachaRan]['type'] == 0:
				for item in bResp[gachaRan]['responses']:
					respStep = respStep + 1
				respStep = respStep - 1
				respRan = random.randint(0, respStep)
				await ctx.channel.send(bResp[gachaRan]['responses'][respRan])
				return
		elif bResp[gachaRan]['type'] == 1:
				for item in bResp[gachaRan]['responses']:
					await ctx.channel.send(bResp[gachaRan]['responses'][respStep])
					await ctx.channel.send('‏')
					respStep = respStep + 1
				return
		elif bResp[gachaRan]['type'] == 2:
				for item in bResp[gachaRan]['responses']:
					respStep = respStep + 1
				respStep = respStep - 1
				respRan = random.randint(0, respStep)
				await ctx.channel.send(file=discord.File("img/" + bResp[gachaRan]['responses'][respRan]))
				return
	
@bot.command(name='help')
async def help(ctx, tag=None):
	helpEmbed = discord.Embed(colour=discord.Colour.red())
	helpEmbed.set_author(name='NANAMONKE APRIL FOOLS 2022')
	helpEmbed.set_thumbnail(url='https://i.ibb.co/Tk27M21/shizuku.png')	

	helpEmbed.add_field(name='lmao', value='get fucked', inline=False)

	await ctx.channel.send(embed=helpEmbed)


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
politics (thanks russia)

Users:
Itself
Kanade Bot [ky!] when in debug mode

Bot will also ignore all messages if ky!noresponse is set on
'''
@bot.event
async def on_message(message):
	if message.author == bot.user or str(message.channel.id) == '751618333912072219' or str(message.channel.id) == '749844960194330714' or str(message.channel.id) == '755183591603961959' or str(message.channel.id) == '792599858572820480' or str(message.channel.id) == '750098737854021655' or str(message.channel.id) == '752960043275780224' or str(message.channel.id) == '812903612551397386' or str(message.author) == '840869717727248444' or str(message.channel.id) == '882690005296873542':
		return

	miku = message.guild.get_member(693294060143640586)
	michael = message.guild.get_member(195748601639600128)

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
		if dumb[0:4] == 'syt!': ##ignores kyt! commands
			await bot.process_commands(message)
			return
	else:
		if dumb[0:3] == 'sy!': ##ignores ky! commands
			await bot.process_commands(message)
			return

	if responseCheck != 1:
		return

	mDict = dictionaryMessages() #generates everything needed for dictionaries

	if debugValue >= 1:
		print('haha')
	if debugValue == 1:
		coinflip = random.randint(1,2)
		chance =  1
		fuckinRare = 1
		print('coinflip: '+ str(coinflip))
		print('chance: ' + str(chance))
		print('fuckinRare: ' + str(fuckinRare) + '\n')
	elif debugValue == 2:
		coinflip = random.randint(1,2)
		chance = random.randint(1,10)
		fuckinRare = random.randint(1,500)
		print('coinflip: '+ str(coinflip))
		print('chance: ' + str(chance))
		print('fuckinRare: ' + str(fuckinRare) + '\n')
	else:
		coinflip = random.randint(1,2)	
		chance = random.randint(1,1)
		fuckinRare = random.randint(1,500)

	lolzep = "126068015094693888"
	if lolzep == dumbLetters:
		await message.delete()
		await message.channel.send(message.author.mention + " fuck u")

	for key in mDict.otherResponses:
		if key in dumbLetters:
			if debugValue >= 1:
				print('Triggered Keyword: ' + key + '\n')
			dumbLetters = mDict.otherResponses.get(key)

#	If rareChance integer equals 1.
#	It will check if the message falls under a keyword.
#	'iidx' will pick a random key within the dictionary and send its value to a message's channel
#	'nanahira' has a 50% chance to either send the Nanahira copypasta or a random key with 'nanahira' dictionary

#	If ultraRare equals 1 (1/100 chance).
#	Checks if message contains the term grace
#	If true, the ENTIRE grace copypasta is sent to the message's channel (im sorry for whomever triggers it)

	match dumbLetters:
		case 'miku':
			mikuCounter = 1 
			if debugValue >= 1:
				while mikuCounter != 0:
					await message.channel.send(f"{michael.mention}")
					mikuCounter = mikuCounter - 1
					pass
			else:	
				while mikuCounter != 0:
					await message.channel.send(f"{miku.mention}")
					mikuCounter = mikuCounter - 1
					pass

		case 'love live':
			await message.channel.send(f"{michael.mention}")
			pass

	if chance == 1:
		if "im " == dumbLetters[0:3]:
			await message.channel.send("Hi \"" + string.capwords(dumb[3:]) + "\", I'm Kanade Bot!")
		if "i am " == dumbLetters[0:5]:
			await message.channel.send("Hi \"" + string.capwords(dumb[5:]) + "\", I'm Kanade Bot!")

	with open ('input.json', 'r', encoding="utf8") as f:
		bResp = json.load(f)

	for data in bResp:
		respStep = 0
		for item in data['keywords']:
			if dumbLetters == data['keywords'][0]:
				if data['type'] == 0:
					ran = random.randint(1, 1)
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
					ran = random.randint(1, 1)
					if ran == 1:
						for item in data['responses']:
							await message.channel.send(data['responses'][respStep])
							await message.channel.send('‏')
							respStep = respStep + 1
						return
					else:
						pass
				elif data['type'] == 2:
					ran = random.randint(1, 1)
					if ran == 1:
						for item in data['responses']:
							respStep = respStep + 1
						respStep = respStep - 1
						respRan = random.randint(0, respStep)
						await message.channel.send(file=discord.File("img/" + data['responses'][respRan]))
						return
					else:
						pass
				else:
					pass


	if random.randint(1, 1) == 1:
		gachaCount = 0

		for data in bResp:
			gachaCount = gachaCount + 1

		gachaCount = gachaCount - 1
		gachaRan = random.randint(0, gachaCount)
		respStep = 0

		if bResp[gachaRan]['type'] == 0:
				for item in bResp[gachaRan]['responses']:
					respStep = respStep + 1
				respStep = respStep - 1
				respRan = random.randint(0, respStep)
				await message.channel.send(bResp[gachaRan]['responses'][respRan])
				return
		elif bResp[gachaRan]['type'] == 1:
				for item in bResp[gachaRan]['responses']:
					await message.channel.send(bResp[gachaRan]['responses'][respStep])
					await message.channel.send('‏')
					respStep = respStep + 1
				return
		elif bResp[gachaRan]['type'] == 2:
				for item in bResp[gachaRan]['responses']:
					respStep = respStep + 1
				respStep = respStep - 1
				respRan = random.randint(0, respStep)
				await message.channel.send(file=discord.File("img/" + bResp[gachaRan]['responses'][respRan]))
				return
		
	if fuckinRare == 2:
		if debugValue != 1:
			pass
		else:
			if coinflip == 1:
				await message.channel.send('*' + dumb + '*')
				return
			else:
				await message.channel.send('||' + dumb + '||')
				return

if masterQuery == 1:
	bot.run(testTOKEN)
else:
	bot.run(TOKEN)
