'''
kanadeBot.py
By: Nanahira Monke Kanade Dev

Priority TODO

General TODO
React Roles Backup (eventually)
QOTD for ridiculous hypotheticals
Bot disabler
more messages

Known Bugs
Time sometimes deviates by a minute when bot is on for awhile.
Testing

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

from discord.ext import commands
from dotenv import load_dotenv
from leoDictionary import dictionaryMessages, dictionaryStatuses
from leoEmbed import iidxSPClassEmbeds, iidxDPClassEmbeds, sdvxDanEmbeds, infoEmbeds

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#intents
intents = discord.Intents.default()
intents.members = True
intents.emojis = True
intents.reactions = True

print('Kanade Bot Speedstar 1.2\n')

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

@bot.command(name='help')
#Command that displays all availible commands in an Embed Object.
async def help(ctx):
	helpEM = infoEmbeds()

	await ctx.channel.send(embed=helpEM.help)

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
async def ealinks(ctx):
	ea = infoEmbeds()

	await ctx.channel.send(embed=ea.eaEmbed)

@bot.command(name='selfie')
#Dumb Picture command
async def selfie(ctx):
	await ctx.channel.send(file=discord.File('img/'+'selfie.jpg'))

@bot.command(name='statuschange')
#Calls the above @bot.event
#Cant spam
async def statuschange(ctx):
	sDict = dictionaryStatuses()
	statusRan = random.randint(1,sDict.statusCount)

	if ctx.author.id == 194605769419784192:
		for key in sDict.multiStatus:
			ranStr = str(statusRan)
			if key == ranStr:
				print('Switching to: ' + sDict.multiStatus.get(key))
				await ctx.channel.send('Switching to: ' + sDict.multiStatus.get(key))
				await bot.change_presence(status=discord.Status.online, activity=discord.Game(sDict.multiStatus.get(key)))
				return
	else:
		await ctx.channel.send('Can\'t do that, sorry!')
		return
'''
ky!iidxdan(sp/dp) and ky!sdvxdan commands
sends the class embeds from leoEmbed.py to the channel the command sent from.
'''
@bot.command(name='iidxdansp')
async def iidxdansp(ctx, iidxClass: str):
	  danSP = iidxSPClassEmbeds()
	  danSel = iidxClass

	  if danSel == 'kyu':
	  	await ctx.channel.send(embed=danSP.kyuEMBED)
	  elif danSel == 'dan':
	  	await ctx.channel.send(embed=danSP.danEMBED)
	  elif danSel == 'den':
	  	await ctx.channel.send(embed=danSP.denEMBED)
	  else:
	  	await ctx.channel.send('I dont think thats a class section.')

@bot.command(name='iidxdandp')
async def iidxdandp(ctx, iidxClass: str):
	  danDP = iidxDPClassEmbeds()
	  danSel = iidxClass

	  if danSel == 'kyu':
	  	await ctx.channel.send(embed=danDP.kyuEMBED)
	  elif danSel == 'dan':
	  	await ctx.channel.send(embed=danDP.danEMBED)
	  elif danSel == 'den':
	  	await ctx.channel.send(embed=danDP.denEMBED)
	  else:
	  	await ctx.channel.send('I dont think thats a class section.')

@bot.command(name='sdvxdan')
async def sdvxdan(ctx, rank: str):
	sdvxDan = sdvxDanEmbeds()
	dan = rank
	dumb = str(rank).strip().lower()

	match dumb:
		case '1':
			await ctx.channel.send(embed=sdvxDan.firstEMBED)
		case '2':
			await ctx.channel.send(embed=sdvxDan.secondEMBED)
		case '3':
			await ctx.channel.send(embed=sdvxDan.thirdEMBED)
		case '4':
			await ctx.channel.send(embed=sdvxDan.fourthEMBED)
		case '5':
			await ctx.channel.send(embed=sdvxDan.fifthEMBED)
		case '6':
			await ctx.channel.send(embed=sdvxDan.sixthEMBED)
		case '7':
			await ctx.channel.send(embed=sdvxDan.seventhEMBED)
		case '8':
			await ctx.channel.send(embed=sdvxDan.eighthEMBED)
		case '9':
			await ctx.channel.send(embed=sdvxDan.ninthEMBED)
		case '10':
			await ctx.channel.send(embed=sdvxDan.tenthEMBED)
		case '11':
			await ctx.channel.send(embed=sdvxDan.eleventhEMBED)
		case 'inf':
			await ctx.channel.send(embed=sdvxDan.infEMBED)
		case _:
			await ctx.channel.send('Not a Valid Class Level')

@bot.command(name='events')
#Sends the event schedule embed from leoEmbed.py to channel the command was sent.
async def events(ctx):
	event = infoEmbeds()

	await ctx.channel.send(embed=event.eventEMBED)

@bot.command(name='about')
#Sends an embed describing the bot from leoEmbed.py to channel the command was sent.
async def about(ctx):
	about = infoEmbeds()

	if debugValue >= 1:
		await ctx.channel.send(embed=about.aboutTEST)
	else:
		await ctx.channel.send(embed=about.aboutEMBED)

@bot.command(name='adminHelp')
@commands.has_any_role("Admin", "Mod")
#sends an embed containing commands for admins only from leoEmbed.py to the channel the command was sent.
async def adminHelp(ctx):
	aHelp = infoEmbeds()
	await ctx.channel.send(embed=aHelp.adminHelp)

@bot.command(name='statuslist')
@commands.has_any_role("Admin")
#sends embeds that contain every possible status for the bot from leoEmbed.py the the channel the command was sent.
#do to limitations of discord embed objects, embeds are split.
async def statuslist(ctx):
	ea = infoEmbeds()

	await ctx.channel.send(embed=ea.statusListOne)
	await ctx.channel.send(embed=ea.statusListTwo)

@bot.command(name='memberupdate')
@commands.has_any_role("Admin", "Mod")
#updates the member counter within the nanahira monke.
async def memberupdate(ctx):
	guild = ctx.guild
	channel = 846317672169603072

	if debugValue == 0:
		await bot.get_channel(channel).edit(name = f'Members: {guild.member_count}')
	else:
		await ctx.channel.send('ERROR: Debug Mode is on!')

@bot.command(name='forceabout')
#shows public facing ky!about for when debug mode is on
async def forceabout(ctx):
	about = infoEmbeds()

	await ctx.channel.send(embed=about.aboutEMBED)

@bot.command(name='noresponse')
@commands.has_any_role("Admin", "Mod")
async def noresponse(ctx):
	global responseCheck

	if responseCheck != 0:
		responseCheck = 0
		while responseCheck != 1:
			await ctx.channel.send('Bot responses have been disabled for 30 mins.')
			await asyncio.sleep(1800)
			responseCheck = 1
			await ctx.channel.send('Bot responses are enabled.')
	else:
		await ctx.channel.send('Bot responses have already been disabled.')

@bot.command(name='user')
async def user(ctx):
	members = []

	for User in ctx.guild.User:
		members.append(User.name)

	with open('members.txt', 'w') as f:
		for item in members:
			f.write(item + '\n')
	await ctx.channel.send('Created members file')
	
@bot.command()
async def copy(ctx):
	start = time.time()
	author = ctx.message.author
	if str(author) != "Lolzep#5723": #checks to see if im running the bot
		await ctx.send("You're not my father... command not executed.", delete_after=5)
		if os.path.exists("file.csv"):
			os.remove("file.csv")
	else:
		#counter that starts at 0 for counting amount of messages
		overallcount = 0
		#list for every variable tracked
		lines = []
		counter = []
		authors = []
		made_at = []
		#react = []
		await ctx.send("Processing channel... this might take awhile (or fail)")
		with open("file.csv", "w") as f:
			async for message in ctx.history(limit=20000): #for every msg in channel (up to limit)
				msg_author = message.author.name
				lines.append(msg_author) #lines list used for sorting
				counter.append(str(overallcount + 1))
				authors.append(msg_author)
				made_at.append(message.created_at.strftime("%m/%d/%Y")) #append each message's content to each list
				#react.append(message.reactions)
				overallcount = overallcount + 1 #increase counter by 1 each for-loop

		channel_name = message.channel.name #variables to limit api requests
		server_name = message.guild.name
		f.write(str(server_name) + " #" + str(channel_name) + "\n") #first line inside csv file

		lines.sort() #sort usernames and then find the frequency to count amount of messages from each user
		results = {value: len(list(freq)) for value,freq in groupby(sorted(lines))}

		numbers = [] #used to write the results of frequency of usernames
		users = []
		for value in results.values():
			numbers.append(value)
		for key in results.keys():
			users.append(key)

		both = zip(numbers,users) #sort the overall messages list
		sorted_both = sorted(both, reverse=True)

		writer = csv.writer(f,delimiter='\t')
		writer.writerows(sorted_both) #write the overall messages list

		f.write(str(overallcount) + " total messages\n\n") #total messages

		for w in range(overallcount):
			writer.writerow([counter[w], authors[w], made_at[w]]) #write the appended lists

		os.rename("file.csv", str(server_name) + " #" + str(channel_name) + ".csv") #rename csv
		end = time.time()
		shutil.move(str(server_name) + " #" + str(channel_name) + ".csv","Copy Data/" + str(server_name) + " #" + str(channel_name) + ".csv")
		totaltime = end - start
		totaltime = "{:.2f}".format(totaltime)
		await ctx.send("Done! Data file made! Time taken was " + str(totaltime) + " seconds") #confirm that file was made successfully

@bot.command()
async def boost(ctx):
	boosters = []
	author = ctx.message.author
	if str(author) != "YggBasil#0573" and str(author) != "Lolzep#5723" and str(author) != '☆LEO!☆#7340': #checks to see if correct people are running the bot
		await ctx.send("You're not the right dood... command not executed.", delete_after=5)
	else:
		await ctx.send("just copy these xd")
		for members in ctx.guild.premium_subscribers: #checks all boosted members
			boosters.append(members.name + "#" + members.discriminator) #puts them in a list
		with open("boosters.txt", "w") as f:
			for item in boosters:
				f.write("ar!member " + item + " give 1000\n")
		await ctx.send(file=discord.File("boosters.txt"))

@bot.command()
async def verify(ctx):
	user = ctx.guild.get_member(ctx.message.author.id)
	channel = bot.get_channel(752960043275780224)
	if not ctx.message.attachments:
		await ctx.send("Please attach your image when sending the command. Example: ky!verify [Image]")
		return
	for attachment in ctx.message.attachments:
		await attachment.save(f'VerifyImages/{attachment.filename}')
		await channel.send(file=discord.File(f"VerifyImages/{attachment.filename}"))
		os.remove(f'VerifyImages/{attachment.filename}')
	await channel.send(f"{user.mention}" + " is attempting to verify a skill level. Give the appropriate role as shown in the image.")
	await ctx.send("This skill level claim is now being verified. Your role will be updated if approved.")

@bot.command()
@commands.has_any_role("Admin", "Mod")
async def bonk(ctx, user: discord.Member):
	role = discord.utils.get(ctx.guild.roles, name="horny jail")
	name = user.name
	if role in user.roles:
		await ctx.send(str(name) + " is already horny.")
		return
	if name == "Kanade Bot [ky!]" or name == "Lolzep":
		await ctx.send("Nice try.")
		return
	await user.add_roles(role)
	await ctx.send(":boom: :hammer: " + str(name) + " has been sent to horny jail. Let this be lesson for you.")

@bonk.error
async def bonk_error(ctx, error):
	if isinstance(error, commands.MissingAnyRole):
		await ctx.send("You're not a mod/admin.")
	if isinstance(error, commands.MissingRequiredArgument):
		role = discord.utils.get(ctx.guild.roles, name="horny jail")
		async for message in ctx.history(limit=2):
			name = message.author
		respond = message.author.name
		if respond == "Kanade Bot [ky!]" or respond == "Lolzep":
			await ctx.send("Nice try.")
		return
		await name.add_roles(role)
		await ctx.send(":boom: :hammer: " + str(respond) + " has been sent to horny jail. Let this be lesson for you.")

@bot.command()
@commands.has_any_role("Admin", "Mod", "A Person")
async def unbonk(ctx, user: discord.Member):
	role = discord.utils.get(ctx.guild.roles, name="horny jail")
	name = user.name
	if role not in user.roles:
		await ctx.send(str(name) + " is not horny.")
		return
	await user.remove_roles(role)
	await ctx.send(str(name) + " does not wish to be horny anymore. They just want to be happy.")

@unbonk.error
async def unbonk_error(ctx, error):
	if isinstance(error, commands.MissingAnyRole):
		await ctx.send("You're not a mod/admin.")
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("Please input a horny user.")

@bot.command()
async def vf(ctx, score, clear, level):
	score = str(score[0:4]).strip().ljust(4,"0") #filter score value
	if score != "1000":
		score = score[:3] + '.' + score[3:]
	score = float(score)

	clear = str(clear).strip().upper() #filter clear value

	level = str(level[0:2]).strip() #filter level value
	if int(level) > 20 or int(level) < 0: #if out of range level, return error message
		await ctx.send("`Level out of range (" + level + ")! Using a level of 20`")
		level = 20

  #select correct medal coefficient for clear given

	medal = 0
	clear_medal = {"PUC":1.10,"UC":1.05,"EC":1.02,"C":1.00,"F":0.50}
	for key in clear_medal:
		if clear == key:
			medal = clear_medal.get(key)
	if clear == "PUC" or clear == "UC" or clear == "EC" or clear == "C" or clear == "F":
		pass
	else: #if unknown clear is given, return error message
		await ctx.send("`Unknown clear value (" + clear + "). Acceptable values are PUC, UC, EC, C, and F. C has been used instead`")
		clear = "C"
		medal = 1.00

  #selects the correct grade coefficient and grade based on score given

	grade = 0
	letter = ""
	counter = -1
	score_range = [1000 >= score >= 990, 990 > score >= 980, 980 > score >= 970, 970 > score >= 950, 950 > score >= 930, 930 > score >= 900, 900 > score >= 870, 870 > score >= 750, 750 > score >= 650, 650 > score]
	for item in score_range:
		if item == False:
			counter += 1
		if item == True:
			counter += 1
		break

	grade_letter = {"S":1.05, "AAA+":1.02, "AAA":1.00, "AA+":0.97, "AA":0.94, "A+":0.91, "A":0.88, "B":0.85, "C":0.82, "D":0.80}
	correct = list(grade_letter.items())[counter]
	letter = correct[0]
	grade = correct[1]

  #calculate eg/vw volforce

	eg_volforce = float(level) * (score/1000) * float(grade) * float(medal) * 2 / 100
	vw_volforce = eg_volforce

	factor = 1 / (10 ** 3) #round down
	eg_volforce = (eg_volforce // factor) * factor
	eg_volforce = "{:.3f}".format(eg_volforce) #formatting

	factor = 1 / (10 ** 2) #round down
	vw_volforce = (vw_volforce // factor) * factor
	vw_volforce = "{:.2f}".format(vw_volforce) #formatting

  #making of the embed that's posted by the bot

	embed = discord.Embed(title = "Volforce for " + str(ctx.message.author.name), color = discord.Color.purple())

	embed.set_thumbnail(url=ctx.author.avatar_url)
	embed.add_field(name="Exceed Gear Volforce", value=eg_volforce, inline=False)
	embed.add_field(name="Vivid Wave Volforce", value=vw_volforce, inline=False)
	embed.add_field(name="Level", value=level, inline=False)
	embed.add_field(name="Grade Coefficient", value=str(grade) + " (" + str(letter) + ")", inline=False)
	embed.add_field(name="Clear Coefficient", value=str(medal) + " (" + str(clear) + ")", inline=False)

	await ctx.send(embed=embed)

@bot.command()
async def remywiki(ctx, *args):
	response = "https://remywiki.com/index.php?search="+ args[0]

	for arg in args[1:len(args)]:
		response = response + "%20" + arg

	await ctx.channel.send(response)

@bot.command()
async def playsleft(ctx, arg):
  await ctx.channel.send("You can play " + str(math.floor(float(arg)/6.4)) + " more rounds of a 6.4 credit rhythm game. You will have " + str(round((float(arg)-((float(math.floor(float(arg)/6.4))*float(6.4)))),1)) + " credits leftover.")

@bot.command()
async def wacca(ctx):
	await ctx.channel.send("Wacca cab works now holy shit.")

@bot.command()
async def sdvxtier(ctx):
	await ctx.channel.send("https://docs.google.com/spreadsheets/d/1cFltguBvPplBem-x1STHnG3k4TZzFfyNEZ-RwsQszoo/edit#gid=327051877")
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

	if debugValue <= 1:
		if dumb[0:4] == 'kyt!': ##ignores kyt! commands
			await bot.process_commands(message)
			return
	else:
		if dumb[0:3] == 'ky!': ##ignores ky! commands
			await bot.process_commands(message)
			return

	if responseCheck != 1:
		return

	mDict = dictionaryMessages() #generates everything needed for dictionaries

	iidxRan = random.randint(1, mDict.iidxCount)
	nanaRan = random.randint(1, mDict.nanaCount)
	mikuRan = random.randint(1, mDict.mikuCount)
	tpazRan = random.randint(1, mDict.tPazCount)
	susRan = random.randint(1, mDict.susCount)
	chillsRan = random.randint(1,mDict.chillsCount)
	amogusRan = random.randint(1,4)
	ddrRan = random.randint(1, mDict.ddrCount)
	itgRan = random.randint(1, mDict.itgCount)
	bsbRan = random.randint(1, mDict.bsbCount)
	dripRan = random.randint(1, mDict.dripCount)
	golfRan = random.randint(1, mDict.golfCount)
	loveliveRan = random.randint(1, mDict.loveliveCount)
	valangaRan = random.randint(1, mDict.valangaCount)
	creditRan = random.randint(1, mDict.creditCount)
	totsugekiRan = random.randint(1, mDict.totsugekiCount)
	fRareRan = random.randint(1, mDict.fRareCount)
	isekaiRan = random.randint(1, mDict.isekaiCount)
	chinaRan = random.randint(1, mDict.chinaCount)
	nanaCopyChance = random.randint(1,2)

	if debugValue >= 1:
		print('iidxRan: ' + str(iidxRan))
		print('nanaRan: ' + str(nanaRan))
		print('mikuRan: ' + str(mikuRan))
		print('tpazRan: ' + str(tpazRan))
		print('susRan: ' + str(susRan))
		print('chillsRan: ' + str(chillsRan))
		print('amogusRan: ' + str(amogusRan))
		print('ddrRan: ' + str(ddrRan))
		print('itgRan: ' + str(itgRan))
		print('bsbRan: ' + str(bsbRan))
		print('dripRan: ' + str(dripRan))
		print('golfRan: ' + str(golfRan))
		print('loveliveRan: ' + str(loveliveRan))
		print('valangaRan: ' + str(valangaRan))
		print('creditRan: ' + str(creditRan))
		print('totsugekiRan: ' + str(totsugekiRan))
		print('fRareRan: ' + str(fRareRan))
		print('isekaiRan: ' + str(isekaiRan))
		print('chinaRan: '+ str(chinaRan))
		print('nanaCopyChance: ' + str(nanaCopyChance) + '\n')

	if debugValue == 1:
		coinflip = random.randint(1,2)
		chance =  1
		superRare = 1
		ultraRare = 1
		fuckinRare = 1
		print('coinflip: '+ str(coinflip))
		print('chance: ' + str(chance))
		print('superRare: ' + str(superRare))
		print('ultraRare: ' + str(ultraRare))
		print('fuckinRare: ' + str(fuckinRare) + '\n')
	elif debugValue == 2:
		coinflip = random.randint(1,2)
		chance = random.randint(1,10)
		superRare =random.randint(1,25)
		ultraRare =random.randint(1,100)
		fuckinRare = random.randint(1,500)
		print('coinflip: '+ str(coinflip))
		print('chance: ' + str(chance))
		print('superRare: ' + str(superRare))
		print('ultraRare: ' + str(ultraRare)) 
		print('fuckinRare: ' + str(fuckinRare) + '\n')
	else:
		coinflip = random.randint(1,2)	
		chance = random.randint(1,10)
		superRare = random.randint(1,25)
		ultraRare = random.randint(1,100)
		fuckinRare = random.randint(1,500)

#	If the message sent contains a keyword in the dumbLetters dictionary.
#	The corresponding value is sent to the message's channel

	for key in mDict.dumbPhrases: #sends simple text replies
		if key in dumbLetters:
			if debugValue >= 1:
				print('Triggered Keyword: ' + key + '\n')
			await message.channel.send(mDict.dumbPhrases.get(key))
			return

	for key in mDict.dumbImages: #sends simple image replies
		if key in dumbLetters:
			if debugValue >= 1:
				print('Triggered Keyword: ' + key + '\n')
			await message.channel.send(file=discord.File("img/" + mDict.dumbImages.get(key)))
			return

	if dumbLetters == "bork":
		if debugValue >= 1:
			print('Triggered Keyword: ' + dumbLetters + '\n')
		with open("txt/bestGabe.txt", "r") as f:
			videos = [(line.strip()).split() for line in f]
			f.close()
		rand = str(videos[random.randint(1,271)])
		rand = rand[2:-2]
		await message.channel.send(rand)

	lolzep = "126068015094693888"
	if lolzep == dumbLetters:
		await message.delete()
		await message.channel.send(message.author.mention + " fuck u")

	for key in mDict.emojiResponses:
		if key in dumb:
			dumbLetters = mDict.emojiResponses.get(key)
			
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
				if chance == 1:
					for key in mDict.mikuDict:
						ranStr = str(mikuRan)
						if key == ranStr:
							await message.channel.send(mDict.mikuDict.get(key))
							return
			else:	
				while mikuCounter != 0:
					await message.channel.send(f"{miku.mention}")
					mikuCounter = mikuCounter - 1
				if chance == 1:
					for key in mDict.mikuDict:
						ranStr = str(mikuRan)
						if key == ranStr:
							await message.channel.send(mDict.mikuDict.get(key))
							return
		case 'love live':
			await message.channel.send(f"{michael.mention}")
			if chance == 1:
				for key in mDict.loveliveDict:
					ranStr = str(loveliveRan)
					if key == ranStr:
						await message.channel.send(mDict.loveliveDict.get(key))
						return
		case 'amogus':
			match amogusRan:
				case 1:
					await message.channel.send('ඞ')
					return
				case 2:
					await message.channel.send('<a:amongass:831517773825441812>')
					return
				case 3:
					await message.channel.send('STOP POSTING ABOUT AMONG US! I\'M TIRED OF SEEING IT! MY FRIENDS ON TIKTOK SEND ME MEMES, ON DISCORD IT\'S FUCKING MEMES! I was in a server, right? and ALL OF THE CHANNELS were just among us stuff. I-I showed my champion underwear to my girlfriend and t-the logo I flipped it and I said \"hey babe, when the underwear is sus HAHA DING DING DING DING DING DING DING DI DI DING\" I fucking looked at a trashcan and said \"THAT\'S A BIT SUSSY\" I looked at my penis I think of an astronauts helmet and I go \"PENIS? MORE LIKE PENSUS\" AAAAAAAAAAAAAAHGESFG')
					return
				case 4:
					await message.channel.send(file=discord.File('img/' + 'adumpus.png'))
					return
		
		case 'valanga':
			for key in mDict.valanga:
				ranStr = str(valangaRan)
				if key == ranStr:
					await message.channel.send(mDict.valanga.get(key))
					return

		case 'totsugeki':
			for key in mDict.totsugeki:
				ranStr = str(totsugekiRan)
				if key == ranStr:
					await message.channel.send(mDict.totsugeki.get(key))
					return

		case 'niegil':
			await message.channel.send(mDict.otherRare.get('4'))
			return

		case 'isekai':
			for key in mDict.isekai:
				ranStr = str(isekaiRan)
				if key == ranStr:
					await message.channel.send(mDict.isekai.get(key))
					return

		case 'mayo':
			if coinflip == 1:
				await message.channel.send('mayo is yummi')
				return
			else:
				await message.channel.send('mayo is bad')
				return

	if chance == 1:
		if "im " == dumbLetters[0:3]:
			await message.channel.send("Hi \"" + string.capwords(dumb[3:]) + "\", I'm Kanade Bot!")
		if "i am " == dumbLetters[0:5]:
			await message.channel.send("Hi \"" + string.capwords(dumb[5:]) + "\", I'm Kanade Bot!")

		match dumbLetters:
			case 'glasses':
				await message.channel.send(mDict.otherRare.get('1'))
				return
			case 'vaporeon':
				await message.channel.send(mDict.otherRare.get('3'))
				return
			case 'kaiden':
				await message.channel.send(mDict.otherRare.get('2'))
				return
			case 'nanahira':
				for key in mDict.nanahira:
					ranStr = str(nanaRan)
					if key == ranStr:
						await message.channel.send(mDict.nanahira.get(key))
						return	
			case 'iidx':
				for key in mDict.iidxQuotes:
					ranStr = str(iidxRan)
					if key == ranStr:
						await message.channel.send(mDict.iidxQuotes.get(key))
						return
			case 'tpazolite':
				for key in mDict.tPaz:
					ranStr = str(tpazRan)
					if key == ranStr:
						await message.channel.send(mDict.tPaz.get(key))
						return
			case 'sus':
				for key in mDict.sus:
					ranStr = str(susRan)
					if key == ranStr:
						await message.channel.send(file=discord.File('img/susImage/' + mDict.sus.get(key)))
						return
			case 'ddr':
				for key in mDict.ddr:
					ranStr = str(ddrRan)
					if key == ranStr:
						await message.channel.send(mDict.ddr.get(key))
						return
			case 'itg':
				for key in mDict.itg:
					ranStr = str(itgRan)
					if key == ranStr:
						await message.channel.send(mDict.itg.get(key))
						return
			case 'golf':
				for key in mDict.golf:
					ranStr = str(golfRan)
					if key == ranStr:
						await message.channel.send(mDict.golf.get(key))
						return
			case 'party':
				await message.channel.send('I came to start the party!\n**CAUSE IM THE PARTY STARTER!!**')
				return
			case 'beach':
				if bsbRan == 4:
					await message.channel.send(file=discord.File('img/' + 'bsb.jpg'))
					return
				for key in mDict.bsb:
					ranStr = str(bsbRan)
					if key == ranStr:
						await message.channel.send(mDict.bsb.get(key))
						return
			case 'credit':
				for key in mDict.credit:
					ranStr = str(creditRan)
					if key == ranStr:
						await message.channel.send(file=discord.File('img/creditImage/' + mDict.credit.get(key)))
						return
			case 'drip':
				for key in mDict.drip:
					ranStr = str(dripRan)
					if key == ranStr:
						await message.channel.send(file=discord.File('img/dripImage/' + mDict.drip.get(key)))
						return
			case 'crazy':
				await message.channel.send('cRRRaAaAZZy')
				return
			case 'china':
				for key in mDict.china:
					ranStr = str(chinaRan)
					if key == ranStr:
						await message.channel.send(file=discord.File('img/chinaImage/' + mDict.china.get(key)))
						return
			case 'chills':
                        	for key in mDict.chills:
                                	ranStr = str(chillsRan)
                                	if key == ranStr:
                                         	await message.channel.send(mDict.chills.get(key))
                                         	return
			case 'persona 5':
				await message.channel.send(mDict.otherRare.get('5'))
				return
			case 'endymion':
				await message.channel.send('https://youtu.be/g1lCI3YfoqQ')
				return

			case 'beast':
				await message.channel.send('Mankind knew they cannot change society.\n\nSo instead of reflecting on themselves, they blamed the Beasts.')
				return


	if ultraRare == 1:
		match dumbLetters:
			case 'grace':
				for key in mDict.cursedGrace:
					await message.channel.send(mDict.cursedGrace.get(key) + '\n')
					await message.channel.send(' ឵឵')
					return
			case 'nanahira':
				for key in mDict.nanaCopy:
					await message.channel.send(mDict.nanaCopy.get(key) + '\n')
					await message.channel.send(' ឵឵')
					return
			case 'ddlc':
				if coinflip == 1:
					await message.channel.send(mDict.otherRare.get('6'))
					return
				else:
					await message.channel.send(mDict.otherRare.get('7'))
					return
	if fuckinRare == 1:
		for key in mDict.fRare:
			ranStr = str(fRareRan)
			if key == ranStr:
				await message.channel.send(mDict.fRare.get(key))
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
