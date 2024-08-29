import pytest


class User:
    def __init__(self, name):
        self.name = name

@pytest.fixture
def new_user():
    return User ('hello')

@pytest.mark.parametrize( "test_name, timeout", [ pytest.param( 'toto', 10 )])

class TestTest:

    @pytest.mark.dependency()
    #@pytest.mark.dependency(name="a")
    def test_new_user(self, new_user, test_name, timeout):
        global g_user
        g_user = new_user
        assert g_user.name  is 'hello'
        print (test_name)

    @pytest.mark.dependency(depends=["TestTest::test_new_user[toto-10]"])
    #@pytest.mark.dependency(depends=["a"])
    def test1(self, test_name, timeout):
        global g_user
        print (g_user.name)
        assert g_user.name  is 'hello'

#class TestTest2:
    def test_test2(self, new_user, test_name, timeout):
        print (test_name)
