import pytest

@pytest.mark.parametrize('init', [pytest.param('A')], indirect=True, scope='session')

def test_2(init):
    print('execute test_t2:' + init)

