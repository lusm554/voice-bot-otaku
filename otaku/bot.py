import discord
import logging
from config import DiscordConfig
from log import get_logger

# TODO: 
# Add logging
# Add error handling
# Check bot name in guilds and in common profile
logger = get_logger(__name__)

class OtakuBot(discord.Bot):
    """ Extend discord.Bot class for own configuration. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extensions_list = kwargs["extensions_list"]
        self.extensions_dir = kwargs["extensions_dir"] 
        self.bot_name = kwargs["bot_name"] 
        self.start_time = discord.utils.utcnow()
        logger.info("Initialization of configuration bot class.")
        logger.debug(f"Configuration bot class config vars:\n{DiscordConfig.JSON_NO_CREDENTIALS_CONF}")
        self.__load_extentions__()
    
    def __load_extentions__(self) -> None:
        """ Loads bot extentions, such as cogs. """
        # Try to load every extention. If any exception has occured, then store it in status.
        exts_status = self.load_extensions(*map(lambda cn: f"{self.extensions_dir}.{cn}", self.extensions_list), store=True)
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
        bot_client = self.user
        # Try to set proper name, if not
        if bot_client.name != self.bot_name:
            try:
                await bot_client.edit(username=self.bot_name)
            except discord.HTTPException:
                logger.exception("Editing bot profile failed.")
        logger.info(f"Logged in as {self.user.name} (ID: {self.user.id}).")

if __name__ == "__main__":
    bot = OtakuBot(
        intents=DiscordConfig.INTENTS,
        extensions_dir=DiscordConfig.EXTENSIONS_DIR,
        extensions_list=DiscordConfig.EXTENSIONS_LIST,
        bot_name = DiscordConfig.BOT_NAME
    )
    # bot.run(DiscordConfig.TOKEN)
