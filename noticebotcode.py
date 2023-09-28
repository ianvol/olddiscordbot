from discord.ext import tasks, commands
import discord
import json
import requests
#import mysql.connector
#import os
from datetime import datetime, timedelta
import pytz
#client = discord.Client();

updateChannel = 828349771542036501

class noticesAndClosures(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.closures.start(bot)
    self.tfrs.start(bot)
  '''
  @commands.Cog.listener()
  async def on_ready(self):
      print("Ready");
      # self.closures.start(bot)
      # self.tfrs.start(bot)
  '''
  def timeCalc(self, source_dt, timezone):
    local = pytz.timezone(timezone)
    real_datetime = source_dt.strftime("%Y-%m-%d %H:%M:%S")
    naive = datetime.strptime(real_datetime, "%Y-%m-%d %H:%M:%S")
    local_dt = local.localize(naive, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)

    return(utc_dt)

  def timeTranslation(self, orig_time):
    if ' to ' in orig_time:
      split = orig_time.split(' to ')
      start = split[0]
      end = split[1]
    if start:
      split = start.split(' ')
      #print('start ' + split)
      suffix = split[1]#.lower()
      hours = int(split[0].split(':')[0])
      minutes = split[0].split(':')[1]
      #if len(minutes) == 1:

      

      if suffix == 'am' or suffix == 'a.m.':
        if hours == 12:
          hour = '00'
      elif suffix == 'pm' or suffix == 'p.m.':
        if hours != 12:
          hours = hours + 12
          hour = str(hours)
      
      start = hour + ':' + minutes
      
    if end:
      print('end: ' + end)
      split = end.split(' ')
      print('split:')
      print(split)
      suffix = split[1]#.lower()
      hours = int(split[0].split(':')[0])
      minutes = split[0].split(':')[1]
      

      if suffix == 'am' or suffix == 'a.m.':
        if hours == 12:
          hours = 0
          hour = '00'
      elif suffix == 'pm' or suffix == 'p.m.':
        if hours != 12:
          hours = hours + 12
          hour = str(hours)
      
      end = hour + ':' + minutes
    return(start, end)
  
  def date_translation(self, date):
    split = date.split(', ')
    year = split[2]
    month_day = split[1]

    split = month_day.split(' ')
    day = split[1]
    month = split[0].lower()

    if month == 'january':
      month = '01'
    elif month == 'february':
      month = '02'
    elif month == 'march':
      month = '03'
    elif month == 'april':
      month = '04'
    elif month == 'may':
      month = '05'
    elif month == 'june':
      month = '06'
    elif month == 'july':
      month = '07'
    elif month == 'august':
      month = '08'
    elif month == 'september':
      month = '09'
    elif month == 'october':
      month = '10'
    elif month == 'november':
      month = '11'
    elif month == 'december':
      month = '12'
    
    date = day + '/' + month + '/' + year
    return date

  def to_dt(self, closure_time, closure_date):
    dt_string = closure_date + ' ' + closure_time
    closure_dt = datetime.strptime(dt_string, '%d/%m/%Y %H:%M')

    if closure_time == '00:00':
      closure_dt = closure_dt + timedelta(days = 1)

    return closure_dt


  def closure_delta(self, now, start, end):

    now = self.timeCalc(now, 'Etc/UTC')
    start = self.timeCalc(start, 'Etc/GMT+5')
    end = self.timeCalc(end, 'Etc/GMT+5')

    elapsed = start - now
    duration_in_s = elapsed.total_seconds()
    if duration_in_s > 0:
      #new closure in:
      days    = divmod(duration_in_s, 86400)        # Get days (without [0]!)
      hours   = divmod(days[1], 3600)               # Use remainder of days to calc hours
      minutes = divmod(hours[1], 60)

      delta = """%s day(s), %s hour(s) and %s minute(s)""" % (days[0], hours[0], minutes[0])
      print('delta: ' + delta)
      type = 'start'
      
      delta_in_s = duration_in_s
      dict = {'delta': delta,
      'type' : type,
      'delta_in_s' : delta_in_s}
      return dict

    elif duration_in_s < 0:
      #closure end in or old closure?

      end_elapsed = end - now 
      end_duration = end_elapsed.total_seconds()
      print('\n\n\n'+str(end_duration) + '\n\n\n')

      if end_duration < 0:
        delta = ''
        type = 'passed'
        delta_in_s = None
        dict = {'delta': delta,
        'type': type,
        'delta_in_s': delta_in_s}
        return dict
      
      else:
        days    = divmod(end_duration, 86400)        # Get days (without [0]!)
        hours   = divmod(days[1], 3600)               # Use remainder of days to calc hours
        minutes = divmod(hours[1], 60) 

        delta = """%s day(s), %s hour(s) and %s minute(s)""" % (days[0], hours[0], minutes[0])
        print('delta: ' + delta)
        type = 'end'
        delta_in_s = end_duration
        dict = {'delta': delta,
        'type': type,
        'delta_in_s': delta_in_s}
        return dict    


  def sort_delta(self, array):
    deltas = []
    for item in array:

      delta = float(item.split('~')[1]) 
      deltas.append(delta)
    print('unsortiert: ')
    print(deltas)
    deltas.sort()
    print('sortiert:')
    print(deltas)

    recent = deltas[0]
    print('recent: ' + str(recent))
    for x in array:
      text = x.split('~')[0]
      delta = float(x.split('~')[1])
      if delta == recent:
    
        break
    print('\nreturned vars:\ndelta: ' + str(delta) + '\ntext: ' + text)
    return delta, text
    


  @commands.command(pass_context=True, aliases=['closures'], help = 'shows the closures')
  async def closureMessage(self, ctx):
      # if message.content.lower().startswith("ac-closures"):
          now = datetime.now()
          closuresArray = requests.get("https://api.bunnyslippers.dev/closures/").json()
          embed = discord.Embed(title=":construction: Closures list", color=0x61B3FF, url = 'https://www.cameroncounty.us/spacex/')
          start_array = []
          end_array = []
          for i in closuresArray:
              time = i["time"]
              date = i["date"]
              start, end = self.timeTranslation(time)
              start_time = self.to_dt(start, self.date_translation(date))
              end_time = self.to_dt(end, self.date_translation(date))

              dict = self.closure_delta(now, start_time, end_time)
              print(dict)
              delta = dict['delta']
              type = dict['type']
              delta_in_s = dict['delta_in_s']



              if type == 'end':
                save = delta + '~' + str(delta_in_s)
                end_array.append(save)
              elif type == 'start':
                save = delta + '~' + str(delta_in_s)
                start_array.append(save)



              
              if '&amp;' in i["status"]:
                split = i["status"].split('&amp;')
                x = 0
                i["status"] = split [0] + '&' + split[1]
              if type != 'passed':
                embed.add_field(name=":warning: " + i["type"] + " | " + i["date"] + " - "   + i["time"], value=i["status"], inline=False)

          if end_array != []:
            delta, text = self.sort_delta(end_array)
            embed.set_footer(text = 'The current closure ends in: ' + text)

          elif start_array != []:
            delta, text = self.sort_delta(start_array)
            
            embed.set_footer(text = 'The next closure starts in: ' + text)
          await ctx.send(embed=embed)

  @commands.command(pass_context=True, aliases=['tfrs'], help = 'shows the tfrs')
  async def tfrMessage(self, ctx):
        #if message.content.lower().startswith("ac-tfrs"):
          tfrsArray = requests.get("https://api.bunnyslippers.dev/tfrs/detailed/").json ()
          embed = discord.Embed(title=":airplane: TFRs list", color=0x61B3FF)
          for i in tfrsArray:
              start = i["startDate"].split()[0].split("/")
              end = i["endDate"].split()[0].split("/")
              notamID = i["notamNumber"]
              notamID = notamID.replace(notamID[1], "_", 1)
              startMonth = ""
              endMonth = ""
              if start[0] == "01":
                  startMonth = "January"
              elif start[0] == "02":
                  startMonth = "February"
              elif start[0] == "03":
                  startMonth = "March"
              elif start[0] == "04":
                  startMonth = "April"
              elif start[0] == "05":
                  startMonth = "May"
              elif start[0] == "06":
                  startMonth = "June"
              elif start[0] == "07":
                  startMonth = "July"
              elif start[0] == "08":
                  startMonth = "August"
              elif start[0] == "09":
                  startMonth = "September"
              elif start[0] == "10":
                  startMonth = "October"
              elif start[0] == "11":
                  startMonth = "November"
              elif start[0] == "12":
                  startMonth = "December"
              else:
                  startMonth = "NULL"

              if end[0] == "01":
                  endMonth = "January"
              elif end[0] == "02":
                  endMonth = "February"
              elif end[0] == "03":
                  endMonth = "March"
              elif end[0] == "04":
                  endMonth = "April"
              elif end[0] == "05":
                  endMonth = "May"
              elif end[0] == "06":
                  endMonth = "June"
              elif end[0] == "07":
                  endMonth = "July"
              elif end[0] == "08":
                  endMonth = "August"
              elif end[0] == "09":
                  endMonth = "September"
              elif end[0] == "10":
                  endMonth = "October"
              elif end[0] == "11":
                  endMonth = "November"
              elif end[0] == "12":
                  endMonth = "December"
              else:
                  endMonth = "NULL"
              startDate = startMonth + " " + start[1] + ", " + start[2] + " at " + i  ["startDate"].split()[1] + " UTC"
              endDate = endMonth + " " + end[1] + ", " + end[2] + " at " + i["endDate"] .split()[1] + " UTC"
              embed.add_field(name="From " + startDate + " To " + endDate,  value="https://tfr.faa.gov/save_pages/detail_" + notamID + ".html",  inline=False)
              embed.set_image(url="https://tfr.faa.gov/save_maps/sect_" + notamID +   ".gif")
          await ctx.send(embed=embed)

  @tasks.loop(seconds=30)
  async def closures(self, bot):
      global updateChannel
      
      lastClosureArray = json.loads(open("closures_tfrs/closures.txt", "r").read())
      
      closuresArray = requests.get("https://api.bunnyslippers.dev/closures/").json()
      #print("Check closures...")
      difference = [i for i in closuresArray if i not in lastClosureArray]
      if(difference == []):
          difference = [i for i in lastClosureArray if i not in closuresArray]
      if difference != []:
          print("CLOSURES UPDATED");
          print(difference)
          channel = bot.get_guild(850451304542633994).get_channel(updateChannel)

          embed = discord.Embed(title=":construction: Closure(s) updated!",   color=0xFFFF00, url = 'https://www.cameroncounty.us/spacex/')
          for i in difference:
              embed.add_field(name=":warning: " + i["type"] + " | " + i["date"] + " - "   + i["time"], value=i["status"], inline=False)
          await channel.send('<@&820418204329050122>', embed=embed)
          file = open("closures_tfrs/closures.txt", "w")
          file.write(json.dumps(closuresArray))
          file.close();
          

  @tasks.loop(seconds=30)
  async def tfrs(self, bot):
      lastTfrsArray = json.loads(open("closures_tfrs/tfrs.txt", "r").read())
      tfrsArray = requests.get("https://api.bunnyslippers.dev/tfrs/detailed/").json()
      #print("Check TFRs...")
      if len(tfrsArray) > len(lastTfrsArray):
          difference = [i for i in tfrsArray if i not in lastTfrsArray];
          if difference != []:
              print("NEW TFR(s)");
              print(difference)
              channel = bot.get_channel(updateChannel)
              embed = discord.Embed(title=":airplane: New TFR(s)", color=0x00FF32)
              for i in difference:
                  start = i["startDate"].split()[0].split("/")
                  end = i["endDate"].split()[0].split("/")
                  notamID = i["notamNumber"]
                  notamID = notamID.replace(notamID[1], "_", 1)
                  startMonth = ""
                  endMonth = ""
                  if start[0] == "01":
                      startMonth = "January"
                  elif start[0] == "02":
                      startMonth = "February"
                  elif start[0] == "03":
                      startMonth = "March"
                  elif start[0] == "04":
                      startMonth = "April"
                  elif start[0] == "05":
                      startMonth = "May"
                  elif start[0] == "06":
                      startMonth = "June"
                  elif start[0] == "07":
                      startMonth = "July"
                  elif start[0] == "08":
                      startMonth = "August"
                  elif start[0] == "09":
                      startMonth = "September"
                  elif start[0] == "10":
                      startMonth = "October"
                  elif start[0] == "11":
                      startMonth = "November"
                  elif start[0] == "12":
                      startMonth = "December"
                  else:
                      startMonth = "NULL"

                  if end[0] == "01":
                      endMonth = "January"
                  elif end[0] == "02":
                      endMonth = "February"
                  elif end[0] == "03":
                      endMonth = "March"
                  elif end[0] == "04":
                      endMonth = "April"
                  elif end[0] == "05":
                      endMonth = "May"
                  elif end[0] == "06":
                      endMonth = "June"
                  elif end[0] == "07":
                      endMonth = "July"
                  elif end[0] == "08":
                      endMonth = "August"
                  elif end[0] == "09":
                      endMonth = "September"
                  elif end[0] == "10":
                      endMonth = "October"
                  elif end[0] == "11":
                      endMonth = "November"
                  elif end[0] == "12":
                      endMonth = "December"
                  else:
                      endMonth = "NULL"
                  startDate = startMonth + " " + start[1] + ", " + start[2] + " at " + i  ["startDate"].split()[1] + " UTC"
                  endDate = endMonth + " " + end[1] + ", " + end[2] + " at " + i  ["endDate"].split()[1] + " UTC"
                  embed.add_field(name=":green_circle: From " + startDate + " To " +  endDate, value="https://tfr.faa.gov/save_pages/detail_" + notamID +  ".html", inline=False)
                  embed.set_image(url="https://tfr.faa.gov/save_maps/sect_" + notamID +   ".gif")
                  await channel.send('<@&820451915628281868>', embed=embed)
                  file = open("closures_tfrs/tfrs.txt", "w")
                  file.write(json.dumps(tfrsArray))
                  file.close()
      elif len(tfrsArray) < len(lastTfrsArray):
          difference = [i for i in lastTfrsArray if i not in tfrsArray];
          if difference != []:
              print("NEW TFR(s)");
              channel = bot.get_channel(updateChannel)
              embed = discord.Embed(title=":airplane: New TFR(s) removed",  color=0xFF0000)
              for i in difference:
                  start = i["startDate"].split()[0].split("/")
                  end = i["endDate"].split()[0].split("/")
                  notamID = i["notamNumber"]
                  notamID = notamID.replace(notamID[1], "_", 1)
                  startMonth = ""
                  endMonth = ""
                  if start[0] == "01":
                      startMonth = "January"
                  elif start[0] == "02":
                      startMonth = "February"
                  elif start[0] == "03":
                      startMonth = "March"
                  elif start[0] == "04":
                      startMonth = "April"
                  elif start[0] == "05":
                      startMonth = "May"
                  elif start[0] == "06":
                      startMonth = "June"
                  elif start[0] == "07":
                      startMonth = "July"
                  elif start[0] == "08":
                      startMonth = "August"
                  elif start[0] == "09":
                      startMonth = "September"
                  elif start[0] == "10":
                      startMonth = "October"
                  elif start[0] == "11":
                      startMonth = "November"
                  elif start[0] == "12":
                      startMonth = "December"
                  else:
                      startMonth = "NULL"

                  if end[0] == "01":
                      endMonth = "January"
                  elif end[0] == "02":
                      endMonth = "February"
                  elif end[0] == "03":
                      endMonth = "March"
                  elif end[0] == "04":
                      endMonth = "April"
                  elif end[0] == "05":
                      endMonth = "May"
                  elif end[0] == "06":
                      endMonth = "June"
                  elif end[0] == "07":
                      endMonth = "July"
                  elif end[0] == "08":
                      endMonth = "August"
                  elif end[0] == "09":
                      endMonth = "September"
                  elif end[0] == "10":
                      endMonth = "October"
                  elif end[0] == "11":
                      endMonth = "November"
                  elif end[0] == "12":
                      endMonth = "December"
                  else:
                      endMonth = "NULL"
                  startDate = startMonth + " " + start[1] + ", " + start[2] + " at " + i  ["startDate"].split()[1] + " UTC"
                  endDate = endMonth + " " + end[1] + ", " + end[2] + " at " + i  ["endDate"].split()[1] + " UTC"
                  embed.add_field(name=":red_circle: From " + startDate + " To " +  endDate, value="https://tfr.faa.gov/save_pages/detail_" + notamID +  ".html", inline=False)
                  embed.set_image(url="https://tfr.faa.gov/save_maps/sect_" + notamID +   ".gif")
                  await channel.send('<@&820451915628281868>', embed=embed)
                  file = open("closures_tfrs/tfrs.txt", "w")
                  file.write(json.dumps(tfrsArray))
                  file.close();
  @closures.before_loop
  async def before_closures(self):
    await self.bot.wait_until_ready()
  
  @tfrs.before_loop
  async def before_tfrs(self):
    await self.bot.wait_until_ready()

def setup(bot):
  bot.add_cog(noticesAndClosures(bot))
