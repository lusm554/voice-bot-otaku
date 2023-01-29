import discord
from discord.ext import commands

class Utils(commands.Cog):
    """ Information about bot status. """

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def ping(self, ctx):
        await ctx.respond("`ping command here`")

    @discord.slash_command()
    async def uptime(self, ctx):
        await ctx.respond("`uptime command here`")

def setup(bot):
    bot.add_cog(Utils(bot))