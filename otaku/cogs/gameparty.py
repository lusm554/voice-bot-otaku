import discord
from discord.ext import commands
from typing import Union


class StackView(discord.ui.View):
    @discord.ui.button(label="Accept", style=discord.ButtonStyle.primary)
    async def button_accept(self, button, interaction):
        print(type(interaction))
        await interaction.response.send_message("You accepted game!")

    @discord.ui.button(label="Denie", style=discord.ButtonStyle.primary)
    async def button_denie(self, button, interaction):
        await interaction.response.send_message("You denied game!")

class GameParty(commands.Cog):
    """ Cog for managing game party. """

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="party",
        description="Dashboard for game stack. (Selecting players is optional)."
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
        desc = f"**READY {len(players_stack)}/5**\n\n" 
        for player in players_stack:
            desc += f"{player.mention}\n"
        embed = discord.Embed(
            title="Valorant Stack",
            description=desc,
            color=discord.Colour.random(),
        )
        await ctx.respond("The button.", view=StackView(), embed=embed)

    async def cog_command_error(
        self,
        ctx: commands.Context,
        error: Exception 
    ):
        """ Handle all errors raised by commands inside that cog. """
        print(f"Error in {ctx.command.qualified_name}: {error}") 
        await ctx.respond("An unknown error occurred while executing the command.")

def setup(bot):
    bot.add_cog(GameParty(bot))