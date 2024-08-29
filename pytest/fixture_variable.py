import pytest


class User:
    def __init__(self, name):
        self.name = name

@pytest.fixture
def new_user():
    return User ('hello')


class TestTest:

    @pytest.mark.dependency()
    #@pytest.mark.dependency(name="a")
    def test_new_user(self, new_user):
        global g_user
        g_user = new_user
        assert g_user.name  is 'hello'

    @pytest.mark.dependency(depends=["TestTest::test_new_user"])
    #@pytest.mark.dependency(depends=["a"])
    def test1(self):
        global g_user
        print (g_user.name)
        assert g_user.name  is 'hello'

