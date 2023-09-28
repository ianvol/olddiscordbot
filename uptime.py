from discord.ext import commands
from datetime import datetime, timedelta

start = ''


class uptime(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    global start
    
    
    start = datetime.now()



  @commands.command(pass_context = True)
  async def uptime(self, ctx):

    global start

    now = datetime.now()

    elapsed = now - start
    duration_in_s = elapsed.total_seconds() 

    days    = divmod(duration_in_s, 86400)        # Get days (without [0]!)
    hours   = divmod(days[1], 3600)               # Use remainder of days to calc hours
    minutes = divmod(hours[1], 60)                # Use remainder of hours to calc    minutes
    seconds = divmod(minutes[1], 1)               # Use remainder of minutes to calc    seconds
    print("The bot is running for: %d days, %d hours, %d minutes and %d seconds" % (days[0], hours[0], minutes[0], seconds[0]))

    await ctx.send("The bot is running for: %d days, %d hours, %d minutes and %d seconds" % (days[0], hours[0], minutes[0], seconds[0]))


def setup(bot):
  bot.add_cog(uptime(bot))