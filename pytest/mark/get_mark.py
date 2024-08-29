import pytest
from _pytest.mark import MarkInfo

@pytest.mark.foo
@pytest.mark.bar
def test_demo(): 
    print(vars(test_demo.items()))

