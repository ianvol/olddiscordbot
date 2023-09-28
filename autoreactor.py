import discord
import random
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands import has_role

bot = discord.Client()

pic_ext = ['.jpg','.png','.jpeg']

emojis = ['⬆️', '⬇️']


class autoreactor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        




    #@commands.has_any_role('admin')



     @commands.Cog.listener()
     #@commands.has_any_role('Moderator', 'Admin')
     #@commands.has_permissions(manage_messages=True)
     async def on_message(self, message):
        
         channel = discord.utils.get(message.guild.text_channels, name="memes")
         channel_id = channel.id
         #print(channel_id)
         if message.channel.id == channel_id: 
           if not message.attachments:
             #if ctx.message.author.guild_permissions.administrator:

               await message.delete()
          
           else:
             await message.add_reaction('👍')
             await message.add_reaction('👎')

    

      #@commands.Cog.listener()
      #async def on_message(self, message):
      #  if "admin" in [r.name for r in member.roles]:
      #    await channel.send("Hey")
    
      

def setup(bot):
  bot.add_cog(autoreactor(bot))