import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because test condition does not match"

def test_SecondCreditCard():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition does not match"