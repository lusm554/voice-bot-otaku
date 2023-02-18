import discord

class UtilsView:
    """ Creates views for util commands. """

    def __init__(self, bot_object) -> None:
        self.bot = bot_object

    def v_ping(self) -> str:
        """ Generate response view of bot server client latency. """
        latency_in_ms = round(self.bot.latency * 1000)
        return f"Pong! {latency_in_ms}ms"

    def v_uptime(self) -> str:
        """ Generate response view of bot uptime since last running. """
        delta = discord.utils.utcnow() - self.bot.start_time
        return f"Uptime is `{delta}`."