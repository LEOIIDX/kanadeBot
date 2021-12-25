'''
leoDictionary.py
classes for creating dictionaries in LEO! BOT
dictionaryMessages is for the response messages
dictionaryStatuses is for randomized statuses
'''
class dictionaryMessages:
	otherResponses = {}

	with open('txt/'+'otherResponses.txt') as f:
		for line in f:
			(key, val) = line.split('|')
			newVal = val.rstrip()
			otherResponses[str(key)] = newVal


class dictionaryStatuses:
	multiStatus = {}
	statusCount = 0

	with open('txt/'+'multiStatus.txt') as f:
		for line in f:
	    		(key, val) = line.split('_')
	    		newVal = val.rstrip()
	    		multiStatus[str(key)] = newVal
	    		statusCount = statusCount + 1