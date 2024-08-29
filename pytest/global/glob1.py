import pytest

@pytest.fixture
def common_value():
    return 'common_value'

@pytest.fixture
def fixture_one(common_value):
    value1 = common_value
    return value1

@pytest.fixture
def fixture_two(common_value):
    value2 = common_value
    return value2

def test_fixtures(fixture_one, fixture_two):
    assert fixture_one == fixture_two

