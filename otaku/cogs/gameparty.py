import discord
from discord.ext import commands

class GameParty(commands.Cog):
    """ Cog for managing game party. """

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def val(self, ctx):
        await ctx.respond("hello world!")

def setup(bot):
    bot.add_cog(GameParty(bot))