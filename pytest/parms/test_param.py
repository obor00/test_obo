# test_param.py 

import pytest

@pytest.fixture(scope="session")
def name(pytestconfig):
    return pytestconfig.getoption("name")

def test_print_name(name):
        print(f"\ncommand line param (name): {name}")

def test_print_name_2(pytestconfig):
    print(f"test_print_name_2(name): {pytestconfig.getoption('name')}")

