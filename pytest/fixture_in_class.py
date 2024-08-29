import pytest


class User:
    name = ''
    def __init__(self, name):
        self.name = name
    def run(self):
        print ('User name' + self.name)


class TestTest:

    myuser = None

    @pytest.fixture()
    def new_user(self):
        self.myuser = User('user1')
        return  self.myuser

    @pytest.mark.dependency()
    @pytest.mark.usefixtures("new_user")
    def test_anew_user(self, new_user):
        self.myuser = new_user
        print ('test: ' + self.myuser.name )

    @pytest.mark.dependency(depends=["TestTest::test_anew_user"])
    #@pytest.mark.dependency(depends=["a"])
    def test1(self):
        print ('test1: ' + self.myuser.name )
        assert self.myuser.name is 'user1'

