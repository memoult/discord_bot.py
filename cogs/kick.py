import discord
from discord.ext import commands
from pymongo import MongoClient
import os

class Kick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def ban(ctx,self, member: discord.Member, reason):
        guild = ctx.guild
        emb = discord.Embed(title='Ban', color=0xff0000)
        emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
        emb.add_field(name='Участник',value=member.mention,inline=False)
        emb.add_field(name='Причина',value=reason,inline=False)
        await member.ban()
        await ctx.send(embed=emb)
        await member.send(f'Вы были забанены на сервере {guild.name} по причине:{reason}')



def setup(bot):
    bot.add_cog(Kick(bot))