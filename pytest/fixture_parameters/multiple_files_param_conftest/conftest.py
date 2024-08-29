import pytest

@pytest.fixture(scope='session')
@pytest.mark.parametrize( 'init', [pytest.param('A')], indirect=True)
def init(request):
    print ('start init fixture=' + request.param)
    yield request.param
    print ('end init fixture=' + request.param)

