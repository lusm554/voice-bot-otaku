import discord
import os
from dotenv import load_dotenv

try:
    load_dotenv()
    DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
except KeyError:
    raise exceptions.MissingEnvironmentVariable(f"Environment variable 'DISCORD_TOKEN' does not defined.")

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.members = True

# TODO: 
# Add error handling
# Add logging


class OtakuBot(discord.Bot):
    """ Extend discord.Bot class for own configuration. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cogs_list = ["admin", "gameparty", "utils"]
        self.__load_extentions__()
    
    def __load_extentions__(self):
        """ Loads bot extentions, such as cogs. """
        for cog_name in self.cogs_list:
            status = self.load_extension(f"cogs.{cog_name}")

    async def on_ready(self):
        print(f"Logged in as {self.user.name} (ID: {self.user.id}).")


bot = OtakuBot(intents=intents)

# @bot.slash_command(name = "ping", description = "Ping pong :)")
# async def ping(ctx):
#     await ctx.respond("pong!")


if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)

