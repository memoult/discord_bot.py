import discord
from discord.ext import commands
from pymongo import MongoClient
import os

class User(commands.Cog):

    def __init__(self, bot):
        self.client = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print('Testing Bot Готов к работе!')

    @commands.command()
    async def info(self, ctx):
        await ctx.send('Тестовая команда...')

def setup(client):
    client.add_cog(User(client))