import discord
from discord.ext import commands
from views import GamepartyView
from log import get_logger

# TODO: add parameter name of party action

logger = get_logger(__name__)

class GameParty(commands.Cog):
    """ Cog for managing game party. """

    def __init__(self, bot):
        self.bot = bot
        self.view = GamepartyView(self.bot)

    @discord.slash_command(
        name="party",
        description="Dashboard for game stack. (Selecting players is optional).",
        guild_only=True
    )
    async def party(
        self,
        ctx: discord.ApplicationContext, *,
        player1: discord.Option(discord.User, description="player1", default=None),
        player2: discord.Option(discord.User, description="player2", default=None),
        player3: discord.Option(discord.User, description="player3", default=None),
        player4: discord.Option(discord.User, description="player4", default=None),
    ):
        players_stack = set(filter(lambda x: x is not None, [player1, player2, player3, player4, ctx.author]))
        embed, view = self.view.v_party(players_stack)
        await ctx.respond(view=view, embed=embed)

    async def cog_command_error(
        self,
        ctx: commands.Context,
        error: Exception 
    ):
        """ Handle all errors raised by commands inside that cog. """
        logger.error(f"In cmd [{ctx.command.qualified_name}] {error}") 
        await ctx.respond("An unknown error occurred while executing the command.")

def setup(bot):
    bot.add_cog(GameParty(bot))