import discord
from discord.ext import commands
from pymongo import MongoClient
import os

class CreateFamilyRoles(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    

def setup(client):
    client.add_cog(CreateFamilyRoles(client))
