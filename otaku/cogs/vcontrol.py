from discord.ext import commands

class Vcontrol(commands.Cog, name="vcontrol"):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def vctl(self, ctx, *, dis: str = commands.parameter(default=None, description="Name of cog file.")):
        if dis is not None:
            await ctx.voice_client.disconnect()
            return

        # if bot not connected to voice chat
        if ctx.voice_client is None:
            # if the user who invoked command connected to voice chat
            if ctx.author.voice:
                # connect bot to voice chat
                await ctx.author.voice.channel.connect() 
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        # if bot play some audio
        elif ctx.voice_client.is_playing():
            # stop playing audio
            ctx.voice_client.stop() 

    # TODO: listen voice state to correctly disconnect from voice server. Due to slow reconnection after incorrect disconnection.
    """
    @commands.Cog.listener()
    async on_voice_state_update(self, member, before, after):
        print("hello")
    """


async def setup(bot) -> None:
    await bot.add_cog(Vcontrol(bot))

