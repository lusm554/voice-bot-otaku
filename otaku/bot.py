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
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

@bot.slash_command(name = "ping", description = "Ping pong :)")
async def ping(ctx):
    await ctx.respond("pong!")

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)

