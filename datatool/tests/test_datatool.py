import datatool
import os


def test_add_basic():
    pth = os.path.join(os.path.dirname(__file__), 'data')
    datatool.add(pth)
    assert pth in datatool.get_paths()


def test_fetch_basic():
    pass


def test_status_basic():
    pass
