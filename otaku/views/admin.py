class AdminView:
    """ Creates views for admin commands group. """

    def __init__(self, bot):
        self.bot = bot

    def v_reload(self, cog_name: str) -> str:
        """ Generate response view of reloaded cog/controller. """
        return f"Cog `{cog_name}` reloaded!"

    def v_load(self, cog_name: str) -> str:
        """ Generate response view of loaded cog/controller. """
        return f"Cog `{cog_name}` loaded!"

    def v_unload(self, cog_name: str) -> str:
        """ Generate response view of unloaded cog/controller. """
        return f"Cog `{cog_name}` unloaded!"