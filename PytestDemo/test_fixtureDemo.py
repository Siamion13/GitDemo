import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("Ï will execute steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("Ï will execute steps in fixtureDemo method")

    def test_fixtureDemo2(self):
        print("Ï will execute steps in fixtureDemo method")