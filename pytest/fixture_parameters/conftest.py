import pytest

@pytest.fixture
def init(request):
    print ('fixture=' + request.param)
    return request.param

