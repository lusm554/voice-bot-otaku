import os
import random
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="$", intents=intents)

class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return f'{ctx.author} slapped {to_slap} because *{argument}*'

@bot.command()
async def slap(ctx, *, reason: Slapper):
    await ctx.send(reason)

bot.run(token)

