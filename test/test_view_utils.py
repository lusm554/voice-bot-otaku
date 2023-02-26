import pytest
import datetime
from otaku.views import UtilsView

LATENCY = .134
START_TIME = datetime.datetime.now(datetime.timezone.utc)
class AttributeDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

@pytest.fixture
def utils_view_instance():
    bot = {
        "latency": LATENCY,
        "start_time": START_TIME
    }
    view = UtilsView(AttributeDict(bot))
    return view

def test_v_ping(utils_view_instance):
    assert utils_view_instance.v_ping() == f"Pong! {round(LATENCY*1000)}ms"

def test_v_uptime(utils_view_instance):
    # remove last values because it's hard to compare time within ms
    assert utils_view_instance.v_uptime()[:-4] == f"Uptime is `{datetime.datetime.now(datetime.timezone.utc) - START_TIME}`."[:-4]

if __name__ == "__main__":
    pytest.main()