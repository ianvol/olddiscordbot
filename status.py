from discord.ext import commands
from discord.ext.commands import bot
import discord


class status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.Cog.listener()
    #@bot.event
    async def on_ready(self):
      #print('Bot is now working!')
      # Set `Playing ` status
      await self.bot.change_presence(activity=discord.Game(name="with deine mutter xdd"))

      # Set `Streaming ` status
      #await self.bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

      # Set `Listening ` status
      #await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Paramore for free therapy"))

      # Set `Watching ` status
      #await #self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="thruple supremacy"))


def setup(bot):
  bot.add_cog(status(bot))