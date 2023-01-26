from discord.ext import commands

class Admin(commands.Cog, name="admin"):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(hidden=True)
    @commands.is_owner()
    async def reloadcog(
        self,
        ctx, *,
        cogname: str = commands.parameter(description="Name of cog file.")
    ):
        """Reload all or specific cog's code."""
        try:
            await self.bot.reload_extension(f"cogs.{cogname}")
        except (commands.ExtensionNotLoaded, commands.ExtensionNotFound) as error:
            await ctx.send(f"Error while loading extention file.")
        except commands.MissingRequiredArgument:
            await ctx.send("Missing required argument.") # TODO: find why missing argument 'cogname' doesn't catch by this exception.
        else:
            await ctx.send(f"Reload good.")
        

async def setup(bot) -> None:
    await bot.add_cog(Admin(bot))
