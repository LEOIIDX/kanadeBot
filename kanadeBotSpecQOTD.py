'''
kanadeBotQOTD.py
By: Nanahira Monke Kanade Dev

Condensed version of Kanade Bot programmed for the purpose of QOTD.

Meant to be executed via crontab
'''
import os
import discord
import random
import re
import asyncio
import string
import math
import json

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
QOTD_TYPE = os.getenv('QOTD_TYPE')

#intents
intents = discord.Intents.default()
intents.members = True
intents.emojis = True
intents.reactions = True

print('Kanade Bot QOTD module\n')

bot = commands.Bot(command_prefix='ky!',intents=intents)

qotdCh = 792646559601917963
qotdTest = 867088318466359338

@bot.event
async def on_ready():
    if QOTD_TYPE == "Special":
        os.system("sed -i \'s/Special/Normal/\' .env ")
    else:
        exit()

    questionID = 1

    with open ('specQOTD.json', 'r', encoding="utf8") as f:
        bQOTD = json.load(f)

    qotdEMBED = discord.Embed(colour = discord.Colour.red(), title=bQOTD[questionID]["title"], description = bQOTD[questionID]["value"])

    if bQOTD[questionID]["footer"] == "none":
        qotdEMBED.set_footer(text = 'Question #' + str(bQOTD[questionID]["id"]))
    else:
        qotdEMBED.set_footer(text = bQOTD[questionID]["footer"])

    await bot.get_channel(qotdTest).send(embed = qotdEMBED)

    print('stopping script')
    exit()
bot.run(TOKEN)
