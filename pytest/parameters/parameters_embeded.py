import pytest
import subprocess

@pytest.fixture
def setup_conf():
    print("setup")

@pytest.mark.parametrize("param1, param2, param3", [
    [ 'a1', 'a2', 'a3' ],
    [ 'b1', 'b2', 'b3' ],
    [ 'c1', 'c2', 'c3' ]] )

def test_param_list(param1, param2, param3):
    print (param1, param2, param3)

@pytest.mark.parametrize("param1", [ 'a1', 'a2', 'a3' ])
@pytest.mark.parametrize("param2", [ 'b1', 'b2', 'b3' ])
@pytest.mark.parametrize("param3", [ 'c1', 'c2', 'c3' ])

def test_param_list2(param1, param2, param3):
    print (param1, param2, param3)
