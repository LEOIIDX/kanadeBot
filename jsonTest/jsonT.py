import json

with open ('input.json', 'r') as f:
	distros_dict = json.load(f)

#print(distros_dict[1]['keyword'])


for data in distros_dict:
	itemList = 0
	for item in data['keywords']:
		print(data['keywords'][itemList])
		itemList = itemList + 1
#	print(data['keywords'][0])