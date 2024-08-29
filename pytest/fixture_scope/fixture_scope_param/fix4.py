import pytest

@pytest.mark.parametrize("myfixture", [ pytest.param(3)], indirect = True)
class TestGlobal:
    def test_t3(self, myfixture):
        print("test_t1")
        print(myfixture)

@pytest.mark.parametrize("myfixture", [ pytest.param(3)], indirect = True)
class TestGlob4:
    def test_t4(self,myfixture):
        print(myfixture)

