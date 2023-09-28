import pandas as pd
import json
import requests
from discord.ext import commands


class population(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @commands.command(name="flag")
    async def population(self, ctx):
      await ctx.message.delete()

      #await ctx.send("What country's flag would you like to see?")
      
      #selection = await ctx.bot.wait_for("message", check=lambda message: message.author == ctx.author)

      #selection = selection.content

      #selection = selection.lower()
      
      url = "https://countriesnow.space/api/v0.1/countries/currency"

      payload = "{\n    \"country\":\"nigeria\"\n}"
      headers = {}

      response = requests.request("POST", url, headers=headers, data=payload)

      await ctx.send(response.text)

  
def setup(bot):
  bot.add_cog(population(bot))