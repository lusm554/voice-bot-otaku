import os
import exceptions
import asyncio
from dotenv import load_dotenv

import discord
from discord.ext import commands
from discord.ext.commands import (ExtensionFailed, ExtensionNotFound, NoEntryPointError)

try:
    load_dotenv()
    DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
except KeyError:
    raise exceptions.MissingEnvironmentVariable(f"Environment variable 'DISCORD_TOKEN' does not defined.")

INITIAL_COGS = ("cogs.admin", "cogs.vcontrol")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


class OtakuBot(commands.Bot):
    def __init__(self, **args):
        super().__init__(**args)

    async def on_ready(self) -> None:
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print()

    async def setup_hook(self) -> None:
        """A coroutine to be called to setup the bot, by default this is blank."""
        # Load cogs or bot extentions or commands.
        try:
            for cog_name in INITIAL_COGS:
                await self.load_extension(cog_name)
        except (ExtensionFailed, ExtensionNotFound, NoEntryPointError):
            print(f"Failed to load extension cogs.vcontrol")


bot = OtakuBot(
    command_prefix=commands.when_mentioned_or("/"),
    intents=intents
)
if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)


