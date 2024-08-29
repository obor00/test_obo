import os
import pytest

@pytest.fixture
def test_name1(request):
    testname = request.node.name
    print(testname)
    #assert testname == 'test_test1'

@pytest.mark.parametrize( "target", [ 'tgt-A' ] )
class TestSmall:
    def test_test1(self, test_name1, target):
        print ('this is test1')

