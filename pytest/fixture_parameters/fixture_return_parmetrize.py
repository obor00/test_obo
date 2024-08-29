import pytest


def compute_function():
    alist = [
        ['a', 1, 2, '>'],
        ['b', 3, 4, '<'],
        ['c', 2, 4, '<']
        ]
    #new_list = [[k, item[k]] for item in alist for k in range(len(item))]
    new_list = alist
    return new_list

# content of conftest.py
def pytest_generate_tests(metafunc):
    #metafunc.parametrize('name,val,ref, op', compute_function())
    metafunc.parametrize('name,val,ref, op', list_parms)

@pytest.fixture()
def list_parms(request):
    yield compute_function()

# def pytest_generate_tests(metafunc, list_parms):
#     metafunc.parametrize('name, val, ref, op', list_parms)

# @pytest.fixture
# def initB(request):
#     print('fixtureB with list:', request.param)
#     return request.param
#

#@pytest.mark.parametrize('name, val, ref, op', [pytest.param(x,y,z,t) for x,y,z,t in list_parms], indirect = True)
#@pytest.mark.parametrize('name, val, ref, op', [pytest.param(x,y,z,t) for x,y,z,t in compute_function())
def test_list(name, val, ref, op):
    assert eval(str(val) + op + str(ref))


