#leoBot.py
'''
General TODO
Turn the dictionary creators into their own classes (might be hard)
React Roles Backup (eventually)
'''
import os
import discord
import random
import re

from discord.ext import commands
from dotenv import load_dotenv
from leoDictionary import dictionaryMessages

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#intents
intents = discord.Intents.default()
intents.members = True
intents.emojis = True
intents.reactions = True
'''
command section
command prefix lx!
'''
bot = commands.Bot(command_prefix='lx!',intents=intents)
bot.remove_command('help')
'''
Changes the status randomly on startup
Statuses come from dictionary generated from a txt file
'''
@bot.event
async def on_ready():
	multiStatus = {}
	statusCount = 0
	readyVer = 1

	with open('txt/'+'multiStatus.txt') as f:
		for line in f:
	    		(key, val) = line.split('_')
	    		multiStatus[str(key)] = val
	    		statusCount = statusCount + 1
	    		
	    		statusRan = random.randint(1,statusCount)
	
	if readyVer == 1:
		for key in multiStatus:
	    		ranStr = str(statusRan)
	    		if key == ranStr:
	    			await bot.change_presence(status=discord.Status.online, activity=discord.Game(multiStatus.get(key)))
	    			return

#command error handler
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Command missing arguments')

@bot.command(name='help')
#Command that displays all availible commands in an Embed Object.
async def help(ctx):
	leoTM = discord.File('img/'+'leo.png')
	
	help = discord.Embed(
		colour = discord.Colour.red()
	)
	
	help.set_author(name='Help')
	help.set_thumbnail(url='attachment://leo.png')
	help.add_field(name='roll', value='lx!roll <value> || Returns random number from 1 to <value>.', inline=False)
	help.add_field(name='exscore', value='lx!exscore <Total Notes> || Calculates the EXSCORE amount necesary to get MAX, AAA, AA, or A from a songs total notes.', inline=False)
	help.add_field(name='ealinks', value='lx!ealinks || Displays various important e-amusement links', inline=False)
	help.add_field(name='selfie', value='lx!selfie || Displays my selfie!', inline=False)
	help.add_field(name='statusChange', value='lx!statusChange || randomly replaces status (☆LEO!☆ only)', inline=False)
	help.add_field(name='certain messages', value='imminent funni', inline=False)
	
	await ctx.channel.send(file=leoTM,embed=help)	

@bot.command(name='roll')
#obligatory roll command
#takes number given and sends a message of a number between 1 and the given number
async def roll(ctx, number: int):
	roll = str (random.randint(0,number))
	
	await ctx.send(roll)

@bot.command(name='exscore')
#Calculates IIDX Score necesary to get IIDX grade ranks
#Calcuations are made by taking a given note count, doubling it to find maximum EXSCORE, then multiplying by percentage corresponding to grade rank.
#Results from above actions aren then put into an embed object and sent to the channel the command was sent in
async def exscore(ctx, number: int):
	exscore = number
	MAX = number * 2
	AAA = MAX * .8889
	AA = MAX * .7778
	A = MAX * .6667
	
	
	exEmbed = discord.Embed(
		colour = discord.Colour.red()
	)
	
	exEmbed.set_author(name='IIDX EXSCORE Calculator')
	exEmbed.add_field(name='Total Notes', value=exscore, inline=False)
	exEmbed.add_field(name='MAX', value=int(MAX), inline=False)
	exEmbed.add_field(name='AAA', value=int(AAA), inline=False)
	exEmbed.add_field(name='AA', value=int(AA), inline=False)
	exEmbed.add_field(name='A', value=int(A), inline=False)
	
	await ctx.channel.send(embed=exEmbed)
	
@bot.command(name='ealinks')
#Display of various important e-amusement links
#TODO:
#Find a frictionless way to implement dictionaries for easy editing
async def ealinks(ctx):
	eaEmbed = discord.Embed(
		colour = discord.Colour.red()
	)
	
	eaEmbed.set_author(name='e-amusement links')
	eaEmbed.set_thumbnail(url='https://i.postimg.cc/XYHdy2Lf/ea.png')
	eaEmbed.add_field(name='e-amusement pass', value='https://p.eagate.573.jp/gate/eapass/menu.html', inline=False)
	eaEmbed.add_field(name='Paseli Charge', value='https://paseli.konami.net/charge/top.html', inline=False)
	eaEmbed.add_field(name='beatmania IIDX 28 Bistrover', value='https://p.eagate.573.jp/game/2dx/28/top/index.html', inline=False)
	eaEmbed.add_field(name='beatmania IIDX INFINITAS', value='https://p.eagate.573.jp/game/infinitas/2/', inline=False)
	eaEmbed.add_field(name='SOUND VOLTEX Vivid Wave', value='https://p.eagate.573.jp/game/sdvx/v/p/top/', inline=False)
	eaEmbed.add_field(name='SOUND VOLTEX Exceed Gear', value='https://p.eagate.573.jp/game/sdvx/vi/', inline=False)
	eaEmbed.add_field(name='SOUND VOLTEX コナステ', value='https://p.eagate.573.jp/game/eacsdvx/iii/p/common/top.html', inline=False)
	eaEmbed.add_field(name='DanceDanceRevolution A20 PLUS', value='https://p.eagate.573.jp/game/ddr/ddra20/p/', inline=False)
	
	await ctx.channel.send(embed=eaEmbed)
	
@bot.command(name='selfie')
#Dumb Picture command
async def selfie(ctx):
	await ctx.channel.send(file=discord.File('img/'+'selfie.jpg'))

