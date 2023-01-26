from discord.ext import commands

class Vcontrol(commands.Cog, name="vcontrol"):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def vctl(self, ctx):
        await ctx.send(f"Hello world")

async def setup(bot) -> None:
    await bot.add_cog(Vcontrol(bot))

