import pytest

var=0

@pytest.fixture(scope="session")
def myfixture(request):
    global var
    print('in fixture', request.param)
    var = var + 1
    return var

@pytest.mark.parametrize("myfixture", ['u1'], indirect = True)
def test_t1(myfixture):
    print("test_t1")
    print(myfixture)

@pytest.mark.parametrize("myfixture", ['u1'], indirect = True)
class TestGlobal:
    class Test1:
        def test_t1(self, myfixture):
            print("test_t1")
            print(myfixture)

    class Test2:
       def test_t2(self, myfixture):
           print("test_t2")
           print(myfixture)

