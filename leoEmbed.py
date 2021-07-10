#leoEmbed.py
'''
Container for all non user input embeds
'''
import discord
from leoDictionary import dictionaryStatuses

class iidxSPClassEmbeds:
	kyuD = {}
	danD = {}
	denD = {}

	with open('embedResources/'+'kyu.txt') as f:
		for line in f:
	    		(key, val) = line.split('~')
	    		kyuD[str(key)] = val

	with open('embedResources/'+'dan.txt') as f:
		for line in f:
	    		(key, val) = line.split('~')
	    		danD[str(key)] = val

	with open('embedResources/'+'den.txt') as f:
		for line in f:
	    		(key, val) = line.split('~')
	    		denD[str(key)] = val

	kyuEMBED = discord.Embed(colour = discord.Colour.red())

	kyuEMBED.set_author(name='7th Kyu (七級) to 1st Kyu (一級)')

	kyuEMBED.add_field(name="7th Kyu (七級)", value='1. ' + kyuD.get('7-1') + '2. ' + kyuD.get('7-2') + '3. ' + kyuD.get('7-3') + '4. ' + kyuD.get('7-4'), inline=False)
	kyuEMBED.add_field(name="6th Kyu (六級)", value='1. ' + kyuD.get('6-1') + '2. ' + kyuD.get('6-2') + '3. ' + kyuD.get('6-3') + '4. ' + kyuD.get('6-4'), inline=False)
	kyuEMBED.add_field(name="5th Kyu (五級)", value='1. ' + kyuD.get('5-1') + '2. ' + kyuD.get('5-2') + '3. ' + kyuD.get('5-3') + '4. ' + kyuD.get('5-4'), inline=False)
	kyuEMBED.add_field(name="4th Kyu (四級)", value='1. ' + kyuD.get('4-1') + '2. ' + kyuD.get('4-2') + '3. ' + kyuD.get('4-3') + '4. ' + kyuD.get('4-4'), inline=False)
	kyuEMBED.add_field(name="3rd Kyu (三級)", value='1. ' + kyuD.get('3-1') + '2. ' + kyuD.get('3-2') + '3. ' + kyuD.get('3-3') + '4. ' + kyuD.get('3-4'), inline=False)
	kyuEMBED.add_field(name="2nd Kyu (二級)", value='1. ' + kyuD.get('2-1') + '2. ' + kyuD.get('2-2') + '3. ' + kyuD.get('2-3') + '4. ' + kyuD.get('2-4'), inline=False)
	kyuEMBED.add_field(name="1st Kyu (一級)", value='1. ' + kyuD.get('1-1') + '2. ' + kyuD.get('1-2') + '3. ' + kyuD.get('1-3') + '4. ' + kyuD.get('1-4'), inline=False)

	danEMBED = discord.Embed(colour = discord.Colour.red())

	danEMBED.set_author(name='1st Dan (初段) to 10th Dan (十段)')

	danEMBED.add_field(name="1st Dan (初段)", value='1. ' + danD.get('1-1') + '2. ' + danD.get('1-2') + '3. ' + danD.get('1-3') + '4. ' + danD.get('1-4'), inline=False)
	danEMBED.add_field(name="2nd Dan (二段)", value='1. ' + danD.get('2-1') + '2. ' + danD.get('2-2') + '3. ' + danD.get('2-3') + '4. ' + danD.get('2-4'), inline=False)
	danEMBED.add_field(name="3rd Dan (三段)", value='1. ' + danD.get('3-1') + '2. ' + danD.get('3-2') + '3. ' + danD.get('3-3') + '4. ' + danD.get('3-4'), inline=False)
	danEMBED.add_field(name="4th Dan (四段)", value='1. ' + danD.get('4-1') + '2. ' + danD.get('4-2') + '3. ' + danD.get('4-3') + '4. ' + danD.get('4-4'), inline=False)
	danEMBED.add_field(name="5th Dan (五段)", value='1. ' + danD.get('5-1') + '2. ' + danD.get('5-2') + '3. ' + danD.get('5-3') + '4. ' + danD.get('5-4'), inline=False)
	danEMBED.add_field(name="6th Dan (六段)", value='1. ' + danD.get('6-1') + '2. ' + danD.get('6-2') + '3. ' + danD.get('6-3') + '4. ' + danD.get('6-4'), inline=False)
	danEMBED.add_field(name="7th Dan (七段)", value='1. ' + danD.get('7-1') + '2. ' + danD.get('7-2') + '3. ' + danD.get('7-3') + '4. ' + danD.get('7-4'), inline=False)
	danEMBED.add_field(name="8th Dan (八段)", value='1. ' + danD.get('8-1') + '2. ' + danD.get('8-2') + '3. ' + danD.get('8-3') + '4. ' + danD.get('8-4'), inline=False)
	danEMBED.add_field(name="9th Dan (九段)", value='1. ' + danD.get('9-1') + '2. ' + danD.get('9-2') + '3. ' + danD.get('9-3') + '4. ' + danD.get('9-4'), inline=False)
	danEMBED.add_field(name="10th Dan (十段) ", value='1. ' + danD.get('10-1') + '2. ' + danD.get('10-2') + '3. ' + danD.get('10-3') + '4. ' + danD.get('10-4'), inline=False)

	denEMBED = discord.Embed(colour = discord.Colour.red())

	denEMBED.set_author(name='Chuuden (中伝) and Kaiden (皆伝)')

	denEMBED.add_field(name="Chuuden (中伝)", value='1. ' + denD.get('1-1') + '2. ' + denD.get('1-2') + '3. ' + denD.get('1-3') + '4. ' + denD.get('1-4'), inline=False)
	denEMBED.add_field(name="Kaiden (皆伝)", value='1. ' + denD.get('2-1') + '2. ' + denD.get('2-2') + '3. ' + denD.get('2-3') + '4. ' + denD.get('2-4'), inline=False)

