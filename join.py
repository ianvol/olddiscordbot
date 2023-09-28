import discord
import random
from datetime import datetime
from discord.ext import commands
colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F,  0x800000,  0x4682B4,  0x006400,  0x808080,  0xA0522D,  0xF08080,  0xC71585,  0xFFB6C1,  0x00CED1]

hour_check = ''
minute_check = ''

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
      guild = member.guild
      x = random.randint(0, len(colors)-1)
      color = colors[x]
      channel = discord.utils.get(member.guild.text_channels, name="general")
      pfp = member.avatar_url
      amount_of_users = str(member.guild.member_count)
      last_char = amount_of_users[-1]
      if last_char == '1':
        suffix = 'st'
      elif last_char == '2':
        suffix = 'nd'
      elif last_char == '3':
        suffix = 'rd'
      else:
        suffix = 'th'
      join_embed = discord.Embed(title = 'Everybody welcome ' + member.name,
        description = 'You are the ' + amount_of_users + suffix + ' member of this server.', color = color)#random.choice(colors))
      join_embed.set_thumbnail(url=pfp)
      join_embed.set_author(name='Welcome', icon_url=member.guild.icon_url)
      await channel.send(embed=join_embed)
      #await channel.send(f"{member.mention} has arrived! The number of members in the server is now {guild.member_count}"".""")
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = member.guild
        x = random.randint(0, len(colors)-1)
        color = colors[x]

        pfp = member.avatar_url
        channel = discord.utils.get(member.guild.text_channels, name="general")
        leave_embed = discord.Embed(title = "Goodbye!", description = f"{member.mention} decided to leave the server. The number of members in the server is now {guild.member_count}"".""", color = color) #random.choice(colors))
        leave_embed.set_thumbnail(url=pfp)
        leave_embed.set_author(name='Goodbye', icon_url=member.guild.icon_url)
        await channel.send(embed=leave_embed)
        #await channel.send(f"{member.mention} decided to leave a pretty cool server :( The number of members in the server is now {guild.member_count}"".""")
        #await channel.send((f"""# of Members: {guild.member_count}""") )



def setup(bot):
  bot.add_cog(Greetings(bot))
