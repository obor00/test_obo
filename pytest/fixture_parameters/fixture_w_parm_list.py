import pytest


@pytest.fixture
def init(request):
    print('fixture with list:', request.param)
    return request.param


@pytest.fixture
def initB(request):
    print('fixtureB with list:', request.param)
    return request.param


@pytest.mark.parametrize('init, initB', [pytest.param(['A', 'B', 'C'], ['X', 'Y', 'Z']),
                                         pytest.param('B', 'Y')], indirect=True)
def test_timeline(init, initB):
    for i in init:
        print(i)
    for i in initB:
        print(i)


if __name__ == "__main__":
    pytest.main([__file__])
