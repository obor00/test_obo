import pytest

@pytest.fixture(scope='session')
def init(request):
    print ('start init fixture=' + request.param)
    yield request.param
    print ('end init fixture=' + request.param)

