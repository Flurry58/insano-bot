import discord
import os
#import pynacl
#import dnspython
import server
from discord.ext import commands

import discord
intents = discord.Intents.default()
intents.members = True
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get
import os
import keep_alive
import random
from datetime import datetime, time, timedelta
import asyncio
from replit import db
import schedule
import json
stop = 1
WHEN = time(18, 0, 0)  # 6:00 PM
channel_id = 1 # Put your channel id here
updatefunc = False
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='%*', intents=intents)
mem = ''

@bot.command(pass_context = True)
async def add_role(ctx, role_add):
  user = ctx.author
  try:
    role_get = discord.utils.get(ctx.guild.roles, name=str(role_add))
    await user.add_roles(role_get)
    await ctx.send(f"Role added to {user}")
  except AttributeError:
    await ctx.send("That role doesn't exist!")

  
@bot.command()
async def heal_all(ctx):
  guild1 = bot.get_guild(803806566881034240)
  keys = guild1.members
  role = discord.utils.get(ctx.guild.roles, name='BRAWHALLA superstar pupil')
  role2 = discord.utils.get(ctx.guild.roles, name='BRAWHALLA superstar')
  if role in ctx.author.roles or role2 in ctx.author.roles:
    with open('battle.json', 'r') as f:
      users = json.load(f)
      for i in keys:
        await update_health(users, str(i))
        if updatefunc == False:
          users[str(i)]['health'] = 100
          print(users[str(i)]['health'])
          with open('battle.json', 'w') as f:
            json.dump(users, f)
  else:
    embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6) 
    await ctx.send(embed=embed)
@bot.command()
async def train(ctx):
  user = await bot.fetch_user(763960952743264307)
  await user.create_dm()
  await user.dm_channel.send(f'{str(user)} needs training (Server name here) come train him/her')

@bot.command(aliases=['helpNeeded'])
async def want_help(ctx):
  user = await bot.fetch_user(763960952743264307)
  server = ctx.message.guild.name
  print(server)
  await user.create_dm()
  await user.dm_channel.send(f'help needed in {server}. Sent from {ctx.author}')

@bot.command()
async def ping(ctx):
  await ctx.send("pong!")

@bot.command()
async def commands(ctx):
  await ctx.send("Commands: %*train, %*commands, %*join, %*war, %*role @user, %*fight @user, %*play, For more info on commands and their uses please visit the bot-commands channel")


@bot.event
async def on_message(message):
  msg = str(message.author)
  msg2 = msg + "(daily)"
  with open('battle.json') as f:
    users = json.load(f)
    await update_health(users, msg)
  await bot.process_commands(message)

async def update_health(users, auth):
  if not f'{auth}' in users:
    users[f'{auth}'] = {}
    users[f'{auth}']["health"] = 100
    updatefunc = True


@bot.event
async def on_ready():
  print("bot ready!")

@bot.command()
async def fight(ctx, member: discord.Member):
    damage = random.randint(1, 10)
    if damage > 4:
      damage = random.randint(1, 20)
      if damage > 15:
        damage = random.randint(1, 30)
        if damage > 26:
          damage = random.randint(1, 40)
          if damage > 37:
            damage=random.radint(1, 50)
            if damage > 48:
              damage=random.radnint(1, 60)
    with open('battle.json', 'r') as f:
      users = json.load(f)
      await update_health(users, str(ctx.author))
      if updatefunc == False:
        if users[str(ctx.author)]['health'] == 0:
          await ctx.send("You can't fight anymore your health is at zero!")
          return
        else:
          users[str(ctx.author)]['health'] = users[str(ctx.author)]['health'] - damage
          await ctx.send(f"{member} was attacked by {ctx.author}! He dealt {damage} points of damage! {member}'s health is now at {users[str(ctx.author)]['health']}")
          with open('battle.json', 'w') as f:
            json.dump(users, f)
  

@bot.command(pass_context=True)
async def join(ctx):
  auth = ctx.author
  guild1 = bot.get_guild(803806566881034240)
  guild2 = bot.get_guild(843483156778188810)
  members1 = guild1.members
  print(members1)
  members2 = guild2.members
  if auth in members2:
    print(auth)
    await ctx.send("You are already in that server")
    if str(auth) == "pianosquad#9714":
      return
    else:
      await auth.kick()
      await ctx.send(f'User {str(auth)} has kicked the bucket.')
  else:
    await ctx.author.create_dm()
    await ctx.author.dm_channel('Invite to bot support server. Once you join this server if you call this command again you wil be kicked. You have been warned. Link: https://discord.gg/zAgaZgrcYn')
  

server.server()
bot.run(TOKEN)
