import discord
from discord.ext import commands
from pymongo import MongoClient
import os

class TempBan(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        @commands.command
        async def report(ctx, members:None):
            


def setup(bot):
    bot.add_cog(TempBan(bot))