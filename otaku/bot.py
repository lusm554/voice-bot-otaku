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

    async def on_message(self, msg):
        if msg.author == client.user:
            return

        if msg.content.startswith("$hello"):
            await msg.channel.send("hello")


client = BaseClient(intents=intents)
client.run(token)


