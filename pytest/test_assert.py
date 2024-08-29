import pytest

from simple_class import Queue

@pytest.fixture(scope='function', autouse=True)
def setup():
    print('doing setup')

@pytest.fixture(scope='function', autouse=True)
def complete():
    print('ending test')



def test_firstlast():
    q = Queue()

    q.add_item(5)
    q.add_item(17)
    q.add_item("hello")

    assert q.first() == 5
    assert q.last() == "hello"

def test_len():
    q = Queue()

    assert q.length() == 0

    q.add_item(1)

    assert q.length() == 1

    for i in range(10):
        q.add_item(i)

    assert q.length() == 11
    assert False

@pytest.fixture(scope='function')
def setup_t3():
    assert False
    yield 'doing setup t3'

def test_t3(setup_t3):
    print(setup_t3)

def test_t4():
    print('test t4')
