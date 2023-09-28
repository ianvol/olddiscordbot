from discord.ext import tasks, commands
import discord
import json
import requests
import turtle
from PIL import Image
import os
import random
import time

MAPBOX = 'pk.eyJ1IjoiaWFudm9sIiwiYSI6ImNrc2M3bGRrYjBlMHkydm51MW91MWUwcWkifQ.-gkpqdTkOEBdafFlkquGGw'

class iss(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(pass_context=True, aliases=['iss'], help = 'shows the current position of the ISS')
  async def issMessage(self, ctx, *input):
        input = " ".join(input)

        global MAPBOX

        if input !='':
          try:
            value = int(input)
          except:
            await ctx.send('You have to give a correct number as input. ' + input + ' is not a number') 


        
        if input != "":
          if int(input) > 0 and int(input) <= 20:
            color = random.randint(0, 0xffffff)
            issJson = requests.get("http://api.open-notify.org/iss-now.json").json()
            longtitude = float(issJson["iss_position"]["longitude"]);
            latitude = float(issJson["iss_position"]["latitude"])
            embed = discord.Embed(title=f":satellite_orbital: Current position of the ISS (Zoom  {input}x)",color=color)
            embed.add_field(name='Longtitude', value=longtitude, inline=True)
            embed.add_field(name='Latitude', value=latitude,  inline=True)
            embed.set_image(url=f"https://api.mapbox.com/styles/v1/mapbox/outdoors-v11/static/pin-l-circle+ffffff({longtitude},{latitude})/{longtitude},{latitude},{input},0/600x500@2x?access_token={MAPBOX}")
            footer = "Use =iss <zoom_level> to get a magnified view of the map up to 20x."
            embed.set_footer(text=footer)
            await ctx.send(embed=embed)
        else:
          color = random.randint(0, 0xffffff)
          issJson = requests.get("http://api.open-notify.org/iss-now.json").json()
          longtitude = float(issJson["iss_position"]["longitude"]);
          latitude = float(issJson["iss_position"]["latitude"])
          embed = discord.Embed(title=":satellite_orbital: Current position of the ISS",color=color)
          embed.add_field(name='Longtitude', value=longtitude, inline=True)
          embed.add_field(name='Latitude', value=latitude,  inline=True)
          embed.set_image(url=f"https://api.mapbox.com/styles/v1/mapbox/outdoors-v11/static/pin-l-circle+ffffff({longtitude},{latitude})/{longtitude},{latitude},1,0/600x500@2x?access_token={MAPBOX}")
          footer = "Use =iss <zoom_level> to get a magnified view of the map up to 20x."
          embed.set_footer(text=footer)
          await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(iss(bot))
