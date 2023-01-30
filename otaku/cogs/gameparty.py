import discord
from typing import Union
from discord.ext import commands
from typing import Union

def render_stack_embed(players: list) -> discord.Embed:
    """ Create discord embed for game stack. """
    desc = f"**READY {len(players)}/5**\n\n" 
    for player in players:
        if isinstance(player, discord.User) or isinstance(player, discord.Member):
            player_mention = player.mention
        else:
            player_mention = player
        desc += f"{player_mention}\n"
    embed = discord.Embed(
        title="Valorant Stack",
        description=desc,
        color=discord.Colour.random(),
    )
    return embed

class StackView(discord.ui.View):
    def __init__(self):
        hour_in_seconds = 60 * 60
        # Timeout means that view will be responsible during this time.
        super().__init__(timeout=hour_in_seconds)

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.primary, custom_id="accept_button")
    async def button_accept(self, button, interaction):
        """ Button for addind player to game stack. """
        if len(interaction.message.embeds) == 0:
            return await interaction.response.send_message("Embed not found. Interaction failed.")
        embed = interaction.message.embeds[0]
        players = embed.description.split("\n")[2:]
        if len(players) == 5:
            button.disabled = True
            return await interaction.response.edit_message(view=self)
        players = set([interaction.user.mention, *players])
        await interaction.response.edit_message(view=self, embed=render_stack_embed(players))

    @discord.ui.button(label="Denie", style=discord.ButtonStyle.primary)
    async def button_denie(self, button, interaction):
        """ Button for removing player from game stack. """
        if len(interaction.message.embeds) == 0:
            return await interaction.response.send_message("Embed not found. Interaction failed.")
        if accept_button := [ch for ch in self.children if ch.custom_id == "accept_button"][0]:
            accept_button.disabled = False
        embed = interaction.message.embeds[0]
        author_id = str(interaction.user.id)
        current_players = embed.description.split("\n")[2:]
        actual_player = list(filter(lambda pl: author_id not in pl, current_players))
        await interaction.response.edit_message(view=self, embed=render_stack_embed(actual_player))

class GameParty(commands.Cog):
    """ Cog for managing game party. """

    def __init__(self, bot):
        self.bot = bot

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
        embed = render_stack_embed(players_stack)
        await ctx.respond(view=StackView(), embed=embed)

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