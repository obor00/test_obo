import pytest

class Target:
    def __init__(self, name):
        self.name = name

@pytest.fixture
def target_MTA():
    yield Target("target_MTA")

@pytest.fixture
def target_MTB():
    yield Target("target_MTB")


# Define a parameterized test with target as a parameter
@pytest.mark.parametrize("target", [target_MTA, target_MTB])
def test_example(target):
    print(type(target))
    # assert isinstance(target, Target)
    assert target.name in ["target_MTA", "target_MTB"]

