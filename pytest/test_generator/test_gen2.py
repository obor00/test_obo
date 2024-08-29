import pytest
import yaml

@pytest.fixture(scope='session')
def test_config():
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    return config

@pytest.fixture(scope='function', params=[0, 1, 2], ids=['val1', 'val2', 'val3'])
def my_fixture(request, test_config):
    return int(test_config['test_values']['my_values'][request.param])

def test_my_fixture(my_fixture):
    assert my_fixture > 0

