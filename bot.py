import json
import aiohttp
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random


bot = commands.Bot(command_prefix="rok?")

load_dotenv()

@bot.event
async def on_ready():
    print(f"{bot.user.name} started!")

@bot.command()
async def test(ctx):
   await ctx.send("i am working!")

@bot.command(pass_context=True)
async def meme(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(title="", description="")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

@bot.command()
async def rock(ctx):
    async with ctx.channel.typing():
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://mrconos.pythonanywhere.com/rock/random') as r:
                res = await r.json()
                embed = discord.Embed(title=res['name'], description=res['desc'])
                embed.set_image(url=res['image'])
                await ctx.send(embed=embed)

@bot.command()
async def owner(ctx):
   await ctx.send("Recoon is my boss")

@bot.command()
async def gaming(ctx):
    await ctx.send("join games channel for gaming")



@bot.command()
async def balance(ctx):
  await open_account(ctx.author)

  user = ctx.author

  users = await get_bank_data()
  
  wallet_amt= users[str(user.id)]["Wallet"]
  bank_amt= users[str(user.id)]["Bank"]


  em = discord.Embed(title=f"{ctx.author.name}'s balance.", color=discord.Color.teal()) 
  em.add_field(
    name="Wallet Balance",value=wallet_amt
  )
  em.add_field(
    name="Bank Balance",value=bank_amt
  )
  await ctx.send(embed=em)

async def open_account(user):
  users = await get_bank_data()
  
  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["Wallet"] = 0
    users[str(user.id)]["Bank"] = 0
  
  with open("bank.json",'w') as f:
    users = json.dump(users,f)
  return True

async def get_bank_data():
  with open("bank.json",'r') as f:
    users = json.load(f)
  return users

@bot.command()
async def beg(ctx):
  await open_account(ctx.author)

  user = ctx.author


  users = await get_bank_data()

  earnings = random.randrange(101)
  await ctx.send(f"Someone gave your {earnings} coins")

  users[str(user.id)]["Wallet"] += earnings

  with open("bank.json",'r') as f:
    users = json.dump(users,f)

 

bot.run(os.getenv("DISCORD_TOKEN"))    