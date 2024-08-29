import pytest

var = 0

@pytest.fixture(scope="module")
def myfixture(request):
    global var
    print('in fixture', request.param)
    return request.param

@pytest.fixture(scope="module", autouse=True)
def m2(request, myfixture):
    print(myfixture + request.param)

@pytest.mark.parametrize("myfixture, m2", [
    pytest.param(3, 20)], indirect = True)
class TestGlobal:
    class Test1:
        def test_t1(self, myfixture):
            print("test_t1")
            print(myfixture)
    class Test2:
        def test_t2(self, myfixture):
            print("test_t2")
            print(myfixture)
