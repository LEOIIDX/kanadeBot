'''
leoDictionary.py
classes for creating dictionaries in LEO! BOT
dictionaryMessages is for the response messages
dictionaryStatuses is for randomized statuses
'''
class dictionaryMessages:
	otherResponses = {}

	emojiResponses = {}

	with open('txt/'+'otherResponses.txt', encoding="utf8") as f:
		for line in f:
			(key, val) = line.split('|')
			newVal = val.rstrip()
			otherResponses[str(key)] = newVal

	with open('txt/'+'emojiResponses.txt', encoding="utf8") as f:
		for line in f:
			(key, val) = line.split('|')
			newVal = val.rstrip()
			emojiResponses[str(key)] = newVal

	with open('qotdResource/'+'qotd.txt', encoding="utf8") as f:
		for line in f:
			(key, val) = line.split('|')
			newVal = val.rstrip()
			qotdList[str(key)] = val
			qotdCount = qotdCount + 1

class dictionaryStatuses:
	multiStatus = {}
	statusCount = 0

	with open('txt/'+'multiStatus.txt', encoding="utf8") as f:
		for line in f:
	    		(key, val) = line.split('_')
	    		newVal = val.rstrip()
	    		multiStatus[str(key)] = newVal
	    		statusCount = statusCount + 1