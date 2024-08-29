import pytest

@pytest.mark.parametrize("myfixture", [ pytest.param(3)], indirect = True)
@pytest.mark.usefixtures("myfixture")
class TestGlobal:
    def test_t1(self, myfixture):
        print("test_t1")
        print(myfixture)

@pytest.mark.usefixtures("myfixture")
@pytest.mark.parametrize("myfixture", [ pytest.param(3)], indirect = True)
class TestGlob2:
    def test_t2(self,myfixture):
        print(myfixture)

    def test_t22(self):
        print('hello')

