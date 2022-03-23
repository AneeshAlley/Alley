import json
import aiohttp
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random

intents = discord.Intents.default()  
intents.members = True
bot = commands.Bot(command_prefix="rok?", intents=intents)

load_dotenv()

@bot.event
async def on_ready():
    activity=discord.Game(name="Love Recoon | rok?bh")
    await bot.change_presence(activity=activity)
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
   own = ctx.guild.owner
   e = discord.Embed(title=f"{own}", description="Recoon is the boss of the world!")
   await ctx.send(embed=e)

@bot.command()
async def gaming(ctx):
    e = discord.Embed(title="Gaming channel", description="Come to my Gaming channel<#894928863992361031>")
    await ctx.send(embed=e)

@bot.command(name="ping", pass_context=True, aliases=["latency", "latence"])
async def ping(ctx):
    
    embed = discord.Embed(title="__**Latence**__", colour=discord.Color.dark_gold(), timestamp=ctx.message.created_at)
    embed.add_field(name="Latence of bot :", value=f"`{round(bot.latency * 1000)} ms`")

    await ctx.send(embed=embed)

@bot.command(aliases=["bh"])
async def bothelp(ctx):
    e = discord.Embed(title="Help! all commands", description="My all commands with how to use.")
    e.set_author(name=f"{bot.user.name}", icon_url=f"{bot.user.avatar_url}")
    e.add_field(name="`rok?bothelp`", value="Shows this message.")
    e.add_field(name="`rok?gaming`", value="Takes you to gaming channel.")
    e.add_field(name="`rok?meme`", value="Sends random memes.")
    e.add_field(name="`rok?owner`", value="Owner is invincible.")
    e.add_field(name="`rok?ping`", value="Shows my ping.")
    e.add_field(name="`rok?rock`", value="Sends random rock images.")
    e.add_field(name="`rok?test`", value="Normal test command.")
    await ctx.send(embed=e)        

 

bot.run(os.getenv("DISCORD_TOKEN"))    
