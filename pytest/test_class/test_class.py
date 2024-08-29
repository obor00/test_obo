
import pytest

@pytest.fixture(name="myvariable", scope="class")
def sample_manager_fixture():
    class SampleManager:
        def __init__(self):
            self.myv = 'this is  fixture'

    return SampleManager()

class TestAll:
    myv="yes"

    def test_second(self, myvariable):
        print(myvariable.myv)
        myvariable.myv = 'this is second'

    def test_third(self, myvariable):
        print(myvariable.myv)

