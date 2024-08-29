import pytest


@pytest.fixture()
def toto(request):
    print('in fixture toto', request.param)


@pytest.mark.parametrize('toto', [
    pytest.param(1, marks=pytest.mark.m1),
    pytest.param(2, marks=pytest.mark.m2)
    ], indirect=True, scope='class')
@pytest.mark.usefixtures('toto')
@pytest.mark.m1
class TestCore:
    def test_m1(self, toto):
        print('test_m1', toto)

    def test_m2(self):
        print('test_m2')
