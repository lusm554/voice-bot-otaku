from discord.ext import commands

class Admin(commands.Cog, name="admin"):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(hidden=True)
    @commands.is_owner()
    async def reloadcog(self, ctx, *, cogname: str = None):
        """Reload all or specific cog's code."""
        try:
            await self.bot.reload_extension("cogs.admin")
            await self.bot.reload_extension("cogs.vcontrol")
        except (commands.ExtensionNotLoaded, ExtensionNotFound) as error:
            await ctx.send(f"Error while loading extention file.")
        

async def setup(bot) -> None:
    await bot.add_cog(Admin(bot))