class iidxDPClassEmbeds:
	kyuD = {}
	danD = {}
	denD = {}

	with open('embedResources/'+'kyuDP.txt') as f:
		for line in f:
	    		(key, val) = line.split('~')
	    		kyuD[str(key)] = val

	with open('embedResources/'+'danDP.txt') as f:
		for line in f:
	    		(key, val) = line.split('|')
	    		danD[str(key)] = val

	with open('embedResources/'+'denDP.txt') as f:
		for line in f:
	    		(key, val) = line.split('~')
	    		denD[str(key)] = val

	kyuEMBED = discord.Embed(colour = discord.Colour.red())

	kyuEMBED.set_author(name='7th Kyu (七級) to 1st Kyu (一級)')

	kyuEMBED.add_field(name="7th Kyu (七級)", value='1. ' + kyuD.get('7-1') + '2. ' + kyuD.get('7-2') + '3. ' + kyuD.get('7-3') + '4. ' + kyuD.get('7-4'), inline=False)
	kyuEMBED.add_field(name="6th Kyu (六級)", value='1. ' + kyuD.get('6-1') + '2. ' + kyuD.get('6-2') + '3. ' + kyuD.get('6-3') + '4. ' + kyuD.get('6-4'), inline=False)
	kyuEMBED.add_field(name="5th Kyu (五級)", value='1. ' + kyuD.get('5-1') + '2. ' + kyuD.get('5-2') + '3. ' + kyuD.get('5-3') + '4. ' + kyuD.get('5-4'), inline=False)
	kyuEMBED.add_field(name="4th Kyu (四級)", value='1. ' + kyuD.get('4-1') + '2. ' + kyuD.get('4-2') + '3. ' + kyuD.get('4-3') + '4. ' + kyuD.get('4-4'), inline=False)
	kyuEMBED.add_field(name="3rd Kyu (三級)", value='1. ' + kyuD.get('3-1') + '2. ' + kyuD.get('3-2') + '3. ' + kyuD.get('3-3') + '4. ' + kyuD.get('3-4'), inline=False)
	kyuEMBED.add_field(name="2nd Kyu (二級)", value='1. ' + kyuD.get('2-1') + '2. ' + kyuD.get('2-2') + '3. ' + kyuD.get('2-3') + '4. ' + kyuD.get('2-4'), inline=False)
	kyuEMBED.add_field(name="1st Kyu (一級)", value='1. ' + kyuD.get('1-1') + '2. ' + kyuD.get('1-2') + '3. ' + kyuD.get('1-3') + '4. ' + kyuD.get('1-4'), inline=False)

	danEMBED = discord.Embed(colour = discord.Colour.red())

	danEMBED.set_author(name='1st Dan (初段) to 10th Dan (十段)')

	danEMBED.add_field(name="1st Dan (初段)", value='1. ' + danD.get('1-1') + '2. ' + danD.get('1-2') + '3. ' + danD.get('1-3') + '4. ' + danD.get('1-4'), inline=False)
	danEMBED.add_field(name="2nd Dan (二段)", value='1. ' + danD.get('2-1') + '2. ' + danD.get('2-2') + '3. ' + danD.get('2-3') + '4. ' + danD.get('2-4'), inline=False)
	danEMBED.add_field(name="3rd Dan (三段)", value='1. ' + danD.get('3-1') + '2. ' + danD.get('3-2') + '3. ' + danD.get('3-3') + '4. ' + danD.get('3-4'), inline=False)
	danEMBED.add_field(name="4th Dan (四段)", value='1. ' + danD.get('4-1') + '2. ' + danD.get('4-2') + '3. ' + danD.get('4-3') + '4. ' + danD.get('4-4'), inline=False)
	danEMBED.add_field(name="5th Dan (五段)", value='1. ' + danD.get('5-1') + '2. ' + danD.get('5-2') + '3. ' + danD.get('5-3') + '4. ' + danD.get('5-4'), inline=False)
	danEMBED.add_field(name="6th Dan (六段)", value='1. ' + danD.get('6-1') + '2. ' + danD.get('6-2') + '3. ' + danD.get('6-3') + '4. ' + danD.get('6-4'), inline=False)
	danEMBED.add_field(name="7th Dan (七段)", value='1. ' + danD.get('7-1') + '2. ' + danD.get('7-2') + '3. ' + danD.get('7-3') + '4. ' + danD.get('7-4'), inline=False)
	danEMBED.add_field(name="8th Dan (八段)", value='1. ' + danD.get('8-1') + '2. ' + danD.get('8-2') + '3. ' + danD.get('8-3') + '4. ' + danD.get('8-4'), inline=False)
	danEMBED.add_field(name="9th Dan (九段)", value='1. ' + danD.get('9-1') + '2. ' + danD.get('9-2') + '3. ' + danD.get('9-3') + '4. ' + danD.get('9-4'), inline=False)
	danEMBED.add_field(name="10th Dan (十段) ", value='1. ' + danD.get('10-1') + '2. ' + danD.get('10-2') + '3. ' + danD.get('10-3') + '4. ' + danD.get('10-4'), inline=False)

	denEMBED = discord.Embed(colour = discord.Colour.red())

	denEMBED.set_author(name='Chuuden (中伝) and Kaiden (皆伝)')

	denEMBED.add_field(name="Chuuden (中伝)", value='1. ' + denD.get('1-1') + '2. ' + denD.get('1-2') + '3. ' + denD.get('1-3') + '4. ' + denD.get('1-4'), inline=False)
	denEMBED.add_field(name="Kaiden (皆伝)", value='1. ' + denD.get('2-1') + '2. ' + denD.get('2-2') + '3. ' + denD.get('2-3') + '4. ' + denD.get('2-4'), inline=False)

