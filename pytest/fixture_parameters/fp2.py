import pytest

@pytest.fixture
def init(request):
    print ('fixture=' + request.param)
    return request.param

@pytest.mark.parametrize(
    'init',
    ('A', 'B', 'C'),
    indirect=True
)
def test_timeline(init):
    for i in init:
        print(i)

if __name__ == "__main__":
    pytest.main([__file__])
