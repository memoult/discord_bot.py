import time
import discord
from discord.ext import commands
from discord.ext.commands import bot
import os

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())
token = 'ODcyOTI1MjQzNjM3OTE1Njg5.YQw8_A.oiTZbafv-hPwoMqdENugqKHY6qk'

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
	bot.load_extension(f"cogs.{extension}")


@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
	bot.unload_extension(f"cogs.{extension}")


@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
	bot.unload_extension(f"cogs.{extension}")
	bot.load_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f"cogs.{filename[:-3]}")

bot.run('ODcyOTI1MjQzNjM3OTE1Njg5.YQw8_A.oiTZbafv-hPwoMqdENugqKHY6qk')