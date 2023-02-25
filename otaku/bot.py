import discord
import logging
from config import DiscordConfig
from log import get_logger

# TODO: 
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
        self.cogs_with_cmd_group = ("Admin")
        logger.info("Initialization of configuration bot class.")
        logger.debug(f"Configuration bot class config vars:\n{DiscordConfig.JSON_NO_CREDENTIALS_CONF}")
        self.__load_extensions__()
    
    def __load_extensions__(self) -> None:
        """ Loads bot extensions, such as cogs. """
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
        """ 
        Verify bot name.
        Called when the client is done preparing the data received from Discord. 
        """
        bot_client = self.user
        # Try to set proper name, if not
        if bot_client.name != self.bot_name:
            try:
                await bot_client.edit(username=self.bot_name)
            except discord.HTTPException:
                logger.exception("Editing bot profile failed.")
        logger.info(f"Logged in as {self.user.name} (ID: {self.user.id}).")
    
    async def on_application_command(self, ctx: discord.ApplicationContext) -> None:
        """
        Logs user interaction with bot through app commands.
        Called when the user is send application command to bot. 
        """
        try:
            channel_type = None
            channel_name = None
            thread_name = None
            guild_name = None
            if isinstance(ctx.channel, discord.PartialMessageable): # msg dm
                channel_type = "DM"
            elif isinstance(ctx.channel, discord.abc.GuildChannel): # msg in guild channel
                channel_type = "GUILD"
                channel_name = ctx.channel.name
                guild_name = ctx.guild.name
            elif isinstance(ctx.channel, discord.Thread): # msg in guild in thread
                channel_type = "GUILD_THREAD"
                channel_name = ctx.channel.name
                guild_name = ctx.guild.name
            msg = f"From user [{ctx.author}] [{ctx.author.id}] received command [{ctx.command.qualified_name}] in [{channel_type}] channel [{channel_name}] [{ctx.channel_id}]"
            if channel_name:
                msg += f" in guild [{guild_name}] [{ctx.guild_id}]"
            if not type(ctx.cog).__name__ in self.cogs_with_cmd_group:
                msg += f" with selected options [{ctx.selected_options}]"
                msg += f" with unselected options [{ctx.unselected_options}]"
            msg += "."
            logger.info(msg)
        except:
            logger.exception(f"Unexpected error while logging.")

if __name__ == "__main__":
    bot = OtakuBot(
        intents=DiscordConfig.INTENTS,
        extensions_dir=DiscordConfig.EXTENSIONS_DIR,
        extensions_list=DiscordConfig.EXTENSIONS_LIST,
        bot_name = DiscordConfig.BOT_NAME
    )
    bot.run(DiscordConfig.TOKEN)
