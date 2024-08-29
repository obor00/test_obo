# test_file.py

import pytest

@pytest.fixture
def V():
    return [0]

def test_modify_V(V):
    V[0] = 10
    assert V[0] == 10

def test_read_V(V):
    assert V[0] == 10

