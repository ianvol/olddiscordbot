from discord.ext import commands, tasks
from discord.ext import commands
from discord.ext.commands import bot

class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name="purge")
    @commands.has_permissions(manage_messages=True)
    async def delete(self, ctx):
      await ctx.message.delete()

      numtodel = await ctx.bot.wait_for("message", check=lambda message: message.author == ctx.author)

      numtodel = numtodel.content

      numtodel = int(numtodel)

      numtodel += 1

      await ctx.channel.purge(limit=numtodel)

      #await ctx.channel.purge(limit=1)





def setup(bot):
  bot.add_cog(mod(bot))