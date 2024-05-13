import pytest

@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul", "Sheety", "rahulshetty.com"]


@pytest.fixture(params=[("chrome", "Rahul"), ("Firefox","Rahul"), ("IE", "SS")])
def crossBrowser(request):
    return request.param
