#import discord
#import random
from discord.ext import commands, tasks
from datetime import datetime
now = datetime.now()

#bot = discord.Client()

#guild = bot.get_guild(800533504818544690)
#channel = bot.get_channel(800533504818544693)
#memcount = guild.member_count

class vcmemberupdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.update_members.start(bot)
    
    #@commands.command()
    #async def on_ready(self):
    #  while True:
    #    for channel in bot.guild.channels:
    #      asyncio.sleep(60*5) 
    #      if channel.name.startswith('Member'):
    #        await channel.edit(name=f'Members: {bot.guild.member_count}')      
    #        break


    #@commands.command()
    #async def memberupdate(self):
    ##  guild = bot.get_guild(800533504818544690)
    #  channel = bot.get_channel(850753075786154014)
    #  memcount = guild.member_count
    #  await asyncio.sleep(10)
    #  await channel.edit(name=f'Member Count: {guild.member_count}')
    #  print(memcount)

    #async def update_member_count(ctx):
    #  while True:
    #      await ctx.send(ctx.guild.member_count)
    #      channel = discord.utils.get(ctx.guild.channels, id=850753075786154014)
    #      await channel.edit(name=f'Member Count: {ctx.guild.member_count}')
    #      await asyncio.sleep(300)

    #@commands.command()
    #@tasks.loop(seconds=30.0)
    #async def update_members():
    #  guild = bot.get_guild()
    #  channel = guild.get_channel(850753075786154014)
    #  #channel = discord.utils.get(guild.voice_channels, name="general")
    #  await channel.edit(name=f'Member Count: {guild.member_count}')


    @tasks.loop(seconds=60)
    async def update_members(self, bot):
      global guild
      now = datetime.now()
      current_time = now.strftime('%M')

      minute_check = current_time[-1]

      if minute_check == '5' or minute_check == '0':
        try:
          channel = bot.get_guild(824223761703895080).get_channel(865179262297571329)
        #for channel in bot.guild.channels:
        #  if channel.name.startswith('Member'):
          await channel.edit(name=f'Members: {bot.get_guild(824223761703895080).member_count}')      
        #    break
        except Exception as e:
          print(e)
          pass
    
    @update_members.before_loop
    async def before_update(self):
      await self.bot.wait_until_ready()


    #@commands.Cog.listener()
    #async def on_member_join(self, member):
    #  now = datetime.now()
    #  current_time = now.strftime('%H %M')
      




    # @tasks.loop(seconds=30.0)
    # async def tim():
    #   while True:
    #      current_time = now.strftime("%H:%M:%S")
    #      await channel.send("Current Time =", current_time)
    


def setup(bot):
  bot.add_cog(vcmemberupdate(bot))