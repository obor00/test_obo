import pytest
import yaml

@pytest.fixture(scope='session')
def test_config():
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    return config

def len_test_config(test_config):
    return len(test_config)

@pytest.fixture(params=range(len_test_config))
def param(test_config, request):
    return request.param

def test_my_test_function(test_config, param):
    value = int(test_config['test_values']['my_values'][param]['value'])
    assert value > 0

