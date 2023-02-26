import discord
from ..log import get_logger

logger = get_logger(__name__)

class StackView(discord.ui.View):
    """ Generate buttons accept and deny. """

    def __init__(self):
        hour_in_seconds = 60 * 60
        # Timeout means that view will be responsible during this time.
        super().__init__(timeout=hour_in_seconds)

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.primary, custom_id="accept_button")
    async def accept_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        """ Button for adding player to embed game stack. """
        logger.info(f"Button accept clicked by [{interaction.user}] in msg [{interaction.message.id}]")
        if len(interaction.message.embeds) == 0:
            return await interaction.response.send_message("Embed not found. Interaction failed.")
        embed = interaction.message.embeds[0]
        players = embed.description.split("\n")[2:]
        if len(players) == 5:
            button.disabled = True
            return await interaction.response.edit_message(view=self)
        players = set([interaction.user.mention, *players])
        await interaction.response.edit_message(view=self, embed=GamepartyView.generate_embed(players))

    @discord.ui.button(label="Deny", style=discord.ButtonStyle.primary)
    async def deny_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        """ Button for removing player from embed game stack. """
        logger.info(f"Button deny clicked by [{interaction.user}] in msg [{interaction.message.id}]")
        if len(interaction.message.embeds) == 0:
            return await interaction.response.send_message("Embed not found. Interaction failed.")
        if accept_button := [ch for ch in self.children if ch.custom_id == "accept_button"][0]:
            accept_button.disabled = False
        embed = interaction.message.embeds[0]
        author_id = str(interaction.user.id)
        current_players = embed.description.split("\n")[2:]
        actual_player = list(filter(lambda pl: author_id not in pl, current_players))
        await interaction.response.edit_message(view=self, embed=GamepartyView.generate_embed(actual_player))

class GamepartyView:
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def generate_embed(players: list) -> discord.Embed:
        """ Generate discord embed for stack of players. """
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

    def v_party(self, players: list) -> [discord.Embed, discord.ui.View]:
        """ Generate response view of players stack. """
        embed = GamepartyView.generate_embed(players)
        view = StackView()
        return [embed, view]