import json

with open ('input.json', 'r') as f:
	distros_dict = json.load(f)

for data in distros_dict:
	print(data['responses'][0])