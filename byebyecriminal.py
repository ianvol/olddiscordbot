import discord
from discord.ext import commands
from discord.ext.commands import bot
from datetime import datetime

class byebyecriminal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_message(self, message):
      guild = message.guild.id
      author = message.author.id
      channel = message.channel.id
      if guild == 824223761703895080:
        now = datetime.now()
        timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
        #timestamp = str.timestamp()
        message = message.content
        message = str(message)
        author = str(author)
        channel = str(channel)
        if channel == "824223761703895083":
          channel = "general"
        elif channel == "828349771542036501":
          channel = "het space"
        file = open("textgobrr.txt","a")
        file.write("\n" + message + " Sent by: " + author + " at: " + timestamp + " in: " + channel)
        file.close()
      else:
        return

       
def setup(bot):
  bot.add_cog(byebyecriminal(bot))
