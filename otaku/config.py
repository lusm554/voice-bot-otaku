import os
import discord
import exceptions
import json
import logging
from dotenv import load_dotenv

class DiscordConfig:
    """ Fetches config variables for Discord bot and API lib. """

    # Getting discord bot token
    try:
        load_dotenv() # read env vars from .env file
        TOKEN = os.environ["DISCORD_TOKEN"]
    except KeyError:
        raise exceptions.MissingEnvironmentVariable("Environment variable 'DISCORD_TOKEN' does not defined.")
    # Setting bot intents
    _INTENTS_CONF = {
        "message_content": True,
        "voice_states": True,
        "members": True,
        "guilds": True
    }
    INTENTS = discord.Intents(**_INTENTS_CONF)
    # Dir where stores extensions/cogs
    EXTENSIONS_DIR = "controllers"
    EXTENSIONS_LIST = ("admin", "gameparty", "utils")
    BOT_NAME = "Otaku"
    # Pretty json view of config without tokens etc.
    JSON_NO_CREDENTIALS_CONF = json.dumps({
        "INTENTS": _INTENTS_CONF,
        "EXTENSIONS_DIR": EXTENSIONS_DIR,
        "EXTENSIONS_LIST": EXTENSIONS_LIST,
        "BOT_NAME": BOT_NAME
    }, indent=4)

class LoggingConfig:
    """ Fetches config for system logging. """
    try:
        LOG_LEVEL = int(os.environ["LOG_LEVEL"])
    except ValueError:
        raise exceptions.UnableCastLiteral(f"Cannot cast LOG_LEVEL literal to int.") 
    except KeyError: # if env not set, then use default value
        LOG_LEVEL = logging.DEBUG

class DatabaseConfig:
    """ Fetches connection variables for data base. """
    pass
