import os
import discord
import exceptions
from dotenv import load_dotenv

class DiscordConfig:
    """ Fetches config variables for Discord API lib. """

    # Getting discord bot token
    try:
        load_dotenv()
        TOKEN = os.environ["DISCORD_TOKEN"]
    except KeyError:
        raise exceptions.MissingEnvironmentVariable(f"Environment variable 'DISCORD_TOKEN' does not defined.")

    # Getting bot intents
    INTENTS = discord.Intents(message_content=True, voice_states=True, members=True)

class DatabaseConfig:
    """ Fetches connection variables for data base. """
    pass