class sdvxDanEmbeds:
	oneToFive = {}
	sixToTen = {}
	elevenAndInf = {}

	with open('embedResources/'+'sdvx1to5.txt') as f:
		for line in f:
	    		(key, val) = line.split('|')
	    		oneToFive[str(key)] = val

	with open('embedResources/'+'sdvx6to10.txt') as f:
		for line in f:
	    		(key, val) = line.split('|')
	    		sixToTen[str(key)] = val

	with open('embedResources/'+'sdvx11andInf.txt') as f:
		for line in f:
	    		(key, val) = line.split('|')
	    		elevenAndInf[str(key)] = val

	firstEMBED = discord.Embed(colour = discord.Colour.red())

	firstEMBED.set_author(name='LV.01 岳翔')

	firstEMBED.add_field(name='COURSE A', value='1. ' + oneToFive.get('1-1-1') + '2. ' + oneToFive.get('1-1-2') + '3. ' + oneToFive.get('1-1-3'), inline=False)
	firstEMBED.add_field(name='COURSE B', value='1. ' + oneToFive.get('1-2-1') + '2. ' + oneToFive.get('1-2-2') + '3. ' + oneToFive.get('1-2-3'), inline=False)
	firstEMBED.add_field(name='COURSE C', value='1. ' + oneToFive.get('1-3-1') + '2. ' + oneToFive.get('1-3-2') + '3. ' + oneToFive.get('1-3-3'), inline=False)

	secondEMBED = discord.Embed(colour = discord.Colour.red())

	secondEMBED.set_author(name='LV.02 流星')

	secondEMBED.add_field(name='COURSE A', value='1. ' + oneToFive.get('2-1-1') + '2. ' + oneToFive.get('2-1-2') + '3. ' + oneToFive.get('2-1-3'), inline=False)
	secondEMBED.add_field(name='COURSE B', value='1. ' + oneToFive.get('2-2-1') + '2. ' + oneToFive.get('2-2-2') + '3. ' + oneToFive.get('2-2-3'), inline=False)
	secondEMBED.add_field(name='COURSE C', value='1. ' + oneToFive.get('2-3-1') + '2. ' + oneToFive.get('2-3-2') + '3. ' + oneToFive.get('2-3-3'), inline=False)

	thirdEMBED = discord.Embed(colour = discord.Colour.red())

	thirdEMBED.set_author(name='LV.03 月衝')

	thirdEMBED.add_field(name='COURSE A', value='1. ' + oneToFive.get('3-1-1') + '2. ' + oneToFive.get('3-1-2') + '3. ' + oneToFive.get('3-1-3'), inline=False)
	thirdEMBED.add_field(name='COURSE B', value='1. ' + oneToFive.get('3-2-1') + '2. ' + oneToFive.get('3-2-2') + '3. ' + oneToFive.get('3-2-3'), inline=False)
	thirdEMBED.add_field(name='COURSE C', value='1. ' + oneToFive.get('3-3-1') + '2. ' + oneToFive.get('3-3-2') + '3. ' + oneToFive.get('3-3-3'), inline=False)

	fourthEMBED = discord.Embed(colour = discord.Colour.red())

	fourthEMBED.set_author(name='LV.04 瞬光')

	fourthEMBED.add_field(name='COURSE A', value='1. ' + oneToFive.get('4-1-1') + '2. ' + oneToFive.get('4-1-2') + '3. ' + oneToFive.get('4-1-3'), inline=False)
	fourthEMBED.add_field(name='COURSE B', value='1. ' + oneToFive.get('4-2-1') + '2. ' + oneToFive.get('4-2-2') + '3. ' + oneToFive.get('4-2-3'), inline=False)
	fourthEMBED.add_field(name='COURSE C', value='1. ' + oneToFive.get('4-3-1') + '2. ' + oneToFive.get('4-3-2') + '3. ' + oneToFive.get('4-3-3'), inline=False)

	fifthEMBED = discord.Embed(colour = discord.Colour.red())

	fifthEMBED.set_author(name='LV.05 天極')

	fifthEMBED.add_field(name='COURSE A', value='1. ' + oneToFive.get('5-1-1') + '2. ' + oneToFive.get('5-1-2') + '3. ' + oneToFive.get('5-1-3'), inline=False)
	fifthEMBED.add_field(name='COURSE B', value='1. ' + oneToFive.get('5-2-1') + '2. ' + oneToFive.get('5-2-2') + '3. ' + oneToFive.get('5-2-3'), inline=False)
	fifthEMBED.add_field(name='COURSE C', value='1. ' + oneToFive.get('5-3-1') + '2. ' + oneToFive.get('5-3-2') + '3. ' + oneToFive.get('5-3-3'), inline=False)

	sixthEMBED = discord.Embed(colour = discord.Colour.red())

	sixthEMBED.set_author(name='LV.06 烈風')

	sixthEMBED.add_field(name='COURSE A', value='1. ' + sixToTen.get('1-1-1') + '2. ' + sixToTen.get('1-1-2') + '3. ' + sixToTen.get('1-1-3'), inline=False)
	sixthEMBED.add_field(name='COURSE B', value='1. ' + sixToTen.get('1-2-1') + '2. ' + sixToTen.get('1-2-2') + '3. ' + sixToTen.get('1-2-3'), inline=False)
	sixthEMBED.add_field(name='COURSE C', value='1. ' + sixToTen.get('1-3-1') + '2. ' + sixToTen.get('1-3-2') + '3. ' + sixToTen.get('1-3-3'), inline=False)

	seventhEMBED = discord.Embed(colour = discord.Colour.red())

	seventhEMBED.set_author(name='LV.07 雷電')

	seventhEMBED.add_field(name='COURSE A', value='1. ' + sixToTen.get('2-1-1') + '2. ' + sixToTen.get('2-1-2') + '3. ' + sixToTen.get('2-1-3'), inline=False)
	seventhEMBED.add_field(name='COURSE B', value='1. ' + sixToTen.get('2-2-1') + '2. ' + sixToTen.get('2-2-2') + '3. ' + sixToTen.get('2-2-3'), inline=False)
	seventhEMBED.add_field(name='COURSE C', value='1. ' + sixToTen.get('2-3-1') + '2. ' + sixToTen.get('2-3-2') + '3. ' + sixToTen.get('2-3-3'), inline=False)

	eighthEMBED = discord.Embed(colour = discord.Colour.red())

	eighthEMBED.set_author(name='LV.08 麗華')

	eighthEMBED.add_field(name='COURSE A', value='1. ' + sixToTen.get('3-1-1') + '2. ' + sixToTen.get('3-1-2') + '3. ' + sixToTen.get('3-1-3'), inline=False)
	eighthEMBED.add_field(name='COURSE B', value='1. ' + sixToTen.get('3-2-1') + '2. ' + sixToTen.get('3-2-2') + '3. ' + sixToTen.get('3-2-3'), inline=False)
	eighthEMBED.add_field(name='COURSE C', value='1. ' + sixToTen.get('3-3-1') + '2. ' + sixToTen.get('3-3-2') + '3. ' + sixToTen.get('3-3-3'), inline=False)

	ninthEMBED = discord.Embed(colour = discord.Colour.red())

	ninthEMBED.set_author(name='LV.09 魔騎士')

	ninthEMBED.add_field(name='COURSE A', value='1. ' + sixToTen.get('4-1-1') + '2. ' + sixToTen.get('4-1-2') + '3. ' + sixToTen.get('4-1-3'), inline=False)
	ninthEMBED.add_field(name='COURSE B', value='1. ' + sixToTen.get('4-2-1') + '2. ' + sixToTen.get('4-2-2') + '3. ' + sixToTen.get('4-2-3'), inline=False)
	ninthEMBED.add_field(name='COURSE C', value='1. ' + sixToTen.get('4-3-1') + '2. ' + sixToTen.get('4-3-2') + '3. ' + sixToTen.get('4-3-3'), inline=False)

	tenthEMBED = discord.Embed(colour = discord.Colour.red())

	tenthEMBED.set_author(name='LV.10 剛力羅')

	tenthEMBED.add_field(name='COURSE A', value='1. ' + sixToTen.get('5-1-1') + '2. ' + sixToTen.get('5-1-2') + '3. ' + sixToTen.get('5-1-3'), inline=False)
	tenthEMBED.add_field(name='COURSE B', value='1. ' + sixToTen.get('5-2-1') + '2. ' + sixToTen.get('5-2-2') + '3. ' + sixToTen.get('5-2-3'), inline=False)
	tenthEMBED.add_field(name='COURSE C', value='1. ' + sixToTen.get('5-3-1') + '2. ' + sixToTen.get('5-3-2') + '3. ' + sixToTen.get('5-3-3'), inline=False)

	eleventhEMBED = discord.Embed(colour = discord.Colour.red())

	eleventhEMBED.set_author(name='LV.11 或帝滅斗')

	eleventhEMBED.add_field(name='COURSE A', value='1. ' + elevenAndInf.get('1-1-1') + '2. ' + elevenAndInf.get('1-1-2') + '3. ' + elevenAndInf.get('1-1-3'), inline=False)
	eleventhEMBED.add_field(name='COURSE B', value='1. ' + elevenAndInf.get('1-2-1') + '2. ' + elevenAndInf.get('1-2-2') + '3. ' + elevenAndInf.get('1-2-3'), inline=False)

	infEMBED = discord.Embed(colour = discord.Colour.red())

	infEMBED.set_author(name='LV.∞ 暴龍天')

	infEMBED.add_field(name='COURSE A', value='1. ' + elevenAndInf.get('2-1-1') + '2. ' + elevenAndInf.get('2-1-2') + '3. ' + elevenAndInf.get('2-1-3'), inline=False)
	infEMBED.add_field(name='COURSE B', value='1. ' + elevenAndInf.get('2-2-1') + '2. ' + elevenAndInf.get('2-2-2') + '3. ' + elevenAndInf.get('2-2-3'), inline=False)

