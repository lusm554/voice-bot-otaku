import discord
from discord.ext import commands

# TODO:
# Add errors handling

class Admin(commands.Cog):
    """ Cog for managing bot. """

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(hidden=True)
    async def reloadcog(
        self,
        ctx, *,
        cogname: str
    ):
        self.bot.reload_extension(f"cogs.{cogname}")
        await ctx.respond("cog reloaded!")

def setup(bot):
    bot.add_cog(Admin(bot))