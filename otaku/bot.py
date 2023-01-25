import os
import exceptions
import discord
from dotenv import load_dotenv

try:
    load_dotenv()
    DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
except KeyError:
    raise exceptions.MissingEnvironmentVariable(f"Environment variable 'DISCORD_TOKEN' does not defined.")

print(DISCORD_TOKEN)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

#bot.run(DISCORD_TOKEN)