class infoEmbeds:
	eventD = {}
	
	sDict = dictionaryStatuses()

	with open('embedResources/'+'events.txt') as f:
		for line in f:
	    		(key, val) = line.split('~')
	    		eventD[str(key)] = val

	eaEmbed = discord.Embed(colour = discord.Colour.red())

	eaEmbed.set_author(name='e-amusement links')
	eaEmbed.set_thumbnail(url='https://i.postimg.cc/XYHdy2Lf/ea.png')
	eaEmbed.add_field(name='e-amusement pass', value='https://p.eagate.573.jp/gate/eapass/menu.html', inline=False)
	eaEmbed.add_field(name='Paseli Charge', value='https://paseli.konami.net/charge/top.html', inline=False)
	eaEmbed.add_field(name='beatmania IIDX 28 Bistrover', value='https://p.eagate.573.jp/game/2dx/28/top/index.html', inline=False)
	eaEmbed.add_field(name='beatmania IIDX INFINITAS', value='https://p.eagate.573.jp/game/infinitas/2/', inline=False)
	eaEmbed.add_field(name='SOUND VOLTEX Exceed Gear', value='https://p.eagate.573.jp/game/sdvx/vi/', inline=False)
	eaEmbed.add_field(name='SOUND VOLTEX コナステ', value='https://p.eagate.573.jp/game/eacsdvx/iii/p/common/top.html', inline=False)
	eaEmbed.add_field(name='DanceDanceRevolution A20 PLUS', value='https://p.eagate.573.jp/game/ddr/ddra20/p/', inline=False)

	help = discord.Embed(colour = discord.Colour.red())

	help.set_author(name='Help')
	help.set_thumbnail(url='https://i.postimg.cc/vTbZZ43s/valanga.png')

	help.add_field(name='about', value='ky!about || Displays Kanade Bot version and patch notes', inline=False)
	help.add_field(name='adminHelp', value='ky!adminHelp || Shows admin commands (admin only)', inline=False)
	help.add_field(name='events', value='ky!events || Displays Nanahira Monkey events within the range of a month', inline=False)
	help.add_field(name='ealinks', value='ky!ealinks || Displays various important e-amusement links', inline=False)
	help.add_field(name='exscore', value='ky!exscore <Total Notes> || Calculates the EXSCORE amount necesary to get MAX, AAA, AA, or A from a songs total notes.', inline=False)
	help.add_field(name='iidxdansp', value='ky!iidxdansp <class-section> || displays IIDX class courses per section. (SP) Valid Arguments: kyu, dan, and den', inline=False)
	help.add_field(name='iidxdandp', value='ky!iidxdandp <class-section> || displays IIDX class courses per section. (DP) Valid Arguments: kyu, dan, and den', inline=False)
	help.add_field(name='sdvxdan', value='ky!sdvxdan <skill-level> || Displays SDVX SKILL ANALYZER courses per skill level. Valid Arguments: 1 - 11 and inf', inline=False)
	help.add_field(name='vf', value='ky!vf <First 4 of score> <PUC, UC, etc.> <difficulty> || Determines Volforce by user provided values.', inline=False)
	help.add_field(name='remywiki', value='ky!remywiki <search term> || Searches RemyWiki and links it to channel used', inline=False)
	help.add_field(name='playsleft', value='ky!playsleft <number of credits> || Sends how many plays left you have on 6.4 credit rhythm game based on user input.', inline=False)
	help.add_field(name='wacca', value='ky!wacca || Tells you that wacca is broke', inline=False)
	help.add_field(name='sdvxtier', value='ky!sdvxtier || Sends link for SDVX clear tierlist', inline=False)
	help.add_field(name='certain messages', value='imminent funni', inline=False)

	eventEMBED = discord.Embed(colour = discord.Colour.red())

	eventEMBED.set_author(name='Nanahira Monkey Events in July')
	eventEMBED.set_thumbnail(url='https://i.ibb.co/z6ftf9X/monke.png')

	eventEMBED.add_field(name="Week 27", value='1. ' + eventD.get('1-1') + '2. ' + eventD.get('1-2') + '3. ' + eventD.get('1-3'), inline=False)
	eventEMBED.add_field(name="Week 28", value='1. ' + eventD.get('2-1') + '2. ' + eventD.get('2-2') + '3. ' + eventD.get('2-3'), inline=False)
	eventEMBED.add_field(name="Week 29", value='1. ' + eventD.get('3-1') + '2. ' + eventD.get('3-2') + '3. ' + eventD.get('3-3'), inline=False)
	eventEMBED.add_field(name="Week 30", value='1. ' + eventD.get('4-1') + '2. ' + eventD.get('4-2') + '3. ' + eventD.get('4-3'), inline=False)
	eventEMBED.add_field(name="Week 31", value='1. ' + eventD.get('5-1') + '2. ' + eventD.get('5-2') + '3. ' + eventD.get('5-3'), inline=False)
	eventEMBED.add_field(name="Week 32", value='1. ' + eventD.get('6-1') + '2. ' + eventD.get('6-2') + '3. ' + eventD.get('6-3'), inline=False)

	aboutEMBED = discord.Embed(colour = discord.Colour.red())

	aboutEMBED.set_thumbnail(url='https://i.postimg.cc/vTbZZ43s/valanga.png')

	aboutEMBED.add_field(name="Kanade Bot Speedstar 1.1.1", value='Multi Purpose Discord bot made for the Nanahira Monke server', inline=False)
	aboutEMBED.add_field(name="Contributors", value='Lolzep #5723\nProphetOfTruth1#1783\n☆LEO!☆#7340', inline=False)
	aboutEMBED.add_field(name="Recent Changes", value='Nerfed a bit', inline=False)

	aboutTEST = discord.Embed(colour = discord.Colour.red())

	aboutTEST.set_thumbnail(url='https://i.postimg.cc/vTbZZ43s/valanga.png')

	aboutTEST.add_field(name="Kanade Bot TEST VERSION", value='Testing branch of the main Kanade Bot', inline=False)
	aboutTEST.add_field(name="Recent Changes", value='Remember to put recent changes in aboutEMBED!', inline=False)

	adminHelp = discord.Embed(colour = discord.Colour.red())

	adminHelp.set_author(name='Kanade Bot Admin Help')
	adminHelp.set_thumbnail(url='https://i.postimg.cc/vTbZZ43s/valanga.png')

	adminHelp.add_field(name='statuschange', value='ky!statuschange || randomly replaces status (☆LEO!☆ only)', inline=False)
	adminHelp.add_field(name='boost', value='ky!boost || Creates a txt file listing all current server boosters', inline=False)
	adminHelp.add_field(name='bonk', value='ky!bonk <user-mention> || Sends mentioned user to horny jail', inline=False)
	adminHelp.add_field(name='unbonk', value='ky!unbonk <user-mention> || Removes mentioned user to horny jail', inline=False)
	adminHelp.add_field(name='copy', value='ky!copy || counts every message sent in every channel (Lolzep Only)', inline=False)
	adminHelp.add_field(name='memberupdate', value='ky!memberupdate || Updates the member count.', inline=False)
	adminHelp.add_field(name='statuslist', value='ky!statuslist || List all availible statuses (currently useless)', inline=False)
	adminHelp.add_field(name='forceabout', value='kyt!forceabout || Forces public facing ky!about while in debug mode.', inline=False)

	statusListOne = discord.Embed(colour = discord.Colour.red())
	statusListTwo = discord.Embed(colour = discord.Colour.red())

	for key in sDict.multiStatus:
		keyInt = int(key)
		statusListOne.add_field(name=key, value=sDict.multiStatus.get(key), inline=True)
		if keyInt > 25:
			 statusListTwo.add_field(name=key, value=sDict.multiStatus.get(key), inline=True)
