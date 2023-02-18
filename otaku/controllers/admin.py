import discord
from discord.commands import SlashCommandGroup
from discord.ext import commands

# TODO:
# Add errors handling
# Add filter to owner

class Admin(commands.Cog):
    """ Cog for managing bot. """

    def __init__(self, bot):
        self.bot = bot

    cogaction = SlashCommandGroup(
        "cogaction",
        "Various extension management actions.",
        checks=[commands.is_owner().predicate]
    )

    @cogaction.command(
        name="reload",
        description="Reloads cog by name."
    )
    async def reload(self, ctx, cog_name: str):
        """ Atomically reloads an extension. """
        self.bot.reload_extension(f"{self.bot.cogs_prefix}.{cog_name}")
        await ctx.respond(f"Cog `{cog_name}` reloaded!")

    @cogaction.command(
        name="load",
        description="Loads cog by name."
    )   
    async def load(self, ctx, cog_name: str):
        """ Loads an extension. """
        self.bot.load_extension(f"{self.bot.cogs_prefix}.{cog_name}")
        await ctx.respond(f"Cog `{cog_name}` loaded!")

    @cogaction.command(
        name="unload",
        description="Unloads cog by name."
    )   
    async def unload(self, ctx, cog_name: str):
        """ Unloads an extension. """
        self.bot.unload_extension(f"{self.bot.cogs_prefix}.{cog_name}")
        await ctx.respond(f"Cog `{cog_name}` unloaded!")

    async def cog_command_error(self, ctx: commands.Context, error: Exception):
        """ Handle all errors raised by commands inside that cog. """
        print(f"Error in {ctx.command.qualified_name}: {error}") 
        if isinstance(error, discord.ExtensionNotLoaded):
            await ctx.respond(f"ExtensionNotLoaded")
        elif isinstance(error, discord.ExtensionNotFound):
            await ctx.respond(f"ExtensionNotFound")
        elif isinstance(error, discord.NoEntryPointError) or isinstance(error, discord.ExtensionFailed):
            await ctx.respond(f"NoEntryPointError or ExtensionFailed")
        elif isinstance(error, discord.ExtensionAlreadyLoaded):
            await ctx.respond(f"ExtensionAlreadyLoaded")
        elif isinstance(error, commands.NotOwner):
            await ctx.respond(f"You can't use that command.")
        else:
            await ctx.respond("An unknown error occurred while executing the command.")



def setup(bot):
    bot.add_cog(Admin(bot))