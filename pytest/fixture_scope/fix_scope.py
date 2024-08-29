import pytest

RELEASE = [{'from': "acs-4.12", 'to': "master"},  {'from': "acs-4.13", 'to': "toto"}]

@pytest.fixture(scope="module", params = RELEASE)
def release(request):
    return request.param

@pytest.fixture(scope="module")
def start_server(release):
    print(f'start_server 1: {release}')
    yield 'fixture1'
    print(f'stop_server 1: {release}')


def test_start11(release, start_server):
    print('my test1')

def test1_start2(release, start_server):
    print('my test2')

