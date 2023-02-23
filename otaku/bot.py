import discord
import logging
from config import DiscordConfig
from log import get_logger

# TODO: 
# Add logging
# Add error handling
logger = get_logger(__name__)

class OtakuBot(discord.Bot):
    """ Extend discord.Bot class for own configuration. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logger.info("Initialization of bot class.")
        self.cogs_list = ["admin", "gameparty", "utils"]
        self.cogs_prefix = "controllers"
        self.start_time = discord.utils.utcnow()
        self.botname = "Otaku"
        self.__load_extentions__()
    
    def __load_extentions__(self) -> None:
        """ Loads bot extentions, such as cogs. """
        # Try to load every extention. If any exception has occured, then store it in status.
        exts_status = self.load_extensions(*map(lambda cn: f"{self.cogs_prefix}.{cn}", self.cogs_list), store=True)
        for ext_name, ext_status in exts_status.items():
            try:
                if isinstance(ext_status, Exception):
                    raise ext_status
            except discord.ExtensionNotFound:
                logger.exception(f"ExtensionNotFound while loading extension {ext_name}.")
            except discord.ExtensionAlreadyLoaded:
                logger.exception(f"ExtensionAlreadyLoaded while loading extension {ext_name}.")
            except (discord.NoEntryPointError, discord.ExtensionFailed):
                logger.exception(f"NoEntryPointError or ExtensionFailed while loading extension {ext_name}.")
            else:
                logger.info(f"Loading {ext_name} extension.")

    async def on_ready(self) -> None:
        """ Called when the client is done preparing the data received from Discord. """
        botclient = self.user
        # Try to set proper name, if not
        if botclient.name != self.botname:
            try:
                await botclient.edit(username=self.botname)
            except discord.HTTPException:
                logger.exception("Editing bot profile failed.")
        logger.info(f"Logged in as {self.user.name} (ID: {self.user.id}).")

if __name__ == "__main__":
    bot = OtakuBot(intents=DiscordConfig.INTENTS)
    bot.run(DiscordConfig.TOKEN)
