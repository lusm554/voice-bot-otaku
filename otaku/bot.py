import discord
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

class BaseClient(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print(f"Bot latency {self.latency}")

    async def on_message(self, msg):
        if msg.author == client.user:
            return

        if msg.content.startswith("$hello"):
            await msg.channel.send("hello")

        if msg.content.startswith("$connect"):
            await msg.channel.send("connecting...")
                
    async def on_reaction_add(self, react, user):
        print("reaction added!")

client = BaseClient(intents=intents)
client.run(token)


