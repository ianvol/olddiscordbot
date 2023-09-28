from discord.ext import commands
from discord.ext.commands import bot
import discord
import requests
import json
import datetime

class tfl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name="tfl")
    async def tfl(self, ctx, *, message):
      def tubeCheck():
        getRequest = requests.get(f"https://api.tfl.gov.uk/line/mode/tube/status")
        print(f"Status code from GET is {getRequest.status_code}")
        print(f"The current type of getRequest variable is {type(getRequest)}")
  
        print("""Welcome to the TfL Underground checker!
    Please enter a number for the line you want to check!
    0 - Bakerloo
    1 - central
    2 - circle
    3 - district
    4 - hammersmith & City
    5 - jubilee
    6 - metropolitan
    7 - northern
    8 - piccadilly
    9 - victoria
    10 - waterloo & city
        """)
        try:
            # getting the input as an integer
            number = int(input(">"))
            print(f"You have selected {number}")
            rawData = getRequest.json()
            tubeLine = rawData[number]
            #print(f"The type of the tubeLine variable is {type(tubeLine)}")
            print(f"Welcome to the {tubeLine['name']} line!")
            # # accessing an element in a nested dictionary
            print(f"The current status on the {tubeLine['name']} line is {tubeLine['lineStatuses'][0]['statusSeverityDescription']}")
        # handling errors if user enters anything else other than a number or an invalid number
        except UnboundLocalError as e:
            print("Error! Please enter a number!")
            print("UnboundLocalError")
            print(e)
        except ValueError as e:
            print("Error! Please enter a number")
            print("ValueError")
            print(e)
        except IndexError as e:
            print("Error! Please enter a valid number!")
            print("IndexError")
            print(e)

def setup(bot):
  bot.add_cog(tfl(bot))