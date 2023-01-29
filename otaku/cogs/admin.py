import discord
from discord.ext import commands

# TODO:
# Add errors handling
# Add filter to owner

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
        """ Atomically reloads an extension. """
        try:
            self.bot.reload_extension(f"cogs.{cogname}")
        except discord.ExtensionNotLoaded:
            await ctx.respond(f"ExtensionNotLoaded")
        except discord.ExtensionNotFound:
            await ctx.respond(f"ExtensionNotFound")
        except (discord.NoEntryPointError, discord.ExtensionFailed):
            await ctx.respond(f"NoEntryPointError or ExtensionFailed")
        else:
            await ctx.respond(f"Cog `{cogname}` reloaded!")

def setup(bot):
    bot.add_cog(Admin(bot))