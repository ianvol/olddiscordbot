import discord
from discord.ext import commands
import discord.utils
from datetime import datetime
#discord == 1.0.1
#discord.py == 0.16
#python-dotenv == 0.15.0
#youtube-dl == 2021.2.10

from stayingalive import keep_alive

#from dotenv import load_dotenv

keep_alive()

#load_dotenv()

print("D version: ", discord.__version__)

intents = discord.Intents.default()
intents.members = True

client = discord.Client()
#bot = discord.Client()
bot = commands.Bot(intents=intents, command_prefix="=")

bot.load_extension('iss')
bot.load_extension('join')
#bot.load_extension('memupdate')
bot.load_extension('mod')
bot.load_extension('nasapod')
#bot.load_extension('noticesAndClosures')
#bot.load_extension('autoreactor')
bot.load_extension('speak')
bot.load_extension('status')
bot.load_extension('population')
bot.load_extension('byebyecriminal')
bot.load_extension('uptime')
bot.load_extension('tfl')


msg_dump_channel = 865647789726892032
@bot.event
async def on_message(message: discord.Message):
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
    author = message.author.id
    channel = bot.get_channel(msg_dump_channel)
    if message.guild is None and not message.author.bot:
        message = message.content
        author = str(author)
        await channel.send(message + "\n" "Sent from: " + author + " at: " + timestamp)
    await bot.process_commands(message)

bot.run('ODM1MTk3NDY5ODYzNzA2NzA2.YIL8Qg.5FiHk1XXi2KxBrZskMWirlZ7SIc')
