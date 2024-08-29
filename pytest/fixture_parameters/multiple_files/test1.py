import pytest

@pytest.mark.parametrize( 'init', [pytest.param('A')], indirect=True, scope='session')
def test_1(init):
    print('execute test_t1:' + init)

