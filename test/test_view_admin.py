import pytest
from otaku.views import AdminView

@pytest.fixture
def admin_view_instance():
    bot = {}
    view = AdminView(bot)
    return view

def test_v_reload(admin_view_instance):
    assert admin_view_instance.v_reload("test") == "Cog `test` reloaded!"
    assert admin_view_instance.v_reload(123) == "Cog `123` reloaded!"
    assert admin_view_instance.v_reload({}) == "Cog `{}` reloaded!"

def test_v_load(admin_view_instance):
    assert admin_view_instance.v_load("sometestname") == "Cog `sometestname` loaded!"
    assert admin_view_instance.v_load(12342314) == "Cog `12342314` loaded!"
    assert admin_view_instance.v_load({}) == "Cog `{}` loaded!"

def test_v_unload(admin_view_instance):
    assert admin_view_instance.v_unload("onemorename") == "Cog `onemorename` unloaded!"
    assert admin_view_instance.v_unload(10000) == "Cog `10000` unloaded!"
    assert admin_view_instance.v_unload({}) == "Cog `{}` unloaded!"

if __name__ == "__main__":
    pytest.main()
