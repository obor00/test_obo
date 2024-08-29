import pytest

@pytest.fixture
def init(request):
    print ('fixture=' + request.param)
    return request.param

@pytest.fixture
def initB(request):
    print ('fixtureB=' + request.param)
    return request.param

@pytest.mark.parametrize( 'init, initB', [ pytest.param( 'A', 'X' ), pytest.param( 'B', 'Y' ) ], indirect=True
)
def test_timeline(init, initB):
    for i in init:
        print(i)
    for i in initB:
        print(i)

if __name__ == "__main__":
    pytest.main([__file__])
