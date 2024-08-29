import yaml
import pytest

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

@pytest.fixture(params=config['test_values']['my_values'])
def my_fixture(request):
    return int(request.param)

def test_my_fixture(my_fixture):
    assert my_fixture > 0

