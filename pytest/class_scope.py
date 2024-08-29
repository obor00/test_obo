import pytest
import random

class User:
    name = ''
    def __init__(self, name):
        self.name = name
    def run(self):
        print ('User name' + self.name)

count = 0
@pytest.fixture(scope = 'class')
def new_user():
    global count
    count = count + 1
    myuser = User('user' + str(random.random()) )
    yield   myuser
    myuser = None


class TestTest:

    def test_anew_user(self, new_user):
        print ('test a new user: ' + new_user.name)

    def test1(self, new_user):
        print ('test1: ' + new_user.name)

