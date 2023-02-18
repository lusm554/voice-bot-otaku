import discord
from discord.ext import commands
from views import UtilsView

class Utils(commands.Cog):
    """ Information about bot status. """

    def __init__(self, bot):
        self.bot = bot
        self.view = UtilsView(bot)

    @discord.slash_command(
        name="ping",
        description="Get network latency of bot commands."
    )
    async def ping(self, ctx):
        """ Respond to ping command with ping view. """
        await ctx.respond(self.view.v_ping())

    @discord.slash_command(
        name="uptime",
        description="Get the time the bot has been running since the last run."
    )
    async def uptime(self, ctx):
        """ Respond to uptime command with uptime view. """
        await ctx.respond(self.view.v_uptime())

    async def cog_command_error(
        self,
        ctx: commands.Context,
        error: Exception 
    ):
        """ Handle all errors raised by commands inside that cog. """
        print(f"Error in {ctx.command.qualified_name}: {error}") 
        await ctx.respond("An unknown error occurred while executing the command.")

def setup(bot):
    bot.add_cog(Utils(bot))