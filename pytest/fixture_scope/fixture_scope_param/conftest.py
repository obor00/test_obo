import pytest


@pytest.fixture(scope="session")
def myfixture(request):
    print('*********in fixture >>>>>>>>>', request.param)
    return request.param

