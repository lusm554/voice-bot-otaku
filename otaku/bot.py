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
# Add logging
# Add error handling


class OtakuBot(discord.Bot):
    """ Extend discord.Bot class for own configuration. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cogs_list = ["admin", "gameparty", "utils"]
        self.__load_extentions__()
    
    def __load_extentions__(self):
        """ Loads bot extentions, such as cogs. """
        # Try to load every extention. If any exception has occured, then store it in status.
        exts_status = self.load_extensions(*map(lambda cn: f"cogs.{cn}", self.cogs_list), store=True)
        for ext_name, ext_status in exts_status.items():
            try:
                if isinstance(ext_status, Exception):
                    raise ext_status
            except discord.ExtensionNotFound:
                print(f"ExtensionNotFound for {ext_name}")
            except discord.ExtensionAlreadyLoaded:
                print(f"ExtensionAlreadyLoaded for {ext_name}")
            except (discord.NoEntryPointError, discord.ExtensionFailed):
                print(f"NoEntryPointError or ExtensionFailed for {ext_name}")
            else:
                print(f"Extention {ext_name} loaded.")

    async def on_ready(self):
        print(f"Logged in as {self.user.name} (ID: {self.user.id}).")


if __name__ == "__main__":
    bot = OtakuBot(intents=intents)
    bot.run(DISCORD_TOKEN)
