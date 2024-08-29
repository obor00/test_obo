import pytest

var = 0
ACS_VERSION_PARAMETERS = ["acs-4.12", "acs-4.13"]


@pytest.fixture(scope="module", params=ACS_VERSION_PARAMETERS)
def myfixture2(request):
    return request.param


class Test1:
    def test_t1(self, myfixture2):
        print("test_t1")
        print(myfixture2)
class Test2:
    def test_t2(self, myfixture2):
        print("test_t2")
        print(myfixture2)

class TestGlobal2:
    class Test1:
        def test_t1(self, myfixture2):
            print("test_t1")
            print(myfixture2)
    class Test2:
        def test_t2(self, myfixture2):
            print("test_t2")
            print(myfixture2)
