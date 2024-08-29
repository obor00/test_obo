import pytest


class User:
    name = ''
    def __init__(self, name):
        self.name = name
    def run(self):
        print ('User name' + self.name)

@pytest.fixture(scope = 'class')
def new_user(user_name):
    myuser = User(user_name)
    yield   myuser
    print ('Destroying name' + user_name)
    myuser = None

@pytest.mark.parametrize( "user_name", [ pytest.param( 'user-1' ), pytest.param( 'user-2' ) ], scope = 'class' )

class TestTest:

    @pytest.mark.usefixtures("new_user")
    def test_anew_user(self, new_user):
        print ('test: ' + new_user.name)

    #@pytest.mark.dependency(depends=["TestTest::test_anew_user"])
    #@pytest.mark.dependency(depends=["a"])
    def test1(self, new_user):
        print ('test1: ' + new_user.name)

