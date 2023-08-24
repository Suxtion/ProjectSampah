import discord
from discord.ext import commands
import os, random
from sampah import sampah_organik, sampah_anorganik

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Kita telah login sebagai {bot.user}')

@bot.command
async def organik(ctx):
    await ctx.send('salah satu sampah organik nya adalah: ')
    await ctx.send(sampah_organik())

@bot.command
async def anorganik(ctx):
    await ctx.send('salah satu sampah anorganik nya adalah: ')
    await ctx.send(sampah_anorganik())

bot.run("Masukin Pin nya kesini Qaqa")
