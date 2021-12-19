'''
leoDictionary.py
classes for creating dictionaries in LEO! BOT
dictionaryMessages is for the response messages
dictionaryStatuses is for randomized statuses
'''
class dictionaryMessages:
	dumbPhrases = {}
	
	iidxQuotes = {}
	iidxCount = 0
	
	otherRare = {}
	
	nanahira = {}
	nanaCount = 0
	nanaCopy = {}
	
	cursedGrace = {}
	
	mikuDict ={}
	mikuCount = 0
	
	tPaz = {}
	tPazCount = 0
	
	sus = {}
	susCount = 0
	
	dumbImages = {}
	
	chills = {}
	chillsCount = 0
	
	ddr = {}
	ddrCount = 0
	
	itg = {}
	itgCount = 0
	
	bsb = {}
	bsbCount = 0
	
	drip = {}
	dripCount = 0

	golf = {}
	golfCount = 0
	
	loveliveDict = {}
	loveliveCount = 0
	
	valanga = {}
	valangaCount = 0
	
	credit = {}
	creditCount = 0

	totsugeki = {}
	totsugekiCount = 0

	fRare = {}
	fRareCount = 0

	otherResponses = {}

	emojiResponses = {}

	isekai = {}
	isekaiCount = 0

	china = {}
	chinaCount = 0

	qotdList = {}
	qotdCount = 0

	lain = {}
	lainCount = 0

	with open('txt/'+'dumbPhrases.txt') as f:
		for line in f:
	    		(key, val) = line.split('~')
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
	    		(key, val) = line.split('|')
	    		nanaCopy[str(key)] = val

	with open('txt/'+'cursedGrace.txt') as f:
		for line in f:
	    		(key, val) = line.split('|')
	    		cursedGrace[str(key)] = val

	with open('txt/'+'miku.txt') as f:
		for line in f:
	    		(key, val) = line.split('~')
	    		mikuDict[str(key)] = val
	    		mikuCount = mikuCount + 1

	with open('txt/'+'tPaz.txt') as f:
		for line in f:
	    		(key, val) = line.split('~')
	    		tPaz[str(key)] = val
	    		tPazCount = tPazCount + 1

	with open('txt/'+'sus.txt') as f:
		for line in f:
	    		(key, val) = line.split('~')
	    		newVal = val.rstrip()
	    		sus[str(key)] = newVal
	    		susCount = susCount + 1

	with open('txt/'+'dumbImages.txt') as f:
		for line in f:
	    		(key, val) = line.split('_')
	    		newVal = val.rstrip()
	    		dumbImages[str(key)] = newVal

	with open('txt/'+'chills.txt') as f:
		for line in f:
	    		(key, val) = line.split('~')
	    		newVal = val.rstrip()
	    		chills[str(key)] = newVal
	    		chillsCount = chillsCount + 1

	with open ('txt/'+'ddr.txt') as f:
		for line in f:
			(key, val) = line.split('|')
			newVal = val.rstrip()
			ddr[str(key)] = newVal
			ddrCount = ddrCount + 1

	with open ('txt/'+'itg.txt') as f:
		for line in f:
			(key, val) = line.split('|')
			newVal = val.rstrip()
			itg[str(key)] = newVal
			itgCount = itgCount + 1

	with open ('txt/'+'bsb.txt') as f:
		for line in f:
			(key, val) = line.split('~')
			newVal = val.rstrip()
			bsb[str(key)] = newVal
			bsbCount = bsbCount + 1

	with open('txt/'+'drip.txt') as f:
		for line in f:
			(key, val) = line.split('|')
			newVal = val.rstrip()
			drip[str(key)] = newVal
			dripCount = dripCount + 1

	with open('txt/'+'putt.txt') as f:
		for line in f:
			(key, val) = line.split('|')
			newVal = val.rstrip()
			golf[str(key)] = newVal
			golfCount = golfCount + 1

	with open('txt/'+'lovelive.txt') as f:
		for line in f:
			(key, val) = line.split('|')
			loveliveDict[str(key)] = val
			loveliveCount = loveliveCount + 1

	with open('txt/'+'valanga.txt') as f:
		for line in f:
			(key, val) = line.split('|')
			valanga[str(key)] = val
			valangaCount = valangaCount + 1
			
	with open('txt/'+'credit.txt') as f:
		for line in f:
			(key, val) = line.split('|')
			newVal = val.rstrip()
			credit[str(key)] = newVal
			creditCount = creditCount + 1

	with open('txt/'+'may.txt') as f:
		for line in f:
			(key, val) = line.split('|')
			newVal = val.rstrip()
			totsugeki[str(key)] = newVal
			totsugekiCount = totsugekiCount + 1

	with open('txt/'+'fuckinRare.txt') as f:
		for line in f:
			(key, val) = line.split('|')
			newVal = val.rstrip()
			fRare[str(key)] = newVal
			fRareCount = fRareCount + 1

	with open('txt/'+'otherResponses.txt') as f:
		for line in f:
			(key, val) = line.split('|')
			newVal = val.rstrip()
			otherResponses[str(key)] = newVal

	with open('txt/'+'emojiResponses.txt') as f:
		for line in f:
			(key, val) = line.split('|')
			newVal = val.rstrip()
			emojiResponses[str(key)] = newVal

	with open('txt/'+'isekai.txt') as f:
		for line in f:
			(key, val) = line.split('|')
			newVal = val.rstrip()
			isekai[str(key)] = newVal
			isekaiCount = isekaiCount + 1

	with open('txt/'+'china.txt') as f:
		for line in f:
			(key, val) = line.split('|')
			newVal = val.rstrip()
			china[str(key)] = newVal
			chinaCount = chinaCount + 1
	
	with open('txt/'+'lain.txt') as f:
		for line in f:
			(key, val) = line.split('|')
			newVal = val.rstrip()
			lain[str(key)] = newVal
			lainCount = lainCount + 1

	with open('qotdResource/'+'qotd.txt') as f:
		for line in f:
			(key, val) = line.split('|')
			newVal = val.rstrip()
			qotdList[str(key)] = val
			qotdCount = qotdCount + 1

class dictionaryStatuses:
	multiStatus = {}
	statusCount = 0

	with open('txt/'+'multiStatus.txt') as f:
		for line in f:
	    		(key, val) = line.split('_')
	    		newVal = val.rstrip()
	    		multiStatus[str(key)] = newVal
	    		statusCount = statusCount + 1