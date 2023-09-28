from discord.ext import commands
#from discord.ext.commands import bot
import discord
import json
import requests
import random
import re
#json_data = []

#@commands.Cog.listener()

class nasapod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name="nasapod")
    async def nasapod(self, ctx):
      response = requests.get("https://api.nasa.gov/planetary/apod?api_key=2LjfSDDU9MIg9rCWsdyh8hHrbAKR4S99QAxVXoAx").json()
      #imglink = (re.search("(?P<url>https?://[^\s]+)", response).group("url"))
      json_data = json.loads(response.text)
      nasapod = json_data["url"]
      #nasa = requests.get("http://api.open-notify.org/iss-now.json").json()
      #longtitude = float(issJson["iss_position"]["longitude"]);
      return (nasapod)

      color = random.randint(0, 0xffffff)
      embed = discord.Embed(color=color, timestamp=ctx.message.created_at)
      embed.set_author(name="NASA picture of the day!",     icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/NASA_logo.svg/2449px-NASA_logo.svg.png")
      #embed.set_image(url=nasapod)
      embed.add_field(name='Note', value="You're awesome :)",  inline=True)
      embed.set_footer("Coded with <3")
      await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(nasapod(bot))