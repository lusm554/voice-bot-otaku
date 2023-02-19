import discord
from config import DiscordConfig

# TODO: 
# Add logging
# Add error handling

class OtakuBot(discord.Bot):
    """ Extend discord.Bot class for own configuration. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cogs_list = ["admin", "gameparty", "utils"]
        self.cogs_prefix = "controllers"
        self.__load_extentions__()
        self.start_time = discord.utils.utcnow()
        self.botname = "Otaku"
    
    def __load_extentions__(self) -> None:
        """ Loads bot extentions, such as cogs. """
        # Try to load every extention. If any exception has occured, then store it in status.
        exts_status = self.load_extensions(*map(lambda cn: f"{self.cogs_prefix}.{cn}", self.cogs_list), store=True)
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

    async def on_ready(self) -> None:
        """ Called when the client is done preparing the data received from Discord. """
        botclient = self.user
        # Try to set proper name, if not
        if botclient.name != self.botname:
            try:
                await botclient.edit(username=self.botname)
            except discord.HTTPException:
                print("Editing your profile failed.")
        print(f"Logged in as {self.user.name} (ID: {self.user.id}).")

if __name__ == "__main__":
    bot = OtakuBot(intents=DiscordConfig.INTENTS)
    bot.run(DiscordConfig.TOKEN)