@bot.command(name='statusSwitch')
#Calls the above @bot.event
#Barely works (dont know why)
async def statusSwitch(ctx):
	multiStatus = {}
	statusCount = 0
	
	with open('txt/'+'multiStatus.txt') as f:
		for line in f:
	    		(key, val) = line.split('_')
	    		multiStatus[str(key)] = val
	    		statusCount = statusCount + 1
	    		
	    		statusRan = random.randint(1,statusCount)
	    			  
	if ctx.author.id == 194605769419784192:
		print('updating')
		for key in multiStatus:
	    		ranStr = str(statusRan)
	    		if key == ranStr:
	    			await bot.change_presence(status=discord.Status.online, activity=discord.Game(multiStatus.get(key)))
	    			return
	    			
	else:
		await ctx.channel.send('Can\'t do that, sorry!')  
		return  			

@bot.command(name='dicttest')
async def dicttest(ctx):
	dictObj = dictionaryMessages()
	print(dictObj.nanaCopy)
	
@bot.event			
#handler for dumb messages
#shameless copy of code from Lolzep Bot (haha)
async def on_message(message):
	if message.author == bot.user or str(message.channel.id) == '751618333912072219' or str(message.channel.id) == '749844960194330714':
		return
	print('Message Guild: ' + str(message.guild))
	print('Message Channel: ' + str(message.channel))
	print('Message Author: ' + str(message.author))
	dumb = str(message.content).strip().lower() #message with punctuation
#	print(dumb)
	dumbLetters = re.sub(r'([^\s\w]|_)+', '', dumb) #message with no punctuation
	print('dumbLetters: ' + dumbLetters + '\n')	
	if 'https' in dumbLetters: #ignores links
		return
	if dumb[0:3] == 'lx!': ##ignores lx! commands
		await bot.process_commands(message)
		return
	if dumbLetters == 'ななひら' or dumbLetters =='confetto':
		dumbLetters = 'nanahira'

#	Initializes objects for for dictionaries and randomizers


	dumbPhrases = {}
	iidxQuotes = {}
	otherRare = {}
	iidxCount = 0
	nanahira = {}
	nanaCount = 0
	nanaCopy = {}
	cursedGrace = {}

#	Populates dictionary objects from txt files
	
	
	with open('txt/'+'dumbPhrases.txt') as f:
		for line in f:
	    		(key, val) = line.split('_')
	    		dumbPhrases[str(key)] = val
	    			
	with open('txt/'+'iidxQuotes.txt') as f:
		for line in f:
	    		(key, val) = line.split('_')
	    		iidxQuotes[str(key)] = val
	    		iidxCount = iidxCount + 1
	    			
	with open('txt/'+'nanahira.txt') as f:
		for line in f:
	    		(key, val) = line.split('~')
	    		nanahira[str(key)] = val
	    		nanaCount = nanaCount + 1
	
	with open('txt/'+'otherRare.txt') as f:
		for line in f:
	    		(key, val) = line.split('~')
	    		otherRare[str(key)] = val
	
	with open('txt/'+'nanaCopy.txt') as f:
		for line in f:
	    		(key, val) = line.split('~')
	    		nanaCopy[str(key)] = val
	    		
	with open('txt/'+'cursedGrace.txt') as f:
		for line in f:
	    		(key, val) = line.split('~')
	    		cursedGrace[str(key)] = val    		
		
	iidxRan = random.randint(1,iidxCount)
	nanaRan = random.randint(1,nanaCount)
	nanaCopyChance = random.randint(1,2)
#	nanaRan = 1

	rareChance = random.randint(1,5)
	print('rareChance: ' + str(rareChance))
	ultraRare = random.randint(1,100)	
	print('ultraRare: ' + str(ultraRare) + '\n')

#	If the message sent contains a keyword in the dumbLetters dictionary. 
#	The corresponding value is sent to the message's channel	
	
	for key in dumbPhrases: #sends simple text replies
		if key in dumbLetters:
#			print('sending') #debug message if it fucking sends
			await message.channel.send(dumbPhrases.get(key))
			return
#	END OF COPIED CODE

#	If rareChance integer equals 1.
#	It will check if the message falls under a keyword.
#	'glasses' and 'iidx' will pick a random key within the dictionary and send its value to a message's channel
#	'nanahira' has a 50% chance to either send the Nanahira copypasta or a random key with 'nanahira' dictionary
	
#	If ultraRare equals 1 (1/100 chance).
#	Checks if message contains the term grace
#	If true, the ENTIRE grace copypasta is sent to the message's channel (im sorry for whomever triggers it)

	if rareChance == 1:
		if 'glasses' in dumbLetters:
			await message.channel.send(otherRare.get('1'))
			return
			
		if 'nanahira' in dumbLetters:
			if nanaCopyChance == 1:
				for key in nanahira:
					ranStr = str(nanaRan)
					if key == ranStr:
						await message.channel.send(nanahira.get(key))
						return
			else:
				for key in nanaCopy:
					await message.channel.send(nanaCopy.get(key) + '\n')
					await message.channel.send(' ឵឵')
					
		if 'iidx' in dumbLetters:
			for key in iidxQuotes: #sends IIDX
				ranStr = str(iidxRan)
				if key == ranStr:
					await message.channel.send(iidxQuotes.get(key))
					return
	
	if ultraRare == 1:
		if 'grace' in dumbLetters:
			print('pray for all' + '\n')
			for key in cursedGrace:
				await message.channel.send(cursedGrace.get(key) + '\n')
				await message.channel.send(' ឵឵')
		
bot.run(TOKEN)
