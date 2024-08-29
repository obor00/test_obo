import pytest

class Target:
    def __init__(self, name):
        self.name = name

@pytest.fixture
def target_MTA():
    return Target("target_MTA")

@pytest.fixture
def target_MTB():
    return Target("target_MTB")

