import pytest
import discord
from otaku.views import GamepartyView

@pytest.fixture
def gameparty_view_instance():
    bot = {}
    view = GamepartyView(bot)
    return view

def test_generate_empty_embed():
    empty_party = GamepartyView.generate_embed([])
    assert empty_party.title == "Valorant Stack"
    assert empty_party.description == "**READY 0/5**\n\n"

def test_generate_filled_embed():
    # players = discord.User()
    # full_party = GamepartyView.generate_embed(players)
    ...

if __name__ == "__main__":
    pytest.main()