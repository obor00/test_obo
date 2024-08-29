import pytest

#@pytest.fixture(scope='class', params=['v1', 'v2'])
@pytest.fixture(scope='class', params=[('v1-va'), ('v2-vb')])
def my_fixture(request):
    version = request.param
    # Setup logic
    print("Setup", version)
    yield version
    # Teardown logic
    print("Teardown", version)
