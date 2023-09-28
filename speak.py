from discord.ext import commands
from discord.ext.commands import bot
import discord
import random
import pyperclip
import json
import requests
color = random.randint(0, 0xffffff)

class say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name="say")
    #@commands.has_permissions(manage_messages=True)
    async def say(self, ctx, *, message):
        await ctx.message.delete()
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(color=color, timestamp=ctx.message.created_at)

        embed.set_author(name="A swag person has smth to say!", icon_url=ctx.author.avatar_url)

        embed.add_field(name=f"Sent by {ctx.message.author}", value=str(message))

        embed.set_thumbnail(url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(name="rick")
    @commands.has_permissions(manage_messages=True)
    async def rick(self, ctx):
        #message  = "https://www.youtube.com/watch?v=O91DT1pR1ew"
        await ctx.message.delete()
        #link = https://www.youtube.com/watch?v=O91DT1pR1ew
        embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

        embed.set_author(name="Important announcement!", icon_url="https://media1.tenor.com/images/8c409e6f39acc1bd796e8031747f19ad/tenor.gif?itemid=17029825")

        embed.set_image(url="https://media1.tenor.com/images/8c409e6f39acc1bd796e8031747f19ad/tenor.gif?itemid=17029825")

        embed.set_thumbnail(url="https://media1.tenor.com/images/467d353f7e2d43563ce13fddbb213709/tenor.gif?itemid=12136175")

        await ctx.send(embed=embed)
        
    @commands.command(name="pmt")
    async def pmt(self,ctx):
  
      await ctx.message.delete()

      color = random.randint(0, 0xffffff)

      embed = discord.Embed(color=color, timestamp=ctx.message.created_at)

      embed.set_author(name="PMT link", icon_url=ctx.author.avatar_url)

      embed.add_field(name=f"PMT", value="https://www.physicsandmathstutor.com")

      await ctx.send(embed=embed)

    
    @commands.command(name="chemrevise")
    async def chemrevise(self,ctx):
  
      await ctx.message.delete()

      color = random.randint(0, 0xffffff)

      embed = discord.Embed(color=color, timestamp=ctx.message.created_at)

      embed.set_author(name="Chemrevise link", icon_url=ctx.author.avatar_url)

      embed.add_field(name=f"Chemrevise", value="https://chemrevise.org/revision-guides/")

      await ctx.send(embed=embed)


    @commands.command(name="tiffin")
    async def tiffin(self,ctx):
  
      await ctx.message.delete()

      color = random.randint(0, 0xffffff)

      embed = discord.Embed(color=color, timestamp=ctx.message.created_at)

      embed.set_author(name="Tiffin Google Site", icon_url=ctx.author.avatar_url)

      embed.add_field(name=f"Tiffin Google Site", value="https://sites.google.com/prod/tiffin.kingston.sch.uk/home/departments?authuser=0")

      await ctx.send(embed=embed)

    @commands.command(name='physqs')
    async def physqs(self,ctx):
  
      await ctx.message.delete()

      color = random.randint(0, 0xffffff)

      embed = discord.Embed(color=color, timestamp=ctx.message.created_at)

      embed.set_author(name="Physics Questions", icon_url=ctx.author.avatar_url)

      embed.add_field(name=f"Questions website", value="https://umutech.net/index.html")

      await ctx.send(embed=embed)

    @commands.command(name='dndsubclass')
    async def subclass(self,ctx):
  
      await ctx.message.delete()

      color = random.randint(0, 0xffffff)

      embed = discord.Embed(color=color, timestamp=ctx.message.created_at)

      embed.set_author(name="Tamara DND Guide thing", icon_url=ctx.author.avatar_url)

      embed.add_field(name=f"PDF Link", value="https://thetrove.is/Books/Dungeons%20&%20Dragons%20[multi]/5th%20Edition%20(5e)/Core/Tasha’s%20Cauldron%20of%20Everything%20%28HQ%2C%20Both%20Covers%29.pdf")

      await ctx.send(embed=embed)

    # @commands.command(name='membercount')
    # async def membercount(self, ctx):

    #   guild = member.guild
      
    #   await ctx.message.delete()

    #   color = random.randint(0, 0xffffff)

    #   embed = discord.Embed(color=color, timestamp=ctx.message.created_at)

    #   embed.set_author(name="Server member count", icon_url=ctx.author.avatar_url)

    #   amount_of_users = str(guild.member_count)

    #   embed.add_field(name=f"Count:", value="The number of users in the server is: " + amount_of_users)


    @commands.command(name="logpurge")
    @commands.has_permissions(manage_messages=True)
    async def logpurge(self, ctx):

      await ctx.message.delete()

      f = open('textgobrr.txt', 'r')
      length = len(f.readlines())
      length = int(length)
      
      if length == 0:
        user = ctx.bot.get_user(440178135154163720)
        await user.send("The log is already empty!")
      else:
        user = ctx.bot.get_user(440178135154163720)
        await user.send(file=discord.File('textgobrr.txt'))
        open('textgobrr.txt', 'w').close()

    @commands.command(name="dm")
    @commands.has_permissions(manage_messages=True)
    async def dm(self, ctx):

      await ctx.message.delete()

      await ctx.send("What is the message you wish to send?")

      msg = await ctx.bot.wait_for("message", check=lambda message: message.author == ctx.author)

      msg = msg.content
      
      await ctx.send("What is the id of the user you wish to send the message to?")

      userid = await ctx.bot.wait_for("message", check=lambda message: message.author == ctx.author)

      userid = userid.content

      userid = int(userid)

      user = ctx.bot.get_user(userid)

      await user.send("You have been sent a message! The message is: " + msg)

      await ctx.channel.purge(limit=4)

	    #await ctx.channel.purge(limit = 4)

      await ctx.send("The message has been sent!")

    @commands.command(name="google")
    async def google(self, ctx):
      await ctx.message.delete()

      googleurl = "https://www.google.com/search?q="

      await ctx.send("What do you wish to search?")

      msg = await ctx.bot.wait_for("message", check=lambda message: message.author == ctx.author)

      msg = msg.content

      search = msg.split()

      length = len(search)
      
      if length > 1:

        tobeadded = search[-1]

        msg = [word + '+' for word in search]

        msg.pop()

        msg.append(tobeadded)

        #msg = str(msg)

        #print(msg)

        msg = ''.join(msg) 
        
        #print(msg)
          

      await ctx.channel.purge(limit=2)

      googlesearch = googleurl + msg

      color = random.randint(0, 0xffffff)

      embed = discord.Embed(color=color, timestamp=ctx.message.created_at)

      embed.set_author(name="Your google search", icon_url=ctx.author.avatar_url)
    
      #await ctx.send("Here is your search link: " + googlesearch)

      embed.add_field(name=f"Search", value=googlesearch)

      await ctx.send(embed=embed)
    
    @commands.command(name="eggcar")
    async def eggcar(self, ctx):
      await ctx.channel.send(file=discord.File('eggcar.png'))

    @commands.command(name="gay")
    async def gaywine(self, ctx):
      await ctx.channel.send(file=discord.File('gaywine.jpg'))


def setup(bot):
  bot.add_cog(say(bot))